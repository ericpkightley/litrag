from langchain_community.llms import Ollama

def get_llm(model="mistral"):
    return Ollama(model=model)

def test_llm(llm):
    return llm.invoke("Say hello!")