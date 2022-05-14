import speech_recognition as sr

# add audiofile to your root folder
file_name = "test.wav"

sr_engine = sr.Recognizer()

with sr.AudioFile(file_name) as file:
  data = sr_engine.record(file)
  # change service / language depnding on your needs:
  text = sr_engine.recognize_google(data, language="de-DE")
  print(text)
