from fastapi import FastAPI
from services import cargar_datos, listar_variables, obtener_datos_variable, obtener_distribucion, obtener_metadatos
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Lista de orígenes permitidos (frontend en Vercel y Railway)
origins = [
    "https://cis-visualizaciones-r7qrpuc3c-pablos-projects-d80d0b2f.vercel.app/",  # Reemplaza con tu URL final en Vercel
    "https://railway.app",
    "http://localhost:5173",  # Para pruebas locales
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir peticiones desde estos dominios
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

@app.get("/")
def leer_raiz():
    return {"mensaje": "API de Visualización del CIS"}

@app.get("/datos")
def obtener_datos():
    data = cargar_datos()
    return {"datos": data.to_dict(orient="records")}

@app.get("/variables")
def obtener_variables():
    return {"variables": listar_variables()}

@app.get("/datos/{variable}")
def obtener_datos(variable: str):
    data = obtener_datos_variable(variable)
    return {"datos": data.to_dict(orient="records")}

@app.get("/distribucion/{variable}")
def obtener_distribucion_variable(variable: str):
    distribucion = obtener_distribucion(variable)
    return {"distribucion": distribucion}

@app.get("/metadatos")
def obtener_metadatos_api():
    return obtener_metadatos()