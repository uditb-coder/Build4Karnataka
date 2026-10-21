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
  - The 20-question Design Thinking Pre-Assessment quiz titled **"RNSIT Pre Assesment"** has been automatically loaded into every mentor and hub account.
  - Topics covered: Design Thinking stages (Empathize, Define, Ideate, Prototype, Test), Empathy Mapping, Problem Framing ("How Might We"), Stakeholder Analysis, Observations vs Assumptions, 5-Why analysis, Brainstorming & Crazy 8s, Low-Fidelity Prototyping, Testing Mindsets, and Minimum Viable Product (MVP).
- **How to Host the Quiz**:
  1. Log in to HubQuiz (`hubquiz.vercel.app` or via your LMS Hub shortcut).
  2. Locate **"RNSIT Pre Assesment" (20 Questions)** on your dashboard.
  3. Click **Start** to open the waiting lobby, project the PIN/QR code for students, and begin the session.
- **One-Click Re-Import**:
  - If you ever delete or modify your quiz and want a clean fresh copy, simply click the **"Import RNSIT Pre-Assessment"** button at the top of your dashboard.
