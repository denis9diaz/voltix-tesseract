1. crear entorno virtual
python3 -m venv env

2. activar entorno virtual
source env/bin/activate
.\env\Scripts\activate

3. instalar dependencias
pip install -r requirements.txt

4. run server
uvicorn main:app --reload
