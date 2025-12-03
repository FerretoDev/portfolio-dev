import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import (
    item_header_style,
    list_vertical_style,
    time_display_style,
)
from portfolio.constants import education
from portfolio.utils.date_utils import format_date_to_year


def education_item(edu: dict) -> rx.Component:
    """
    Componente individual para cada educación
    """
    institution = edu["institution"]
    start_date = edu["startDate"]
    end_date = edu.get("endDate")
    area = edu["area"]

    # Formatear años
    start_year = format_date_to_year(start_date)
    end_year = format_date_to_year(end_date)
    years = f"{start_year} - {end_year}"

    return rx.list_item(
        rx.box(
            # Header con institución y años
            rx.box(
                # Información de la institución
                rx.box(
                    rx.heading(
                        institution,
                        level=3,
                        style={
                            "font_weight": "500",
                            "color": "#111",
                            "margin": "0",
                        },
                    ),
                ),
                # Años de estudio
                rx.text(
                    years,
                    # tag="time",
                    style=time_style,
                ),
                style=header_style,
            ),
            # Footer con área de estudio
            rx.box(
                rx.text(
                    area,
                    style={
                        "color": "#666",
                        "font_size": "0.9rem",
                        "line_height": "1.5",
                        "margin": "0",
                    },
                ),
                # tag="footer",
            ),
            # tag="article",
        )
    )


def education_section() -> rx.Component:
    """
    Sección completa de educación
    """
    return rx.fragment(
        section_component(
            title="Educación",
            children=[
                rx.unordered_list(
                    *[education_item(edu) for edu in education],
                    style=education_ul_style,
                )
            ],
        ),
        # Estilos CSS para responsive
        # rx.style(
        #    """
        #    @media (max-width: 700px) {
        #        .education-time {
        #           text-align: right !important;
        #        }
        #    }
        # """
        # ),
    )


# Estilos definidos como diccionarios
education_ul_style = list_vertical_style
header_style = item_header_style
time_style = time_display_style

# Versión extendida con más información
education_extended = [
    {
        "institution": "Universidad Tecnológica Nacional",
        "startDate": "2018-03-01",
        "endDate": "2022-12-15",
        "area": "Ingeniería en Sistemas de Información",
        "degree": "Grado",
        "gpa": "8.5/10",
        "description": "Especialización en desarrollo de software y gestión de proyectos tecnológicos.",
        "highlights": [
            "Proyecto final: Sistema de gestión hospitalaria",
            "Promedio: 8.5/10",
            "Mejor estudiante 2022",
        ],
    },
    {
        "institution": "Instituto de Desarrollo Web",
        "startDate": "2021-06-01",
        "endDate": "2021-11-30",
        "area": "Certificación Full Stack Developer",
        "degree": "Certificación",
        "description": "Programa intensivo de desarrollo web full stack con tecnologías modernas.",
        "highlights": ["MERN Stack", "Proyectos reales", "100% completado"],
    },
    {
        "institution": "Coursera - Universidad de Stanford",
        "startDate": "2020-01-15",
        "endDate": "2020-06-30",
        "area": "Machine Learning Specialization",
        "degree": "Certificación Online",
        "description": "Especialización en aprendizaje automático con Andrew Ng.",
        "highlights": [
            "Python",
            "TensorFlow",
            "Algoritmos ML",
            "Certificado verificado",
        ],
    },
]


