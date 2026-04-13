import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Error importing RPi.GPIO! This script must be run on a Raspberry Pi or with GPIO libraries installed.")
    exit(1)

MIST_PIN = 18

def setup():
    """Configure the GPIO pin to output mode and ensure it defaults to LOW."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MIST_PIN, GPIO.OUT)
    GPIO.output(MIST_PIN, GPIO.LOW)

def cleanup():
    """Set the GPIO pin LOW (OFF) and release GPIO resources."""
    try:
        GPIO.output(MIST_PIN, GPIO.LOW)
    except:
        pass
    GPIO.cleanup()

def run_demo_cycle():
    """Turn the atomizer ON for 5 seconds, then OFF for 25 seconds."""
    print("Mist ON (5 seconds)")
    GPIO.output(MIST_PIN, GPIO.HIGH)
    time.sleep(5)
    
    print("Mist OFF (25 seconds)")
    GPIO.output(MIST_PIN, GPIO.LOW)
    time.sleep(25)
    
    print("Cycle complete.")

def main():
    print("--- Atomizer Demo Script ---")
    try:
        setup()
        
        while True:
            # Wait for user prompt
            user_input = input("\nPress Enter to run the demo cycle (type 'q' to quit): ").strip().lower()
            
            if user_input == 'q':
                print("Exiting demo...")
                break
            
            # Run one demo cycle
            run_demo_cycle()
                
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
    finally:
        print("Cleaning up GPIO state...")
        cleanup()
        print("Cleanup complete. Safe to exit.")

if __name__ == "__main__":
    main()
