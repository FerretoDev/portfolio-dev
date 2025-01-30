import reflex as rx
from portfolio.components.card import card

# from portfolio.components.layout.layout import layout


@rx.page("#proyectos", "Projects Page")
def project_section() -> rx.Component:
    return rx.grid(
        card(
            "Análisis Predictivo",
            "Modelo de machine learning para predicción de series temporales",
            "chart-no-axes-combined",
        ),
        card(
            "Optimización Matemática",
            "Sistema de optimización para logística y distribución",
            "sigma",
        ),
        card(
            "Dashboard Analytics",
            "Dashboard interactivo para visualización de datos",
            "layout-dashboard",
        ),
    )
