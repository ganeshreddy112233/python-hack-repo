import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak out the provided text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        audio = recognizer.listen(source)
    try:
        # Using Google's speech recognition
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def retrieve_knowledge(query):
    """Retrieve a brief summary from Wikipedia for the given query."""
    try:
        # Get summary from Wikipedia (2 sentences)
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "Your query is ambiguous. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic."
    except Exception as e:
        return "An error occurred: " + str(e)

def main():
    speak("Hello, how can I help you today?")
    while True:
        query = listen().strip()
        if not query:
            continue
        # Check for exit commands
        if query.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        # Retrieve knowledge and respond
        response = retrieve_knowledge(query)
        print("Response:", response)
        speak(response)

if __name__ == "__main__":
    main()