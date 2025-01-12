from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import procesar_pdf

# ruta localhost/ocr/procesar
router = APIRouter(prefix="/ocr", tags=["OCR"])

@router.post("/procesar")
async def procesar(file: UploadFile = File(...)):
    file_bytes = await file.read()
    resultado = await procesar_pdf(file_bytes)
    return resultado