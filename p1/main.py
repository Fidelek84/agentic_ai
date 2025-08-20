from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import re

load_dotenv()

def calculate(input: str) -> str:
    """Performs basic arithmetic. Accepts input like '3 + 12', 'add 7 and 9', '7 plus 9', etc."""
    print("Tool has been called")
    match = re.match(r"(\d+)\s*([+\-*/])\s*(\d+)", input)
    if match:
        a, op, b = match.groups()
    else:
        match = re.match(r"(add|sum|plus)\s*(\d+)\s*(and|with|to)?\s*(\d+)", input, re.IGNORECASE)
        if match:
            a = match.group(2)
            b = match.group(4)
            op = '+'
        else:
            return "Sorry, I couldn't parse the calculation. Please use format like '3 + 12' or 'add 7 and 9'."
    a, b = float(a), float(b)
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    else:
        return "Unsupported operation."
    # Return a direct answer
    return f"{a} {op} {b} = {result}"

calculate_tool = Tool(
    name="calculate",
    func=calculate,
    description="Performs basic arithmetic. Accepts input like '3 + 12', 'add 7 and 9', '7 plus 9', etc."
)

def main():
    model = ChatOpenAI(temperature=0)

    tools = [calculate_tool]
    agent_executor = create_react_agent(model, tools)

    print("welcome I'm your AI assistant. Type 'quit' to end the conversation.")
    print("You can ask me to perform calculation or we can chat.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        print("\nAssistant: ", end="")
        tool_output_printed = False
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            # Print agent messages
            if "agent" in chunk and "message" in chunk["agent"]:
                for message in chunk["agent"]["message"]:
                    print(message.content, end="")
            # Print tool output
            if "tool" in chunk and "output" in chunk["tool"]:
                print(chunk["tool"]["output"], end="")
                tool_output_printed = True
            # Print final output (agent's answer)
            if "final" in chunk and "output" in chunk["final"]:
                print(chunk["final"]["output"], end="")
                tool_output_printed = True
            # Print output key (sometimes used for final answer)
            if "output" in chunk and isinstance(chunk["output"], str):
                print(chunk["output"], end="")
                tool_output_printed = True
        # If nothing was printed, try printing the tool output directly
        if not tool_output_printed:
            result = calculate(user_input)
            print(result, end="")
        print()
        
if __name__ == "__main__":
    main()