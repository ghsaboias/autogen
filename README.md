# Main Python Application

This Python application demonstrates the use of the `ConversableAgent` class from the `autogen` module to create and manage conversational agents. It showcases the creation of two agents, Cathy and Joe, both designed to be part of a duo of comedians. The application leverages the GPT-4 model, accessed via an API key stored in the environment variable `OPENAI_API_KEY`, to generate responses.

## Features

- **Conversational Agents**: Utilizes the `ConversableAgent` class to create two distinct agents with unique personalities and roles.
- **Custom Configuration**: Each agent is configured with specific parameters, including the model temperature and system messages, to tailor their responses.
- **Environment Variable Integration**: Securely accesses the OpenAI API key through an environment variable.
- **No Human Input**: Configured to operate without human input, ensuring a fully automated conversation flow.

## Setup

1. Ensure Python 3.11 is installed on your system.
2. Set up a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   .\venv\Scripts\Activate.ps1  # On Windows
   ```

3. Install the required dependencies (assuming `requirements.txt` is provided):

   ```sh
   pip install -r requirements.txt
   ```

4. Set the `OPENAI_API_KEY` environment variable to your OpenAI API key:

   ```sh
   export OPENAI_API_KEY='your_api_key_here'  # Unix/macOS
   set OPENAI_API_KEY=your_api_key_here  # Windows
   ```

## Usage

Run the script with Python:

```sh
python main.py
```

This will initiate a conversation between the two agents, Cathy and Joe, where Joe asks Cathy to tell a joke. The conversation is limited to a maximum of three turns.

## Note

This application is designed for demonstration purposes and showcases the use of conversational AI in Python. It does not include error handling or production-level features.

For more information on the ConversableAgent class and its configuration, refer to the autogen module documentation.
