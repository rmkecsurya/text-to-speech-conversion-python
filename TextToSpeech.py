import os
from gtts import gTTS

# user input for the text that to be converted into a mp3 file
textInput = input("Enter the text to be converted....")

# Print statement is to inform the user to wait for the processing
print("Please wait...... Your speech is processing")

# Creating an object of the text
myobj = gTTS(text=textInput, lang="en")

# Saving the file into mp3
myobj.save("voice1.mp3")

# Invoking the voice to play in the mp3 player
os.system("start voice1.mp3")
