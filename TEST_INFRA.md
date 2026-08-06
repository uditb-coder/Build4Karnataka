# Comedkares Report Agent Test Infrastructure (TEST_INFRA.md)

## Introduction & Testing Philosophy
The Comedkares Report Agent testing strategy relies on **opaque-box E2E testing**. This approach validates the entire pipeline (Ingestion, Mapping, Rendering, and QA validation layers) by invoking the Command Line Interface (CLI) via `pytest` and verifying:
- Exit codes returned by the CLI.
- Standard error/output messages.
- Generation and correctness of output artifacts (schemas of `knowledge_db.json` and `timeline_mapped.json`, and presence of report `.docx` and `.pdf` files).

By treating the tool as a single unit, we ensure that changes to internal processing do not break the API contract or the expected behavior.

## Directory Structure
```
comedkares_report_agent/
├── main.py                    # CLI Stub / Entry Point
├── tests/
│   ├── conftest.py            # Pytest fixtures (tmp directories, runner utilities)
│   ├── test_tier1_features.py  # Happy-path feature validations (20 tests)
│   ├── test_tier2_boundaries.py# Boundary and edge case validations (20 tests)
│   ├── test_tier3_combos.py    # Cross-feature combinations (7 tests)
│   └── test_tier4_scenarios.py # Real-world deployment scenarios (6 tests)
```

## Detailed Feature Inventory
1. **Feature 1: Ingestion & Data Extraction (F1)**
   - Ingests config.json, schedules (XLSX), student projects (PDF/DOCX), weekly logs, chat logs, feedback (XLSX/CSV).
   - Validates configuration structure and extractions, outputting `knowledge_db.json`.
2. **Feature 2: Timeline & Evidence Mapping (F2)**
   - Reconstructs chronological timeline.
   - Maps JPEG photos to chat messages using a ±5-minute window.
   - Generates captions (Gemini Multimodal API mock/fallback).
   - Outputs `timeline_mapped.json` listing timeline, unmapped photos, and evidence gaps.
3. **Feature 3: Modular Report Renderer (F3)**
   - Generates stylized DOCX reports (Weekly, Monthly, Course Completion, Workshop).
   - Follows theme guidelines (Navy primary, Teal accent, alternating table backgrounds).
   - Compiles output to PDF using LibreOffice (or mocks).
4. **Feature 4: QA Compliance Layer (F4)**
   - Audits mathematical consistency of student/hub counts.
   - Scans and blocks on placeholder tags (e.g. `{{PLACEHOLDER}}`, `[TBD]`).
   - Runs RAG narrative grounding checks against `knowledge_db.json`.
   - Compiles to PDF only if all QA audits pass.

## Test Case Matrix
The test suite consists of exactly **53 test cases** distributed across four tiers:

### Tier 1: Feature Coverage (20 tests, E2E-T1-F1-01 to E2E-T1-F4-20)
- **E2E-T1-F1-01**: Ingest valid config.json and directory structure (Happy Path). Expected exit code: `0`.
- **E2E-T1-F1-02**: Extract Excel schedules & rosters correctly. Expected exit code: `0`.
- **E2E-T1-F1-03**: Parse syllabus proposals from DOCX files. Expected exit code: `0`.
- **E2E-T1-F1-04**: Aggregate learner feedback scores from XLSX/CSV. Expected exit code: `0`.
- **E2E-T1-F1-05**: Extract student project abstracts and domains from PDF. Expected exit code: `0`.
- **E2E-T1-F2-06**: Verify chronological sorting in reconstructed timeline. Expected exit code: `0`.
- **E2E-T1-F2-07**: Map photos to chat messages within a ±5-minute window. Expected exit code: `0`.
- **E2E-T1-F2-08**: Generate captions using mock Gemini API (<25 words, including Hub/Topic). Expected exit code: `0`.
- **E2E-T1-F2-09**: Identify and log evidence gaps for missing sessions. Expected exit code: `0`.
- **E2E-T1-F2-10**: Compile unmapped photos into the `unmapped_photos` array. Expected exit code: `0`.
- **E2E-T1-F3-11**: Validate DOCX theme styles (Navy `#0D1B3E` and Teal). Expected exit code: `0`.
- **E2E-T1-F3-12**: Validate DOCX table styling (alternating light gray `#F0F4F8`). Expected exit code: `0`.
- **E2E-T1-F3-13**: Verify inline captioned photo placement in generated DOCX. Expected exit code: `0`.
- **E2E-T1-F3-14**: Verify LibreOffice PDF compilation from generated DOCX. Expected exit code: `0`.
- **E2E-T1-F3-15**: Verify weekly report type outline generation. Expected exit code: `0`.
- **E2E-T1-F4-16**: QA math audit passes when hub student totals sum matches summary count. Expected exit code: `0`.
- **E2E-T1-F4-17**: QA placeholder check passes when report is clean. Expected exit code: `0`.
- **E2E-T1-F4-18**: QA RAG narrative grounding check passes when claims align with database. Expected exit code: `0`.
- **E2E-T1-F4-19**: QA math audit fails when hub sums diverge from summary count. Expected exit code: `3`.
- **E2E-T1-F4-20**: QA placeholder check fails when tags like `[TBD]` or `{{PLACEHOLDER}}` exist. Expected exit code: `3`.

