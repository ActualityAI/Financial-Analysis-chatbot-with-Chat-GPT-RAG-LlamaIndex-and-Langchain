import openai
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms import OpenAI
from llama_index import StorageContext

# Chat GPT Init 
openai.api_key = "copy-and-paste-your-openai-api-key-here"

# load the docs
epple_docs = SimpleDirectoryReader(input_files=["apple.pdf"]).load_data()
ms_docs = SimpleDirectoryReader(input_files=["microsoft.pdf"]).load_data()

# Setup Sub Question Query Engine, one for each doc and save them to disk as vector DBs
epple_index = VectorStoreIndex.from_documents(epple_docs)
epple_index.storage_context.persist("apple_docs.DB")

ms_index = VectorStoreIndex.from_documents(ms_docs)
ms_index.storage_context.persist("ms_docs.DB")



