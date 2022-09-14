import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.responses import Response

from schema import ProductSchema, ProductUserSchema
from models import Product, ProductUser
import os
from dotenv import load_dotenv

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url='postgresql://postgres:admin123@localhost/main')


@app.get('/api/products')
def index():
    products = Product.query.all()
    return Response(products, status_code=200)

@app

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
