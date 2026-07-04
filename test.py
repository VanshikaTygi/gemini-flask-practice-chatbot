from services.llm import GeminiService

def test_connection():
    print("[INIT] Verifying Google Generative AI Gateway...")
    client = GeminiService()
    try:
        res = client.get_chat_response("Ping")
        print(f"[SUCCESS] Core connectivity running stable. Response received.")
    except Exception as e:
        print(f"[FAILURE] Test exception thrown: {str(e)}")

if __name__ == "__main__":
    test_connection()
