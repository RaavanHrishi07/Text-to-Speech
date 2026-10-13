
from pathlib import Path
import os
import sys

from gtts import gTTS
from gtts.tts import gTTSError


def main():
    input_file = Path("abc.txt")
    output_file = Path("voice.mp3")

    # Check whether the input file exists.
    if not input_file.is_file():
        print("Error: abc.txt was not found in the project folder.")
        sys.exit(1)

    # Read and validate the input text.
    try:
        text = input_file.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError) as error:
        print(f"Error reading abc.txt: {error}")
        sys.exit(1)

    if not text:
        print("Error: abc.txt is empty. Please add some text.")
        sys.exit(1)

    # Convert text to speech and save the MP3.
    try:
        speech = gTTS(text=text, lang="en", slow=False)
        speech.save(str(output_file))
        print(f"Audio saved successfully: {output_file}")
    except (gTTSError, OSError) as error:
        print(f"Error generating audio: {error}")
        sys.exit(1)

    # Play the generated audio using the default Windows application.
    try:
        if os.name == "nt":
            os.startfile(str(output_file.resolve()))
        else:
            print("Automatic playback is configured for Windows only.")
    except OSError as error:
        print(f"Audio was saved, but playback failed: {error}")


if __name__ == "__main__":
    main()
