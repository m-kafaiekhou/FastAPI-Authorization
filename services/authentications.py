from config.settings import get_settings
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.auth import decode
from services.redis import get_redis


settings = get_settings()


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == settings.jwt_token_prefix:
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return await decode(credentials.credentials)
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
            token = await get_one({'jti': jti}, jwt_collection) # TODO redis

            if token is not None:
                isTokenValid = True
        return isTokenValid
    
    async def get_the_token_from_header(self, token):
        token = token.replace(settings.jwt_token_prefix, '').replace(' ', '')
        return token
    
    async def validate_token(self, token):
        cleaned_token = self.get_the_token_from_header(token)

        sel
    