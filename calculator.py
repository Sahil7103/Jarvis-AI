import pyttsx3
import speech_recognition as sr
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Speak function to give output in voice format"""
    engine.say(audio)
    engine.runAndWait()

def wolfram_query(query):
    api = "YVUG4L-EEXLTP9K2U"
    requester = wolframalpha.Client(api)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text  # Assigning result to 'answer'
        return answer
    except:
        speak("Value is not answerable")
        return None

def calculate(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")

    Final = str(Term)
    try:
        result = wolfram_query(Final)  # Call the renamed function
        if result:
            print(f"Result: {result}")
            speak(result)  # Speak the actual result
    except:
        speak("Value is not answerable")


