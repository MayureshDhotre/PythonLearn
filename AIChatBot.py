from openai import OpenAI
import time


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="olama",
)

flag: bool = True

while flag == True:
    user_string: str = input("User: ")
    start = time.perf_counter()
    if user_string.lower() == "bye":
        print("It was nice talking to you ...Bbye !!")
        flag = False
    else:
        response = client.chat.completions.create(
            model="qwen2.5:0.5b-instruct",
            temperature=0.6,
            messages=[
                {"role": "system", "content": "Be very precise"},
                {
                    "role": "user",
                    "content": user_string,
                },
            ],
        )

        end = time.perf_counter()

        print(f"Cooked in : {end - start:.4f} seconds")
        print(f"Bot: {response.choices[0].message.content}")
