# Management Update Report — Build 4 Karnataka Operations & Buildathon Proposal (v2.0 Ultimate)

## Overview
This report documents the latest functional updates, proposal assets, operational manuals, social media calendars, and workbook tools developed for the **Build 4 Karnataka (ಬಿಲ್ಡ್ 4 ಬೆಂಗಳೂರು)** buildathon.

## Recent Updates

### 1. Build 4 Karnataka Single-Hub Proposal & Master Plan (v6)
- **Event Scope:** Single-hub execution at **JP Nagar Innovation Hub** (South Bengaluru) on Saturday, August 29, 2026 (Tentative).
- **Outreach Framework:** 3 Regional Outreach Squads covering 45 colleges across South (Astle), North (Nivedha), and West (Abhinandan) corridors.
- **Screening Funnel:** 50+ online team applications (₹399 fee) screened down to **25–30 top teams (~100–120 participants)** on-site.
- **Revised Prize Pool:** 🥇 1st Place: ₹20,000 (TDS applies) | 🥈 2nd Place: ₹10,000 (TDS applies) | 🥉 3rd Place: ₹5,000 | 5 Domain Best Builds.
- **Stage Presentation:** Grand Finale live on stage at JP Nagar at 6:30 PM, presented by **CEO & Director, ComedKares**.

### 2. Ultimate Internal Operations Manual (`operations_checklist.md` v2.0)
- **Section 1B — Initial Screening & Selection Criteria:** Detailed 100-point evaluation matrix (30 pts Problem Alignment, 40 pts GenAI/No-Code Feasibility, 30 pts Team Skill Complementarity), online submission fields (Idea Pitch, Tech Stack, Roles), eligibility rules, shortlist cut-offs, and 5-team standby waitlist SOP.
- Detailed directory of Central Operations Leads and 3 Regional Outreach Squads (45 Colleges).
- **Social Media Content Calendar:** Pre-launch teasers, Launch Reel, 5 Domain Spotlight Reels, Jury reveal stories, and countdown posts.
- **Email Marketing Plan (Mailchimp):** 5 segmented campaign waves sent to 12,000+ student & passout database.
- Itemized procurement, merchandise, and vendor payment tracker (~₹99,880 total spend).
- Minute-by-minute day-of master run of show (06:30 AM to 07:30 PM).
- Recommended GenAI/No-Code tools matrix, jury scoring rubric (100% scale + 5% bonus), technical infrastructure checklist, and emergency SOPs.

### 3. 13-Tab Master Planner Excel (`Build4Karnataka_MasterPlanner.xlsx`) — NEW
- **Location:** `D:\Anti_spamm\Build4Karnataka_MasterPlanner.xlsx`
- **Total Sheets:** 13 fully formatted, color-coded, formula-driven tabs
- **Tabs Included:**
  1. 📊 **Dashboard** — KPI blocks (registrations, revenue, budget, prize pool) + clickable navigation hyperlinks to all 12 other sheets
  2. 📋 **Master Timeline** — 40-row phased milestone tracker (5 phases, Pre-Event through Post-Event) with status dropdowns + conditional row coloring
  3. 👥 **Team Registrations** — Live COUNTA/COUNTIF summary bar; 19-column tracker for 50+ teams incl. payment UTR, domain, team roles, idea pitch, tech stack; payment status dropdown + conditional formatting
  4. 🔍 **Screening Tracker** — 100-pt auto-scoring formula (F+G+H=I); color scale on total score; Selected/Waitlisted/Rejected status dropdowns + conditional row formatting
  5. 🗓️ **Day-of ROS** — 40-item minute-by-minute run of show from 5:30 AM setup to 8:00 PM teardown; status dropdowns + Done/In Progress conditional coloring
  6. 💰 **Budget & Financials** — Revenue projection table (with GST formulas) + 28-item expense breakdown + P&L summary with auto-calculated net investment exposure; ₹ number formatting throughout
  7. 🛒 **Procurement Tracker** — 25-line vendor procurement list with unit cost × qty auto-total, delivery dates, order/payment status dropdowns + conditional formatting; Grand Total row
  8. 🏫 **College Outreach** — Full directory of all 45 target colleges organized by South/North/West region with PM assignment, visit date, flyer count, registration count; auto-sum totals; status dropdowns
  9. 🙋 **Staff & Volunteers** — 22-person roster (Core Team, Jury Panel × 4, Volunteers × 12) with roles, zones, shift times, T-shirt sizes, confirmation status
  10. ⚖️ **Jury Scoring** — 5-criterion auto-total scoring formula per team; color scale leaderboard; score range data validation per criterion; Award dropdown; 30-team capacity
  11. 🏆 **Prize & TDS** — Prize distribution table with 30% TDS auto-calculation formulas; full 8-item TDS compliance checklist with deadlines and owners
  12. 📱 **Social Media** — 28-post content calendar from 1 Aug pre-launch through 7 Sep post-event recap; platform, caption, visual brief, hashtags, scheduled time, status dropdown
  13. ⚠️ **Risk & Contingency** — 16-risk register with Likelihood × Impact score (color-scaled), mitigation strategy, contingency plan, owner; status dropdown
