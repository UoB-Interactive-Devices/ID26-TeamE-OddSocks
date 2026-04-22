"""Stage 'awake' + stimulus 'smell'.

This file owns the logic for this exact stage/stimulus combination.
"""

from __future__ import annotations
import asyncio

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

MIST_PIN = 16

# Keep track of the background task so we don't accidentally run multiple
_mist_task = None

async def _run_mist_cycles(log):
    log("Starting background mist cycles (5s ON / 25s OFF for 10 minutes)")
    
    if GPIO is not None:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(MIST_PIN, GPIO.OUT)
            GPIO.output(MIST_PIN, GPIO.LOW)
        except Exception as e:
            log(f"GPIO setup failed: {e}")
            return
    else:
        log("RPi.GPIO not found. Simulating mist cycles.")

    try:
        # 10 minutes = 600 seconds. Each cycle is 30 seconds -> 20 cycles
        for cycle in range(20):
            log(f"Mist cycle {cycle + 1}/20: ON for 5s")
            if GPIO is not None:
                GPIO.output(MIST_PIN, GPIO.HIGH)
            
            await asyncio.sleep(5)
            
            log(f"Mist cycle {cycle + 1}/20: OFF for 25s")
            if GPIO is not None:
                GPIO.output(MIST_PIN, GPIO.LOW)
                
            await asyncio.sleep(25)
            
        log("10 minutes completed. Mist turned OFF.")
        
    except asyncio.CancelledError:
        log("Awake smell stimulus cancelled.")
    except Exception as e:
        log(f"Scent error: {e}")
    finally:
        if GPIO is not None:
            try:
                GPIO.output(MIST_PIN, GPIO.LOW)
            except Exception as e:
                log(f"Error during GPIO cleanup: {e}")

async def run(context: dict) -> tuple[str, str, bool]:
    global _mist_task
    log = context.get("log", print)
    
    # Cancel any previous task if this gets called again while already running
    if _mist_task is not None and not _mist_task.done():
        _mist_task.cancel()
        
    # Start the cycles in the background
    _mist_task = asyncio.create_task(_run_mist_cycles(log))

    return "mist_started", "Background 10 minute mist task started", True