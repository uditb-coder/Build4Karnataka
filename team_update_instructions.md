# Team Update Instructions

## Workflow Updates
- **Newsletter Generation Strategy:** We have transitioned from standard DOCX python automation to generating highly detailed Markdown (`.md`) reports for rich-text publications. This allows for inline CSS styling, better image alignment, and a more magazine-like layout while remaining entirely text-based and easy to version control.
- **Image Referencing:** Ensure that when rendering the Markdown newsletter (`D:\Mgmt_Reports\ComedKares_Jan_Sept_2026_Newsletter.md`), the absolute local paths pointing to `D:\Mgmt_Reports\extracted_images\...` remain valid on the host machine.
- **Copywriting Standard:** Ensure no em-dashes are used in future copy additions, adhering strictly to commas or hyphens.


### Program Activation & Syllabus Uploads
- **Programs Activated**: Several Yelahanka and Mangaluru programs have been enabled in the LMS.
- **Syllabus Automation**: The program syllabi have been bulk-uploaded from the provided document to the `program_syllabus` tables. Note that some programs (like Applied AI) did not have a syllabus in the master document and will need to be manually updated later.

- **Applied AI Syllabus Generation**: Created and successfully injected a 12-week custom syllabus for "Applied AI & Agentic Systems – Semester 6" which was previously missing from the master document.

- **Robotics & System Intelligence Syllabus Generation**: Created and successfully injected a 12-week custom syllabus for "Robotics & System Intelligence – Semester 3" which was previously missing from the master document.

- **Data Science Internship & Semester 5 Syllabus Sync**: Corrected a mapping issue where the 90-day internship was applied to Semester 5. The 96 internship entries are now loaded correctly in the `DATA SCIENCE & AI/ML Internship`, and a new 12-week syllabus has been generated and populated for `Data Science & AI/ML – Semester 5`.

### Flagship Programs HTML Portal
- **New Deliverable**: Created `ComedKares_Flagship_Programs.html`, a fully styled, responsive HTML file containing the collated flagship programs data. 
- **Usage**: The HTML file uses CSS variables for easy updates to the brand colours if required.

- **Refined Deliverable**: Created `ComedKares_Flagship_Programs_v2.html` featuring a streamlined 5-section structure and enhanced visual styling.

- **Collapsible UI Update**: Eliminated horizontal tables for session content and implemented a sleek, mobile-friendly accordion (collapsible) UI.

## Attached Screenshots
![Session Table Before Redesign](./screenshot_1.png)

- **Session Content Restriction**: Restricted the inner content of each session accordion to strictly display only the Session Description, Topics Covered, and Outcomes. All extraneous columns have been removed.

- **Semester Mapping & Filtering**: Each program card header now explicitly displays the mapped semester (e.g., "Semester 1"). Additionally, any session rows related to "CIE deliverables" have been filtered out to ensure only actual training sessions are visible.

- **Main Program UI Update**: Modified the main program cards to behave as collapsible accordions. When clicked, the program's details and session lists expand or collapse natively without needing JavaScript.

- **Session Enumeration**: Replaced the "Week" label in the session breakdown with an automatic sequential "Session 1", "Session 2", etc.

- **Administrative Filtering**: Added logic to successfully filter out administrative sessions like "Program Enrolment Form" and "Pre-Assessment" from the generated HTML view.

![Administrative Filter](./screenshot_2.png)

- **CIE Filter Fix**: Implemented a Regex word-boundary filter to accurately target and remove all sessions titled "CIE:" or containing the exact word "CIE" without falsely matching standard words like "science". 

![CIE Filter](./screenshot_3.png)

- **Internship Title & Description Updates**: Integrated custom descriptions for the Data Science and Robotics internships. Updated their session listings to display "Day X" instead of "Session X", while dynamically stripping out redundant "Day X" text from the titles themselves.

![Internships Update](./screenshot_4.png)

