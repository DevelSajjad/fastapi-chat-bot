from pydantic import BaseModel

class AIProviderCreate(BaseModel):
    name:str

    provider_type:str

    api_key:str | None = None

    base_url:str | None = None

    model:str

    temperature:float = 0.7

    max_tokens:int = 2000

    is_active:bool = True





class AIProviderUpdate(BaseModel):

    name:str | None = None

    provider_type:str | None = None

    api_key:str | None = None

    base_url:str | None = None

    model:str | None = None

    temperature:float | None = None

    max_tokens:int | None = None

    is_active:bool | None = None




class AIProviderResponse(BaseModel):

    id:int

    name:str

    provider_type:str

    model:str

    is_active:bool


    class Config:

        from_attributes=True