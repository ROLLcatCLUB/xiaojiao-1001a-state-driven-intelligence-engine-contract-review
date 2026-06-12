# Xiaojiao Dynamic Work Surface E5_R1 To New Product Shape Line Handoff

Date: 2026-06-12

Workspace:

```text
D:\Documents\SmartEdu\xiaobei-core
```

Purpose:

```text
This handoff lets a new Codex session continue from the completed Xiaojiao 1000E5_R1 Dynamic Work Surface mock.
It records the current package evidence, the product-shape diagnosis from review screenshots, and the recommended next line.
It must not be treated as authorization to enter runtime, real frontend integration, provider/model, database, memory, Feishu, formal export, 1000F, or 1001 implementation.
```

## Current Completed Stage

Latest completed package:

```text
1000E5_R1_DYNAMIC_WORK_SURFACE_END_TO_END_MOCK
```

Final status:

```text
XIAOJIAO_DYNAMIC_WORK_SURFACE_END_TO_END_MOCK_PASS
```

Validator marker:

```text
ALL_1000E5_R1_DYNAMIC_WORK_SURFACE_END_TO_END_MOCK_CHECKS_OK
```

Current next stage recorded by package:

```text
1000E5_R1_REVIEW_PENDING_BEFORE_1001
```

Important interpretation:

```text
1000E5_R1 is a static product-shape mock package.
It is not real frontend integration.
It is not runtime.
It is not model/provider work.
It did not enter 1001 or 1000F.
```

## Validation Evidence

Local validator:

```powershell
python scripts/validate_xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.py
python scripts/validate_xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.py --root .
```

Both no-arg and `--root` passed.

ZIP:

```text
docs/audit_packages/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.zip
```

ZIP SHA256:

```text
942EBD042219150F2F108826DAC05A2B63E3C89BB493EBE799DE4E4B7A0BD348
```

ZIP_ENTRY_COUNT:

```text
25
```

Manifest:

```text
docs/audit_packages/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1_manifest.json
```

Manifest alignment:

```text
manifest_minus_zip=[]
zip_minus_manifest=[]
```

GitHub review repo:

```text
https://github.com/ROLLcatCLUB/xiaojiao-1000e5-r1-dynamic-work-surface-review
```

## Current Local Experience Pages

Open these directly in browser:

```text
file:///D:/Documents/SmartEdu/xiaobei-core/samples/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/state_initialized_surface_1000E5_R1.html
file:///D:/Documents/SmartEdu/xiaobei-core/samples/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/state_plan_focus_surface_1000E5_R1.html
file:///D:/Documents/SmartEdu/xiaobei-core/samples/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/state_today_focus_surface_1000E5_R1.html
```

Screenshots:

```text
docs/audit/screenshots/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/initialized_surface_desktop.png
docs/audit/screenshots/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/plan_focus_surface_desktop.png
docs/audit/screenshots/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/today_focus_surface_desktop.png
docs/audit/screenshots/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/initialized_surface_mobile.png
docs/audit/screenshots/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/plan_focus_surface_mobile.png
docs/audit/screenshots/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/today_focus_surface_mobile.png
```

## Required Prior Context To Read

Read these before making changes:

```text
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md
docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_to_new_planning_line_handoff_20260612.md
docs/foundation/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.md
docs/foundation/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.json
samples/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/dynamic_work_surface_fixture_1000E5_R1.json
docs/audit/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1_result.json
docs/audit/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1_report.md
docs/audit_packages/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1_manifest.json
```

## Review Diagnosis To Carry Forward

The latest product review diagnosis must be treated as a product-shape correction, not as mere visual polish.

Core diagnosis:

```text
The problem is not the warm coffee color palette.
The problem is that internal system structure is visible as interface structure.
```

Screenshot 1 diagnosis, warm beige Dynamic Work Surface:

```text
1. "今日工作项主焦点" is an internal state label and should not be teacher-facing.
2. Left big card plus right small cards creates a card-wall feeling.
3. "辅助对象" and "工作记录" are internal/system terms exposed to teachers.
4. The solid dark-brown action button is too heavy for the surface.
5. Left content is too thin while right content is fragmented.
6. Empty space feels uncomposed rather than intentionally directed.
```

