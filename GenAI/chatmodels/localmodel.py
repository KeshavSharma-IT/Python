from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 500},
)

chat_model=ChatHuggingFace(llm=llm);

result=chat_model.invoke("What shuould we do to improve focus");
print(result.content)