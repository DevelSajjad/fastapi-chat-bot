from openai import OpenAI
from google import genai
import requests



def generate_ai_response(provider, message):


    if provider.provider_type == "openai":


        client = OpenAI(
            api_key=provider.api_key
        )


        response = client.chat.completions.create(

            model=provider.model,

            messages=[

                {
                    "role":"system",
                    "content":"You are a helpful AI assistant."
                },

                {
                    "role":"user",
                    "content":message
                }

            ],

            # temperature=float(
            #     provider.temperature
            # ),

            # max_completion_tokens=provider.max_tokens

        )


        return response.choices[0].message.content





    elif provider.provider_type == "ollama":


        response = requests.post(

            provider.base_url,

            json={

                "model":provider.model,

                "prompt":message,

                "stream":False

            }

        )


        return response.json()["response"]
    
    elif provider.provider_type == "gemini":

        client = genai.Client(
            api_key=provider.api_key
        )

        response = client.models.generate_content(
            model=provider.model,
            contents=message
        )

        return response.text
    
    elif provider.provider_type == "deepseek":

        client = OpenAI(

            api_key=provider.api_key,

            base_url=provider.base_url
        )

        response = client.chat.completions.create(

            model=provider.model,

            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],

            # max_tokens=provider.max_tokens
        )

        return response.choices[0].message.content

    elif provider.provider_type == "openrouter":

        client = OpenAI(
            api_key=provider.api_key,
            base_url=provider.base_url
        )

        response = client.chat.completions.create(
            model=provider.model,

            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.choices[0].message.content

    else:

        raise Exception(
            "Unsupported AI provider"
        )