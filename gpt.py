from g4f.client import Client

def text_manager(prompt):
    """
    Takes a prompt and returns the AI's response using the g4f (GPT4Free) library.
    """
    try:
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"