Screenshot 2 diagnosis, dark left chat plus right form:

```text
1. It returns to the forbidden "left big chat + right business form" shape.
2. Chat bubbles become the main interface instead of a temporary tool.
3. Horizontal tabs and dense field grids feel like a traditional backend page.
4. Form-field data structure is exposed as the teacher workspace.
5. The timetable has some local value, but the whole structure is wrong for Xiaojiao.
```

Shared root problem:

```text
The interface directly translated internal data structures into visible UI structures.
Dynamic Work Surface must translate internal structures into teacher perception and action logic.
```

## Product Principles To Preserve

Do preserve:

```text
Page is not the product; state is the product.
The teacher sees the current projection of Work State.
Work State -> Work View Composer -> Dynamic Work Surface -> Render Blocks.
Work results are primary; conversation is temporary.
One main focus object should dominate at a time.
Supporting objects should become edge references, quiet affordances, or hidden context.
Xiaojiao prompts should attach near relevant work objects, not live as a central chat stream.
Work record is a record of work-state changes, not chat history.
Teacher-facing language should say what the teacher is doing now, not what the system component is called.
```

Teacher-facing wording rule:

```text
Do not put explanatory paragraphs into the page.
Use short labels, questions, choices, actions, and direct work-object names.
No engineering terms.
No "主焦点", "辅助对象", "状态", "composer", "payload", "fixture", "sufficiency gate" on teacher-facing pages.
Do not put Jarvis into teacher-facing product copy.
```

Recommended teacher-facing replacements:

```text
"今日工作项主焦点" -> "今天"
"今日工作项" -> "今天要处理的课"
"辅助对象" -> remove as title; use object names such as "这节课的设计", "本学期计划", "本周安排"
"工作记录" -> "今天做了什么" or remove the heading and show a quiet activity trace
"展开课时设计" -> a light text action such as "看这节课的设计 ->"
```

## Recommended New Line

Recommended next line:

```text
1000E5_R2_DYNAMIC_WORK_SURFACE_TEACHER_PERCEPTION_REFACTOR
```

Goal:

```text
Refactor the E5_R1 Dynamic Work Surface mock so that internal structure is no longer exposed to the teacher.
Keep it static/reviewable.
Do not integrate with the real frontend.
Do not enter runtime.
Do not enter 1001 yet.
```

Expected outputs:

```text
contract / foundation docs
JSON contract
checklist
result
report
manifest
ZIP
validator
visual smoke screenshots
GitHub review repo upload
```

Required validator support:

```text
no-arg
--root
```

The validator should explicitly check:

```text
No teacher-facing "主焦点".
No teacher-facing "辅助对象".
No teacher-facing "工作记录" if used as an exposed system section label.
No left-side large chat surface.
No dense backend-style tab/form page.
No teacher-facing engineering terms.
No provider/model/database/memory/Feishu/export/runtime integration.
Manifest and ZIP are aligned.
```

## Suggested E5_R2 Product Shape

State A, just initialized:

```text
Teacher sees what can be started now.
Primary object: "本学期工作空间" or a natural first action area.
Quiet affordances: "生成教学工作计划草稿", "补教材目录", "查看本周安排".
No card wall.
No system labels.
```

State B, teaching work plan focus:

```text
Primary object: "教学工作计划草稿".
Supporting references become quiet side notes or reference strips.
Xiaojiao hint attaches beside the relevant missing/uncertain section.
Do not expose "plan_focus" or "main_focus".
```

State C, today focus:

```text
Primary object: "今天".
Items are ordered by lesson/session.
The current lesson is visually dominant.
Related lesson design appears as contextual detail for the selected lesson.
Other references are quiet and visibly subordinate.
```

Interaction logic for review mock:

```text
The selected work item should determine the surrounding context.
Right/edge context must feel related to the selected item, not like an unrelated static column.
Buttons should be light actions unless a single irreversible/primary action truly needs emphasis.
```

