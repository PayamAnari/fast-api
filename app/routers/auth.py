from fastapi import APIRouter, Depends, HTTPException, Response
from .. import schemas, models, utils, oauth2
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(tags=["Authentications"])


@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):

    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.email)
        .first()
    )
    if not user:
        raise HTTPException(status_code=404, detail=f"Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=404, detail=f"Invalid credentials")

    access_token = oauth2.create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
