from services.llm import GeminiService

def run_explainer():
    print("--- Local Explainer Service Debug System ---")
    ai = GeminiService()
    sample_code = "def add(a, b): return a + b"
    print(f"Testing code snippet transmission: '{sample_code}'")
    
    prompt = f"Explain this code execution block concisely: {sample_code}"
    response = ai.get_chat_response(prompt, system_instruction="You are a clear code reviewer.")
    print("\n[Engine Diagnostics Reply]:")
    print(response)

if __name__ == "__main__":
    run_explainer()
