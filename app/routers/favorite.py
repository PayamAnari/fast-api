from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, models, database, oauth2

router = APIRouter(
    prefix="/favorite",
    tags=["favorite"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def favorite_post(
    favorite: schemas.Favorite,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == favorite.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with {favorite.post_id} not found",
        )

    favorite_query = db.query(models.Favorite).filter(
        models.Favorite.post_id == favorite.post_id,
        models.Favorite.user_id == current_user.id,
    )
    found_favorite = favorite_query.first()
    if favorite.dir == 1:
        if found_favorite:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.id} has already Added post {favorite.post_id} to favorites",
            )

        new_favorite = models.Favorite(
            post_id=favorite.post_id, user_id=current_user.id
        )
        db.add(new_favorite)
        db.commit()
        return {
            "message": f"Post {favorite.post_id} has been added to favorites for user {current_user.id}"
        }
    else:
        if not found_favorite:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User {current_user.id} has not added post {favorite.post_id} to favorites",
            )

        favorite_query.delete()
        db.commit()
        return {
            "message": f"Post {favorite.post_id} has been removed from favorites for user {current_user.id}"
        }
