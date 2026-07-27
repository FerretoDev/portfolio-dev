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
        "Soy desarrollador de software y estudiante de Modelación Matemática en la Universidad de Costa Rica. Disfruto construir software que combina matemáticas, ingeniería y análisis de datos para resolver problemas reales.",
        "Trabajo principalmente con Python, desarrollando APIs, aplicaciones backend y herramientas de automatización enfocadas en el procesamiento y análisis de datos.",
        "Actualmente profundizo en áreas como Machine Learning, Data Science y modelado matemático aplicado, buscando integrar fundamentos matemáticos con el desarrollo de software.",
        "También contribuyo al ecosistema open source como colaborador en la traducción oficial de la documentación de Python al español y comparto mi proceso de aprendizaje a través de mi blog técnico.",
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
        "name": "Open Source Contributor",
        "startDate": "2024-01-01",
        "endDate": None,
        "position": "Official Spanish Translation Team",
        "summary": "Participo como voluntario en la traducción oficial de la documentación de Python al español. Este trabajo contribuye a mejorar el acceso a recursos educativos y documentación técnica para la comunidad hispanohablante.",
        "highlights": [
            "Traducción de documentación técnica de Python para el público hispanohablante",
            "Colaboración con otros miembros de la comunidad de código abierto",
        ],
        "url": "https://www.python.org/psf/",
    },
    {
        "name": "Dirección Regional de Educación Grande de Térraba – Ministerio de Educación Pública (MEP)",
        "startDate": "2024-10-01",
        "endDate": "2024-12-01",
        "position": "Practicante de Tecnología de la Información (TI)",
        "summary": "Realicé mi práctica profesional del Técnico Medio colaborando con el Departamento de Asesoría Pedagógica y el Centro de Formación, participando en proyectos de automatización de procesos, gestión tecnológica y soporte administrativo para fortalecer la transformación digital de la institución.",
        "highlights": [
            "Desarrollé soluciones con Microsoft Power Apps integradas con Microsoft Excel para automatizar procesos administrativos.",
            "Administré y mantuve actualizadas bases de datos institucionales de centros educativos y personal.",
            "Gestioné documentos oficiales mediante firma digital, agilizando procesos administrativos.",
            "Realicé el control y actualización del inventario de equipos tecnológicos y mobiliario institucional.",
            "Instalé y configuré Windows 11 y Microsoft Office en equipos de cómputo.",
            "Brindé apoyo técnico en talleres y capacitaciones mediante la preparación de equipos audiovisuales.",
            "Colaboré estrechamente con personal administrativo y jefaturas regionales en proyectos de mejora tecnológica.",
        ],
        "technologies": [
            "Microsoft Power Apps",
            "Microsoft Excel",
            "Microsoft Office",
            "Windows 11",
            "Firma Digital",
            "Gestión de Bases de Datos",
            "Inventario de Activos",
        ],
        "url": None,
    },
    {
        "name": "Independent Software Developer",
        "startDate": "2023-01-01",
        "endDate": None,
        "position": "Proyectos Personales",
        "summary": "Desarrollo aplicaciones web y herramientas orientadas al análisis de datos y automatización utilizando Python. Trabajo principalmente en la construcción de APIs, sistemas backend y herramientas que facilitan la manipulación y visualización de datos.",
        "highlights": [
            "Tecnologías utilizadas: Python, FastAPI, Reflex, Flet, Docker."
        ],
        "url": None,
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
    {
        "institution": "Colegio Técnico Profesional de Buenos Aires",
        "startDate": "2022-02-01",
        "endDate": "2024-12-01",
        "area": "Técnico Medio en Informática Empresarial",
        "summary": "Formación técnica en desarrollo de software, bases de datos, redes, soporte técnico y gestión de infraestructura informática.",
    },
]

# ─── Habilidades ───────────────────────────────────────────────────────────────
# Nombres deben coincidir con las claves de SKILLS_ICONS en utils/icons.py
# Estilo anterior (lista plana de habilidades)
skills = [
    {"name": "Python"},
    {"name": "FastAPI"},
    {"name": "PostgreSQL"},
    {"name": "Docker"},
    {"name": "Git"},
    {"name": "Linux"},
    {"name": "Pandas"},
    {"name": "NumPy"},
    {"name": "JavaScript"},
    {"name": "SQL"},
    {"name": "Reflex"},
    {"name": "SQLite"},
    {"name": "REST APIs"},
]

# Estilo categorizado (disponible para uso futuro)
skills_categorized = {
    "Languages": ["Python", "JavaScript", "SQL"],
    "Backend": ["FastAPI", "Reflex", "Flask", "REST APIs"],
    "Data & Science": ["Pandas", "NumPy"],
    "Databases": ["PostgreSQL", "SQLite"],
    "Tools": ["Docker", "Git", "Linux"],
}

# ─── Proyectos ─────────────────────────────────────────────────────────────────
# isActive: True muestra el indicador animado de proyecto activo
# github: None si el repositorio es privado o no existe
projects = [
    {
        "name": "Ferreto.dev",
        "url": "https://ferreto.dev",
        "github": None,
        "description": "Sitio web personal desarrollado para presentar proyectos, experiencia y habilidades en desarrollo de software y ciencia de datos.",
        "isActive": True,
        "highlights": ["Python", "Reflex", "FastAPI", "CSS"],
    },
    {
        "name": "Blog (Quartz + Obsidian)",
        "url": "https://blog.ferreto.dev",
        "github": None,
        "description": "Sitio web personal desarrollado para presentar proyectos, experiencia y habilidades en desarrollo de software y ciencia de datos.",
        "isActive": True,
        "highlights": ["Python", "Reflex", "FastAPI", "CSS"],
    },
]
