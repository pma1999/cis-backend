import pandas as pd
import pyreadstat
import os

def cargar_datos():
    archivo_sav = "data/3492.sav"  # Asegúrate de subir el archivo aquí
    df, meta = pyreadstat.read_sav(archivo_sav)
    return df

def listar_variables():
    archivo_sav = os.path.abspath("data/3492.sav")
    _, meta = pyreadstat.read_sav(archivo_sav)
    
    # Crear un diccionario que asocia el nombre de la variable a su etiqueta
    mapping = {}
    for name, label in zip(meta.column_names, meta.column_labels):
        mapping[name] = label
    return mapping


def obtener_datos_variable(variable: str):
    archivo_sav = "data/3492.sav"
    df, _ = pyreadstat.read_sav(archivo_sav)
    
    if variable not in df.columns:
        return {"error": "Variable no encontrada"}
    
    return df[[variable]].dropna()  # Devuelve solo la columna solicitada, eliminando nulos

def obtener_distribucion(variable: str):
    archivo_sav = "data/3492.sav"
    df, _ = pyreadstat.read_sav(archivo_sav)
    
    if variable not in df.columns:
        return {"error": "Variable no encontrada"}
    
    conteo = df[variable].value_counts().to_dict()  # Cuenta respuestas
    return conteo



def obtener_metadatos():
    archivo_sav = os.path.abspath("data/3492.sav")
    df, meta = pyreadstat.read_sav(archivo_sav)

    # Diccionario de etiquetas de variables
    etiquetas_variables = meta.column_labels

    # Diccionario de etiquetas de valores
    etiquetas_valores = meta.variable_value_labels

    return {
        "etiquetas_variables": etiquetas_variables,
        "etiquetas_valores": etiquetas_valores
    }

def obtener_contingencia(variable1: str, variable2: str):
    archivo_sav = "data/3492.sav"
    df, meta = pyreadstat.read_sav(archivo_sav)
    
    if variable1 not in df.columns or variable2 not in df.columns:
        return {"error": "Una o ambas variables no encontradas"}
    
    # Crear tabla de contingencia
    contingencia = pd.crosstab(df[variable1], df[variable2], margins=True)
    
    # Calcular porcentajes por fila y columna
    porcentajes_fila = pd.crosstab(df[variable1], df[variable2], normalize='index') * 100
    porcentajes_columna = pd.crosstab(df[variable1], df[variable2], normalize='columns') * 100
    
    # Convertir a diccionarios para la respuesta JSON
    return {
        "tabla": contingencia.to_dict(),
        "porcentajes_fila": porcentajes_fila.to_dict(),
        "porcentajes_columna": porcentajes_columna.to_dict(),
        "total_casos": int(contingencia.iloc[-1, -1])  # Total general
    }
