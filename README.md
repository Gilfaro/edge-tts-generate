# EdgeTTS Audio Generator for Anki

Generate high quality Japanese audio for your Anki cards using the edge-tts speech synthesis software

# What does this do?

This is a text to speech addon for Anki that makes use of the edge-tts synthesis engine to generate audio for Japanese Anki cards.

# Setup

1. You need to have a venv with edge-tts

Windows

```
cd %HOMEPATH%\AppData\Roaming\Anki2\addons21
py -3.9 -m pip install --upgrade pip virtualenv
py -3.9 -m venv edge-tts
edge-tts\Scripts\activate
py -m pip install --upgrade edge-tts
```

macOS

```
cd ~/Library/Application\ Support/Anki2/addons21
python3.9 -m pip install --upgrade pip virtualenv
python3.9 -m venv edge-tts
. edge-tts/bin/activate
python -m pip install --upgrade edge-tts
```

Linux

```
cd ~/.local/share/Anki2/addons21/
python3.9 -m pip install --upgrade pip virtualenv
python3.9 -m venv edge-tts
source edge-tts/bin/activate
python -m pip install --upgrade edge-tts
```

2. Open the Anki card browser and right click on any card and select "Generate edge-tts Audio" from the dropdown
    * You can drag and select multiple cards to generate audio for many cards at once. Note that if you select two different types of cards only the fields that they have in common will appear in the source/destination dropdown.

3. Select the source and destination fields for generating audio
    * Source refers to which field the addon should read from to generate audio. For example you usually want to read from the `Sentence` field or similar.
    * Destination refers to the field that the addon should output the audio to. Fields like `SentenceAudio`. Whatever field you want the audio to be placed in. NOTE: This will overwrite the contents of this field, so don't select any field you don't want overwritten with audio

4. Select a speaker from the dropdown. You can preview the voices by selecting "Preview Voice"

5. Click "Generate Audio" and wait for the audio to be generated
