Language Translator

Project Overview

This project is developed as part of the CodeAlpha Artificial Intelligence Internship.

The Language Translator is a Python-based desktop application that translates text from one language to another using the Google Translate service. The application provides a simple graphical user interface (GUI) built with Tkinter.

Features

- Translate text into multiple languages
- User-friendly graphical interface
- Automatic source language detection
- Fast and accurate translation
- Built using Python

Technologies Used

- Python
- Tkinter
- deep-translator

Project Structure

Language Translator/
│
├── translator.py
└── README.md

How It Works

1. User enters text in the input box.
2. User specifies the target language code.
3. The application sends the text to Google Translator.
4. The translated text is displayed in the output box.

Installation

Install the required library:

pip install deep-translator

Tkinter is included with most Python installations.

Running the Project

Run the following command:

python translator.py

Supported Language Codes

Language| Code
English| en
Telugu| te
Hindi| hi
Tamil| ta
Kannada| kn
Malayalam| ml
French| fr
German| de
Spanish| es

Sample Usage

Input Text:

Hello, how are you?

Target Language Code:

te

Output:

హలో, మీరు ఎలా ఉన్నారు?

Code Description

- Tkinter is used to create the graphical user interface.
- deep-translator is used to access Google Translate services.
- The application automatically detects the source language.
- The translated text is displayed in a separate output box.

Future Improvements

- Add a dropdown menu for language selection
- Add voice input and output
- Support file translation
- Improve user interface design

Author

Nirupama Pamarthi

Internship

CodeAlpha Artificial Intelligence Internship