import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("Loading...")
    with m as source: r.adjust_for_ambient_noise(source)

    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Audio Received. Processing!")
        try:
            value = r.recognize_whisper(audio, model='large-v2', language='english')

            print("Text: {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Error: {}".format(e))
except KeyboardInterrupt:
    pass