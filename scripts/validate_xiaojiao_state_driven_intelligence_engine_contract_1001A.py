from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path


STAGE_CODE = "1001A_XIAOJIAO_STATE_DRIVEN_INTELLIGENCE_ENGINE_CONTRACT"
FINAL_STATUS = "XIAOJIAO_STATE_DRIVEN_INTELLIGENCE_ENGINE_CONTRACT_PASS"
SLUG = "xiaojiao_state_driven_intelligence_engine_contract_1001A"
MARKER = "ALL_1001A_XIAOJIAO_STATE_DRIVEN_INTELLIGENCE_ENGINE_CONTRACT_CHECKS_OK"
NEXT_STAGE = "1001B_WORK_STATE_MANAGER_AND_COMPOSER_RULE_FIXTURE_PENDING_REVIEW"
DEFERRED_STAGE = "1000F_MODEL_CANDIDATE_AND_RESOURCE_CONTEXT_INTEGRATION"

REQUIRED_FILES = [
    "docs/handoff/xiaojiao_dynamic_work_surface_e5_r1_to_new_product_shape_line_handoff_20260612.md",
    "docs/handoff/xiaojiao_teacher_jarvis_workbench_1000A_execution_handoff_20260612.md",
    "docs/handoff/teacher_jarvis_workbench_planning_notes_1000_20260612.md",
    "docs/foundation/xiaojiao_agent_action_policy_and_work_state_contract_1000D.md",
    "docs/foundation/xiaojiao_agent_action_policy_and_work_state_contract_1000D.json",
    "docs/foundation/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.md",
    "docs/foundation/xiaojiao_dynamic_work_surface_end_to_end_mock_1000E5_R1.json",
    f"docs/foundation/{SLUG}.md",
    f"docs/foundation/{SLUG}.json",
    f"docs/audit/{SLUG}_report.md",
    f"docs/audit/{SLUG}_result.json",
    f"docs/audit/{SLUG}_checklist.json",
    f"docs/audit_packages/{SLUG}_manifest.json",
    f"scripts/validate_{SLUG}.py",
]

REQUIRED_MODULE_IDS = [
    "intent_parser",
    "work_state_manager",
    "work_view_composer",
    "suggestion_engine",
    "generation_pipeline",
    "preference_learner",
    "observation_metrics",
]

HARD_FALSE_KEYS = [
    "runtime_change_allowed",
    "ui_implementation_allowed",
    "real_frontend_modification_allowed",
    "provider_model_call_allowed",
    "database_write_allowed",
    "memory_write_allowed",
    "feishu_write_allowed",
    "formal_export_allowed",
    "classroom_student_runtime_allowed",
    "enter_1000F_allowed",
    "enter_1001B_allowed",
    "old_sealed_stage_modification_allowed",
    "full_repo_blind_rename_allowed",
]

BOUNDARY_FALSE_KEYS = [
    "real_ui_implemented",
    "real_frontend_modified",
    "runtime_connected",
    "provider_model_called",
    "database_written",
    "memory_written",
    "feishu_written",
    "formal_export_created",
    "classroom_student_runtime_connected",
    "old_sealed_stage_modified",
    "full_repo_blind_rename_performed",
    "entered_1000F",
    "entered_1001B",
    "llm_direct_frontend_control_allowed",
    "full_chat_history_context_allowed",
    "full_work_state_prompt_allowed",
    "preference_candidate_promoted",
]

FORBIDDEN_ZIP_PARTS = [
    ".env",
    "token",
    "secret",
    "node_modules",
    "__pycache__",
    ".db",
    ".sqlite",
    "student_data",
    "provider_raw",
]


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION_FAILED: {message}")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot read JSON {path}: {exc}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=None)
    return parser.parse_args()


