import json
import random
import os

from app.api_models.base_response import BaseResponseModel

class GetQuotesResponseModel(BaseResponseModel):
    class Config:
        json_schema_extra = {
            'example': {
                'data': {
                    'Id': 1000,
                    'Title': 'Bersabar',
                    'Description': 'Dan kami jadikan sebagian kalian cobaan bagi sebagian yang lain. Maukah kalian bersabar? Q.S Al-Furqan: 20',
                    'Image': '/api/v1/images/1.png'
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }

async def get_quotes(count: int = 1):
    # Load quotes from the JSON file
    with open('app/data/quotes.json', 'r') as file:
        data = json.load(file)

    # List image files in the app/data/images_quotes folder
    image_quotes_folder = 'app/data/image_quotes'
    image_files = [f for f in os.listdir(image_quotes_folder) if os.path.isfile(os.path.join(image_quotes_folder, f))]

    quotes = data.get("data", [])  # Access the "data" key

    if not quotes:
        return GetQuotesResponseModel(data="No Quotes found")  # Handle the case where no quotes are available

    if count <= 0:
        return GetQuotesResponseModel(data="Invalid count")  # Handle invalid count values

    # Select random quote(s) along with their associated images
    selected_quotes = []
    for _ in range(count):
        random_quote = random.choice(quotes)
        random_image = random.choice(image_files)
        random_quote['Image'] = f'/api/v1/images/{random_image}'
        selected_quotes.append(random_quote)

    return GetQuotesResponseModel(data=selected_quotes)