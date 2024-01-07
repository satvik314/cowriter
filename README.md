# cowriter

by [Satvik](https://www.linkedin.com/in/satvik-paramkusham/)

An interesting game that lets you write stories with AI.

You write a line, and then the AI writes the next, and so on!

You can run the app with local LLMs without internet! (also works with GPT models!)

## Getting Started

Follow these instructions to get the Streamlit app running on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/satvik314/cowriter.git
```

### 2. Navigate to the cloned repository
```bash
cd cowriter
```

### 3.1. (For GPT model) Add OpenAI Key to ```secrets.toml```
```bash
OPENAI_API_KEY = <"your_token">
```

### 3.2. (For local model) Install Ollama and run the below command
```bash
ollama run dolphin-phi
```

### 4. Install required Python libraries
```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit App
```bash
streamlit run cowriter.py
```

In the app, enter the your line of the story and let the get lost in the game!