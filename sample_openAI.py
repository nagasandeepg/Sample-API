from openai import OpenAI

client = OpenAI(api_key="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")

def main():
    while True:
        user_input = input("\nAsk something (or type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=user_input
            )

            answer = response.output[0].content[0].text
            print("\nAI:", answer)

        except Exception as e:
            print("Error:", str(e))


if __name__ == "__main__":
    main()