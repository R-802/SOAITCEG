import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "text-embedding-ada-002"
WORD = input("Enter a word or string of text: ")


def create_embedding(input, model=MODEL) -> str:
    response = openai.Embedding.create(input=input, model=model)
    return response


def return_tokens():
    tokens = create_embedding(WORD)
    print(f"Total tokens used: ", {tokens["usage"]["total_tokens"]}.pop())


def return_embedding():
    embedding = create_embedding(WORD)
    print(embedding["data"][0]["embedding"])


if __name__ == "__main__":
    return_embedding()
    print("----------------------------------------------")
    return_tokens()