- **IDT Session Content Replacement**: The session coverage for Innovation and Design Thinking (IDT) has been completely rewired. It now actively parses and uses the validated reference data directly from `IDT_Session_Coverage_and_Learning_Activities.docx`, bringing in accurate Descriptions, Topics Covered, and Learning Outcomes for each session.

- **IoT Curriculum Expansion**: Wrote and integrated a detailed 12-session curriculum module for the "Internet of Things (IoT)" program, expanding the provided session topics into full descriptions, learning outcomes, and topic breakdowns. Also populated its missing program description and skills list.

![IoT Missing Data Expansion](./screenshot_5.png)

- **AI/ML Internship Detail Fixes**: Added the specific missing "Skills Acquired" list for the Data Science and AI/ML Internship. Additionally, stripped hardcoded prefix numbers from session titles and dynamically mapped the provided week-by-week topic syllabus to fill in the missing "Topics Covered" fields for all its sessions.

![AI/ML Internship Fixes](./screenshot_6.png)

- **Session Formatting Styling Update**: Redesigned the individual session breakdown sections across all programs. Replaced the generic tags with a unified `.session-section` style container that features the requested solid blue left border, 1rem padding, and bold, uppercase `#5b7b97` colored subheadings that perfectly matches the reference design.

![Session Styling Update](./screenshot_7.png)

- **Session Title Punctuation Cleanup**: Strengthened the regex filtering logic for session titles. It now successfully targets and strips any lingering colons (`:`) or hyphens that might have been left orphaned at the beginning of a title after stripping the "Day X" or numerical prefixes.

![Title Punctuation Cleanup](./screenshot_8.png)

- **Branding Upgrade**: Replaced the subtitle underneath the main page heading with the official ComedKares logo image (`Comedkares-Logo-EPS.png`), giving it a clean white padded background to ensure proper contrast against the dark blue `<header>`.

![Branding Upgrade Request](./screenshot_9.png)

- **Internship Boilerplate Pruning**: Cleared out the heavily repetitive and placeholder "Session Description" text found within the Data Science & AI/ML track syllabus data. This eliminates visual clutter so that the focus directly hits the meticulously mapped `Topics Covered` and `Outcomes`.

![Pruning Boilerplate Text](./screenshot_10.png)

- **Dynamic Content Generation for AI/ML Internship**: Wrote a dynamic contextual content engine (`dsai_content_generator.py`) to systematically analyze the 90+ individual session titles of the Data Science & AI/ML Internship and automatically populate highly specific `Session Descriptions` and `Topics Covered` where the syllabus data was missing or too vague.

![Vague Session Descriptions Replacements](./screenshot_11.png)

- **Applied AI & Agentic Systems Rewrite**: Completely overhauled the program description and outcomes for the Semester 6 Applied AI course to match the newly provided copy. Tools like LangChain and Vector Databases were added strictly to the 'Skills Acquired' pill list rather than hardcoded into the session timelines to ensure marketing safety as requested.

- **Curriculum Normalization and Em-Dash Rule Enforcement**: I completely rewrote the 12-week internal session content for the `Applied AI & Agentic Systems` track, moving it away from the old, hardcoded hackathon data (which had nothing to do with the prompt engineering/RAG syllabus). I wrote a brand new module sequence (`applied_ai_data.py`) with highly detailed, syllabus-appropriate descriptions and clean, comma-separated keywords for 'Topics Covered'.
- Additionally, I implemented a global cleanup rule in the generator script to recursively find and replace any stray em-dashes (`--`) found in the RSI and other programs, converting them to standard hyphens to ensure strict compliance with project copywriting rules.

![RSI Example Reference](./screenshot_12.png)

- **RSI Internship Content Generation**: Analysed the `Robotics & System Intelligence Internship` program and discovered it was suffering from the same repetitive boilerplate descriptions as the DSAI Internship used to have. I wrote a dedicated dynamic Python content generator (`rsi_content_generator.py`) and wired it into the HTML generation pipeline. This automatically scans all 90 days of the RSI Internship, detects keywords (like 'Python', 'Arduino', 'YOLO', 'ROS'), and assigns contextually accurate, highly professional `SESSION DESCRIPTION`s and comma-separated `TOPICS COVERED`, ensuring all programs match the high-quality layout style requested.

