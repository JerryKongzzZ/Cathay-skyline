
import vertexai
import json
from vertexai.language_models import TextGenerationModel, ChatModel, InputOutputTextPair

vertexai.init(project="cathay-hackathon-405510", location="us-central1")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison")
chat_model = ChatModel.from_pretrained("chat-bison@001")
chat_model = chat_model.start_chat(
    context="""You are an assistant chatbot for an airline company, your responsibilities include chatting with the passengers and answer their queries, you also should have the ability to help amend the flight details for the passengers. You should also include a function to pre-order meals for the passengers.""",
    examples=[
        
    ]
)

response = chat_model.send_message(
    """""",
    **parameters
)
while True:
    print(f"Response from Model: {response.text}")
    response = chat_model.send_message(
        input(),
        **parameters
    )