- **Excel Features:** Color-coded headers (Dark Navy + Green theme), freeze panes on all sheets, dropdown data validation on all status columns, conditional formatting (Green=Done/Selected, Yellow=In Progress/Pending, Red=Blocked/Rejected), auto-sum formulas, scoring formulas, ₹ currency formatting, hyperlinks from Dashboard to each sheet

### 4. Custom Website & Registration System (`Build4Karnataka_Website.html`) — NEW
- **Portable HTML Page:** Developed a single-file, highly optimized landing page ready for 1-minute deployment on Vercel/Netlify.
- **Brand Alignment:** Fully integrated official ComedKares brand colors (Deep Navy Blue `#071d57` & Bright Orange `#eea022`), new logo integration (`b4b_logo.png`), and official social media footprints.
- **Gallery Integration:** Scraped and embedded real event photos from ComedKares' official gallery (featuring JP Nagar Hub specifically).
- **Registration Flow Overhaul:** Replaced the heavy embedded 4-step form with a streamlined "Proceed to Google Form" CTA box emphasizing the ₹399 fee and UTR requirement.
- **Google Form Generator (`Create_Form.gs`):** Provided a custom Google Apps Script to auto-generate the 4-section Build 4 Karnataka Google Form seamlessly.

---

## Comparison Table
| Feature / Metric | Previous State | Current State |
| --- | --- | --- |
| **Event Location** | Multi-Hub Virtual Broadcast | **1 Physical Venue: JP Nagar Innovation Hub** |
| **Outreach Model** | Hub-restricted | **Citywide 3-Region Squads (45 Target Colleges)** |
| **Selection Flow** | Unrestricted registration | **50+ Online Regs $\rightarrow$ 25–30 Screened On-Site Teams** |
| **Initial Screening Criteria** | Summary mention | **Explicit 100-Pt Matrix (Problem 30%, Feasibility 40%, Skills 30%) + Standby SOP** |
| **Prize Pool** | 1st ₹15k, 2nd ₹7.5k, 3rd ₹3.5k | **🥇 1st ₹20,000 \| 🥈 2nd ₹10,000 \| 🥉 3rd ₹5,000** |
| **Grand Finale Host** | Astle / Udit (Virtual) | **CEO & Director, ComedKares (Live On-Stage)** |
| **Operations Manual** | Basic summary | **Ultimate `operations_checklist.md` (v2.0) + Excel Master Tab** |
| **Total Spend** | ₹93,800 | **₹99,880 (Lean Plan A Budget)** |

---

## UI Screenshots & Documentation Assets
*(Pending user upload: Please provide screenshots of the updated Excel Operations Master Sheet, HTML Dashboard, or Word Proposal view once rendered)*





## GenAI Partnership Strategy Update
- Added AI Platform Partners tier to the website's sponsor section to target Google, Lovable, Emergent, Vercel, and Replit.
- A comprehensive outreach plan and 1-page pitch deck have been developed to secure GenAI API credits and no-code tool access for the 200+ hackathon participants.

## Screening Strategy Update
- Implemented a 2-stage screening process to filter 500+ applicants to the final 200. Stage 1 verifies GitHub/Portfolio links. Stage 2 requires a 'Vibe Check' take-home task (deploying a simple AI-generated app in 48 hours).
- Drafted 5 GenAI-focused problem statements aligned with the 5 domain tracks (Healthcare, EdTech, FinTech, Smart City, Open Innovation).

## Strategic Pivot: Online Industry Hackathon
- Scrapped the offline GenAI partnership strategy in favor of a scalable online-first model targeting specific industries (Healthcare and Robotics).
- Drafted formal partnership proposals focusing on 'Crowdsourced R&D' and zero-friction talent pipelining for companies like Practo, GreyOrange, and Narayana Health.

- **Industry Proposals Update:** Finalized the Healthcare and Robotics proposals by integrating the 9 ComedKares Hub addresses, adjusting the masterclass schedule (pre-event), and outlining flexible problem statement releases.

- **Website Domain & Timeline Pivot:** Updated the Build4Karnataka website with the 5 new official domains (AgriTech, Healthcare, Retail, FinTech, Manufacturing). Shifted the timeline to push registrations to Aug 8th, introduced the Domain Proficiency Mini-Challenge for screening, and added a Networking & Incubation feature.
