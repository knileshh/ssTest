import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_llm_response(messages, system_prompt):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    
    full_messages = [
        {"role": "system", "content": system_prompt},
        *messages
    ]
    
    try:
        chat_completion = client.chat.completions.create(
            messages=full_messages,
            model="llama3-groq-8b-8192-tool-use-preview",
            max_tokens=1000
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        raise

# Example usage
if __name__ == "__main__":
    system_prompt = "You are a helpful movie director assistant."
    user_message = "What are some key elements of film noir?"
    messages = [{"role": "user", "content": user_message}]
    
    try:
        response = get_llm_response(messages, system_prompt)
        print("Groq API Response:")
        print(response)
    except Exception as e:
        print(f"Failed to get response: {e}")