def assert_false(mapping: dict, key: str) -> None:
    if mapping.get(key) is not False:
        fail(f"expected false for {key}")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            fail(f"missing required file: {rel}")

    contract = load_json(root / f"docs/foundation/{SLUG}.json")
    checklist = load_json(root / f"docs/audit/{SLUG}_checklist.json")
    result = load_json(root / f"docs/audit/{SLUG}_result.json")
    manifest = load_json(root / f"docs/audit_packages/{SLUG}_manifest.json")
    report_text = (root / f"docs/audit/{SLUG}_report.md").read_text(encoding="utf-8")
    contract_text = (root / f"docs/foundation/{SLUG}.md").read_text(encoding="utf-8")

    if contract.get("stage_code") != STAGE_CODE:
        fail("contract stage_code mismatch")
    if contract.get("final_status_target") != FINAL_STATUS:
        fail("contract final_status_target mismatch")
    if contract.get("stage_type") != "intelligence_engine_contract_only":
        fail("stage_type mismatch")
    if result.get("stage_code") != STAGE_CODE or result.get("final_status") != FINAL_STATUS:
        fail("result identity mismatch")
    if result.get("pass") is not True or result.get("marker") != MARKER:
        fail("result pass/marker mismatch")
    if checklist.get("stage_code") != STAGE_CODE:
        fail("checklist stage_code mismatch")
    if manifest.get("stage_code") != STAGE_CODE:
        fail("manifest stage_code mismatch")
    if contract.get("next_stage") != NEXT_STAGE or result.get("next_stage") != NEXT_STAGE:
        fail("next_stage mismatch")
    if contract.get("deferred_stage") != DEFERRED_STAGE or result.get("deferred_stage") != DEFERRED_STAGE:
        fail("deferred_stage mismatch")

    auth = contract.get("authorization_boundary", {})
    if auth.get("explicit_user_authorized_stage") != STAGE_CODE:
        fail("authorization boundary missing explicit stage")
    if auth.get("authorization_limited_to_contract_only") is not True:
        fail("authorization must be contract-only")
    if auth.get("previous_e5_r1_no_1001_rule_acknowledged") is not True:
        fail("previous E5_R1 stop rule not acknowledged")
    assert_false(auth, "enter_1001B_allowed")
    assert_false(auth, "enter_1000F_allowed")

    principles = contract.get("core_principles", {})
    if principles.get("work_state_is_backend_core_asset") is not True:
        fail("Work State backend ownership missing")
    if principles.get("work_state_is_not_frontend_ui_state") is not True:
        fail("Work State frontend UI boundary missing")
    if principles.get("frontend_is_projection_only") is not True:
        fail("frontend projection boundary missing")
    assert_false(principles, "llm_direct_frontend_control_allowed")
    assert_false(principles, "teacher_facing_jarvis_allowed")
    assert_false(principles, "teacher_facing_internal_state_terms_allowed")

    layers = {item.get("layer"): item for item in contract.get("three_layer_intelligence_model", [])}
    if layers.get("deterministic_logic", {}).get("token_cost") != "0":
        fail("deterministic logic must be 0 token")
    if layers.get("rule_engine", {}).get("token_cost") != "0_or_extremely_low":
        fail("rule engine token policy mismatch")
    if layers.get("llm", {}).get("token_cost") != "paid_model_cost":
        fail("LLM token policy mismatch")

    modules = {item.get("id"): item for item in contract.get("modules", [])}
    for module_id in REQUIRED_MODULE_IDS:
        if module_id not in modules:
            fail(f"missing module: {module_id}")

    if modules["work_view_composer"].get("llm_call_allowed") is not False:
        fail("composer must not call LLM")
    generation = modules["generation_pipeline"]
    if generation.get("context_trimming_required") is not True:
        fail("context trimming must be required")
    if generation.get("structured_output_required") is not True:
        fail("structured LLM output must be required")
    assert_false(generation, "full_work_state_prompt_allowed")
    assert_false(generation, "full_chat_history_context_allowed")

    preference = modules["preference_learner"]
    if preference.get("stage_mode") != "candidate_only_readonly":
        fail("preference stage mode mismatch")
    assert_false(preference, "real_memory_write_allowed")
    assert_false(preference, "silent_preference_promotion_allowed")

    metrics = modules["observation_metrics"].get("required_metrics", [])
    if len(metrics) < 10 or "fallback_rate" not in metrics or "llm_call_rate_by_intent" not in metrics:
        fail("observation metrics too thin")
    if modules["observation_metrics"].get("self_improvement_policy", {}).get("automatic_self_evolution_claim_allowed") is not False:
        fail("automatic self-evolution claim must be forbidden")

    cost = contract.get("cost_control_contract", {})
    if cost.get("state_changes_token_cost") != "0" or cost.get("view_decisions_token_cost") != "0":
        fail("state/view cost must be zero")
    if cost.get("content_generation_llm_allowed") is not True:
        fail("content generation LLM allowance missing")

    hard = contract.get("hard_boundaries", {})
    for key in HARD_FALSE_KEYS:
        assert_false(hard, key)

    flags = result.get("boundary_flags", {})
    for key in BOUNDARY_FALSE_KEYS:
        assert_false(flags, key)

    combined = contract_text + "\n" + report_text + "\n" + json.dumps(contract, ensure_ascii=False)
    required_terms = [
        "Work State is the backend core asset, not frontend UI state.",
        "LLM output -> structured parse -> policy gate -> Work State candidate update -> Composer projection",
        "do not send the full chat history",
        "candidate-only and readonly",
        "1000F remains deferred",
        NEXT_STAGE,
    ]
    for term in required_terms:
        if term not in combined:
            fail(f"missing required term: {term}")

    zip_path = root / f"docs/audit_packages/{SLUG}.zip"
    if not zip_path.exists():
        fail(f"missing ZIP: {zip_path}")
    with zipfile.ZipFile(zip_path, "r") as zf:
        zip_entries = zf.namelist()

    for entry in zip_entries:
        normalized = entry.replace("\\", "/")
        if normalized.startswith("/") or ":" in normalized:
            fail(f"absolute or unsafe ZIP path: {entry}")
        lowered = normalized.lower()
        if any(part in lowered for part in FORBIDDEN_ZIP_PARTS):
            fail(f"forbidden ZIP entry: {entry}")

    manifest_entries = manifest.get("zip_entries", [])
    if manifest.get("manifest_minus_zip") != [] or manifest.get("zip_minus_manifest") != []:
        fail("manifest alignment fields are not empty")
    if sorted(manifest_entries) != sorted(zip_entries):
        fail("manifest entries do not match ZIP")
    if manifest.get("zip_entry_count") != len(zip_entries):
        fail("zip_entry_count mismatch")

    print(MARKER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
