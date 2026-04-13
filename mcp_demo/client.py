from openai import OpenAI
import requests

client = OpenAI(api_key="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")

def main():
    while True:
        user_input = input("\nAsk something: ")

        ai_response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"Decide if this needs a tool (weather/calc): {user_input}"
        )

        mcp_response = requests.post(
            "http://127.0.0.1:5000/mcp",
            json={"query": user_input}
        )

        tool_result = mcp_response.json()["result"]

        final_response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"User asked: {user_input}\nTool result: {tool_result}\nGive final answer"
        )

        print("\nAI:", final_response.output[0].content[0].text)

if __name__ == "__main__":
    main()
