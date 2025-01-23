1. crear entorno virtual
python3 -m venv env

2. activar entorno virtual
source env/bin/activate
.\env\Scripts\activate

3. instalar dependencias
python install -r requirements.txt

4. run server
uvicorn main:app --reload
uvicorn app.main:app --reload --port 8080

5. .../docs
