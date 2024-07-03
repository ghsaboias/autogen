# Autogen + LiteLLM + Claude

This Python project consists, basically, on a LiteLLM server and Autogen for agent orchestration. LiteLLM is responsible for creating a Claude API in the OpenAI format, to be consumed by the Autogen agents. Project can also be used with OpenAI (see scripts/human_in_loop.py).

## Features

- **Conversational Agents**: Utilizes the `ConversableAgent` class to create two distinct agents with unique personalities and roles.
- **Custom Configuration**: Each agent is configured with specific parameters, including the model temperature and system messages, to tailor their responses.

## Setup

1. Install LiteLLM (if using Anthropic/Claude):

   ```sh
   pip install litellm
   ```

2. Run LiteLLM server (if using Anthropic/Claude):

   ```sh
   litellm --model claude-3-5-sonnet-20240620
   ```

3. Set up a virtual environment and activate it:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Unix/macOS
   .\venv\Scripts\Activate.ps1  # On Windows
   ```

4. Install the required dependencies (assuming `requirements.txt` is provided):

   ```sh
   pip install -r requirements.txt
   ```

5. Set the api key as an environment variable:

   OpenAI:

   ```sh
   export OPENAI_API_KEY='your_api_key_here'  # Unix/macOS
   set OPENAI_API_KEY=your_api_key_here  # Windows
   ```

   Anthropic:

   ```sh
   export ANTHROPIC_API_KEY='your_api_key_here'  # Unix/macOS
   set ANTHROPIC_API_KEY=your_api_key_here  # Windows
   ```

## Usage

Run a script with Python (e.g. coder_assistant.py):

```sh
python coder_assistant.py
```

This will initiate a conversation between User Proxy and Assistant.

Check the coding directory for files created by Agents.

## Note

This application is designed for demonstration purposes and showcases the use of conversational AI in Python. It does not include error handling or production-level features.

For more information on the ConversableAgent class and its configuration, refer to the autogen module documentation.
