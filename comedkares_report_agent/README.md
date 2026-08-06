# Comedkares Report Agent 🎓

An automated, production-grade report generation system for **Comedkares Innovation Hub** that ingests raw program materials and produces styled, audit-compliant institutional reports.

## Features
- 📂 Multi-format data ingestion: PDF, DOCX, XLSX, WhatsApp chats, JPEG photos
- 🗓️ Chronological timeline reconstruction from all source files
- 📸 Automatic photo-to-event mapping via WhatsApp timestamp alignment
- 🤖 AI-powered caption generation (Gemini API)
- 📝 Modular report rendering: Weekly / Monthly / Course Completion / Workshop
- ✅ QA compliance: placeholder detection, math integrity checks, grounding validation
- 🎨 Comedkares brand styling (Navy `#0D1B3E`, Teal `#008B8B`, Gold `#D4AF37`)

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare your input folder
Create a program folder following this structure:
```
sample_input/
├── config.json             # Program metadata and report settings
├── 01_proposals/           # Syllabus, guidelines (PDF/DOCX)
├── 02_schedules/           # Batch rosters, timetables (XLSX)
├── 03_weekly_logs/         # Weekly reports (DOCX/XLSX)
├── 04_chat_logs/           # WhatsApp export (_chat.txt)
├── 05_photos/              # JPEG images (PHOTO-YYYY-MM-DD-HH-MM-SS.jpg)
├── 06_feedback/            # Survey responses (XLSX/CSV)
└── 07_student_projects/    # Project briefs (DOCX/PDF)
```

### 3. Run the agent
```bash
# Generate a Monthly report
python main.py --input sample_input --report-type MONTHLY

# Generate a Workshop Completion report
python main.py --input sample_input --report-type WORKSHOP

# Generate a Course Completion report
python main.py --input sample_input --report-type COURSE_COMPLETION

# Generate a Weekly report
python main.py --input sample_input --report-type WEEKLY
```

### 4. Output
Generated files are written to the `output/` directory:
- `[HUB]_[PROGRAM]_[TYPE]_[DATE].docx`
- `[HUB]_[PROGRAM]_[TYPE]_[DATE].pdf` (if LibreOffice is installed)
- `evidence_manifest.json` (photo mapping validation report)
- `qa_report.json` (QA check results)

## Configuration (`config.json`)
| Field | Description |
|---|---|
| `program_name` | Full name of the program |
| `program_code` | Course code (e.g. `1BIDTL158`) |
| `report_type` | `WEEKLY`, `MONTHLY`, `COURSE_COMPLETION`, `WORKSHOP` |
| `hubs` | List of hub objects with names, colleges, facilitators, batch counts |
| `gemini_api_key` | Gemini API key for photo caption generation (optional) |
| `pdf_compile` | `true` to compile DOCX to PDF via LibreOffice |

## Report Types Supported
| Report Type | Description |
|---|---|
| `WEEKLY` | Per-week facilitator log with session table and evidence photos |
| `MONTHLY` | Single-hub or multi-center consolidated monthly overview |
| `COURSE_COMPLETION` | Full academic report with CO/PO mappings, CIE grades, and project outcomes |
| `WORKSHOP` | Standalone event completion report with participant roster and survey results |
