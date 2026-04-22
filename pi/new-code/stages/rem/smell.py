"""Stage 'rem' + stimulus 'smell'.

This file owns the logic for this exact stage/stimulus combination.
"""

from __future__ import annotations
import asyncio
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

# Note: Using 16 here to maintain consistency with previous MIST_PIN usage.
# If peppermint is physically wired to a different pin (e.g. 27), change this safely!
MIST_PIN = 16

# Keep track of the background task so we don't accidentally run multiple
_mist_task = None


async def _run_peppermint_cycles(logger):
    def log_msg(msg, level="info"):
        if logger and hasattr(logger, level):
            getattr(logger, level)(msg)
        else:
            print(f"[{level.upper()}] {msg}")

    log_msg("Starting REM Peppermint mist cycles (5s ON / 25s OFF for 15 minutes)")
    
    if GPIO is not None:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(MIST_PIN, GPIO.OUT)
            GPIO.output(MIST_PIN, GPIO.LOW)
        except Exception as e:
            log_msg(f"GPIO setup failed: {e}", "error")
            return
    else:
        log_msg("RPi.GPIO not found. Simulating REM mist cycles.")

    try:
        start_time = time.time()
        # 15 minutes = 900 seconds
        duration = 900 
        
        # While current time is less than 15 minutes from start
        while (time.time() - start_time) < duration:
            log_msg("Scent Dispersing. (5s ON)")
            if GPIO is not None:
                GPIO.output(MIST_PIN, GPIO.HIGH)
            
            await asyncio.sleep(5)
            
            log_msg("Receptor Recovery. (25s OFF)")
            if GPIO is not None:
                GPIO.output(MIST_PIN, GPIO.LOW)
                
            await asyncio.sleep(25)
            
        log_msg("15 minutes completed. REM Peppermint turned OFF.")
        
    except asyncio.CancelledError:
        log_msg("REM smell stimulus cancelled gracefully.")
    except Exception as e:
        log_msg(f"Scent error: {e}", "error")
    finally:
        if GPIO is not None:
            try:
                GPIO.output(MIST_PIN, GPIO.LOW)
            except Exception as e:
                log_msg(f"Error during GPIO cleanup: {e}", "error")


async def run(context: dict) -> tuple[str, str, bool]:
    global _mist_task
    logger = context.get("log")
    
    # Cancel any previous task if this gets called again while already running
    if _mist_task is not None and not _mist_task.done():
        _mist_task.cancel()
        
    # Start the Peppermint cycles in the background
    _mist_task = asyncio.create_task(_run_peppermint_cycles(logger))

    return "peppermint_mist_started", "Background 15 minute peppermint mist started", True
