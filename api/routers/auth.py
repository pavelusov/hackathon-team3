# from jose import jwt
# from starlette import status
# from typing import Annotated
# from pydantic import BaseModel
# from datetime import timedelta, datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from api.models import User
from api.dependencies import db_dependency_type, bcrypt_context, SECRET_KEY, ALGORITHM


router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

#
# class SignupModel(BaseModel):
#     username: str
#     email: str
#     password: str
#
#
# class LoginModel(BaseModel):
#     username: str
#     password: str
#
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str

#
# def authenticate_user(username: str, password: str, db):
#     user = db.query(User).filter(User.username == username).one_or_none()
#     if not user:
#         return False
#     if not bcrypt_context.verify(password, user.hashed_password):
#         return False
#     return user
#
#
# def create_access_token(username: str, user_id: int, expires_delta: timedelta):
#     encode = {'sub': username, 'id': user_id}
#     expires = datetime.utcnow() + expires_delta
#     encode.update({'exp': expires})
#     return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM[0])


@router.get('/test')
async def testing_page():
    return {"data": "Data from our Python server"}

@router.get('/leaderboard')
async def leaderboard():
#   SELECT DISTINCT name, id, score FROM leaderboard ORDER BY score DESC LIMIT 3

    return {
        "data": [
            {"id": 1, "name": "Johny", "score": 30},
            {"id": 2, "name": "Mary", "score": 31},
            {"id": 3, "name": "Bloody Mary", "score": 32},
            {"id": 4, "name": "Ann", "score": 33},
            {"id": 5, "name": "Ann", "score": 20},
            {"id": 6, "name": "Ann", "score": 11},
        ]
    }

#
# @router.post('/signup')
# async def create_user(db: db_dependency_type, signup_data: SignupModel):
#     hashed_password = bcrypt_context.hash(signup_data.password)
#     user_to_create = User(
#         email=signup_data.email,
#         username=signup_data.username,
#         hashed_password=hashed_password
#     )
#
#     db.add(user_to_create)
#     db.commit()
#
#     return {
#                 "data":
#                 {
#                     "username": user_to_create.username,
#                     "email": user_to_create.username,
#                     "message": "Registration succeeded",
#                 }
#             }
#
#
# @router.post('/token', response_model=Token)
# async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency_type):
#     user = authenticate_user(form_data.username, form_data.password, db)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not valid user')
#
#     token = create_access_token(user.username, user.id, expires_delta=timedelta(minutes=20))
#     return {'access_token': token, 'token_type': 'bearer'}
