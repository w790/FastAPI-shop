from pydantic import BaseModel, Field
from typing import Optional, Dict

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="New Quantity")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity in cart")  
    subtotal: float = Field(..., description="Total price for this item (price * quantity)")
    image_url: Optional[str] = Field(None, description="Product image URL")

class GetCartRequest(BaseModel):
    cart: Dict[int, int] = Field(default_factory=dict, description="Cart data (product_id: quantity)")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in the cart")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in cart")
    cart: Dict[int, int] = Field(..., description="Current state of cart (product_id: quantity)")
