import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)
model = ChatHuggingFace(llm=llm)
responce=model.invoke("Who are you ?");
print(responce.content)
