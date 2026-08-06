# Project: Comedkares Report Agent

## Architecture
The Comedkares Report Agent is a command-line tool written in Python. It ingests program raw input folders (schedules, weekly reports, chats, photos, proposals, learner feedback, student projects), extracts and standardizes them into a Comedkares Knowledge Schema JSON database, maps photos to chat timelines using a ±5 min window and Gemini Multimodal captions, renders structured reports in DOCX and compiles them to PDF, and validates quality using a QA layer checking mathematical consistency, placeholders, and RAG grounding.

```
+---------------------------------------------------------------------------------+
|                                  Input Files                                    |
| (config.json, proposals, schedules, weekly logs, chats, photos, feedback, proj) |
+---------------------------------------------------------------------------------+
                                       |
                                       v
                     +-----------------------------------+
                     |    Ingestion & Data Extraction    |
                     +-----------------------------------+
                                       |
                                       v
                    +-------------------------------------+
                    | Comedkares Knowledge Schema (JSON)  |
                    +-------------------------------------+
                                       |
                                       v
                    +-------------------------------------+
                    |  Timeline & Photo Evidence Mapping  | (Gemini Multimodal API)
                    +-------------------------------------+
                                       |
                                       v
                    +-------------------------------------+
                    |       Modular Report Renderer       | (DOCX & PDF)
                    +-------------------------------------+
                                       |
                                       v
                    +-------------------------------------+
                    |        QA Compliance Layer          | (Math, Placeholder, RAG Grounding)
                    +-------------------------------------+
                                       |
                                       v
                              [Final Report PDF]
```

## Code Layout
- `comedkares_report_agent/main.py`: Entry point CLI.
- `comedkares_report_agent/ingestion/`: Ingests raw files, parses structured/unstructured formats, outputs schema JSON.
- `comedkares_report_agent/mapping/`: Reconstructs timeline, aligns photos to messages, calls Gemini API for captions, produces manifest.
- `comedkares_report_agent/renderer/`: Generates stylized DOCX reports and compiles them to PDF.
- `comedkares_report_agent/qa/`: Runs QA compliance guardrails (math checks, placeholder checks, RAG grounding checks).

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| E2E | E2E Testing Track | Designs, implements, and compiles E2E test suite (Tiers 1-4) | None | IN_PROGRESS (Conv ID: 1f8ee2ce-2c22-41c3-83e5-c1db1ff5a21a) |
| 1 | Ingestion & Schema | Parse config.json, schedules, logs, etc. output JSON schema | None | IN_PROGRESS (Conv ID: df88b81e-a4d1-4519-b463-12e4e9cd93f0) |
| 2 | Photo Mapping & Captioning | Reconstruct timeline, map photos (±5m), call Gemini API for captions | M1 | PLANNED |
| 3 | Report Renderer | Dynamically generate DOCX and compile to PDF using LibreOffice | M2 | PLANNED |
| 4 | QA Compliance Layer | Verify math, check placeholders, RAG narrative grounding | M3 | PLANNED |
| 5 | Final Integration & Hardening | Phase 1: Pass 100% E2E test suite. Phase 2: Adversarial hardening | M4, E2E | PLANNED |

## Interface Contracts
### Ingestion -> Mapping
- Output: `knowledge_db.json` containing standardized Hubs, Schedules, Weekly Logs, Student Projects, and Feedback data.
- Format:
  ```json
  {
    "program_name": "...",
    "academic_year": "...",
    "hubs": [
      {
        "hub_id": "...",
        "hub_name": "...",
        "students": [
          {"name": "...", "team": "..."}
        ]
      }
    ],
    "sessions": [
      {"hub_id": "...", "date": "YYYY-MM-DD", "topic": "...", "facilitator": "...", "attendance": 12}
    ]
  }
  ```

### Mapping -> Renderer
- Output: `timeline_mapped.json` containing photo-aligned timeline events and validation manifest.
- Format:
  ```json
  {
    "timeline": [
      {
        "timestamp": "YYYY-MM-DDTHH:MM:SS",
        "type": "chat_message / session / log_entry",
        "description": "...",
        "matched_photos": [
          {
            "photo_path": "...",
            "caption": "Hub Name - Topic - Visual description"
          }
        ]
      }
    ],
    "unmapped_photos": ["..."],
    "evidence_gaps": ["..."]
  }
  ```

### Renderer -> QA
- Output: Draft DOCX path to audit.
