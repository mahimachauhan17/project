import speech_recognition as sr
import pyttsx3
import webbrowser
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            messagebox.showinfo("Error", "Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            messagebox.showinfo("Error", "Could not request results; check your internet connection.")
            return None

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def on_speak_button():
    command = listen()
    if command:
        search_google(command)

def on_type_button():
    query = entry.get()
    if query:
        search_google(query)
    else:
        messagebox.showinfo("Input Error", "Please enter a search query.")

def on_exit():
    speak("Goodbye!")
    root.quit()

# Create the main application window
root = tk.Tk()
root.title("Google Assistant")
root.geometry("700x300")
root.resizable(False, False)

# Style configuration
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TButton", padding=6, relief="flat", background="#0078d7", foreground="black")
style.map("TButton", background=[('active', '#0056a0')])

# Create and place a frame
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Create and place the input field
entry = ttk.Entry(frame, width=50)
entry.pack(pady=10)

# Create and place buttons
speak_button = ttk.Button(frame, text="Speak", command=on_speak_button)
speak_button.pack(pady=5)

type_button = ttk.Button(frame, text="Search", command=on_type_button)
type_button.pack(pady=5)

exit_button = ttk.Button(frame, text="Quit", command=on_exit)
exit_button.pack(pady=20)

# Start the application
speak("Hello! I am your Google Assistant. You can speak or type your search query.")
root.mainloop() 