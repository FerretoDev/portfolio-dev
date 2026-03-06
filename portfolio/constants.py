# ─── Analytics ────────────────────────────────────────────────────────────────
# Google Analytics — conectar en rxconfig.py cuando esté listo
G_TAG = "G-3YGHT3XJFS"

# ─── URLs de redes sociales ────────────────────────────────────────────────────
GITHUB_URL = "https://github.com/FerretoDev"
TWITTER_X_URL = "https://x.com/FerretoDev"
LINKEDIN_URL = "https://www.linkedin.com/in/marcos-ferreto/"

# ─── Contacto ──────────────────────────────────────────────────────────────────
EMAIL = "marcosferretoestrada@gmail.com"
PHONE = "+506 6352-8891"

# ─── Datos básicos del CV ──────────────────────────────────────────────────────
# Editar aquí para actualizar el hero y el about
basics: dict = {
    "name": "Marcos Ferreto Estrada",
    "label": "Especializado en desarrollo de software, modelación matemática y análisis de datos.",
    "image": "Designer.jpeg",
    "location": {"city": "Grecia", "region": "Costa Rica"},
    # Texto de la sección "Sobre mí" — un string por párrafo
    "summary": [
        "Soy un desarrollador de software apasionado por la intersección entre matemáticas, ciencia de datos y tecnología. Me especializo en crear soluciones innovadoras que transforman datos complejos en información accionable.",
        "Mi enfoque se centra en combinar rigor matemático con implementaciones de software eficientes y escalables, utilizando las últimas tecnologías en desarrollo y análisis de datos.",
    ],
    "profiles": [
        {
            "network": "Email",
            "url": f"mailto:{EMAIL}",
            "username": EMAIL,
        },
        {
            "network": "Phone",
            "url": f"tel:{PHONE}",
            "username": PHONE,
        },
        {
            "network": "LinkedIn",
            "url": LINKEDIN_URL,
            "username": "marcos-ferreto",
        },
        {
            "network": "X",
            "url": TWITTER_X_URL,
            "username": "FerretoDev",
        },
        {
            "network": "GitHub",
            "url": GITHUB_URL,
            "username": "FerretoDev",
        },
    ],
    "phone": PHONE,
    "email": EMAIL,
}

# ─── Experiencia laboral ───────────────────────────────────────────────────────
# Orden: más reciente primero
# endDate: None = "Actual"
work = [
    {
        "name": "Proyectos Personales",
        "startDate": "2023-01-01",
        "endDate": None,
        "position": "Desarrollador Full Stack",
        "summary": "Desarrollo de aplicaciones web y de escritorio utilizando Python, FastAPI, Reflex, Flet, Docker y otras tecnologías. Enfoque en automatización, visualización de datos y productividad.",
        "highlights": [
            "Desarrollé una app de tareas multiplataforma con Flet y Flutter",
            "Creé una API de scraping con FastAPI y Selenium, incluyendo visualización con Seaborn y Pandas",
            "Desarrollé una app de inventario web con Reflex y FastAPI",
        ],
        "url": None,
    },
    {
        "name": "Python Software Foundation",
        "startDate": "2024-01-01",
        "endDate": None,
        "position": "Colaborador en Traducción",
        "summary": "Participación voluntaria en la traducción oficial de la documentación de Python al español.",
        "highlights": [
            "Traducción de documentación técnica de Python para el público hispanohablante",
            "Colaboración con otros miembros de la comunidad de código abierto",
        ],
        "url": "https://www.python.org/psf/",
    },
]

# ─── Educación ─────────────────────────────────────────────────────────────────
# endDate: None = "Actual"
education = [
    {
        "institution": "Universidad de Costa Rica",
        "startDate": "2025-03-18",
        "endDate": None,
        "area": "Bachillerato en Modelación Matemática",
    },
]

# ─── Habilidades ───────────────────────────────────────────────────────────────
# Nombres deben coincidir con las claves de SKILLS_ICONS en utils/icons.py
skills = [
    {"name": "HTML"},
    {"name": "CSS"},
    {"name": "JavaScript"},
    {"name": "Git"},
    {"name": "GitHub"},
    {"name": "Python"},
    {"name": "PostgreSQL"},
]

# ─── Proyectos ─────────────────────────────────────────────────────────────────
# isActive: True muestra el indicador animado de proyecto activo
# github: None si el repositorio es privado o no existe
projects = [
    {
        "name": "Portfolio",
        "url": "https://ferreto.dev",
        "github": None,
        "description": "Sitio web portfolio minimalista y diseño responsivo.",
        "isActive": True,
        "highlights": ["Python", "Reflex", "FastAPI", "CSS"],
    },
]
