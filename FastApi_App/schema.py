from pydantic import BaseModel


class ProductSchema(BaseModel):
    title: str
    image: str

    class config:
        orm_model = True


class ProductUserSchema(BaseModel):
    user_id: int
    product_id: int

    class config:
        orm_mode = True
