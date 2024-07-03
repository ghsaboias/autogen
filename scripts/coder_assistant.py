import os

import autogen

from config import config_list_claude

assistant = autogen.AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list_claude,
    },
    system_message="""
    You are a helpful coding assistant. It is necessary to install required packages before running any Python script, in a simulated environment, so give exact instructions with markdown in the format ```sh<code to install packages>``` install the packages. The code must run in the first attempt.
    """
)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "coding",
    },
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    max_consecutive_auto_reply=3,
)

# Prompt user for input
prompt = input("Please enter your prompt: ")

# Initiate chat with the provided prompt
user_proxy.initiate_chat(
    assistant, message=prompt
)