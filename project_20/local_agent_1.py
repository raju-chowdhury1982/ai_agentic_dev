"""
The local agent implementation for the travel assistant app.
This file contains the code for the nodes in the graph, which are imported from the notebook.
The notebook is used to develop and test the nodes, while this file is used to build the app and run it locally.
"""

# import statement
import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent   # type: ignore
from langchain_core.tools import tool   # type: ignore
from langchain_core.messages import HumanMessage


# 1 - initialization of local llm
loc_llm = ChatOpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "ollama",
    model = "llama3.1:8b",
    temperature = 0.1,
)


# 2 - defining the tool
@tool
def udf_calculator(expression: str) -> str:
    """A calculator tool that can evaluate mathematical expressions."""
    try:
        return str(eval(expression))
    except Exception as err:
        return f"Error evaluating expression: {err}"

# 3 - binding user defined tool with agent toolkit
toolset = [udf_calculator]


# 4 -  ccreate agent with llm and tools
udf_agent = create_agent(
    model=loc_llm,
    tools = toolset,
    # system_prompt = "You are a helpfull assistent that can do math.",
    # max_iterations = 3,
)

def execute_agent():
    while True:
        user_input = input("Enter a math expression to evaluate (or 'exit'/'quit'/'bye' to stop): ")
        if user_input in ['exit', 'quit', 'bye']:
            print("Exiting the agent. Goodbye!")
            break
        response = udf_agent.invoke({"messages": [HumanMessage(content=user_input)]})
        print(f"\tAgent response: {response['messages'][-1].content}")


# 5 - execute the agent with user query
if __name__ == "__main__":
    execute_agent()




