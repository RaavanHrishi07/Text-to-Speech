
# Text-to-Speech

A simple Python application that converts text from a file into spoken English audio and saves it as an MP3 file using Google Text-to-Speech (gTTS).

## Features

- Reads text from `abc.txt`
- Converts English text into speech using gTTS
- Saves the generated audio as `voice.mp3`
- Automatically opens the generated audio using the default Windows application
- Checks whether the input file exists
- Handles empty input and common file-reading errors
- Displays useful error messages when speech generation fails

## Technologies Used

- Python 3.11+
- Google Text-to-Speech (gTTS)
- Python standard library

## Requirements

- Python installed on your system
- An active internet connection for speech generation
- A system with an audio player for playback

Install the required dependency using:

    python -m pip install gTTS

## Project Structure

    Text-to-Speech/
    ├── abc.txt
    ├── txtToSpeech.py
    ├── requirements.txt
    ├── README.md
    ├── LICENSE
    └── .gitignore

## Installation and Setup

1. Clone the repository:

       git clone https://github.com/RaavanHrishi07/Text-to-Speech.git

2. Open the project directory:

       cd Text-to-Speech

3. Install the dependency:

       python -m pip install -r requirements.txt

4. Add your desired English text to `abc.txt`.

## How to Run

Execute the application from the project directory:

    python txtToSpeech.py

The application reads the text from `abc.txt`, generates `voice.mp3`, and attempts to play the generated audio automatically on Windows.

## Error Handling

The application checks for a missing input file, empty text, file-reading errors, and common speech-generation failures.

## Notes

- Speech generation requires an internet connection.
- The default language is English.
- The generated `voice.mp3` file is excluded from Git tracking through `.gitignore`.

## Author

**Hrishikesh**  
GitHub: [RaavanHrishi07](https://github.com/RaavanHrishi07)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
