from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.beckend.db_depends import get_db
from typing import Annotated
from app.models.user import User
from sqlalchemy import insert, select, update, delete
from app.schemas import CreateUser, UpdateUser

from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.post('/create')
def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    # Проверка на существование пользователя
    existing_user = db.scalar(select(User).where(User.username == create_user.username))
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this username already exists")

    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


# ---------------------------------
# ---------------------------------


@router.get('/user_id')
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Получение пользователя по id
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    

@router.get('/')
def all_users(db: Annotated[Session, Depends(get_db)]):
    username = db.scalars(select(User)).all()
    return username


# -----------------------------
@router.put('/update_user')
def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: CreateUser):
    usernames = db.scalar(select(User).where(User.id == user_id))
    if usernames is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age,
    ))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


# -----------------------------------------------


@router.delete('/delete')
def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    db.execute(delete(User).where(User.id == user_id))
    # db.execute(update(User).where(user.id == user_id).values(is_active=False))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'
    }


# # Удаление всех пользователей и задач из базы данных для теста
# @router.delete("/deleteAll")
# def delete_all_users(db: Annotated[Session, Depends(get_db)]):
#     # Проверяем, есть ли пользователи в базе данных
#     result = db.execute(select(User)).scalars().all()
#
#     if result:  # Если список пользователей не пуст
#         db.execute(delete(User))
#         db.commit()
#         return {'status_code': status.HTTP_200_OK, 'transaction': 'All users and tasks deleted!'}
#     else:  # Если список пользователей пуст
#         return {'status_code': status.HTTP_200_OK, 'transaction': 'No users and tasks to delete'}
