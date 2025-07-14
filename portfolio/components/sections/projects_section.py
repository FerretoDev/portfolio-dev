import reflex as rx

from portfolio.components.card import card
from portfolio.components.section import section
from portfolio.components.styles.styles import GlobalThemeVariables, SectionStyle


@rx.page("proyectos", "Projects Page")
def projects_section2() -> rx.Component:
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


def projects_section():
    """Sección de proyectos."""
    projects = [
        {
            "title": "Análisis Predictivo",
            "description": "Modelo de predicción financiera usando machine learning",
            "technologies": ["Python", "Pandas", "Scikit-learn"],
        },
        # {
        #    "title": "API de Optimización",
        #    "description": "Servicio REST para problemas de optimización matemática",
        #    "technologies": ["FastAPI", "Docker", "Numpy"],
        # },
        # {
        #    "title": "Dashboard de Datos",
        #    "description": "Visualización interactiva de métricas empresariales",
        #    "technologies": ["React", "D3.js", "TypeScript"],
        # },
    ]

    return section(
        rx.vstack(
            rx.heading(
                "Proyectos Destacados",
                **SectionStyle.title_style,
            ),
            rx.hstack(
                *[
                    rx.box(
                        rx.heading(project["title"], size="2", margin_bottom="1rem"),
                        rx.text(
                            project["description"],
                            color="#D1D5DB",
                            margin_bottom="1rem",
                        ),
                        rx.hstack(
                            *[
                                rx.badge(tech, margin_x="0.25rem")
                                for tech in project["technologies"]
                            ]
                        ),
                        style=rx.Style(
                            {
                                "background": "rgba(31, 41, 55, 0.5)",
                                "border-radius": "0.75rem",
                                "padding": "1.5rem",
                                "transition": "transform 0.3s ease",
                                "hover": {"transform": "translateY(-10px)"},
                            },
                        ),
                    )
                    for project in projects
                ],
                width="100%",
                # spacing="4",
            ),
        ),
    )
