from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    title = Column(String)
    image = Column(String)


class ProductUser(Base):
    __tablename__ = "product_user"
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    product_id = Column(String)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')