### Tier 2: Boundary & Corner Cases (20 tests, E2E-T2-F1-21 to E2E-T2-F4-36a)
- **E2E-T2-F1-21**: Ingestion of empty subfolders (e.g. photos/chats empty). Expected exit code: `0`.
- **E2E-T2-F1-22**: Ingestion of syntactically invalid/malformed config.json. Expected exit code: `2`.
- **E2E-T2-F1-23**: Roster Excel contains unknown columns. Expected exit code: `0`.
- **E2E-T2-F1-24**: Chat log contains non-ASCII characters and emojis. Expected exit code: `0`.
- **E2E-T2-F1-24a**: Config with empty hubs/target list. Expected exit code: `2`.
- **E2E-T2-F2-25**: Photo matched at the exact boundary of the ±5-minute window (300 seconds). Expected exit code: `0`.
- **E2E-T2-F2-26**: Match multiple photos to a single chat message window. Expected exit code: `0`.
- **E2E-T2-F2-27**: Gemini API timeout fallback to timestamp-based captions. Expected exit code: `0`.
- **E2E-T2-F2-28**: Handling of future photo timestamps. Expected exit code: `0`.
- **E2E-T2-F2-28a**: Photos with invalid/non-standard file names. Expected exit code: `1`.
- **E2E-T2-F3-29**: Render a massive table exceeding 100 student rows. Expected exit code: `0`.
- **E2E-T2-F3-30**: Fallback handling when system host lacks specific brand fonts. Expected exit code: `0`.
- **E2E-T2-F3-31**: Session lacks photos, rendering an "Evidence Missing" text box placeholder. Expected exit code: `0`.
- **E2E-T2-F3-32**: Output directory is write-protected or permission blocked. Expected exit code: `4`.
- **E2E-T2-F3-32a**: Renderer where report output already exists (overwrite check). Expected exit code: `0`.
- **E2E-T2-F4-33**: Boundary math check with zero students. Expected exit code: `0`.
- **E2E-T2-F4-34**: Detection of malformed or nested placeholder tags (e.g., `{{[NESTED]}}`). Expected exit code: `3`.
- **E2E-T2-F4-35**: Grounding check passes with paraphrased valid narratives. Expected exit code: `0`.
- **E2E-T2-F4-36**: Grounding check fails when narrative contains contradictory claims. Expected exit code: `3`.
- **E2E-T2-F4-36a**: RAG grounding check on empty text (no qualitative claims). Expected exit code: `0`.

### Tier 3: Cross-Feature Combinations (7 tests, E2E-T3-CB-37 to E2E-T3-CB-43)
- **E2E-T3-CB-37**: End-to-end happy-path flow writing all database and report files. Expected exit code: `0`.
- **E2E-T3-CB-38**: Schedule missing a session date that is present in weekly logs. Expected exit code: `0` (warns / logs).
- **E2E-T3-CB-39**: Verification of photo caption layout placement in generated Word document. Expected exit code: `0`.
- **E2E-T3-CB-40**: Rerunning CLI with updated config to resolve a previous QA audit failure. Expected exit code: `0`.
- **E2E-T3-CB-41**: Sequentially generating weekly, monthly, completion, and workshop reports. Expected exit code: `0` (each).
- **E2E-T3-CB-42**: Brand color custom overrides through `--config` file. Expected exit code: `0`.
- **E2E-T3-CB-43**: CLI execution under `--check-only` mode against existing outputs without rebuilding. Expected exit code: `0`.

### Tier 4: Real-World Application Scenarios (6 tests, E2E-T4-RW-44 to E2E-T4-RW-49)
- **E2E-T4-RW-44**: Full workshop report generation scenario with feedback forms. Expected exit code: `0`.
- **E2E-T4-RW-45**: Course completion report scenario with all project abstracts. Expected exit code: `0`.
- **E2E-T4-RW-46**: Stress-testing high-volume datasets (10,000 line chat logs, 500 photos). Expected exit code: `0`.
- **E2E-T4-RW-47**: Fuzzy mapping of regional names and multi-hub name variants. Expected exit code: `0`.
- **E2E-T4-RW-48**: Evidentiary gap weekly report where a week has no images. Expected exit code: `0`.
- **E2E-T4-RW-49**: Multiple validation failures returned simultaneously (e.g. math discrepancy + placeholder tags). Expected exit code: `3`.

## Execution Instructions
Tests are run using `pytest` from the workspace root or the package test directory:
```bash
# Run the entire E2E test suite
python -m pytest comedkares_report_agent/tests/

# Run a specific tier of tests
python -m pytest comedkares_report_agent/tests/test_tier1_features.py

# Run a single test case
python -m pytest comedkares_report_agent/tests/ -k "E2E_T1_F1_01"
```

## Assertions & Code Standards
- **Opaque CLI Execution**: Subprocess calls invoke `python -m comedkares_report_agent.main` with appropriate flags.
- **Exit Code Verification**: Every test case must explicitly assert that the CLI exits with the expected integer code.
- **Outputs Verification**: Tests check for file presence (e.g., `knowledge_db.json`, `timeline_mapped.json`, and reports) in the temporary directories.
- **Console Log / Error Checks**: Tests assert presence of descriptive words like `"Error"`, `"QA Error"`, `"Warning"` on stderr.
