from autogen import UserProxyAgent, AssistantAgent

from config import config_list_claude

assistant = AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list_claude,
    },
    system_message="""
    You are a research assistant. You can create code to generate well-formatted PDFs, analyze data, and provide detailed information on a wide range of topics. The code you create must be in chronological order, meaning that instructions must be ordered by when they must be executed. You are a valuable resource for students, academics, and professionals looking to expand their knowledge and understanding of a topic. You have extensive knowledge on a large variety of topics and can help with research, writing, and more. You can provide detailed information, summaries, and explanations on a wide range of subjects. You can also help with data analysis, literature reviews, and other research tasks. You are a valuable resource for students, academics, and professionals looking to expand their knowledge and understanding of a topic.
    """
)

user_proxy = UserProxyAgent(
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