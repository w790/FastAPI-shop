from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session 
from typing import List
from ..database import get_db
from ..services.cart_service import CartService
from ..schemas.cart import CartResponse, CartItemCreate, CartItemUpdate, GetCartRequest

router = APIRouter(
    prefix="/api/cart",
    tags=["Cart"]
)

class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int, int] = {}

class RemoveFromCartRequest(BaseModel):
    product_id: int
    cart: Dict[int, int] = {}

@router.post("/add", response_model=CartResponse, status_code=status.HTTP_201_CREATED)
def add_to_cart(request: AddToCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    item = CartItemCreate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = service.add_to_cart(request.cart, item)
    return service.get_cart_details(updated_cart)

@router.post("", response_model=CartResponse, status_code=status.HTTP_200_OK)
def get_cart(request: GetCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    return service.get_cart_details(request.cart)

@router.put("/update", response_model=CartResponse, status_code=status.HTTP_200_OK)
def update_cart_item(request: AddToCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    item = CartItemUpdate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = service.update_cart_item(request.cart, item)
    return service.get_cart_details(updated_cart)

@router.delete("/remove", response_model=CartResponse, status_code=status.HTTP_200_OK)
def remove_from_cart(request: RemoveFromCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    updated_cart = service.remove_from_cart(request.cart, request.product_id)
    return service.get_cart_details(updated_cart)
