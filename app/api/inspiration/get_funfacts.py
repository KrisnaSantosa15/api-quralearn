import json
import random

from app.api_models.base_response import BaseResponseModel

class GetFunfactsResponseModel(BaseResponseModel):
    class Config:
        json_schema_extra = {
            'example': {
                'data': {
                    'Id': 1000,
                    'Description': 'Oksigen dapat memiliki warna. Sebagai gas, oksigen tidak berbau dan tidak berwarna. Namun dalam bentuk cair dan padatnya, oksigen akan berwarna biru pucat.',
                    'Image': 'https://thumbs.dreamstime.com/b/oxigen-formula-vector-illustration-chemical-oxygen-65601560.jpg'
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }

async def get_funfacts():
    # Load fun facts from the JSON file
    with open('app/data/fun_facts.json', 'r') as file:
        data = json.load(file)

    fun_facts = data.get("data", [])  # Access the "data" key

    if not fun_facts:
        return GetFunfactsResponseModel(data="No fun facts found")  # Handle the case where no fun facts are available

    # Select a random fun fact
    random_fact = random.choice(fun_facts)
    return GetFunfactsResponseModel(data=random_fact)