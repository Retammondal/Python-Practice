# Write a program to print Twinkle twinkle little star poem in python.

song = """Twinkle, twinkle, little star,
\tHow I wonder what you are!
\tUp above the world so high,
\tLike a diamond in the sky.
Twinkle, twinkle, little star,
\tHow I wonder what you are"""

import pyttsx3

# Initializes the Text-to-Speech engine.
engine = pyttsx3.init()

# Adjust speaking rate and volume (optional)
engine.setProperty('rate', 200)    # Speed (words per minute, default ~200)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Speak text directly
print("\nSaying The song :")
print(song)

engine.say(song)
engine.runAndWait()
# runAndWait() forces the program to actually process and speak the text, 
# blocks the code from moving forward until the speaking is finished.

print("Finished.. Thank for coming..")


# --------------------------------------------------------------------------------------------
#           pyttsx3 Module
# --------------------------------------------------------------------------------------------
# Core Concepts
#   Definition: An offline text-to-speech (TTS) conversion library in Python.
#   Offline Usage: Works completely without an internet connection.
#   Multi-OS: Bridges directly to native system voices 
#             (SAPI5 on Windows, NSSpeechSynthesizer on macOS, Espeak on Linux).

# Essential Lifecycle
#     pyttsx3.init() Initializes the speech engine engine driver.
#     engine.say("text") Queues a text string to be spoken. It remains silent until played.
#     engine.runAndWait() Processes the queue, plays the audio, and pauses code execution until speaking finishes.