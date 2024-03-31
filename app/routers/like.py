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
    like_query = db.query(models.Like).filter(
        models.Like.post_id == like.post_id, models.Like.user_id == current_user.id
    )
    found_like = like_query.first()
    if like.dir == 1:
        if found_like:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.id} already liked post {like.post_id}",
            )

        new_like = models.Like(post_id=like.post_id, user_id=current_user.id)
        db.add(new_like)
        db.commit()
        return {"message": f"User {current_user.id} liked post {like.post_id}"}
    else:
        if not found_like:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {current_user.id} has not liked post {like.post_id}",
            )

        like_query.delete()
        db.commit()
        return {"message": f"User {current_user.id} unliked post {like.post_id}"}
