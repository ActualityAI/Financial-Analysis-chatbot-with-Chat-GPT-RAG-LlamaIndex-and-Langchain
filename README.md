# Revolutionising-Investment-Analysis-with-AI---Annual-Reports-Compared

This chatbot is different to others in that is built to avoid the poor performance of chatbots that have the embeddings of multiple PDF and other documents all embedded together in one large dataset.

Instead it uses Retrieval Augmented Generation (RAG) and LlamaIndex to not only create a separate embeddings dataset for each PDF but it uses QueryEngineTool and SubQuestionQueryEngine to break down a complex query (like compare and contrast) into multiple sub questions and sends them to their specific targetted dataset.

All responses are then gathered and sent to a response synthesiser to produce the final response to your question.

# Video
[![Watch the walkthrough]([https://img.youtube.com/vi/nTQUwghvy5Q/default.jpg)](https://youtu.be/nTQUwghvy5Q](https://www.youtube.com/watch?v=VeyTTpZs5S8&ab_channel=ActualityAI))

# Instructions

## Step 1

First, install the required packages:

```
pip install -r requirements.txt
```

## Step 2

Copy and paste your Open AI API key in both the embed.py and chat.py files here

```python
openai.api_key = "copy-and-paste-your-openai-api-key-here"
```

## Step 3 

Run embed.py 

```python
python embed.py 
```

This will create 2 new sub directories containing embeddings created from the 2 PDF files which will be called apple_docs.DB and ms_docs.DB

apple_docs.DB are the emebeddings created from the text of the PDF of Apple's most recent 10-K (Annual Report) and ms_docs.DB are the emebeddings created from the text of the PDF of Microsoft's most recent 10-K (Annual Report)

## Step 4

Talk to the chatbot :

```python
python chat.py
```

Any question you ask will result in two things : 

1) It will be broken down into multiple sub questions and then sent to both datasets.
2) All responses are then gathered and sent to a response synthesiser to produce the final response to your question.
 
The multiple sub questions in step one will all be colour coded so you can see what questions are being directed to what dataset and also what their response was.

The final response from step 2 (which is not colour coded) will then be displayed.

For example try a simple question like "What was the profit info for the year?"

Or perhaps something much more complicated like ... "How have the profit margins evolved, and what are the key drivers? Break them down into a summary for both companies formatted as bullet points."

