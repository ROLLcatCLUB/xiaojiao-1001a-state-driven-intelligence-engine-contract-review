# 1001A_XIAOJIAO_STATE_DRIVEN_INTELLIGENCE_ENGINE_CONTRACT

Date: 2026-06-12

## Stage Identity

```text
package_code=1001_XIAOJIAO_STATE_DRIVEN_INTELLIGENCE_ENGINE_PACKAGE
stage_code=1001A_XIAOJIAO_STATE_DRIVEN_INTELLIGENCE_ENGINE_CONTRACT
stage_name=Xiaojiao State Driven Intelligence Engine Contract
stage_type=intelligence_engine_contract_only
final_status_target=XIAOJIAO_STATE_DRIVEN_INTELLIGENCE_ENGINE_CONTRACT_PASS
runtime_change_allowed=false
ui_implementation_allowed=false
provider_model_call_allowed=false
```

## Explicit Authorization Boundary

The previous E5_R1 handoff recorded `Do not enter 1001 without explicit authorization`.

This 1001A package is created from the current 2026-06-12 user instruction that explicitly names and authorizes:

```text
1001A_XIAOJIAO_STATE_DRIVEN_INTELLIGENCE_ENGINE_CONTRACT
```

That authorization is limited to this contract-only package. It does not authorize 1001B implementation, 1000F model candidate work, real frontend changes, runtime connection, provider/model calls, database writes, memory writes, Feishu writes, formal export, or classroom student runtime.

## Purpose

Define how Xiaojiao creates a low-cost Jarvis feeling without calling an LLM on every step.

The core product judgment is:

```text
Xiaojiao's intelligence does not come from thinking again on every turn.
It comes from continuously maintaining Work State and invoking the right intelligence layer at the right moment.
```

Teacher-facing product copy must not expose Jarvis as a brand. `Jarvis` remains an internal planning metaphor only.

## Source Handoffs And Prior Contracts

- `docs/handoff/xiaojiao_dynamic_work_surface_e5_r1_to_new_product_shape_line_handoff_20260612.md`
- `docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md`
- `docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md`
- `docs/foundation/xiaojiao_agent_action_policy_and_work_state_contract_1000D.md`
- `docs/foundation/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.md`

## Core Principle

```text
Work State is the backend core asset, not frontend UI state.
```

The frontend is only a projection of Work State:

```text
Work State -> Work View Composer -> Dynamic Work Surface -> Render Blocks
```

The LLM must not directly control the frontend. Any LLM output must pass through structured parsing, policy gates, Work State update rules, and the Work View Composer before it can affect what a teacher sees.

## Three-Layer Intelligence Model

| Layer | Role | Cost |
| --- | --- | --- |
| Deterministic Logic | click confirmation, state transition, time refresh, marking complete | 0 token |
| Rule Engine | priority, suggestions, view composition, gap reasoning, reminder timing | 0 or extremely low token |
| LLM | content generation, complex revision, open question answering, preference summarization | paid model cost |

This package treats most daily teacher interactions as state and rule work, not model work.

## Module Contract

### A. Intent Parser

Input sources:

```text
teacher text
teacher click
time trigger
work object event
```

Output:

```json
{
  "intent": "view_today",
  "confidence": 0.92,
  "source": "rule",
  "work_object_ref": "lesson_L003",
  "escalation_required": false
}
```

Parsing order:

```text
rule matching
lightweight semantic classification or embedding
LLM escalation only when confidence is low or the request is open-ended
```

Required intent examples:

```text
view_today
view_week
generate_plan
prepare_lesson
confirm_current
revise_section
generate_handout
inspect_gap
ask_open_question
save_preference_candidate
```

### B. Work State Manager

This is the core engine. It maintains:

```text
teacher_profile
temporal_state
focus_state
work_objects
gaps
pending_suggestions
preference_profile
work_log
audit_trace
```

It performs state reasoning such as:

```text
teaching_work_plan.confirmed -> weekly_work_graph.available
lesson_draft.pending_confirmation -> today_work_items.highlight_current_lesson
textbook_catalog.missing -> draft_generation.allowed_with_progress_review_flag
teacher_prefers_shorter_activities -> revision_suggestion.default_to_compact_rhythm
```

The manager owns backend state. It does not expose raw internal state labels directly to teacher-facing UI.

### C. Work View Composer

The composer maps Work State into a teacher-facing surface. It does not call an LLM.

Responsibilities:

```text
choose the current primary work object
decide which supporting objects remain visible
hide irrelevant internal state
attach Xiaojiao hints near the relevant object
prevent chat history from becoming the primary workspace
```

Example output:

```json
{
  "layout": "today_sequence",
  "primary": "today_work_items",
  "supporting": ["week_strip"],
  "hidden": ["semester_plan"],
  "agent_notes": [
    {
      "attach_to": "lesson_L003",
      "text": "草稿已生成，第二环节需要你确认一下。",
      "actions": ["现在查看草稿", "稍后处理"],
      "source": "structured_suggestion"
    }
  ]
}
```

### D. Suggestion Engine

Most Xiaojiao prompts are structured suggestions:

```text
template + data + correct timing + correct attachment point
```

