from fastapi.responses import FileResponse
import os

from app.api_models.base_response import BaseResponseModel

class getFunfactsImagesResponseModel(BaseResponseModel):
    class Config:
        json_schema_extra = {
            'example': {
                'data': {
                    'Image': '/api/v1/images/1.png'
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }

async def get_funfacts_images(image: str):
    path = 'app/data/image_funfacts'
    image_path = os.path.join(path, image)

    if os.path.exists(image_path):
        return FileResponse(image_path, headers={"Content-Type": "image/png"})
    else:
        return getFunfactsImagesResponseModel(data="No image found")
