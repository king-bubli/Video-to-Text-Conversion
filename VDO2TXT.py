!pip install speechrecognition
import speech_recognition as sr
!pip install moviepy
from moviepy.editor import VideoFileClip

#importing the video to the program
clip = VideoFileClip('/content/video.mp4')

#extracting the audio from the video
audio = clip.audio

#naming the  wave format file
audio_file = "video.wav"

#writing the audio file
audio.write_audiofile(audio_file)

#closing the clip after processing the audio out of it
clip.close()

#using Recognizer class from speechrecognition package
r =  sr.Recognizer()
with sr.AudioFile(audio_file) as source :
  audio = r.record(source)

#Creating the text using google recognizing API
text = r.recognize_google(audio)

#writing the file with the text identified
with open("recognized.txt", "w") as file:
  file.write("Recognized text: \n\n")
  file.write(text)
print("Video to Text conversion done :-)")
