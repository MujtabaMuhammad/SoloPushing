
import time

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(2)  # Sleep for 1 second
        seconds -= 1
    print("Time's up!")

# Example usage:
countdown(10)  # Countdown from 10 seconds
