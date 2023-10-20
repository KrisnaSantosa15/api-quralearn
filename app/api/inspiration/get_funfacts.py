import json
import random
import os 

from app.api_models.base_response import BaseResponseModel

class GetFunfactsResponseModel(BaseResponseModel):
    class Config:
        json_schema_extra = {
            'example': {
                'data': {
                    'Id': 1000,
                    'Description': 'Oksigen dapat memiliki warna. Sebagai gas, oksigen tidak berbau dan tidak berwarna. Namun dalam bentuk cair dan padatnya, oksigen akan berwarna biru pucat.',
                    'Image': '/api/v1/images/1.png'
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

    # List image files in the app/data/images_quotes folder
    image_funfact_folder = 'app/data/image_funfacts'
    image_files = [f for f in os.listdir(image_funfact_folder) if os.path.isfile(os.path.join(image_funfact_folder, f))]

    
    fun_facts = data.get("data", [])  # Access the "data" key

    if not fun_facts:
        return GetFunfactsResponseModel(data="No fun facts found")  # Handle the case where no fun facts are available

    # select a random image
    random_image = random.choice(image_files)
    # add the image to the fun facts
    # Select a random fun fact
    random_fact = random.choice(fun_facts)
    random_fact['image'] = f'/api/v1/funfacts_images/{random_image}'
    return GetFunfactsResponseModel(data=random_fact)