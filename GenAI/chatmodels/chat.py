from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


load_dotenv()

# model = init_chat_model(
#     "google_genai:gemini-3.5-flash"
# )
model = init_chat_model(
    "google_genai:gemini-3.5-flash", temperature=0.9, max_tokens=1000)

response = model.invoke("Write a poem about AI")
# print(response)
# print(response.content)
print(response.content[0]["text"])