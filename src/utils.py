from .dependencies import *
from .instructions import *
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_question(chat) :
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": system_instruction
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": chat
                }
            ]
            },
        ],
        response_format={
            "type": "text"
        },
        temperature=0.8,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response