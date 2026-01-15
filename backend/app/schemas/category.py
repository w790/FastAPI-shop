from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="Category name")
    slug: str = Field(..., min_length=5, max_length=100, description="URL-friendly category name")

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=100)
    slug: Optional[str] = Field(None, min_length=5, max_length=100)

class CategoryResponse(CategoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description="Unique category identifier")
    
