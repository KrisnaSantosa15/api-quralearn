# Speech Quran Recognier (API)
## Description
This is a simple API for speech recognition of the Quran. It is based on the [Quran_speech_recognizer](https://huggingface.co/Nuwaisir/Quran_speech_recognizer). This API build on top of [FastAPI](https://fastapi.tiangolo.com/).

## Usage

### Endpoints
```
POST: api/v1/recognizer
Response: {
    "message": transcribed_text, 
    "success": True, 
    "code": 200, 
    "meta": {}, 
    "data": ""
}
```
