# Sound Record and AI Transcribe
It is workable in .venv environment.

version control: python3.13.5 venv.

## Packages you have to install
1. pyaudio (for recording)
   
   https://pypi.org/project/PyAudio/
   
3. keyboard (for key space pressing)
   
   https://pypi.org/project/keyboard/
   
4. openai-whisper (for transcribing sound to text)

   Please check the github. There are additional and essential applications you have to install.

   https://github.com/openai/whisper
   
## a quick new start with VS code
1. set the workplace enviroment.
   
   Create a new folder for your project by terminal.
   
         mkdir [directory name]

         cd [directory name]

   Create virtual environment by terminal.
   
   (replace [.venv] with the name if you like)

         python3.13 -m venv [.venv]

   Activate the environment by terminal.

   On Windows:

         .venv\Scripts\activate

2. install all the aforementioned packages by terminal.

         pip install pyaudio

         pip install keyboard

         pip install openai-whisper
   
3. build the repository for the storage of records on File Explorer.
   
4. Start to use it.

## the second use 

(please read if you don't know how to find the previous workplace environment in VS Code)

1. Activate the previous workplace environment.

click the icon or button in the following order:

   Python icon on the sidebar >> GLOBAL ENVIRONMENTS >> Venv >> [the needed venv you named] >> Icon of "Open in Terminal"

2. Start to use it.
   
## Some problem I met
1. scoop is gone (I use scoop to install ffmpeg, which is necessary for openai-whisper.)

    Ans: Chat-GPT can help you, at least I solved it successffully by Chat-GPT assistance.
