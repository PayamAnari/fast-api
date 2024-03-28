from .. import models, schemas, utils
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from ..database import get_db

router = APIRouter()


@router.get("/posts", response_model=list[schemas.Post])
def get_posts(
    db: Session = Depends(get_db),
):
    posts = db.query(models.Post).all()

    return posts


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.CreatePost, db: Session = Depends(get_db)):

    new_post = models.Post(
        **post.dict(),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": "Post successfully created", "data": new_post}


@router.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    return post


@router.put(
    "/posts/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Post
)
def update_post(
    id: int, updated_post: schemas.UpdatePost, db: Session = Depends(get_db)
):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {"message": "Post successfully updated", "data": post_query.first()}


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
