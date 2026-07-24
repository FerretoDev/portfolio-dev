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

# ─── Configuración del sitio ───────────────────────────────────────────────────
VERSION = "v1.0.0"

# ─── Datos básicos del CV ──────────────────────────────────────────────────────
# Editar aquí para actualizar el hero y el about
basics: dict = {
    "name": "Marcos Ferreto Estrada",
    "title": "Software Developer & Mathematical Modeling Student",
    "description": "Building software where mathematics, data and engineering meet.",
    "image": "icon.svg",
    "location": {"city": "", "region": "Costa Rica"},
    # Texto de la sección "Sobre mí" — un string por párrafo
    "summary": [
        "Soy desarrollador de software y estudiante de Modelación Matemática en la Universidad de Costa Rica. Mi interés principal se encuentra en la intersección entre matemáticas, ciencia de datos y desarrollo de software.",
        "Disfruto construir herramientas y sistemas que permiten transformar datos complejos en información útil. Me interesa especialmente el desarrollo de software orientado al análisis de datos, la automatización de procesos y la creación de sistemas escalables.",
        "Actualmente estoy explorando áreas como Machine Learning, Data Science, Big Data y modelado matemático aplicado, combinando pensamiento matemático con desarrollo de software para construir soluciones eficientes y reproducibles.",
        "Además, contribuyo a proyectos open source como colaborador en la traducción oficial de la documentación de Python al español.",
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
        "name": "Full Stack Developer",
        "startDate": "2023-01-01",
        "endDate": None,
        "position": "Proyectos Personales",
        "summary": "Desarrollo aplicaciones web y herramientas orientadas al análisis de datos y automatización utilizando Python. Trabajo principalmente en la construcción de APIs, sistemas backend y herramientas que facilitan la manipulación y visualización de datos.",
        "highlights": [
            "Tecnologías utilizadas: Python, FastAPI, Reflex, Flet, Docker."
        ],
        "url": None,
    },
    {
        "name": "Python Software Foundation",
        "startDate": "2024-01-01",
        "endDate": None,
        "position": "Colaborador en Traducción",
        "summary": "Participo como voluntario en la traducción oficial de la documentación de Python al español. Este trabajo contribuye a mejorar el acceso a recursos educativos y documentación técnica para la comunidad hispanohablante.",
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
        "summary": "Formación enfocada en matemáticas aplicadas, modelado matemático, análisis numérico y herramientas computacionales para la resolución de problemas complejos.",
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
        "name": "Portfolio Website",
        "url": "https://ferreto.dev",
        "github": None,
        "description": "Sitio web personal desarrollado para presentar proyectos, experiencia y habilidades en desarrollo de software y ciencia de datos.",
        "isActive": True,
        "highlights": ["Python", "Reflex", "FastAPI", "CSS"],
    },
]
