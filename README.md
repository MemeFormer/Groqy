# Groqy

Groqy: Chat with AI like a pro, right from your command line. No setup hassle, zero distractions. The only thing faster than a Groq response is how quickly you can open and close Groqy. Save your chats with auto-named files, and keep the flow going. Works in macOS/Linux terminal.

This project was inspired by groq-cli by PR4S4D. The original project was a Windows-only CLI tool written in Go. Groqy extends this idea with additional features like conversation history tracking and user-triggered saving of responses with auto-generated filenames.


## Features

- Easy setup and installation using pipx
- Interactive chat with AI language models powered by Groq
- Customizable model selection and max tokens configuration
- User-triggered saving of individual AI responses with auto-generated filenames
- Conversation history tracking for context-aware AI responses
- Markdown rendering for enhanced readability
- Cross-platform compatibility (macOS/Linux)
- Accessible to everyone, not behind a paywall like some other AI APIs
- Generous free tier provided by Groq, no credit card required for setup


## Prerequisites

- Python 3.6 or above
- pipx package manager


## Installation

Install pipx if you haven't already:

```bash
python3 -m pip install --user pipx
python3 -m userpath append ~/.local/bin
```

Install Groqy using pipx:

```bash
pipx install groqy
```


## Obtaining a Groq API Key

To use Groqy, you'll need a Groq API key. You can obtain one by going to groq.com, then navigating to Groq Cloud and creating an API key. Be sure to copy the API key when it's shown, as it will only be displayed once.


## Usage

1. Run Groqy from your terminal:

```bash
groqy
```

2. Follow the prompts to enter your Groq API key and select the desired model and max tokens.

3. Start chatting with the AI by typing your messages and pressing Enter.

4. Groqy maintains a conversation history to provide context for subsequent AI responses. However, the history is not automatically saved to files.

5. To save an individual AI response, type "save" as your input. Groqy will generate a descriptive filename based on the last AI response and save that specific response as a Markdown file.

6. To exit Groqy, press `Ctrl+C`.


## Configuration

Groqy uses a `.env` file to store your configuration settings. If the file doesn't exist, Groqy will prompt you to enter your Groq API key, select the model, and set the max tokens value during the first run.

The following settings are available in the `.env` file:

- `GROQ_API_KEY`: Your Groq API key.
- `GROQ_MODEL`: The selected AI model to use for chat completions.
- `MAX_TOKENS`: The maximum number of tokens to generate in the AI response.

You can modify these settings directly in the `.env` file or delete the file to be prompted again on the next run.


## Linux Usability

Please note that while Groqy is expected to work out of the box on Linux, this has not been extensively tested yet. We will be looking into this and providing updates as soon as possible.


## License

This project is licensed under the [MIT License](LICENSE).


## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


## Acknowledgements

- [Groq API](https://www.groq.com/) for providing the AI language models.
- [Rich](https://github.com/Textualize/rich) for the beautiful Markdown rendering.
- [python-dotenv](https://github.com/theskumar/python-dotenv) for handling environment variables.
- [PyInquirer](https://github.com/CITGuru/PyInquirer) for the interactive prompts.
- [Halo](https://github.com/manrajgrover/halo) for the spinner during processing.





