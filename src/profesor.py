import os
import random
import requests

# Catálogo completo de 20 temas disponibles para redes sociales
TEMAS_DISPONIBLES = [
    "Disciplina financiera",
    "Mentalidad de crecimiento",
    "Superación de obstáculos",
    "Productividad extrema",
    "Hábitos de éxito",
    "Control de emociones",
    "Gestión del tiempo",
    "Educación financiera",
    "Liderazgo personal",
    "Resiliencia ante el fracaso",
    "Inversión inteligente",
    "Inteligencia emocional",
    "Construcción de activos",
    "Mentalidad antifrágil",
    "Hábitos de los millonarios",
    "Toma de decisiones bajo presión",
    "Eliminación de distracciones",
    "Construcción de marca personal",
    "Persistencia y constancia",
    "Dominio de la atención"
]

def obtener_tema(parametro_usuario="aleatorio"):
    """Selecciona un tema diario o aleatorio para los videos."""
    if parametro_usuario.lower() == "aleatorio":
        return random.choice(TEMAS_DISPONIBLES)
    return parametro_usuario

def buscar_imagen_pexels(query, api_key):
    """Busca una imagen en Pexels usando la API y devuelve la URL."""
    headers = {"Authorization": api_key}
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            photos = data.get("photos", [])
            if photos:
                return photos[0]["src"]["large2x"]
    except Exception as e:
        print(f"Error al conectar con Pexels: {e}")
    return None

def generar_guion_video(tema):
    """Genera la estructura del video con gancho y párrafos motivacionales (Duración objetivo: 75-85s)."""
    ganchos = [
        f"¿Sabías que el 99% de las personas fracasan en {tema.lower()} por este único error?",
        f"Deja de hacer esto si realmente quieres dominar {tema.lower()} este año.",
        f"Nadie te está diciendo la verdad sobre {tema.lower()}, hasta hoy."
    ]
    
    guion = {
        "gancho": random.choice(ganchos),
        "escenarios": [
            "Párrafo 1: El punto de quiebre y la realidad actual a la que te enfrentas cada día.",
            "Párrafo 2: La estrategia clave o el cambio de mentalidad necesario para romper el ciclo.",
            "Párrafo 3: La ejecución práctica, el esfuerzo diario y la consistencia inquebrantable.",
            "Párrafo 4: El llamado a la acción final y la visión de éxito a largo plazo."
        ]
    }
    return guion

def iniciar_proceso():
    print("Iniciando el generador de videos - Módulo Profesor...")
    
    # Obtenemos la API Key de Pexels desde los secrets de GitHub o entorno local
    pexels_api_key = os.getenv("PEXELS_API_KEY", "TU_API_KEY_POR_DEFECTO")
    
    # Producción de 5 videos por día (Total 35 semanales simulados en la ejecución)
    videos_por_dia = 5
    print(f"Planificando la creación de {videos_por_dia} videos para la jornada...")
    
    for i in range(1, videos_por_dia + 1):
        tema_actual = obtener_tema("aleatorio")
        guion = generar_guion_video(tema_actual)
        imagen_url = buscar_imagen_pexels(tema_actual, pexels_api_key)
        
        print(f"\n--- Video {i} de {videos_por_dia} ---")
        print(f"Tema: {tema_actual}")
        print(f"Gancho: {guion['gancho']}")
        print(f"Escenarios (Motivación): {len(guion['escenarios'])} párrafos listos.")
        print(f"Imagen de Pexels asignada: {'Éxito' if imagen_url else 'No disponible'}")

if __name__ == "__main__":
    iniciar_proceso()
