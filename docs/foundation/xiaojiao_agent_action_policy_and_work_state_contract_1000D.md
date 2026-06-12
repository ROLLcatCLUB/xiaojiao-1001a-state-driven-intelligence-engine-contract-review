# 1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT

Date: 2026-06-12

## Stage Identity

```text
package_code=1000_XIAOJIAO_TEACHER_JARVIS_WORKBENCH_PLANNING_PACKAGE
stage_code=1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT
stage_name=Agent Action Policy And Work State Contract
stage_type=agent_action_policy_contract_only
final_status_target=XIAOJIAO_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT_PASS
runtime_change_allowed=false
ui_implementation_allowed=false
```

## Purpose

Define how the unified Xiaojiao Agent decides what to show, ask, generate, repair, confirm, or defer from Work State.

This stage is a review package and contract artifact only. It does not implement UI, modify real frontend pages, connect runtime, call provider/model, write database, write memory, write Feishu, create formal export, connect classroom student-side runtime, modify old sealed stages, or perform blind repository rename.

## Source Handoffs

- `docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md`
- `docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md`

## Product Identity And Naming Boundary

The product agent remains `小教智能体 / Xiaojiao Agent`.

`Jarvis` is an internal planning metaphor only. Teacher-facing product copy must use Xiaojiao / 小教 language and must not expose Jarvis unless a later branding stage explicitly approves it.

Old `小备 / Xiaobei / xiaobei` wording remains a legacy internal namespace. Blind full-repository rename is forbidden; any future rename must be allowlist-based.

## Main Document Boundary

`教学工作计划 / teaching_work_plan` remains the role-scoped main document. Supporting tables such as `单元课时分配`, `学期周历表`, `课务日程表`, and `课表` remain supporting artifacts and do not replace the main document.

## Weekly Work Graph Boundary

`周工作图谱 / weekly_work_graph` does not replace `学期周历表 / semester_weekly_calendar`.

- `学期周历表 / semester_weekly_calendar`: semester progress supporting table; answers which week teaches what.
- `周工作图谱 / weekly_work_graph`: higher-level weekly work panel; organizes what to teach, prepare, evaluate, adjust, submit, handle, and carry over this week.

## Stage Contract

```json
{
  "work_state_schema": {
    "fields": [
      "state_id",
      "teacher_role_profile_ref",
      "active_work_scope",
      "active_work_object",
      "known_slots",
      "missing_slots",
      "candidate_artifacts",
      "linked_artifacts",
      "risks",
      "available_actions",
      "blocked_reasons",
      "confirmation_required",
      "renderer_mapping",
      "state_summary",
      "audit_trace_ref"
    ],
    "token_saving_state_summary_required": true
  },
  "action_policy": {
    "allowed_action_types": [
      "ASK",
      "GENERATE_DRAFT",
      "REVISE",
      "DERIVE_SUPPORTING_ARTIFACT",
      "INSPECT_GAP",
      "LINK_ARTIFACT",
      "PREPARE_EXPORT_REVIEW_ONLY",
      "CONFIRM",
      "DEFER",
      "BLOCK",
      "RECORD_TRACE"
    ],
    "single_unified_agent": true,
    "business_specific_agent_split_allowed": false
  },
  "gates": {
    "turn_detection_gate": "classifies teacher intent and active work scope",
    "sufficiency_gate": "checks whether slots are enough before generation or derivation",
    "renderer_mapping_gate": "maps Work State to Dynamic Work Panel through Work View Composer",
    "confirmation_gate": "requires teacher confirmation before write, export, sync, or irreversible action",
    "boundary_gate": "blocks UI/runtime/provider/database/memory/Feishu/formal export in this stage"
  },
  "audit_trace_policy": {
    "separated_from_teacher_facing_ui": true,
    "teacher_view_shows": [
      "status",
      "gaps",
      "next_action",
      "safe_summary"
    ],
    "internal_trace_keeps": [
      "decision_reason",
      "source_refs",
      "validator_stage",
      "boundary_flags"
    ]
  }
}
```

## Hard Boundaries

```json
{
  "runtime_change_allowed": false,
  "ui_implementation_allowed": false,
  "provider_call_allowed": false,
  "database_write_allowed": false,
  "memory_write_allowed": false,
  "feishu_write_allowed": false,
  "formal_export_allowed": false,
  "classroom_student_runtime_allowed": false,
  "full_repo_blind_rename_allowed": false
}
```

## Validation Focus

- work state schema is explicit
- action policy is gate-based
- single unified Xiaojiao Agent remains intact
- confirmation is required for write/export/sync
- audit trace is separated from teacher-facing UI

## Prohibited Patterns

1. implement real UI
2. modify real frontend pages
3. connect runtime
4. call provider or model
5. write database
6. write memory
7. write Feishu
8. create formal export
9. connect classroom student runtime
10. modify old sealed stages
11. blind full-repository rename
12. globally replace Xiaobei with Xiaojiao
13. put Jarvis into teacher-facing product copy
14. make Dynamic Work Panel a fixed dead card
15. split Xiaojiao into multiple business agents
16. let chat history dominate the workspace
17. replace semester weekly calendar with weekly work graph
18. let supporting tables replace the teaching work plan main document
19. hardcode art-teacher logic as a system-wide rule
20. turn sample room into classroom execution runtime
21. expose audit flags in teacher-facing primary copy
22. skip validator before next stage

## Future Milestones

- `1000B_EDUCATION_PRE_CLASS_WORK_SAMPLE_ROOM_BUSINESS_STRUCTURE`
- `1000C_DYNAMIC_WORK_PANEL_CONTRACT`
- `1000D_AGENT_ACTION_POLICY_AND_WORK_STATE_CONTRACT`
- `1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT`

Do not enter 1000E without explicit user authorization.

## Validation Requirements

- required files exist
- validator supports no-arg and `--root .`
- JSON contract, checklist, result, report, manifest, and ZIP exist
- stage identity and final status match
- all hard boundaries remain false
- no `.env`, token, secret, database, real student data, provider raw prompt/response, `node_modules`, or `__pycache__` enters the ZIP
- ZIP entries use relative `/` paths only
- `manifest_minus_zip=[]`
- `zip_minus_manifest=[]`

## Next Stage

```text
next_stage=1000E_ART_TEACHER_PRE_CLASS_WORKBENCH_PILOT_PENDING_REVIEW
```
