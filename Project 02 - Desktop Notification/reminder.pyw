# **Health Ping** is a lightweight desktop wellness notifier built in Python.

# It runs continuously in the background to combat sedentary habits 
# by triggering automated desktop notifications every 30 minutes, 
# reminding users to hydrate, adjust their posture, and take a brief stretch break.

import time
from plyer import notification

# 30 minutes = 30 * 60 seconds
INTERVAL_SECONDS = 30 * 60

print("Reminder active! Running in the background every 30 minutes.")
print("Press Ctrl + C in the terminal to stop.\n")

try:
    while True:
        notification.notify(
            title="Hydration & Posture Check",
            message="30 minutes passed! Drink some water and stretch your back.",
            app_name="Health Ping",
            timeout=10  # Notification stays on screen for 8 seconds
        )
        # Pause script execution for 30 minutes
        time.sleep(INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("\nReminder stopped.")