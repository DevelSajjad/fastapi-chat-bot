from openai import OpenAI
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

            temperature=float(
                provider.temperature
            ),

            max_tokens=provider.max_tokens

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

    else:

        raise Exception(
            "Unsupported AI provider"
        )