- **3-Column Grid Layout Implementation**: Converted the main `.container` from a single-column stacked layout to a responsive 3-column CSS Grid. The max-width was expanded to `1600px` to comfortably accommodate the three columns on large displays, with progressive media queries ensuring it falls back to 2-column or 1-column grids on smaller devices (tablets and mobiles). The cards now use `align-items: start;` so they expand independently without artificially stretching neighbouring cards vertically.
- **Program Removal**: Removed the `PrepIndia Career Readiness` track from the `PROGRAMS` array in the generator configuration, ensuring it is completely excised from the final rendered brochure.

![3-Column Grid Reference](./screenshot_13.png)

- **Multi-Page Architecture Re-factor**: Overhauled the HTML generation pipeline. The system no longer produces a single monolithic, slow-loading accordion page. Instead, it generates a clean `index.html` featuring a perfectly aligned 3-column grid of program cards. When clicked, these cards navigate the user to dedicated standalone HTML pages for each specific program (e.g., `program_innovation___design_thinking.html`). The cards use `display: flex; align-items: center;` to ensure perfectly centered alignment of titles and badges regardless of text wrapping.

![Multi-Page Grid Cards](./screenshot_14.png)

- **Modern 4-Column Card Grid Implementation**: Completely redesigned the `index.html` dashboard grid based on the provided modern white-card reference. The layout has been migrated to a sleek 4-column responsive CSS Grid. The cards now feature a white background with a subtle hover drop-shadow, rounded borders (16px), and a clean vertical flow:
  - Top: Injected SVG iconography corresponding to the program type (stack of layers for standard semesters, a brain for AI/ML, and a robot for RSI).
  - Subheader: Automatically formatted semester identifiers (e.g., "1st Semester", "Internship") in the brand's accent orange color.
  - Body: A dark blue program title, followed by a truncated excerpt of the program description (first 150 characters) designed to equalize card heights naturally.
  - Footer: A bold "LEARN MORE" call-to-action anchored to the bottom.

![Modern 4-Column Dashboard View](./screenshot_15.png)

- **Details Page UI Synchronization**: Ensured every individual program's dedicated page precisely matches the requested detailed UI structure:
  - Fixed a Python string-interpolation bug (`f-string` escaping issue) that temporarily rendered variable names instead of dynamic data in the accordions.
  - Replaced native OS emojis with scalable, monochrome orange SVG icons (Target, Book, Calendar, Tools, Document) for section titles, giving them a perfectly consistent, professional rendering across all devices.
  - Adjusted the grid-boxes for `Program Outcomes` and `Program Overview` to feature the subtle `#f8fafc` background with perfectly scaled orange circle bullet points.
  - Cleaned up the accordion design to maintain a crisp white background with minimalistic typography.

![Details UI Top View](./screenshot_16.png)
![Details UI Accordion View](./screenshot_17.png)

- **Data Science & AI/ML Curriculum Override**: Overrode the default Excel sheet mapping for the "Data Science & AI/ML" (Semester 5) program. Created a dedicated `ds_aiml_data.py` data structure to store the new, highly specific 12-session curriculum provided by the user.
  - The new curriculum covers everything from Python fundamentals and EDA, to math foundations, SQL, and End-to-End ML Pipelines over exactly 12 structured sessions.
  - Modified `generate_multi_page.py` to bypass the `MLOps` spreadsheet for this program and instead dynamically render the custom Python data.

![Data Science & AI/ML Curriculum](./screenshot_18.png)

- **Internship Session Title Regex Fix**: Updated the title cleaning logic (`clean_titles.py`) to systematically remove repetitive "Day X:", "Session X:", and "Week X:" prefixes from the raw dataset. The UI now relies entirely on the programmatic counter (`label = "Day" if "INTERNSHIP" in sheet_name else "Session"`) for the orange pill-tag, ensuring the dark blue session title remains perfectly clean (e.g. `Day 1 | 6 hrs` → `Program Onboarding & Electronics Basics`).

