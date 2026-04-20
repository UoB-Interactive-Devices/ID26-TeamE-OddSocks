"""Stage router.

Each stage/stimulus module is a placeholder for future stage-specific logic.
"""

from __future__ import annotations

import importlib

from config import VALID_STIMULI


async def run_single_stimulus(
    stage: str,
    stimulus: str,
    ble_transport,
    db,
    session_id: int | None,
    log,
) -> None:
    """Run one stage/stimulus module and log its event.

    Each stage/stimulus module owns its own logic.
    """
    module_name = f"stages.{stage}.{stimulus}"
    module = importlib.import_module(module_name)
    context = {
        "stage": stage,
        "stimulus": stimulus,
        "send_watch_json": ble_transport.send_json,
        "log": log.getChild(stimulus),
    }
    action, details, success = await module.run(context)

    db.log_stimulus_event(
        session_id=session_id,
        stage=stage,
        stimulus=stimulus,
        action=action,
        details=details,
        success=success,
    )
    log.info("stage=%s stimulus=%s action=%s success=%s", stage, stimulus, action, success)


async def run_stage(stage: str, ble_transport, db, session_id: int | None, log) -> None:
    """Run all stimuli for a stage in a fixed simple order."""
    for stimulus in VALID_STIMULI:
        await run_single_stimulus(
            stage=stage,
            stimulus=stimulus,
            ble_transport=ble_transport,
            db=db,
            session_id=session_id,
            log=log,
        )
