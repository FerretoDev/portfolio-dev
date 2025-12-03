# Comunes
G_TAG = "G-3YGHT3XJFS"

# Cabecera
GITHUB_URL = "https://github.com/FerretoDev"
TWITTER_X_URL = "https://x.com/MarcosFerretoE"
LINKEDIN_URL = "https://www.linkedin.com/in/marcos-ferreto/"


# Recursos y más
BOOK_URL = "https://mouredev.com/libro-git"
BOOKS_URL = "https://amazon.es/shop/mouredev/list/2ZIHJJFJ9AVZ3"
SETUP_URL = "https://mouredev.com/setup"
COFFEE_URL = "https://buymeacoffee.com/mouredev"

# Contacto
MYPUBLICINBOX_URL = "https://mypublicinbox.com/mouredev"
EMAIL = "marcosferretoestrada@gmail.com"
PHONE = "+506 6352-8891"

basics: dict[str, dict[str, str] | list[dict[str, str]] | str] = {
    "name": "Marcos Ferreto Estrada",
    "label": "Especializado en desarrollo de software, modelación matemática y análisis de datos.",
    "image": "Designer.jpg",
    "location": {"city": "Grecia", "region": "Costa Rica"},
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
            "username": "usuario",
        },
        {
            "network": "X",
            "url": TWITTER_X_URL,
            "username": "MarcosFerretoE",
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

# Experiencia laboral
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

# Educación
education = [
    {
        "institution": "Universidad de Costa Rica",
        "startDate": "2021-06-01",
        "endDate": "2021-11-30",
        "area": "Bachillerato en Modelación Matemática",
    },
]

# Habilidades
skills = [
    {"name": "HTML"},
    {"name": "CSS"},
    {"name": "JavaScript"},
    {"name": "Git"},
    {"name": "GitHub"},
    {"name": "Python"},
    {"name": "PostgreSQL"},
]

# Proyectos
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
