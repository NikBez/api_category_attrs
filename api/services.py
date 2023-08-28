from fastapi.exceptions import HTTPException

from api import queries
from clickhouse.connect import db


async def get_categories_attrs(category_id: str, product_id: str):
    query = queries.get_product_analitic_query(category_id, product_id)
    response = await db.execute(query)

    if not response:
        raise HTTPException(404, detail='Нет данных по заданным параметрам')
    annotation = response[0][4]
    modified_images = response[0][5] + ';https://ir.ozone.ru/s3/multimedia-a/wc1000/6136837342.jpg'
    pointer = annotation.find("<br/>")
    required_values = '<br/>'.join(response[0][6])

    if not pointer == -1:
        modified_annotation = annotation[0:pointer + 5] + '😀' + '<br/>' + required_values + annotation[pointer + 5:]
    else:
        modified_annotation = annotation + '<br/>😀<br/>' + required_values

    result = {
        'total_count': response[0][0],
        'blank_percentage': response[0][1],
        'annotation_length': response[0][2],
        'images_count': response[0][3],
        'modified_annotation': modified_annotation,
        'modified_images': modified_images
    }
    return result
