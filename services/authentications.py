import jwt
import time
from config.settings import get_settings
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


settings = get_settings()

SECRET_KEY = settings.secret_key
JWT_ALGORITHM = settings.jwt_algorithm


async def decode(token):
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=JWT_ALGORITHM)
    return decoded_token


async def encode(token):
    encoded_token = jwt.encode(token, SECRET_KEY, algorithms=JWT_ALGORITHM)
    return encoded_token


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    async def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = await decode(jwtoken)

        except:
            payload = None
        if payload:
            jti = payload['jti']
            token = await get_one({'jti': jti}, jwt_collection)

            if token is not None:
                isTokenValid = True
        return isTokenValid
    