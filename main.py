import shutil
import uvicorn
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # Importa StaticFiles
from api.routes import router
from db.connection import Base, engine

app = FastAPI()

# Monta el directorio de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/upload/")
async def upload_file(usuario: str=  Form(...), file: UploadFile = File(...)):
    nombre_archivo= f"{usuario}_{file.filename}"
    file_location = f"static/images/{nombre_archivo}"
    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": nombre_archivo, "fileLocation": file_location}



app.include_router(router=router)



origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



Base.metadata.create_all(bind=engine)





if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
