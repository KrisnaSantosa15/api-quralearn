import json
import random

from app.api_models.base_response import BaseResponseModel

class GetQuotesResponseModel(BaseResponseModel):
    class Config:
        json_schema_extra = {
            'example': {
                'data': {
                    'Id': 1000,
                    'Title': 'Bersabar',
                    'Description': 'Dan kami jadikan sebagian kalian cobaan bagi sebagian yang lain. Maukah kalian bersabar? Q.S Al-Furqan: 20',
                    'Image': 'https://www.finansialku.com/wp-content/uploads/2017/12/Ilustrasi-Cara-Bertahan-dari-Badai-Kehidupan-02-Finansialku.jpg'
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }

async def get_quotes():
    # Load fun facts from the JSON file
    with open('app/data/quotes.json', 'r') as file:
        data = json.load(file)

    quotes = data.get("data", [])  # Access the "data" key

    if not quotes:
        return GetQuotesResponseModel(data="No Quotes found")  # Handle the case where no fun facts are available

    # Select a random fun fact
    random_fact = random.choice(quotes)
    return GetQuotesResponseModel(data=random_fact)