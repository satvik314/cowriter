import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOllama



import os
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

from models import Story, StoryLine

# llm = ChatOpenAI(temperature=0.8)

# llm = ChatOllama(
#     model="dolphin-phi",
# )

st.header("🧸 The Co-writer")
st.subheader("Write a storyyy!")

model = st.selectbox(
   label =  'Select the model',
   options = ("GPT-3.5 - OpenAI", "Phi"),
   index=None,
   placeholder="Select the model!",
#    label_visibility="collapsed"
)

st.divider()

if 'my_model' not in st.session_state:
    st.session_state.my_model = ""

if 'llm' not in st.session_state:
    st.session_state.llm = ""

if model == "GPT-3.5 - OpenAI":
    st.session_state.my_model = "gpt-3.5-turbo-1106"
    st.session_state.llm = ChatOpenAI(model = "gpt-3.5-turbo-1106", temperature=0.8)
elif model == "Phi":
    st.session_state.my_model = "dolphin-phi"
    st.session_state.llm = ChatOllama(model = "dolphin-phi")

line = st.chat_input(placeholder="enter your line")

if 'my_story' not in st.session_state:
    st.session_state.my_story = Story(story_lines=[])

if line:
    # st.write(line)
    user_line = StoryLine(role="User", line=line)
    st.session_state.my_story.story_lines.append(user_line)
    ai_turn = st.session_state.llm.predict("\n".join([s.line for s in st.session_state.my_story.story_lines]) + "\n" + "predict the next line of the story. Keep in very short")
    ai_line = StoryLine(role="AI", line=ai_turn)
    st.session_state.my_story.story_lines.append(ai_line)


for story_line in st.session_state.my_story.story_lines:
    st.write(f"{story_line.line}")
        
        






