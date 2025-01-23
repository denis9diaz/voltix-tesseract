from fastapi import FastAPI, File, UploadFile, HTTPException
from app.services.ocr_service import procesar_pdf, procesar_imagen
from tempfile import NamedTemporaryFile
import os

app = FastAPI()

@app.post("/ocr/procesar")
async def procesar_ocr(file: UploadFile = File(...)):

    file_extension = os.path.splitext(file.filename)[1].lower()

    with NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    # Verifica si es PDF o imagen
    if file_extension == ".pdf":
        try:
            texto_extraido = procesar_pdf(temp_file_path)
            return {"extracted_text": texto_extraido}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error al procesar el PDF: {e}")
    
    elif file_extension in [".jpg", ".jpeg", ".png", ".tiff"]:
        try:
            texto_extraido = procesar_imagen(temp_file_path)
            return {"extracted_text": texto_extraido}
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error al procesar la imagen: {e}")
    
    else:
        raise HTTPException(status_code=400, detail="Formato no soportado. Solo se admiten archivos PDF o de imagen (JPG, PNG, TIFF).")