![Cleaned Internship Titles](./screenshot_19.png)

- **ComedKares Knowledge Portal Creation**: Created a new single-page React-like web application (`index.html`) using vanilla HTML, inline CSS, and JavaScript. The portal integrates directly with Supabase for data and Google Auth.
- **Login Restriction**: Implemented a secure Google OAuth flow restricted exclusively to `@erafoundationindia.org` and `@comedkares.org` email accounts.
- **Inline Editor**: Added dynamic "Edit session" and "Add session" admin panels. Admins can seamlessly update sessions on the fly without leaving the portal or requiring redeployments.
- **Unified Media Embeds**: Wired the system to perfectly embed Google Docs, Slides, and external videos inside a unified viewing pane for each session.

![Knowledge Portal Home View](./screenshot_20.png)
![Knowledge Portal Session View](./screenshot_21.png)
![Knowledge Portal Admin Editor](./screenshot_22.png)

## Update - October 8, 2026
* **Session Details**: You will now see a "Revised" date in the top right of the session page indicating when the content was last updated.
* **Layout Adjustments**: The presentation grid has been tweaked. Slides will now appear noticeably larger than the Facilitator Script for easier presenting. The Activity Book preview has also been condensed so it doesn't take up as much screen space.

* **Layout Priorities**: You will notice "Files & Presentation" is now displayed higher on the page than "Resources", allowing mentors to quickly jump into their script.
* **Resources Layout**: Resources are grouped into a neat 2-column list containing Videos, Activity Books, and Reference Articles.

* **Scroll Protection**: When scrolling down the page, embedded documents will no longer "trap" your mouse wheel. You must first click the "Click to interact" overlay to scroll inside the document itself.
* **Loading State**: Files now show a sleek pulsing background while they load, rather than just empty white space.
* **Support Contact**: If a file fails to load or asks for permission, a helpful support message and contact email are now displayed directly underneath the file.

* **Slide Controls**: The native Google Slides controls (previous/next arrows, slide counter) are now visible and fully functional at the bottom of the presentation viewer! No more black bars.
* **Streamlined Spacing**: The entire page spacing has been standardized. The Slides and Script cards are perfectly aligned in height and width ratios, with clean borders and no inner grey gaps. 

* **Improved Slides View**: The maximum width of the layout has been expanded, giving the Slides viewer a much larger preview footprint on big screens.
* **Locked-Down Links**: The "Google Slides" logo on the presentation control bar has been visually blocked to prevent users from accidentally navigating away to the raw file URL.

* **Bigger Slides Layout**: The layout order has been swapped! The Slides player is now positioned on the left side of the grid, taking up the vast majority (75%) of the screen real-estate for a much better viewing experience.
* **Theater Mode Upgrade**: The native popout button in the Google Slides player has been heavily restricted. "Theater Mode" now fullscreens the entire secure wrapper rather than just the raw presentation, keeping our custom protections in place even when viewing full screen!

- **New AI/ML Mechanical Workshop**: A new 5-day workshop titled "5 Day AI/ML for Mechanical Students Skill Lab Workshop" has been created for the Belagavi Hub.
  - A new institute profile was created for "KLS Gogte Institute of Technology (GIT)".
  - The batch is scheduled from 12 October 2026 to 16 October 2026.
  - The 5-day syllabus has been fully parsed and loaded, so mentors can immediately begin using the classwork and session views for this batch.

- **AI/ML Workshop Classwork Availability**: 
  - All 5 daily sessions have been scheduled inside the LMS Classwork tab.
  - The Day 5 Capstone Project is active under the Design Challenges tab. Mentors can guide teams using the recommended public datasets (NASA C-MAPSS, Kaggle Casting Images, etc.).
  - A 10-question Final Assessment Quiz is fully live and will automatically gate the final certificate generation upon passing (70%).
  - Daily Feedback Forms are now accessible natively inside the LMS Feedback tab. No external Google Forms are needed!

