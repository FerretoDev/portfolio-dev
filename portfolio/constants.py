# Comunes
G_TAG = "G-3YGHT3XJFS"

# Cabecera
GITHUB_URL = "https://github.com/FerretoDev"
TWITTER_X_URL = "https://x.com/MarcosFerretoE"
LINKEDIN_URL = "https://linkedin.com/in/braismoure/"


# Recursos y más
BOOK_URL = "https://mouredev.com/libro-git"
BOOKS_URL = "https://amazon.es/shop/mouredev/list/2ZIHJJFJ9AVZ3"
SETUP_URL = "https://mouredev.com/setup"
COFFEE_URL = "https://buymeacoffee.com/mouredev"

# Contacto
MYPUBLICINBOX_URL = "https://mypublicinbox.com/mouredev"
EMAIL = "braismoure@mouredev.com"
PHONE = "+506 6352-8891"

basics: dict[str, dict[str, str] | list[dict[str, str]] | str] = {
    "name": "Marcos Ferreto Estrada",
    "label": "Especializado en desarrollo de software, modelación matemática y análisis de datos.",
    "image": "Designer.jpg",
    "location": {"city": "Grecia", "region": "Costa Rica"},
    "profiles": [
        {
            "network": "GitHub",
            "url": GITHUB_URL,
            "username": "FerretoDev",
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
    ],
    "phone": PHONE,
    "email": EMAIL,
}
