import os
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "default_secret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

def validate_token(token: str) -> bool:
    """
    Valida un JWT y retorna True si es válido, False si es inválido o expirado.
    """
    try:
        jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return True
    except (ExpiredSignatureError, InvalidTokenError):
        return False