- **Modules & Resources Live**: The "Modules" tab in the LMS has now been fully populated. It contains 5 distinct daily modules that include the lesson topics and direct references/links to the exact real-world datasets (Kaggle CNC Mill Tool Wear, NASA C-MAPSS, etc.) mentors should use for each session.

- **Innovation and Design Thinking (IDT) Feedback Forms Now Live Across All Batches**:
  - Mentors across all hubs no longer need to manually construct feedback forms inside their individual batch views.
  - All 16 session feedback forms (Sessions 1 to 16) have been automatically synchronized and mapped across all 34 IDT batches statewide (covering JP Nagar, Tumkur, Mysuru, Hubballi, Kalaburagi, Yelahanka, and Mysuru Road).
  - When opening any IDT batch, navigate to the **Feedback** tab to view the full set of 16 feedback forms ready for responses.

- **Batch Feedback Questions Display Fix**:
  - Resolved an issue where questions inside the "Edit Questions" modal appeared empty when editing batch feedback forms.
  - All feedback questions across all batches now populate properly inside the editor and student forms.

## Update - October 14, 2026: Program Access Control & Request Management
- **Program Permissions & Locked Views**:
  - Curriculum materials, facilitator scripts, presentation decks, and student handouts are now protected based on assigned mentor permissions.
  - If you open a program you are not currently assigned to, you will see a clear **"Access Required"** screen showing the program overview and a **[Request Access to Program]** button.
- **Requesting Program Access**:
  - Simply click **[Request Access]** on the program card or locked session view. You can optionally include a note with your assigned hub or batch.
  - Once submitted, your screen will immediately update to show **"⏳ Access Request Pending Administrator Approval"**.
- **Admin Workflow for Program Grants (`#/admin/access`)**:
  - Administrators will see a **User Access** tab in the top navigation bar with a live count badge indicating pending requests.
  - **Approving Requests**: Click the green **Approve** button to immediately grant access, or **Reject** to decline.
  - **Direct Grant (No Request Needed)**: Admins can proactively grant access to any team member by selecting their name from the team roster and choosing the specific program or **[All Programs]**.
  - **Revoking Access**:
    - *Single Grant*: Click Revoke next to any entry in the Active Grants tab.
    - *All Programs for a User*: Click Revoke All next to any mentor in the Team Members tab to remove their access across all programs.
    - *Program Statewide Revocation*: Filter to a specific program in the Active Grants tab and click Revoke from All to remove access from all non-admin users at once.
- **Program Creation and Default Access**:
  - When adding a new program, administrators can set Initial Mentor Access:
    1. Keep Locked (Mentors request access as needed): Default setting, ideal while drafting new curriculum.
    2. Grant Access to All Team Members Immediately: Automatically provisions access for all team members upon creation.
  - Platform administrators always maintain full unrestricted access to all programs.



## Update - October 21, 2026: RNSIT Pre-Assessment Quiz Available for All Hubs

### What is New
- **RNSIT Pre-Assessment Quiz Now Live**:
  - The refined 14-question Design Thinking Pre-Assessment quiz titled **"RNSIT Pre Assesment"** has been updated across every mentor and hub account. Questions 5, 6, 12, 16, 17, and 18 were removed to keep the quiz focused, and the MVP question was updated to directly test 'What is a Minimum Viable Product (MVP)?'.
  - Topics covered: Design Thinking stages (Empathize, Define, Ideate, Prototype, Test), Empathy Mapping, Problem Framing ("How Might We"), Stakeholder Analysis, Observations vs Assumptions, 5-Why analysis, Brainstorming & Crazy 8s, Low-Fidelity Prototyping, Testing Mindsets, and Minimum Viable Product (MVP).
- **How to Host the Quiz**:
  1. Log in to HubQuiz (`hubquiz.vercel.app` or via your LMS Hub shortcut).
  2. Locate **"RNSIT Pre Assesment" (14 Questions)** on your dashboard.
  3. Click **Start** to open the waiting lobby, project the PIN/QR code for students, and begin the session.
