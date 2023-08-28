from fastapi import FastAPI

from api.schemas import AttrsParam
from api import services

app = FastAPI()


@app.post('/', response_model=AttrsParam)
async def get_categories_attrs(category_id: str, product_id: str):
    response = await services.get_categories_attrs(category_id, product_id)
    return response
