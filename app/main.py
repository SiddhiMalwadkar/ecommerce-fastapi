from fastapi import FastAPI
from .database import Base, engine
from .routes import user, product, order

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scalable E-Commerce API")

# Root route (IMPORTANT for deployment check)
@app.get("/")
def home():
    return {"message": "E-Commerce API is running 🚀"}

# Routers
app.include_router(user.router, prefix="/auth", tags=["Auth"])
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])