- **One-Click Re-Import**:
  - If you ever delete or modify your quiz and want a clean fresh copy, simply click the **"Import RNSIT Pre-Assessment"** button at the top of your dashboard.

- **RPDT Program Content Live (RNSIT | Mysore Road)**:
  - The complete 7-week syllabus is now available for "Rapid Prototyping & Design Thinking | RNSIT | Mysore Road".
  - Mentors can access the weekly quizzes (Weeks 1 to 7 plus the Final Assessment Quiz) and all 8 session feedback forms directly within the LMS portal without manual configuration.
  - All feedback forms have been pre-synchronized to the active batch (`RNSIT | RPDT | AIML-D | ME 306`) so students and mentors can start collecting responses immediately.

- **Batch Classwork Sessions Live (RNSIT | RPDT | AIML-D | ME 306)**:
  - Mentors can now view the entire 7-session delivery schedule directly under the **Classwork > Sessions** tab for the RNSIT batch.
  - All sessions are scheduled for Thursday afternoons (03:00 PM to 06:00 PM) running through December 2026.
  - The final capstone project is active under the **Design Challenges** tab, configured for team submissions with a 100-point rubric.


## Update - October 22, 2026: Robotics Workshop Content Live (Kalaburagi Hub)

### What is New
- **1-Day Robotics Workshop Content Available**:
  - Content for the 6-hour "Robotics Workshop" in the Kalaburagi hub is now live inside the LMS portal.
  - Students will assemble and control their own 2WD RC mobile bot using dual BO motors, an L298N motor driver, an HC-05 Bluetooth module, and an Arduino Uno.
- **Syllabus Sessions Live**:
  - Mentors can view the complete 7-session breakdown in the program syllabus accordion:
    1. Session 1: Introduction to Robotics & Hardware Components Overview (0.5h)
    2. Session 2: Understanding Robot Components & Working Principles (0.5h)
    3. Session 3: Chassis Mechanical Assembly & Drive Wheel Mounting (1.0h)
    4. Session 4: Power System & Circuit Wiring (1.0h)
    5. Session 5: Arduino IDE Setup & Microcontroller Fundamentals (1.0h)
    6. Session 6: Firmware Programming & HC-05 Bluetooth RC Control Logic (1.0h)
    7. Session 7: Testing, Calibration, Troubleshooting & RC Bot Arena Challenge (1.0h)
- **7 Curriculum Quizzes Configured**:
  - 7 interactive quizzes (10 questions each, totaling 70 questions) are active under the Curriculum section.
  - Covers hardware unboxing, mechanical balance, wiring safety, common grounding, level shifting, serial character decoding ('F', 'B', 'L', 'R', 'S'), and motor brownout troubleshooting.
- **Native Feedback Forms Ready**:
  - All 7 session feedback forms and the End of Workshop Feedback form are active.
  - Forms are synchronized across both the master program curriculum and batch views, eliminating the need to set up external Google Forms.


## Update - October 22, 2026: RPDT (Rapid Prototyping & Design Thinking) Portal Content Live

### What is New for Mentors & Facilitators
- **Complete 8-Week RPDT Curriculum Now Live**:
  - The flagship "Rapid Prototyping and Design Thinking" program (`RPDT`) has been fully compiled and added to the Knowledge Portal catalog (`#/p/RPDT`).
  - Aligned with RNSIT and designed for an 8-week (40-hour) engagement, alternating between 2 hours of active lab facilitation and 1 hour of student portal deliverables (Sessions 1 and 7 feature full 3-hour facilitation).
- **Embedded Slides & Delivery Mode for Every Session**:
  - Each of the 7 sessions includes a verified Google Slides presentation embedded directly into the portal view, complete with presentation controls and Theater Mode.
  - Phased Facilitator Scripts are organized across 5 standardized phases:
    1. *Phase 1 - Hook & Provocation*: Engaging kick-offs, user stories, and provocations.
    2. *Phase 2 - Direct Instruction & Concept Modeling*: Teacher talk-tracks and live demonstrations.
    3. *Phase 3 - Guided Lab Challenge*: Time-boxed, hands-on student builds with mentor checkpoints.
    4. *Phase 4 - Debrief & Assessment*: Formative reflection questions, peer critique, and deliverable logging.
    5. *Phase 5 - Closure & Preview*: Key takeaways and teaser for the upcoming session.
