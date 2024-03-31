from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, models, database, oauth2


router = APIRouter(
    prefix="/likes",
    tags=["likes"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def like_post(
    like: schemas.Like,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == like.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    post.likes += 1
    db.commit()
    return {"message": "Post liked successfully"}
