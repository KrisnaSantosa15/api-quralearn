import os
from os import path
import sounddevice as sd
import scipy.io.wavfile as wav
import torch
import librosa

from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from lang_trans.arabic import buckwalter
from fastapi import UploadFile, File
from fastapi.responses import JSONResponse
from typing import List

# Define a directory where you want to save the sound files
UPLOAD_DIRECTORY = "upload_directory"

def load_Quran_fine_tuned_elgeish_xlsr_53_model_and_processor():
    global loaded_model, loaded_processor
    loaded_model = Wav2Vec2ForCTC.from_pretrained("Nuwaisir/Quran_speech_recognizer").eval()
    loaded_processor = Wav2Vec2Processor.from_pretrained("Nuwaisir/Quran_speech_recognizer")

def predict_sound_file(file_path, loaded_model, loaded_processor):
    speech, _ = librosa.load(file_path, sr=16000)
    inputs = loaded_processor(speech, sampling_rate=16000, return_tensors="pt", padding=True)
    with torch.no_grad():
        predicted = torch.argmax(loaded_model(inputs.input_values).logits, dim=-1)
    predicted[predicted == -100] = loaded_processor.tokenizer.pad_token_id  # see fine-tuning script
    pred_1 = loaded_processor.tokenizer.batch_decode(predicted)[0]
    predicted_text = buckwalter.untrans(pred_1)
    return predicted_text

load_Quran_fine_tuned_elgeish_xlsr_53_model_and_processor()

async def quran_recognizer(sounds: List[UploadFile] = File(...)):
    """Quran Recognizer
            
            This API is used to recognize quran sound.
            
            the sound file must be in .wav format. 
    """
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)

    for sound in sounds:
        # Save the uploaded sound file to a local directory
        sound_path = os.path.join(UPLOAD_DIRECTORY, sound.filename)
        with open(sound_path, "wb") as file:
            file.write(sound.file.read())

        # Predict the transcribed text
        transcribed_text = predict_sound_file(sound_path, loaded_model, loaded_processor)
        response_data = {"message": transcribed_text, "success": True, "code": 200, "meta": {}, "data": ""}


    return JSONResponse(content=response_data)