- **Hands-On Lab Activities & Deliverables**:
  - **Session 1**: Catapult Design Challenge (distance battle, build-test-iterate logging).
  - **Session 2**: UI/UX Figma Challenge (clickable high-fi prototypes, 5 Why Titanic case analysis).
  - **Session 3**: Onshape CAD Lab (2D dimensioned sketches for laser cutting, 3D Part Studio modeling, Cura slicing).
  - **Session 4**: Adventuretronics Electronics (LED torch, RGB code lock, LDR automatic street light, circuit soldering).
  - **Session 5**: IoT NodeMCU Lab (ESP8266 Wi-Fi configuration, ThingSpeak live sensor charts, threshold alert rules).
  - **Session 6**: Campus Waste Design Thinking Lab (customer journey mapping, 5W1H/POEMS interviews, empathy & stakeholder mapping, solution-free HMW statements).
  - **Session 7**: Feasibility & Concept Selection Lab (technical/economic/social screening, weighted decision matrices, Rs 3,000-5,000 BOM budget scoping, pitch rehearsal).
- **Research Literature & Video Playlists**:
  - Every session features 4-5 curated academic papers, books, and reference guides (Harvard Business Review, Stanford d.school, Nielsen Norman Group, Maker Media).
  - 4 curated YouTube video links per session are indexed for quick classroom projection or student post-session review.


## Update - October 22, 2026: External User Whitelisting & Admin Visitor Tracker

