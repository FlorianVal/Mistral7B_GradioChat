import gradio as gr
import openai
from config import API_URL, MODEL

openai.api_base = API_URL
openai.api_key = "None"


def chatbot(message, history):
    messages = []
    for history_messages in history:
        messages.append({"role": "user", "content": history_messages[0]})
        messages.append({"role": "assistant", "content": history_messages[1]})
    messages = messages + [{"role": "user", "content": message}]
    print(messages)
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        stream=True,
    )
    message_content = ""
    for chunk in response:
        if "content" in chunk.choices[0].delta.keys():
            message_content += chunk.choices[0].delta.content
            yield message_content


iface = (
    gr.ChatInterface(
        fn=chatbot,
        title="Chatbot",
    )
    .queue()
    .launch(server_name="0.0.0.0")
)  # 0.0.0.0 is for docker purposes
