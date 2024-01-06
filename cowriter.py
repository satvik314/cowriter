import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

import os
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

from models import Story, StoryLine

llm = ChatOpenAI(temperature=0.8)

st.header("🧸 The Co-writer")
st.subheader("Write a storyyy!")
st.divider()

line = st.chat_input(placeholder="enter your line")

if 'my_story' not in st.session_state:
    st.session_state.my_story = Story(story_lines=[])

if line:
    # st.write(line)
    user_line = StoryLine(role="User", line=line)
    st.session_state.my_story.story_lines.append(user_line)
    ai_turn = llm.predict("\n".join([s.line for s in st.session_state.my_story.story_lines]) + "\n" + "predict the next line of the story. Keep in very short")
    ai_line = StoryLine(role="AI", line=ai_turn)
    st.session_state.my_story.story_lines.append(ai_line)


for story_line in st.session_state.my_story.story_lines:
    st.write(f"{story_line.line}")
        
        






