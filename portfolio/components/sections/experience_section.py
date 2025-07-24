from datetime import datetime
from typing import List, Optional

import reflex as rx

from portfolio.components.section import section
from portfolio.components.styles.styles import SectionStyle


def experience_section1(title: str = "Experiencia Profesional") -> rx.Component:
    """Sección de experiencia laboral."""
    return section(
        rx.heading(
            title,
            **SectionStyle.title_style,
        ),
        rx.vstack(
            rx.box(
                rx.heading("Científico de Datos Senior", size="2"),
                rx.text("Empresa Tech Innovadora", color="#D1D5DB"),
                rx.text("2020 - Presente", color="#9CA3AF"),
                rx.text(
                    "Desarrollo de modelos predictivos y soluciones de machine learning para optimización de procesos.",
                    color="#D1D5DB",
                    # margin_top="0.5rem",
                ),
                # style=section_styles["card"],
                # margin_bottom="1rem",
            ),
            rx.box(
                rx.heading("Desarrollador de Software", size="2"),
                rx.text("Startup de Análisis de Datos", color="#D1D5DB"),
                rx.text("2018 - 2020", color="#9CA3AF"),
                rx.text(
                    "Implementación de APIs y servicios backend para análisis de grandes volúmenes de datos.",
                    color="#D1D5DB",
                    # margin_top="0.5rem",
                ),
                # style=section_styles["card"],
            ),
            # width="100%",
        ),
    )


# Simulamos la importación de datos de trabajo
# En tu caso real, importarías desde tu archivo de datos
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


def experience_section() -> rx.Component:
    """Sección de experiencia laboral."""

    return rx.fragment(
        section(
            children=[
                rx.heading(
                    "Experiencia Profesional",
                ),
                rx.vstack(
                    *[
                        rx.box(
                            rx.heading(
                                work_item["position"],
                                size="2",
                            ),
                            rx.text(
                                work_item["name"],
                            ),
                            rx.text(
                                f"{datetime.strptime(str(work_item['startDate']), '%Y-%m-%d').strftime('%B %Y')} - "
                                f"{'Presente' if not work_item.get('endDate') else datetime.strptime(str(work_item['endDate']), '%Y-%m-%d').strftime('%B %Y')}",
                            ),
                            rx.text(
                                work_item["summary"],
                            ),
                            rx.vstack(
                                *[
                                    rx.text(
                                        highlight,
                                    )
                                    for highlight in (work_item.get("highlights") or [])
                                ],
                                spacing="1",
                            ),
                            # (
                            #    rx.link(
                            #        "Ver más",
                            #        href=(
                            #            str(work_item["url"])
                            #            if work_item["url"] is not None
                            #            else None
                            #        ),
                            #        # color="#3B82F6",
                            #    )
                            #    if work_item["url"]
                            #    else None
                            # ),
                        )
                        for work_item in work
                    ],
                    spacing="1",
                ),
            ]
        )
    )
