from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0, description="Product price")
    category_id: int = Field(..., description="Category ID")
    image_url: Optional[str] = Field(None, description="Product image URL")

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=100)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    category_id: Optional[int] = None
    image_url: Optional[str] = None

class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="Unique product ID")
    created_at: datetime
    category: CategoryResponse = Field(..., description="Product category details")

class ProductListResponse(BaseModel):
    products: list[ProductResponse] = Field(..., description="List of products")
    total: int = Field(..., description="Total number of products")