from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter()

@router.post(
    "/signup",
    tags=["users"],
    summary="User Signup",
    description="Endpoint for user signup",
    response_model=schemas.UserDetails
)
async def signup(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.usertable(
        username=user.username,
        email=user.email,
        password=user.password,
        confirmpassword=user.confirmpassword
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
