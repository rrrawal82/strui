import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
import openai
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_answer_csv(query: str) -> str:
    file = "raw.csv"
    agent = create_csv_agent(OpenAI(temperature=0), file, verbose=False)
    answer = agent.run(query)
    return answer

st.header("Chat with TicketGPT and it talks back!")

query = st.text_area("Ask any question related to the tickets")
button = st.button("Submit")
if button:
  st.write(get_answer_csv(query))
  text = get_answer_csv(query)
  tts_button = Button(label="Talk to me", width=100)

  tts_button.js_on_event("button_click", CustomJS(code=f"""
    var u = new SpeechSynthesisUtterance();
    u.text = "{text}";
    u.lang = 'en-US';

    speechSynthesis.speak(u);
    """))

  st.bokeh_chart(tts_button)