## Hard Boundaries

Do not:

```text
Implement real UI in the production frontend.
Modify real frontend pages.
Connect real runtime.
Connect provider/model.
Write database.
Write memory.
Write Feishu.
Create formal export.
Connect classroom student side.
Modify old sealed stages.
Perform blind rename.
Globally replace 小备 with 小教.
Put Jarvis into teacher-facing product copy.
Use large left-side chat as the main interface.
Expose internal system section names in teacher-facing UI.
Turn the Dynamic Work Surface into fixed dead cards.
Turn it into a traditional tab/form backend page.
Enter 1000F.
Enter 1001 without explicit authorization.
```

Stop conditions:

```text
1. Any validator fails after 2 auto-fix rounds.
2. Work requires real UI/runtime/provider/model/database/memory/Feishu/formal export.
3. Work requires blind rename or touching unrelated sealed stages.
4. Manifest / ZIP alignment evidence cannot be generated.
5. Product shape drifts back to left big chat, dense backend forms, or visible internal state labels.
6. The session is about to enter 1001 or 1000F without explicit user authorization.
```

## GitHub Review Upload Habit

Use a dedicated review repo.

Do not upload:

```text
the whole xiaobei-core repo
secrets
environment files
real runtime state
unrelated dirty working tree files
```

Upload only package files listed in the manifest.

Recommended repo name:

```text
xiaojiao-1000e5-r2-dynamic-work-surface-teacher-perception-review
```

If local HTTPS git push is unreliable, use the existing `gh api` clean-tree upload habit.

Include `.gitattributes` to preserve line endings and avoid hash drift:

```text
* text=auto
*.json text eol=lf
*.md text eol=lf
*.py text eol=lf
*.js text eol=lf
*.css text eol=lf
*.html text eol=lf
```

Raw link template:

```text
https://raw.githubusercontent.com/ROLLcatCLUB/<repo>/main/<path>
```

## Prompt For GPT Review After Upload

Use this after the package is uploaded:

```text
Please review the Xiaojiao 1000E5_R2 Dynamic Work Surface teacher-perception refactor package.

Focus on product shape, not implementation polish:

1. Does the page stop exposing internal system terms such as main focus, supporting object, work record, state, composer, payload, or fixture?
2. Does the surface guide teacher attention to one current work object?
3. Are supporting objects clearly subordinate and contextually related?
4. Does Xiaojiao remain a lightweight attached guide rather than a large chat panel?
5. Does it avoid the traditional left-chat/right-form backend shape?
6. Does it avoid dense tabs, field grids, and card-wall feeling?
7. Does teacher-facing copy stay short and work-oriented?
8. Does the package remain static/review-only with no runtime/provider/model/database/memory/Feishu/formal export?

Please return PASS / CONDITIONAL PASS / FAIL and list product-shape blockers first.
```

## New Session Startup Instruction

Paste this into the next Codex session:

```text
You are continuing Xiaojiao Teacher Workbench after 1000E5_R1.

First read:
docs/handoff/xiaojiao_dynamic_work_surface_e5_r1_to_new_product_shape_line_handoff_20260612.md
docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md
docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md
docs/foundation/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.md
docs/foundation/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.json
samples/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1/dynamic_work_surface_fixture_1000E5_R1.json
docs/audit_packages/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1_manifest.json

Then start the next review package:
1000E5_R2_DYNAMIC_WORK_SURFACE_TEACHER_PERCEPTION_REFACTOR

Do not enter 1001 or 1000F.
Do not implement real UI.
Do not modify real frontend pages.
Do not connect runtime/provider/model/database/memory/Feishu/export.

Main product correction:
Stop exposing internal system structures as teacher-facing interface.
Remove teacher-facing "主焦点", "辅助对象", and system-section language.
Avoid left big chat, backend tabs/forms, and card-wall layout.
Make the teacher's current work object the clear first visual target.

Every package must include foundation docs, JSON contract, checklist, result, report, manifest, ZIP, validator, no-arg and --root PASS evidence, and GitHub review upload.
```

