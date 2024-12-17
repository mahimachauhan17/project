import speech_recognition as sr
import pyttsx3
import openai

# Initialize the speech recognizer and text-to-speech engine1
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set OpenAI API key (make sure to replace this with your actual API key)
openai.api_key = 'YOUR_API_KEY'

def speak(text):
    """Function to speak out the text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen and recognize voice input."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand your voice team gen{z} repeat again.")
            return "None"
        except sr.RequestError:
            print("API request failed.")
            return "None"

def ask_gpt(question):
    """Function to get a response from OpenAI's GPT API."""
    response = openai.Completion.create(
      engine="text-davinci-003",  # You can use 'gpt-3.5-turbo' if available.
      prompt=question,
      max_tokens=100
    )
    return response.choices[0].text.strip()

def virtual_assistant():
    """Main function to run the virtual assistant."""
    #speak("Hello, how can I assist you team gen{z}?")
    speak("hello, how are you rajeev and naman")
    while True:
        query = listen().lower()
        
        if 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break
        elif query:
            response = ask_gpt(query)
            print(f"Assistant: {response}")
            speak(response)

if __name__ == "__main__":
    virtual_assistant()
