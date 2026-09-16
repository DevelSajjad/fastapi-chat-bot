from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto"
)

def hash_password(password: str):

    return pwd_context.hash(password[:72])

def verify_password(plainpassword, hashedpassword):

    return pwd_context.verify(plainpassword[:72], hashedpassword)

def common_parameters():

    return {
        'id': 1
    }