def education_item_extended(edu: dict) -> rx.Component:
    """
    Versión extendida del item de educación con más detalles
    """
    institution = edu["institution"]
    start_date = edu["startDate"]
    end_date = edu.get("endDate")
    area = edu["area"]
    degree = edu.get("degree", "")
    gpa = edu.get("gpa", "")
    description = edu.get("description", "")
    highlights = edu.get("highlights", [])

    start_year = format_date_to_year(start_date)
    end_year = format_date_to_year(end_date)
    years = f"{start_year} - {end_year}"

    return rx.list_item(
        rx.box(
            # Header
            rx.box(
                rx.box(
                    rx.heading(
                        institution,
                        level=3,
                        style={"font_weight": "500", "color": "#111", "margin": "0"},
                    ),
                    rx.box(
                        rx.text(
                            area,
                            style={
                                "color": "#333",
                                "font_weight": "500",
                                "font_size": "0.9rem",
                            },
                        ),
                        (
                            rx.text(
                                f"• {degree}",
                                style={"color": "#666", "font_size": "0.8rem"},
                            )
                            if degree
                            else rx.fragment()
                        ),
                        (
                            rx.text(
                                f"• {gpa}",
                                style={"color": "#666", "font_size": "0.8rem"},
                            )
                            if gpa
                            else rx.fragment()
                        ),
                        style={
                            "display": "flex",
                            "gap": "8px",
                            "align_items": "center",
                            "flex_wrap": "wrap",
                        },
                    ),
                ),
                rx.text(
                    years,
                    # tag="time",
                    style=time_style,
                ),
                style=header_style,
            ),
            # Body con descripción
            rx.box(
                (
                    rx.text(
                        description,
                        style={
                            "color": "#666",
                            "font_size": "0.85rem",
                            "margin_bottom": "8px",
                        },
                    )
                    if description
                    else rx.fragment()
                ),
                (
                    rx.unordered_list(
                        *[
                            rx.list_item(
                                highlight,
                                style={"color": "#666", "font_size": "0.8rem"},
                            )
                            for highlight in highlights
                        ],
                        style={
                            "margin": "0",
                            "padding_left": "16px",
                            "font_size": "0.8rem",
                        },
                    )
                    if highlights
                    else rx.fragment()
                ),
                # tag="footer",
            ),
            # tag="article",
            style={"border_bottom": "1px solid #f0f0f0", "padding_bottom": "16px"},
        )
    )


def education_section_extended() -> rx.Component:
    """
    Versión extendida de la sección de educación
    """
    return section_component(
        title="Educación",
        children=[
            rx.unordered_list(
                *[education_item_extended(edu) for edu in education_extended],
                style=education_ul_style,
            )
        ],
    )


# Versión agrupada por tipo de educación
def education_by_type() -> rx.Component:
    """
    Versión agrupada por tipo de educación
    """
    # Separar educación formal de certificaciones
    formal_education = [
        edu for edu in education_extended if edu.get("degree") == "Grado"
    ]
    certifications = [
        edu
        for edu in education_extended
        if edu.get("degree") in ["Certificación", "Certificación Online"]
    ]

    return section_component(
        title="Educación",
        children=[
            # Educación formal
            (
                rx.box(
                    rx.heading(
                        "🎓 Educación Formal",
                        level=3,
                        style={
                            "font_size": "1.1rem",
                            "margin_bottom": "16px",
                            "color": "#333",
                        },
                    ),
                    rx.unordered_list(
                        *[education_item_extended(edu) for edu in formal_education],
                        style={**education_ul_style, "margin_bottom": "32px"},
                    ),
                )
                if formal_education
                else rx.fragment()
            ),
            # Certificaciones
            (
                rx.box(
                    rx.heading(
                        "📜 Certificaciones",
                        level=3,
                        style={
                            "font_size": "1.1rem",
                            "margin_bottom": "16px",
                            "color": "#333",
                        },
                    ),
                    rx.unordered_list(
                        *[education_item_extended(edu) for edu in certifications],
                        style=education_ul_style,
                    ),
                )
                if certifications
                else rx.fragment()
            ),
        ],
    )


# Versión compacta para CVs minimalistas
def education_item_compact(edu: dict) -> rx.Component:
    """
    Versión compacta del item de educación
    """
    institution = edu["institution"]
    start_date = edu["startDate"]
    end_date = edu.get("endDate")
    area = edu["area"]

    start_year = format_date_to_year(start_date)
    end_year = format_date_to_year(end_date)
    years = f"{start_year} - {end_year}"

    return rx.box(
        rx.box(
            rx.text(institution, style={"font_weight": "600", "color": "#111"}),
            rx.text(years, style={"color": "#666", "font_size": "0.85rem"}),
            style={
                "display": "flex",
                "justify_content": "space-between",
                "align_items": "center",
            },
        ),
        rx.text(
            area, style={"color": "#666", "font_size": "0.9rem", "margin_top": "2px"}
        ),
        style={
            "margin_bottom": "12px",
            "padding_bottom": "12px",
            "border_bottom": "1px solid #f5f5f5",
        },
    )


def education_section_compact() -> rx.Component:
    """
    Versión compacta de la sección de educación
    """
    return section_component(
        title="Educación",
        children=[rx.box(*[education_item_compact(edu) for edu in education])],
    )
