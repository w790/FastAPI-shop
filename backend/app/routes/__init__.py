from .categories import router as categories_router
from .products import router as products_router
from .cart import router as cart_router

__all__ = [
    "categories_router",
    "products_router",
    "cart_router"
]
