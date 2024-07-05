from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

from config import config_list_claude, config_list_gpt


userProxy = UserProxyAgent(
    name="userProxy",
    code_execution_config=False,
    # is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    # max_consecutive_auto_reply=3,
    system_message="A human user. Interact with the planner to discuss the book concept and structure. The book writing needs to be approved by this user."
)

author = AssistantAgent(
    name="Author",
    llm_config=config_list_gpt,
    system_message='''Author. You follow an approved plan. You write book chapters according to the plan. The user can't modify your content directly. So do not suggest incomplete chapters which require others to modify. Always write the book content as python code which is ready to write the content to file. Don't include multiple chapters in one response. Do not ask others to copy and paste the content. Suggest the full content instead of partial content or content changes. If the content is not up to mark, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.'''
)

planner = AssistantAgent(
    name="Planner",
    llm_config=config_list_gpt,
    system_message='''Planner. Suggest a plan. Revise the plan based on feedback from user and critic, until user approval. The plan may involve an author who writes the book content within a python script which is ready to write the content to file and an editor who reviews the content written by the author and provides feeback.'''
)

editor = AssistantAgent(
    name="Editor",
    llm_config=config_list_gpt,
    system_message='''Editor. Review the content written by the book writer and provide feedback.'''
)

executor = AssistantAgent(
    name="Executor",
    llm_config=config_list_gpt,
    system_message='''Executor. Execute the code written by the author to write the contents of the book into files. Report the result if there is any error or if the task is completed.''',
    code_execution_config={"last_n_messages": 3, "work_dir": "book", "use_docker": False}
)

critic = AssistantAgent(
    name="Critic",
    llm_config=config_list_gpt,
    system_message='''Critic. Double check plan, claims and content. Author will write the book content as python code which is ready to write the content to file. Provide feedback on the content and the plan.''',
)
    
groupchat = GroupChat(
    agents=[userProxy, author, planner, editor, executor, critic],
    messages=[],
    max_round=50
)

manager = GroupChatManager(groupchat=groupchat, llm_config=config_list_gpt)

userProxy.initiate_chat(
    manager,
    message="Write a 3 chapter book on Mongolia."
)