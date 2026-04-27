"""Stage 'rem' + stimulus 'smell'.

This file owns the logic for this exact stage/stimulus combination.

REM smell intent: pulse peppermint 5s on / 25s off for a 15 minute REM window.
Peppermint acts as a reality-check cue; gaps reduce habituation.
"""

from __future__ import annotations
import asyncio
import time
import sys

try:
    import lgpio
except ImportError:
    lgpio = None

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

MIST_PINS = [12, 16]

async def _run_peppermint_cycles(logger):
    def log_msg(msg, level="info"):
        if logger and hasattr(logger, level):
            getattr(logger, level)(msg)
        else:
            print(f"[{level.upper()}] {msg}")

    log_msg("Starting REM Peppermint mist cycles (5s ON / 25s OFF for 15 minutes)")
    
    use_lgpio = False
    use_rpi_gpio = False
    h = None

    if lgpio is not None:
        try:
            h = lgpio.gpiochip_open(0)
            for pin in MIST_PINS:
                lgpio.gpio_claim_output(h, pin)
                lgpio.gpio_write(h, pin, 0)
            use_lgpio = True
            sys._smell_handle = h
        except Exception as e:
            log_msg(f"lgpio claim failed: {e}", "warning")

    if not use_lgpio and GPIO is not None:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            for pin in MIST_PINS:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.LOW)
            use_rpi_gpio = True
        except Exception as e:
            log_msg(f"RPi.GPIO setup failed: {e}", "error")
            return

    if not use_lgpio and not use_rpi_gpio:
        log_msg("No GPIO module found. Simulating REM mist cycles.")

    try:
        start_time = time.time()
        duration = 900 
        
        while (time.time() - start_time) < duration:
            log_msg("Scent Dispersing. (5s ON)")
            if use_lgpio:
                for pin in MIST_PINS:
                    lgpio.gpio_write(h, pin, 1)
            elif use_rpi_gpio:
                for pin in MIST_PINS:
                    GPIO.output(pin, GPIO.HIGH)
            
            await asyncio.sleep(5)
            
            log_msg("Receptor Recovery. (25s OFF)")
            if use_lgpio:
                for pin in MIST_PINS:
                    lgpio.gpio_write(h, pin, 0)
            elif use_rpi_gpio:
                for pin in MIST_PINS:
                    GPIO.output(pin, GPIO.LOW)
                
            await asyncio.sleep(25)
            
        log_msg("15 minutes completed. REM Peppermint turned OFF.")
        
    except asyncio.CancelledError:
        log_msg("REM smell stimulus cancelled gracefully.")
    except Exception as e:
        log_msg(f"Scent error: {e}", "error")
    finally:
        if use_lgpio and h is not None:
            try:
                for pin in MIST_PINS:
                    lgpio.gpio_write(h, pin, 0)
                lgpio.gpiochip_close(h)
                sys._smell_handle = None
            except Exception as e:
                log_msg(f"lgpio cleanup error: {e}", "error")
        elif use_rpi_gpio:
            try:
                for pin in MIST_PINS:
                    GPIO.output(pin, GPIO.LOW)
            except Exception as e:
                log_msg(f"RPi.GPIO cleanup error: {e}", "error")


async def run(context: dict) -> tuple[str, str, bool]:
    logger = context.get("log")
    
    # Cancel any previous smell task from OTHER stages
    prev_task = getattr(sys, "_smell_mist_task", None)
    if prev_task is not None and not prev_task.done():
        prev_task.cancel()
        await asyncio.sleep(0.5) # Wait for hardware release
        
    # Sweep any orphaned GPIO handles
    prev_handle = getattr(sys, "_smell_handle", None)
    if prev_handle is not None and lgpio is not None:
        try:
            lgpio.gpiochip_close(prev_handle)
        except Exception:
            pass
        sys._smell_handle = None

    # Start the Peppermint cycles
    sys._smell_mist_task = asyncio.create_task(_run_peppermint_cycles(logger))

    return "peppermint_mist_started", "Background 15 minute peppermint mist started", True
