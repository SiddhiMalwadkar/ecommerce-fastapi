from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud
from ..auth import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🛒 Place Order (Protected)
@router.post("/")
def place_order(
    order: schemas.OrderCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return crud.create_order(db, user_id=user_id, product_id=order.product_id)