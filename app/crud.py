from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models
from .auth import hash_password


# 👤 User
def create_user(db: Session, email, password):
    existing_user = db.query(models.User).filter(models.User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(password)
    user = models.User(email=email, password=hashed)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, email):
    return db.query(models.User).filter(models.User.email == email).first()


# 🛍️ Product
def create_product(db: Session, data):
    product = models.Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_products(db: Session, skip=0, limit=10):
    return db.query(models.Product).offset(skip).limit(limit).all()


# 📦 Order
def create_order(db: Session, user_id, product_id):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    order = models.Order(user_id=user_id, product_id=product_id)

    db.add(order)
    db.commit()
    db.refresh(order)
    return order