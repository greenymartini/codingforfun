import speech_recognition as sr


r = sr.Recognizer()
#mic= sr.Microphone()

file_attilla= sr.AudioFile("audio_2_18-05-2020_11-48-26.wav")

with file_attilla as source: 
    r.adjust_for_ambient_noise(source)
    audio=r.record(source)
    text=r.recognize_google(audio, language= "de")

print(text)

"""
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
    text=r.recognize_google(audio, language='de')"""