### What is New for Administrators & Mentors
- **Adding External Users Outside the Organization**:
  - Administrators can now grant access to external collaborators, guest speakers, partner college faculty (e.g. RNSIT, GIT), and external evaluators who use personal Gmail or institutional email addresses.
  - To whitelist an external collaborator:
    1. Navigate to **User Access** in the top navigation bar (`#/admin/access`).
    2. Switch to the **Team Members** tab.
    3. Click the **[+ Whitelist External Member]** button at the top right of the table.
    4. Fill in their Full Name, Google Account Email, Role/Institution, and select their initial program access (e.g. `RPDT`, `★ All Programs`, or leave locked).
    5. Click **Whitelist & Grant Access**.
  - The collaborator can now open the [Knowledge Portal](https://comedkares-knowledge-portal.vercel.app), click **Sign in with Google**, and immediately access their assigned programs.
- **Auto-Whitelisting via Direct Grant**:
  - Administrators using the **Direct Grant Access** tab can also type any external email directly under *-- Other / Enter Email Address --*. Granting access will automatically whitelist the user into the team roster as an "External Member".
- **Confidential Visitor & Content Activity Tracker (Admin Only)**:
  - Administrators now have access to a dedicated **Visitor Tracker** link in the top navigation bar (`#/admin/tracker`).
  - This dashboard is protected by database security policies and is visible only to authorized administrators.
  - **Key Features**:
    - **Visitor Leaderboard**: Identify top active mentors, see which programs each user has explored, and view their last active timestamp.
    - **Content Popularity**: Track which sessions are being viewed the most and how often mentors launch Delivery Mode.
    - **Live Audit Feed**: Monitor recent page visits in real-time.
    - **CSV Export**: Click **[Export Activity CSV]** to download a detailed log for reporting and attendance verification.


## Update - October 22, 2026: Vercel Web Analytics Enabled on HubQuiz

### What is New
- **Live Visitor & Participation Tracking**:
  - Vercel Web Analytics has been integrated directly into the HubQuiz platform (`hubquiz.vercel.app`).
  - The system now records page views, unique visitors, devices, geographical distribution, and participation activity in real time.
- **Viewing Analytics**:
  - Project administrators can log into the [Vercel Dashboard](https://vercel.com), open the **HubQuiz** project, and click the **Analytics** tab to view real-time traffic graphs and student engagement metrics.


## Update - October 22, 2026: Vercel Platform Analytics Live

### Infrastructure Telemetry
- **Vercel Web Analytics Active**: In addition to the internal in-app Visitor Tracker, platform-level analytics from Vercel are now enabled across the portal.
- **Real-Time Traffic Dashboard**: Leadership can monitor global visitor traffic, device breakdowns, and pageview volumes directly from the Vercel project dashboard.


## Update - October 23, 2026: Kalaburagi Robotics Batch Classwork & Feedback Live

### What is New for Mentors in Kalaburagi
- **Kalaburagi Robotics Batch Ready (`Robotics Workshop · Kalaburagi · Oct 2026`)**:
  - All content is live inside the batch portal for Saturday, October 24, 2026.
  - Mentors can navigate directly to the batch to review the delivery schedule, run student feedback checkpoints, and evaluate the final arena challenge.
- **Classwork Schedule (7 Sessions)**:
  - The complete 1-day agenda (09:30 AM to 04:30 PM) is populated under the **Classwork > Sessions** tab.
  - Each session is linked to its matching module (unboxing, component theory, chassis assembly, power wiring, Arduino IDE, Bluetooth firmware, and arena testing).
- **RC Bot Arena Design Challenge Active**:
  - The final hands-on challenge ("RC Bot Bluetooth Arena Challenge & Obstacle Navigation") is live under **Classwork > Design Challenges**.
  - Teams of up to 4 students can submit their bot demo. Mentors can evaluate teams using the built-in 100-point rubric (Chassis Assembly 25 pts, Wiring & Power 25 pts, Bluetooth Firmware 25 pts, Arena Navigation 25 pts).
- **Online Tests / Quizzes Available**:
  - All 7 quizzes (10 questions each) are active under the batch **Online Tests** and **Classwork** views.
- **Single Streamlined Feedback Form Active**:
  - All separate per-session feedback forms have been removed to avoid survey fatigue during the 1-day workshop.
  - A single comprehensive **"Robotics Workshop Feedback"** form is active under the **Feedback** tab.
  - Students will complete this single form at the conclusion of the workshop. Responses are recorded natively within the LMS database, so external Google Forms are not needed.


## Update - October 23, 2026: Login Usability & Admin Access Improvements

### What is New
- **Show/Hide Password Button**:
  - A password visibility toggle button is now available on the login screen. You can tap the eye icon to verify your password before signing in.
- **Direct Admin Dashboard Access**:
  - Administrators are now routed immediately to the Admin Dashboard upon sign-in.
  - One-click admin login is also supported via the SSO shortcut (`?hub=admin`).


## Update - October 23, 2026: One-Click Server Switcher & Login Fix

### What is New
- **Login Loop Resolved**:
  - Fixed an issue where signing in could loop back to the login screen.
  - The login system now recognizes your active session immediately.
- **Manual Server Switcher (JP Nagar vs Cloud)**:
  - You can now see exactly which server you are connecting to right on the login card.
  - If you ever want to force connection to JP Nagar or Cloud, simply click the **(Switch)** link on the login screen or click the server badge in your dashboard header.



## Update - October 23, 2026: Server Switcher Exclusively Reserved for Administrators

### What is New
- **Distraction-Free Login and Dashboard for Mentors**:
  - The server indicator and manual switch buttons are now reserved exclusively for the system administrator (`admin@comedkares.org`).
  - Mentors logging into HubQuiz do not need to choose or switch servers. The system automatically connects you to the primary JP Nagar server, and will automatically switch to Cloud backup if JP Nagar ever goes offline.
- **Administrative Server Switch Controls**:
  - When the administrator enters `admin@comedkares.org` into the login email field, the server switch control becomes active.
  - The administrator can also toggle servers directly inside the Admin Dashboard using the new **Switch Server** button.
- **Stability Improvement**:
  - Fixed an initialization issue where connection checks could temporarily cause an undefined client error on slower networks.
