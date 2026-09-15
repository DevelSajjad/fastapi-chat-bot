from fastapi import FastAPI
from app.schemas import ProductCreate, ResponseProduct

app = FastAPI()

@app.get('/')
def home():
    return {
        'Welcome Home. This fastapi project.'
    }

@app.get('/about')
def about():
    return {
        "Name" : "Ai Chat Platform",
        "Version": "1.0.0",
        "Developer": "Devel"
    }

@app.get('/hello/{name}')
def hello(name):
    return {
        "Hello " + name
    }

# @app.post('/users', response_model=UserResponse)
# def create_user(user: UserCreate):
#     return {
#         "message": "User Create Successfully",
#         "user": user
#     }

@app.post('/products', response_model=ResponseProduct)
def create_product(product: ProductCreate):
    return product