Examples that do not require LLM:

```text
四年级第2课还在草稿状态，要现在确认吗？
周五的学习单建议今天生成。
教材目录还没补，进度安排我会先标记待复核。
```

Generative suggestions are allowed only when the suggestion requires content understanding, complex judgment, or natural-language synthesis beyond a template.

### E. Generation Pipeline

The LLM is allowed only for high-value work:

```text
generate teaching work plan content
generate lesson design
generate handout
generate evaluation rubric
revise complex content
answer open-ended professional questions
summarize preference candidates
```

Context rules:

```text
send only the current relevant work object
send required source snippets and gaps
send preference candidates only when relevant
do not send the full Work State
do not send the full chat history
```

LLM output must be structured before use:

```text
LLM output -> structured parse -> policy gate -> Work State candidate update -> Composer projection
```

### F. Preference Learner

Preference learning begins as candidate-only and readonly.

This stage allows:

```text
preference_candidate
teacher_profile_candidate
readonly_preference_summary
confirmation_required_before_promotion
```

This stage forbids:

```text
real memory write
silent preference promotion
unconfirmed teacher profile mutation
```

Candidate examples:

```text
teacher_often_shortens_activity_sections
teacher_prefers_fewer_stronger_tasks
teacher_simplifies_handouts
teacher_prefers_specific_evaluation_language
teacher_keeps_certain_lesson_structure
```

### G. Observation Metrics

The engine must be observable before it is made autonomous.

Required metrics:

```text
fallback_rate
suggestion_acceptance_rate
draft_acceptance_rate
average_revision_rounds
direct_confirmation_ratio_after_generation
teacher_dwell_longest_step
unknown_intent_top_list
ignored_suggestion_top_list
skipped_work_object_top_list
llm_call_rate_by_intent
token_cost_by_work_object
```

Correct self-improvement wording:

```text
The system accumulates usage signals, forms candidate improvements, and reduces manual intervention cost over time.
```

Forbidden self-improvement wording:

```text
The system will automatically evolve after completion.
```

## Cost Control Contract

| Scenario | Handling |
| --- | --- |
| Click confirm draft | deterministic logic |
| View today work | Work State + Composer |
| Monday weekly prompt | rule engine |
| "What should I do today?" | rule or state query |
| "Generate a handout" | LLM |
| "Shorten the second activity" | scoped LLM |
| "How can this lesson be improved?" | LLM |
| "Use this style from now on" | preference candidate, confirmation required |

Cost rules:

```text
all state changes: 0 token
all view decisions: 0 token
most reminders: 0 token
simple intent recognition: 0 token or lightweight classifier
content generation: LLM allowed
complex professional questions: LLM allowed
```

## Hard Boundaries

```json
{
  "runtime_change_allowed": false,
  "ui_implementation_allowed": false,
  "real_frontend_modification_allowed": false,
  "provider_model_call_allowed": false,
  "database_write_allowed": false,
  "memory_write_allowed": false,
  "feishu_write_allowed": false,
  "formal_export_allowed": false,
  "classroom_student_runtime_allowed": false,
  "enter_1000F_allowed": false,
  "enter_1001B_allowed": false,
  "old_sealed_stage_modification_allowed": false,
  "full_repo_blind_rename_allowed": false
}
```

## Prohibited Patterns

1. calling a real provider or model
2. wiring a provider candidate
3. writing database state
4. writing memory
5. writing Feishu
6. creating formal export
7. modifying real frontend pages
8. implementing production UI
9. connecting runtime
10. entering 1000F
11. entering 1001B without explicit approval
12. letting LLM directly control frontend output
13. sending full chat history as generation context
14. sending full Work State as generation context
15. exposing internal state terms as teacher-facing page labels
16. making chat history the main workspace
17. treating frontend UI state as the product core
18. silently promoting preference candidates
19. claiming automatic self-evolution
20. putting Jarvis in teacher-facing product copy

## Required Next Route

Recommended next stage after review:

```text
1001B_WORK_STATE_MANAGER_AND_COMPOSER_RULE_FIXTURE_PENDING_REVIEW
```

1001B should prove, with fixtures only:

```text
open workbench -> no model call -> today work appears
confirm draft -> no model call -> work object state turns confirmed
"today's work" -> no model call -> render today work items
"generate handout" -> LLM candidate is allowed only as a later candidate boundary
```

1000F remains deferred until this state-driven intelligence contract has passed review.

## Validation Requirements

- required files exist
- validator supports no-arg and `--root .`
- JSON contract, checklist, result, report, manifest, and ZIP exist
- stage identity and final status match
- required modules A-G exist
- Work State is declared as backend core asset, not frontend UI state
- LLM direct frontend control is forbidden
- context trimming is required
- full chat history and full Work State prompts are forbidden
- preference learning remains candidate-only and readonly
- all hard boundaries remain false
- manifest and ZIP are aligned
- no `.env`, token, secret, database, real student data, provider raw prompt/response, `node_modules`, or `__pycache__` enters the ZIP

## Next Stage

```text
next_stage=1001B_WORK_STATE_MANAGER_AND_COMPOSER_RULE_FIXTURE_PENDING_REVIEW
```
