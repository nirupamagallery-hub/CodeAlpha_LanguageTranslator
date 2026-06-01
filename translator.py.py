from tkinter import *
from deep_translator import GoogleTranslator

# Function to translate text
def translate_text():

    text = input_text.get("1.0", END)

    target_language = language_var.get()

    translated = GoogleTranslator(source='auto', target=target_language).translate(text)

    output_text.delete("1.0", END)

    output_text.insert(END, translated)

# Main window
root = Tk()

root.title("Language Translator")

root.geometry("500x400")

# Input label
Label(root, text="Enter Text").pack()

# Input box
input_text = Text(root, height=5)

input_text.pack()

# Language label
Label(root, text="Target Language Code").pack()

# Language input
language_var = StringVar()

language_var.set("te")

Entry(root, textvariable=language_var).pack()

# Translate button
Button(root, text="Translate", command=translate_text).pack(pady=10)

# Output label
Label(root, text="Translated Text").pack()

# Output box
output_text = Text(root, height=5)

output_text.pack()

root.mainloop()