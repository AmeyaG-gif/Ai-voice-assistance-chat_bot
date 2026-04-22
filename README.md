# AI Voice Assistance Chat Bot

A Python-based interactive voice assistant and chatbot that can perform various tasks via text input or voice commands. Created by Ameya.

## Features

- **Dual Modes:** Choose between Text Input mode or Voice Command mode.
- **AI Chatbot Integration:** Chat with an advanced AI model using natural language via the custom `gpt.py` module (powered by `g4f`).
- **Voice Recognition:** Uses Google's Speech Recognition API to understand your voice commands.
- **Text-to-Speech:** Responds to you audibly using the built-in Windows SAPI voice engine.
- **Open Websites & Apps:** Can automatically open a massive list of popular websites (Social Media, Search Engines, Video Platforms, Shopping, etc.) and desktop applications like MySQL Workbench, MS Office, VS Code, and Notepad++.
- **Time Telling:** Ask the assistant for the current time.
- **Colorful Terminal UI:** Uses `colorama` for a visually appealing command-line experience.

## Prerequisites

Before running the project, you need to install the required Python packages. 

Run the following command in your terminal:
```bash
pip install SpeechRecognition colorama pywin32 g4f curl_cffi
```
*Note: The `g4f` package is used for free access to AI models, and `pywin32` provides the text-to-speech functionality on Windows.*

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the main script:
   ```bash
   python project1.py
   ```
4. When prompted, enter `1` for Text Input Mode or `2` for Voice Command Mode.
5. **In Text Mode:** Type your questions or tasks, and the AI will respond. Type `exit`, `stop`, or `end` to quit.
6. **In Voice Mode:** Say a command out loud (e.g., "open youtube", "what is the time", or a conversation prompt). Say "exit" or "stop" to quit.

## Project Structure

- `project1.py`: The main script handling the user interface, speech recognition, and web automation logic.
- `gpt.py`: A custom integration module utilizing `g4f` to fetch responses from AI models.

## Creator
Created by **Ameya**