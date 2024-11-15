# litrag/__main__.py
from litrag.llm import get_llm, test_llm

# Global for easy testing
llm = get_llm()

def run():
    try:
        response = test_llm(llm)
        print("Ollama test successful!")
        print(f"Model response: {response}")
    except Exception as e:
        print(f"Error testing Ollama: {e}")

if __name__ == '__main__':
    run()