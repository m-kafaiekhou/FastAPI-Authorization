from typing import Dict
from fastapi import Body, Depends, HTTPException, Header, APIRouter

from schemas.authorization_schemas import *
from services.authentications import JWTBearer


router = APIRouter()

@router.post('/login', response_model=Dict)
async def login(
        payload: UserLoginSchema,
    ):

    pass


@router.post('/register', response_model=Dict)
async def register(
        payload: CreateUserSchema = Body(),
    ):

    pass


@router.post('/logout', response_model=Dict)
async def logout(
        token: bool = Depends(JWTBearer())
    ):

    pass


@router.post('/reset-password', response_model=Dict)
async def reset_password(
        payload: CreateUserSchema = Body(),
    ):

    pass


@router.post('/forgot-password', response_model=Dict)
async def forgot_password(
        payload: CreateUserSchema = Body(),
    ):

    pass


@router.post('/forgot-password-reset', response_model=Dict)
async def forgot_password(
        payload: CreateUserSchema = Body(),
    ):

    pass


@router.get('/testauth')
async def testauth(token: bool = Depends(JWTBearer())):
    return {'message': 'Authenticated Ahmad Mohsen'}
