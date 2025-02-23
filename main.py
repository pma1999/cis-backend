from fastapi import FastAPI
from backend.services import cargar_datos, listar_variables, obtener_datos_variable, obtener_distribucion, obtener_metadatos

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS para el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permite peticiones desde el frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
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