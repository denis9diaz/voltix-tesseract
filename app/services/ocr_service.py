from pdf2image import convert_from_path
import pytesseract
from fastapi import HTTPException
from PIL import Image

def convertir_pdf_a_imagen(pdf_path: str):
    images = convert_from_path(pdf_path)
    return images


def procesar_pdf(pdf_path: str):
    images = convertir_pdf_a_imagen(pdf_path)
    
    texto_extraido = ""
    for image in images:
        texto_extraido += pytesseract.image_to_string(image)
    
    return texto_extraido


def procesar_imagen(image_path: str):
    imagen = Image.open(image_path)

    texto_extraido = pytesseract.image_to_string(imagen)
    
    return texto_extraido
