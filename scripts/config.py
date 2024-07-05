import os

config_list_claude = [
    {
        # Choose your model name.
        "model": "claude-3-5-sonnet-20240620",
        # You need to provide your API key here.
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "api_type": "anthropic",
        "base_url": "http://0.0.0.0:2536"
    }
]

config_list_gpt = {
        # Choose your model name.
        "model": "gpt-3.5-turbo-0125",
        # You need to provide your API key here.
        "api_key": os.getenv("OPENAI_API_KEY"),
}

