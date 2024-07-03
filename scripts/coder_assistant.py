import os

import autogen

from config import config_list_claude

assistant = autogen.AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list_claude,
    },
    system_message="""
    You are a helpful coding assistant. For python scripts, instruct user to install packages using ```sh<code to install packages>``` before running python script. The code must run in the first attempt. You have access to newsapi.org with the api key c97fa37cdd604063879046f62b0006a5. For HTML files (with CSS, JS), create python script to save the HTML file. DO NOT instruct the user to open HTML files.
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
    system_message="Make sure to save files in the coding directory."
)

# Prompt user for input
prompt = input("Please enter your prompt: ")

# Initiate chat with the provided prompt
user_proxy.initiate_chat(
    assistant, message=prompt
)