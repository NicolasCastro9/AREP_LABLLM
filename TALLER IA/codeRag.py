from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import os


os.environ["OPENAI_API_KEY"] = ""

# Clone
repo_path = "/tmp/test_repo"
repo = Repo.clone_from(
    "https://github.com/hwchase17/langchain", to_path= repo_path
)

# Load
loader = GenericLoader.from_filesystem(
    repo_path + "/libs/core/langchain_core",
    glob="**/*",
    suffixes=[".py"],
    exclude=["**/non-utf8-encoding.py"],
    parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
)
documents = loader.load()
len(documents)

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
)
texts = python_splitter.split_documents(documents)
len(texts)

db = Chroma.from_documents(texts, OpenAIEmbeddings(disallowed_special=()))
retriever = db.as_retriever(
    search_type="mmr",  # Also test "similarity"
    search_kwargs={"k": 8},
)


llm = ChatOpenAI(temperature=0)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever)
chat_history = []

question = "How can I load a source code as documents, for a QA over code, spliting the code in classes and functions?"
result = qa({"question": question, "chat_history": chat_history})
chat_history.append((question, result["answer"]))
print(result["answer"])

