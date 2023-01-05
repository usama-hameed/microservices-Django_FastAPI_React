import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.responses import Response

from schema import ProductSchema, ProductUserSchema
from models import Product, ProductUser
import os
from dotenv import load_dotenv
from .producer import publish
app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url='postgresql://postgres:admin123@localhost/main')


@app.get('/api/products')
def index():
    products = Product.query.all()
    return Response(products, status_code=200)


@app.post('api/products/{id}/like')
def like(id: int):
    import requests
    req = requests.get('http://host.docker.internal:8000/api/user')
    try:
        productuser = ProductUser(user_id=req['id'], product_id=id)
        db.session.add(productuser)
        publish('Product Liked', id)
    except:
        return Response({'message': 'You already liked this project'}, status_code=400)
    return Response({'message': 'Success'}, status_code=200)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
