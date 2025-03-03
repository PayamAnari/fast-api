from .. import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from fastapi import Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy import func

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    existing_user = (
        db.query(models.User).filter(models.User.email == user.email).first()
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )

    new_user = models.User(
        **user.dict(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = (
        db.query(models.User, func.count(models.Favorite.post_id).label("favorites"))
        .outerjoin(models.Favorite, models.Favorite.user_id == models.User.id)
        .group_by(models.User.id)
        .all()
    )

    user_out_list = []
    for user, favorites in users:
        user_out = schemas.UserOut(
            **user.__dict__,
            favorites=favorites,
        )
        user_out_list.append(user_out)

    return user_out_list


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user, favorites = (
        db.query(models.User, func.count(models.Favorite.post_id).label("favorites"))
        .outerjoin(models.Favorite, models.Favorite.user_id == models.User.id)
        .group_by(models.User.id)
        .filter(models.User.id == id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} was not found",
        )

    user_out = schemas.UserOut(
        **user.__dict__,
        favorites=favorites,
    )

    return user_out


@router.put("/{id}", response_model=schemas.UserOut)
def update_user(
    id: int,
    updated_user: schemas.UserCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} was not found",
        )
    hashed_password = utils.hash(updated_user.password)
    updated_user.password = hashed_password

    for key, value in updated_user.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    user = db.query(models.User).filter(models.User.id == id)

    if user.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id: {id} was not found",
        )

    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
