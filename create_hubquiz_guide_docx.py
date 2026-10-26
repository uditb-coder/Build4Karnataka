import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Sets cell background color using oxml."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets inner padding for table cells in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_callout(doc, text, title="NOTE"):
    """Adds a styled callout box with a colored left border."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, "F1F5F9")
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border only (Navy or Gold)
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="none"/>\n'
        f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="0F1B35"/>\n'
        f'  <w:bottom w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    
    run_title = p.add_run(f"[{title}] ")
    run_title.bold = True
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(10)
    run_title.font.color.rgb = RGBColor(15, 27, 53)
    
    run_text = p.add_run(text)
    run_text.font.name = "Calibri"
    run_text.font.size = Pt(10)
    run_text.font.color.rgb = RGBColor(51, 65, 85)
    
    # Add spacing after callout
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_figure(doc, img_path, caption):
    """Adds a centered image with a styled caption."""
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(5.8))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(12)
        run_cap = p_cap.add_run(f"Figure: {caption}")
        run_cap.italic = True
        run_cap.font.name = "Calibri"
        run_cap.font.size = Pt(9.5)
        run_cap.font.color.rgb = RGBColor(100, 116, 139)
    else:
        p_err = doc.add_paragraph(f"[Image not found: {img_path}]")
        p_err.font.color.rgb = RGBColor(220, 38, 38)

def build_guide():
    doc = Document()
    
    # Page Setup (Letter, 0.8 in margins)
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    NAVY = RGBColor(15, 27, 53)
    GOLD = RGBColor(217, 119, 6)
    SLATE = RGBColor(71, 85, 105)
    DARK = RGBColor(30, 41, 59)
    
    # Header Banner Table
    banner_table = doc.add_table(rows=1, cols=1)
    banner_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    banner_cell = banner_table.rows[0].cells[0]
    banner_cell.width = Inches(6.9)
    set_cell_background(banner_cell, "0F1B35")
    set_cell_margins(banner_cell, top=200, bottom=200, left=240, right=240)
    
    bp = banner_cell.paragraphs[0]
    bp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    bp.paragraph_format.space_after = Pt(2)
    r_sub = bp.add_run("COMEDKARES INNOVATION HUBS\n")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(10)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(245, 158, 11)
    
    r_main = bp.add_run("HubQuiz: Mentor Operational Guide & FAQ")
    r_main.font.name = "Arial"
    r_main.font.size = Pt(20)
    r_main.font.bold = True
    r_main.font.color.rgb = RGBColor(255, 255, 255)
    
    bp2 = banner_cell.add_paragraph()
    bp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    bp2.paragraph_format.space_before = Pt(4)
    bp2.paragraph_format.space_after = Pt(0)
    r_desc = bp2.add_run("Complete Step-by-Step Manual for Hosting Real-Time Classroom Assessments")
    r_desc.font.name = "Calibri"
    r_desc.font.size = Pt(11)
    r_desc.font.color.rgb = RGBColor(203, 213, 225)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    
    # Metadata Box
    meta_table = doc.add_table(rows=3, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_rows = [
        ("Target Audience:", "ComedKares Mentors, Hub In-Charges, Academic Leads, Program Coordinators"),
        ("Platform Access:", "Integrated directly into ComedKares LMS (Online Tests Tab) / hubquiz.vercel.app"),
        ("Release Version:", "Version 2.4 - Full LMS Single Sign-On (SSO) & Automatic Failover Enabled")
    ]
    for i, (label, val) in enumerate(meta_rows):
        row_cells = meta_table.rows[i].cells
        row_cells[0].width = Inches(1.8)
        row_cells[1].width = Inches(5.1)
        set_cell_background(row_cells[0], "F8FAFC")
        set_cell_background(row_cells[1], "FFFFFF")
        set_cell_margins(row_cells[0], top=60, bottom=60, left=100, right=100)
        set_cell_margins(row_cells[1], top=60, bottom=60, left=100, right=100)
        
        p0 = row_cells[0].paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.name = "Calibri"
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = NAVY
        
        p1 = row_cells[1].paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(val)
        r1.font.name = "Calibri"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = DARK
        
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # SECTION 1
    h1 = doc.add_heading("1. Executive Summary: What is HubQuiz?", level=1)
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(6)
    for r in h1.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)
        
    p = doc.add_paragraph(
        "HubQuiz is ComedKares' proprietary, interactive live quiz platform engineered specifically for our innovation hub workshops "
        "and training batches. It replaces commercial subscription platforms such as Kahoot and Mentimeter with a tailored, "
        "zero-friction solution built directly for our curriculum."
    )
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    for r in p.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        r.font.color.rgb = DARK
        
    p_benefits = doc.add_paragraph()
    p_benefits.paragraph_format.space_after = Pt(6)
    p_benefits.paragraph_format.line_spacing = 1.15
    benefits = [
        ("Zero Student Setup: ", "Students do not download apps, create accounts, or remember passwords. They simply scan a QR code with their phone camera or enter a 6-digit PIN on any mobile browser."),
        ("One-Click LMS Single Sign-On (SSO): ", "Mentors do not need a separate password. Clicking the 'Start Live Quiz' button inside any LMS batch automatically opens and logs your hub into HubQuiz."),
        ("Curriculum Pre-loaded: ", "Assessments for Innovation & Design Thinking (IDT), VTU modules, and special workshops are pre-configured with 10 questions each, ready to launch with a single click."),
        ("High Reliability & Automatic Failover: ", "The platform runs on a dual-tier backend architecture. It connects to the high-speed local JP Nagar hub server for zero-latency in-person games and automatically fails over to Cloud backup if internet connectivity drops.")
    ]
    for title, desc in benefits:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(3)
        bp.paragraph_format.line_spacing = 1.15
        r_b = bp.add_run(title)
        r_b.bold = True
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(10.5)
        r_b.font.color.rgb = NAVY
        r_d = bp.add_run(desc)
        r_d.font.name = "Calibri"
        r_d.font.size = Pt(10.5)
        r_d.font.color.rgb = DARK

    add_callout(
        doc,
        "HubQuiz was designed to make classroom knowledge checks lively, fast, and 100% dependable. "
        "A typical 10-question assessment takes only 7 to 8 minutes of classroom time and provides immediate insights into batch comprehension.",
        title="WHY IT MATTERS"
    )

    # SECTION 2
    h2 = doc.add_heading("2. Accessing HubQuiz Directly from the LMS", level=1)
    h2.paragraph_format.space_before = Pt(16)
    h2.paragraph_format.space_after = Pt(6)
    for r in h2.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)

    p2 = doc.add_paragraph(
        "You do not need to navigate to external websites or search for login credentials. "
        "HubQuiz is integrated right where you manage your batch in the ComedKares LMS portal."
    )
    p2.paragraph_format.space_after = Pt(6)
    p2.paragraph_format.line_spacing = 1.15
    for r in p2.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        r.font.color.rgb = DARK

    steps_lms = [
        ("Step 1: ", "Log in to the ComedKares LMS portal with your mentor credentials."),
        ("Step 2: ", "Navigate to your active batch (e.g., IDT Test Batch, Kalaburagi Robotics Batch, etc.)."),
        ("Step 3: ", "Click on the Online Tests tab in the secondary navigation bar."),
        ("Step 4: ", "Look for the orange ((•)) Start Live Quiz button located right next to '+ Create Quiz'. Click this button to launch HubQuiz.")
    ]
    for s_title, s_desc in steps_lms:
        sp = doc.add_paragraph(style='List Bullet')
        sp.paragraph_format.space_after = Pt(3)
        sp.paragraph_format.line_spacing = 1.15
        r_st = sp.add_run(s_title)
        r_st.bold = True
        r_st.font.name = "Calibri"
        r_st.font.size = Pt(10.5)
        r_st.font.color.rgb = NAVY
        r_sd = sp.add_run(s_desc)
        r_sd.font.name = "Calibri"
        r_sd.font.size = Pt(10.5)
        r_sd.font.color.rgb = DARK

    add_figure(doc, "D:/Anti_spamm/assets/hubquiz/lms_placement.png", "LMS Batch View: Locating the orange ((•)) Start Live Quiz button under the Online Tests tab.")

    add_callout(
        doc,
        "Clicking 'Start Live Quiz' generates a secure single-use token and opens HubQuiz in a new browser tab. "
        "Your hub profile (e.g. blryelahanka.hub@comedkares.org) is automatically authenticated, skipping the login screen entirely.",
        title="ONE-CLICK SSO FEATURE"
    )

    # SECTION 3
    h3 = doc.add_heading("3. The Mentor Dashboard & Pre-loaded Quizzes", level=1)
    h3.paragraph_format.space_before = Pt(16)
    h3.paragraph_format.space_after = Pt(6)
    for r in h3.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)

    p3 = doc.add_paragraph(
        "Upon entering HubQuiz, you arrive at the Mentor Dashboard. The dashboard gives you instant access to your quiz repository, "
        "quick curriculum import buttons, and your game history from the past 24 hours."
    )
    p3.paragraph_format.space_after = Pt(6)
    p3.paragraph_format.line_spacing = 1.15
    for r in p3.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        r.font.color.rgb = DARK

    add_figure(doc, "D:/Anti_spamm/assets/hubquiz/hubquiz_home_page.png", "Mentor Dashboard: Showing quiz cards, 1-click curriculum import shortcuts, and the + New Quiz button.")

    dash_features = [
        ("Quick Curriculum Imports: ", "Buttons at the top allow you to re-import standard sets anytime, including 13 IDT Quizzes, 6 VTU Curriculum Quizzes, or RNSIT Pre-Assessments."),
        ("Quiz Cards: ", "Each quiz displays its title, total question count, and creation status. Every card contains a '▶ Start' button, an Edit pencil icon, and a Delete trash icon."),
        ("Create Custom Quizzes: ", "Click '+ New Quiz' on the top-right to create a completely new quiz tailored for your workshop session."),
        ("Recent Games History: ", "Scroll down to see sessions hosted in the past 24 hours along with final participant counts and game PINs.")
    ]
    for f_title, f_desc in dash_features:
        dp = doc.add_paragraph(style='List Bullet')
        dp.paragraph_format.space_after = Pt(3)
        dp.paragraph_format.line_spacing = 1.15
        r_ft = dp.add_run(f_title)
        r_ft.bold = True
        r_ft.font.name = "Calibri"
        r_ft.font.size = Pt(10.5)
        r_ft.font.color.rgb = NAVY
        r_fd = dp.add_run(f_desc)
        r_fd.font.name = "Calibri"
        r_fd.font.size = Pt(10.5)
        r_fd.font.color.rgb = DARK

    # SECTION 4
    h4 = doc.add_heading("4. Customizing and Editing Quizzes", level=1)
    h4.paragraph_format.space_before = Pt(16)
    h4.paragraph_format.space_after = Pt(6)
    for r in h4.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)

    p4 = doc.add_paragraph(
        "You have complete freedom to adapt pre-loaded quizzes or refine questions based on your batch's pace. "
        "To edit any quiz, click the pencil icon next to the '▶ Start' button on its quiz card."
    )
    p4.paragraph_format.space_after = Pt(6)
    p4.paragraph_format.line_spacing = 1.15
    for r in p4.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        r.font.color.rgb = DARK

    add_figure(doc, "D:/Anti_spamm/assets/hubquiz/edit_quiz_option.png", "Opening the Quiz Editor: Click the pencil icon on the quiz card.")

    p4_sub = doc.add_paragraph(
        "The Quiz Editor opens in an interactive modal. Here you can modify the quiz title, edit question descriptions, "
        "add or remove answer choices, and designate the correct answer by selecting the corresponding radio button."
    )
    p4_sub.paragraph_format.space_after = Pt(6)
    p4_sub.paragraph_format.line_spacing = 1.15
    for r in p4_sub.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        r.font.color.rgb = DARK

    add_figure(doc, "D:/Anti_spamm/assets/hubquiz/edit_page.png", "Quiz Editor View: Modifying question text, reassigning answer options, and selecting the correct answer.")

    edit_tips = [
        ("Designating Correct Answer: ", "Click the radio button next to Option A, B, C, or D to set it as the correct key. The selected option will highlight clearly."),
        ("Question Reordering & Deletion: ", "You can delete individual questions using the trash can icon on the right side of each question card."),
        ("Saving Changes: ", "Scroll to the bottom of the editor modal and click 'Save Quiz'. Your changes take effect immediately for all subsequent live sessions.")
    ]
    for et_title, et_desc in edit_tips:
        ep = doc.add_paragraph(style='List Bullet')
        ep.paragraph_format.space_after = Pt(3)
        ep.paragraph_format.line_spacing = 1.15
        r_et = ep.add_run(et_title)
        r_et.bold = True
        r_et.font.name = "Calibri"
        r_et.font.size = Pt(10.5)
        r_et.font.color.rgb = NAVY
        r_ed = ep.add_run(et_desc)
        r_ed.font.name = "Calibri"
        r_ed.font.size = Pt(10.5)
        r_ed.font.color.rgb = DARK

    # SECTION 5
    h5 = doc.add_heading("5. Launching a Live Session & The Phone Display Option", level=1)
    h5.paragraph_format.space_before = Pt(16)
    h5.paragraph_format.space_after = Pt(6)
    for r in h5.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)

    p5 = doc.add_paragraph(
        "When you are ready to conduct the quiz in class, click '▶ Start' on the desired quiz card. "
        "Connect your laptop to the classroom projector so the entire room can see the lobby."
    )
    p5.paragraph_format.space_after = Pt(6)
    p5.paragraph_format.line_spacing = 1.15
    for r in p5.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        r.font.color.rgb = DARK

    add_figure(doc, "D:/Anti_spamm/assets/hubquiz/quiz_session_start.png", "Live Quiz Lobby: Showing QR code, 6-digit Game PIN, live participant counter, and the Phone Questions toggle.")

    p5_steps = [
        ("1. Display PIN and QR Code: ", "Students scan the large QR code with their mobile cameras, which opens the game link directly. Alternatively, students can open hubquiz.vercel.app/play and enter the 6-digit Game PIN."),
        ("2. Real-Time Player Roster: ", "As students type their names and join, their names appear dynamically in the 'Players Joined' box with an active participant count."),
        ("3. Important Setting: 'Show questions on participant phones': ", "Notice the checkbox indicated by the red arrow. By default, questions appear only on the host projector screen. If you check this box, question text and answer choices will be transmitted directly to students' phone screens. This is especially helpful in large seminar halls where students seated in back rows cannot easily read the projector screen."),
        ("4. Launch the Game: ", "Once all participating students have joined the lobby, click the golden '▶ Start Quiz' button to begin.")
    ]
    for s_title, s_desc in p5_steps:
        lp = doc.add_paragraph(style='List Bullet')
        lp.paragraph_format.space_after = Pt(4)
        lp.paragraph_format.line_spacing = 1.15
        r_lt = lp.add_run(s_title)
        r_lt.bold = True
        r_lt.font.name = "Calibri"
        r_lt.font.size = Pt(10.5)
        r_lt.font.color.rgb = NAVY
        r_ld = lp.add_run(s_desc)
        r_ld.font.name = "Calibri"
        r_ld.font.size = Pt(10.5)
        r_ld.font.color.rgb = DARK

    # SECTION 6
    h6 = doc.add_heading("6. Running the Game: Live Host Controls", level=1)
    h6.paragraph_format.space_before = Pt(16)
    h6.paragraph_format.space_after = Pt(6)
    for r in h6.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)

    p6 = doc.add_paragraph(
        "During live gameplay, the host screen acts as the master broadcast console. "
        "Questions are presented with high-contrast color cards, an animated circular timer, and real-time response counters."
    )
    p6.paragraph_format.space_after = Pt(6)
    p6.paragraph_format.line_spacing = 1.15
    for r in p6.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        r.font.color.rgb = DARK

    add_figure(doc, "D:/Anti_spamm/assets/hubquiz/quiz_question.png", "Host Question Screen: Active 30-second countdown timer, live response tracker, and color-coded answer blocks.")

    p6_controls = [
        ("30-Second Question Timer: ", "Each question counts down from 30 seconds with an animated green circle. Background synthesizer music plays automatically to build classroom engagement (you can mute audio anytime via the speaker icon)."),
        ("Live Answer Tracker: ", "The top-right corner displays 'X / Total answered' in real time. Once all connected students have locked in their answers, the timer concludes automatically."),
        ("Skip Timer Button (⏭ Skip Timer): ", "If all students in class have submitted early or if you wish to proceed immediately, click 'Skip Timer' on the bottom right to advance to the answer reveal."),
        ("Answer Reveal & Analytics: ", "When time expires, HubQuiz displays an immediate bar chart showing how many students picked each option (A, B, C, D). The correct answer is highlighted with a green checkmark, allowing you to explain the concept on the spot."),
        ("Leaderboard: ", "Click 'Next' to view the top 5 students ranked by combined accuracy and response speed. Scores update live with animated point additions."),
        ("Podium Celebration: ", "After Question 10, the session concludes with a 1st, 2nd, and 3rd place podium animation complete with confetti celebrations.")
    ]
    for c_title, c_desc in p6_controls:
        cp = doc.add_paragraph(style='List Bullet')
        cp.paragraph_format.space_after = Pt(3)
        cp.paragraph_format.line_spacing = 1.15
        r_ct = cp.add_run(c_title)
        r_ct.bold = True
        r_ct.font.name = "Calibri"
        r_ct.font.size = Pt(10.5)
        r_ct.font.color.rgb = NAVY
        r_cd = cp.add_run(c_desc)
        r_cd.font.name = "Calibri"
        r_cd.font.size = Pt(10.5)
        r_cd.font.color.rgb = DARK

    # SECTION 7
    h7 = doc.add_heading("7. Comprehensive Frequently Asked Questions (FAQ)", level=1)
    h7.paragraph_format.space_before = Pt(16)
    h7.paragraph_format.space_after = Pt(6)
    for r in h7.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)

    faqs = [
        ("Q1: Where do I find the Start Live Quiz button?",
         "Log in to the ComedKares LMS, open your batch, and click the 'Online Tests' tab in the top tab menu. The orange '((•)) Start Live Quiz' button is located at the top of the test list."),
        
        ("Q2: Do I need separate login credentials for HubQuiz?",
         "No. Clicking the 'Start Live Quiz' button in your LMS automatically signs you in using Single Sign-On (SSO). It maps your active LMS mentor identity to your hub's HubQuiz workspace seamlessly."),
        
        ("Q3: Do students need an app or account to join?",
         "No. Students do not need to download any application, and they never need to register an account. They only need a phone with a web browser. Scanning the QR code or visiting hubquiz.vercel.app/play and typing their name is all that is required."),
        
        ("Q4: Can students see the question text on their phones?",
         "Yes, if you enable the 'Show questions on participant phones' checkbox in the game lobby before clicking 'Start Quiz'. If unchecked, students see the 4 colored symbol buttons and look at your projector screen for the question."),
        
        ("Q5: Can I edit the pre-loaded IDT and VTU quizzes?",
         "Yes. On any quiz card on your dashboard, click the pencil icon. You can adjust question wording, update options, remove questions, or add new ones to match your specific lesson plan."),
        
        ("Q6: What happens if my browser tab closes accidentally during a game?",
         "HubQuiz features an automatic Session Recovery system. If you reopen the dashboard, it detects your active session and asks 'Active Game Found - Do you want to resume?'. Click 'Resume' to restore your game with all connected students intact."),
        
        ("Q7: What if classroom internet is slow or unstable?",
         "HubQuiz is optimized with an ultralight realtime protocol that consumes less than 50 KB of data per game. It operates reliably even on 3G and 4G mobile hotspots. Furthermore, the platform automatically switches between local hub servers and Cloud failover."),
        
        ("Q8: What if a student accidentally refreshes their phone browser?",
         "The student's browser preserves their player identity in local storage. When they reopen the page or tap 'Rejoin Game', they are placed right back into the active question without losing their score."),
        
        ("Q9: How are student scores calculated?",
         "HubQuiz awards up to 1,000 points per question based on correctness and speed. Fast correct answers earn maximum points. Incorrect answers earn zero points."),
        
        ("Q10: How many students can join a single game session?",
         "A single session comfortably accommodates up to 200 simultaneous students on cloud backup, and unlimited concurrent participants when connected to local hub servers."),
        
        ("Q11: Can I turn off the game music?",
         "Yes. There is a speaker mute button located at the top right of your dashboard and in the lobby. Clicking it toggles background synthesizer audio on or off."),
        
        ("Q12: Who can access the Admin Dashboard or switch servers?",
         "The server switcher and Admin Dashboard are strictly restricted to system administration (admin@comedkares.org). Regular mentor accounts connect automatically to the best available server without needing any manual configuration.")
    ]

    for q, a in faqs:
        qp = doc.add_paragraph()
        qp.paragraph_format.space_before = Pt(8)
        qp.paragraph_format.space_after = Pt(2)
        qp.paragraph_format.line_spacing = 1.15
        r_q = qp.add_run(q)
        r_q.bold = True
        r_q.font.name = "Calibri"
        r_q.font.size = Pt(11)
        r_q.font.color.rgb = NAVY
        
        ap = doc.add_paragraph()
        ap.paragraph_format.space_before = Pt(0)
        ap.paragraph_format.space_after = Pt(6)
        ap.paragraph_format.line_spacing = 1.15
        r_a = ap.add_run(a)
        r_a.font.name = "Calibri"
        r_a.font.size = Pt(10.5)
        r_a.font.color.rgb = DARK

    # SECTION 8: Quick Troubleshooting Table
    h8 = doc.add_heading("8. Quick Troubleshooting Reference", level=1)
    h8.paragraph_format.space_before = Pt(16)
    h8.paragraph_format.space_after = Pt(6)
    for r in h8.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)

    t_table = doc.add_table(rows=1, cols=3)
    t_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_table.autofit = False
    
    headers = ["Observed Issue", "Probable Cause", "Recommended Solution"]
    widths = [Inches(1.8), Inches(2.2), Inches(2.9)]
    
    hdr_cells = t_table.rows[0].cells
    for i, h_text in enumerate(headers):
        hdr_cells[i].width = widths[i]
        set_cell_background(hdr_cells[i], "0F1B35")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        hp = hdr_cells[i].paragraphs[0]
        hp.paragraph_format.space_after = Pt(0)
        r = hp.add_run(h_text)
        r.bold = True
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    trouble_data = [
        ("Student phone says 'Game not found'", "Typo in the 6-digit Game PIN.", "Ask student to re-enter the exact 6-digit PIN shown on the projector screen, or rescan the QR code."),
        ("No sound during live quiz", "Browser autoplay policy or tab muted.", "Click anywhere on the host screen to unlock Web Audio, and verify the speaker toggle is unmuted."),
        ("Student cannot read projector from back row", "Large classroom or poor projector resolution.", "Ensure the 'Show questions on participant phones' checkbox was enabled in the lobby before starting."),
        ("Start Live Quiz button does not open HubQuiz", "Browser popup blocker active.", "Allow popups for the LMS domain in your browser settings bar, then click the button again."),
        ("Accidentally closed browser tab", "Accidental tab closure during session.", "Reopen hubquiz.vercel.app/host. Click 'Resume' on the prompt to restore the ongoing session instantly.")
    ]
    
    for row_idx, (issue, cause, sol) in enumerate(trouble_data):
        row = t_table.add_row()
        bg_col = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate([issue, cause, sol]):
            cell = row.cells[c_idx]
            cell.width = widths[c_idx]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.color.rgb = DARK
            if c_idx == 0:
                r.bold = True
                
    doc.add_paragraph().paragraph_format.space_after = Pt(16)
    
    # SECTION 9: Contact & Support
    h9 = doc.add_heading("9. Support and Assistance", level=1)
    h9.paragraph_format.space_before = Pt(16)
    h9.paragraph_format.space_after = Pt(6)
    for r in h9.runs:
        r.font.name = "Arial"
        r.font.color.rgb = NAVY
        r.font.size = Pt(14)
        
    p9 = doc.add_paragraph(
        "If you encounter any questions or require custom quiz packages loaded for your hub, "
        "please reach out directly to the academic operations and technical team:"
    )
    p9.paragraph_format.space_after = Pt(6)
    p9.paragraph_format.line_spacing = 1.15
    for r in p9.runs:
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        r.font.color.rgb = DARK
        
    contacts = [
        ("Technical & LMS Support: ", "admin@comedkares.org"),
        ("Academic Coordination: ", "Academic Head & Lead Mentors"),
        ("Live HubQuiz Web App: ", "https://hubquiz.vercel.app")
    ]
    for c_title, c_val in contacts:
        cp = doc.add_paragraph(style='List Bullet')
        cp.paragraph_format.space_after = Pt(3)
        cp.paragraph_format.line_spacing = 1.15
        r_ct = cp.add_run(c_title)
        r_ct.bold = True
        r_ct.font.name = "Calibri"
        r_ct.font.size = Pt(10.5)
        r_ct.font.color.rgb = NAVY
        r_cv = cp.add_run(c_val)
        r_cv.font.name = "Calibri"
        r_cv.font.size = Pt(10.5)
        r_cv.font.color.rgb = DARK

    # Save to both Desktop and Anti_spamm
    desktop_out = r"C:\Users\DELL\Desktop\ComedKares_HubQuiz_Mentor_Guide.docx"
    repo_out = r"D:\Anti_spamm\ComedKares_HubQuiz_Mentor_Guide.docx"
    
    doc.save(desktop_out)
    doc.save(repo_out)
    print(f"SUCCESS: Saved to {desktop_out}")
    print(f"SUCCESS: Saved to {repo_out}")

if __name__ == "__main__":
    build_guide()
