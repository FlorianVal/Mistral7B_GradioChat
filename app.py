import gradio as gr
from gradio.components import Textbox
import openai
from config import OPENAI_API_URL, OPENAI_API_KEY, OPENAI_MODEL

openai.api_key = OPENAI_API_KEY
if OPENAI_API_URL:
    openai.api_base = OPENAI_API_URL
else:
    print("No OPENAI_API_URL set, using default.")


def chatbot(message, history):
    messages = []
    for history_messages in history:
        messages.append({"role": "user", "content": history_messages[0]})
        messages.append({"role": "assistant", "content": history_messages[1]})
    messages = messages + [{"role": "user", "content": message}]
    print(messages)
    response = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=messages,
    )
    return response.choices[0].message.content.strip()


iface = gr.ChatInterface(
    fn=chatbot,
    title="Chatbot",
).launch(server_name="0.0.0.0")  # 0.0.0.0 is for docker purposes
