import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import (
    item_header_style,
    list_vertical_style,
    time_display_style,
)
from portfolio.constants import work
from portfolio.utils.date_utils import format_date_to_year


def experience_item(job: dict) -> rx.Component:
    """
    Componente individual para cada trabajo
    """
    name = job["name"]
    start_date = job["startDate"]
    end_date = job.get("endDate")
    position = job["position"]
    summary = job["summary"]
    url = job.get("url")

    # Formatear años
    start_year = format_date_to_year(start_date)
    end_year = format_date_to_year(end_date)
    years = f"{start_year} - {end_year}"

    # Crear enlace del nombre de la empresa o texto plano
    if url:
        company_name = rx.link(
            name,
            href=url,
            title=f"Ver {name}",
            target="_blank",
            rel="noopener noreferrer",
            style={
                "color": "#111",
                "text_decoration": "none",
                "_hover": {"text_decoration": "underline"},
            },
        )
    else:
        company_name = rx.text(name, style={"color": "#111"})

    return rx.list_item(
        rx.box(
            # Header con empresa, posición y fechas
            rx.box(
                # Información de la empresa y posición
                rx.box(
                    rx.heading(
                        company_name,
                        level=3,
                        style={
                            "font_weight": "500",
                            "color": "#111",
                            "margin": "0",
                        },
                    ),
                    rx.heading(
                        position,
                        level=4,
                        style={
                            "color": "#222",
                            "font_weight": "400",
                            "margin": "0",
                        },
                    ),
                ),
                # Fechas
                rx.box(
                    rx.text(
                        years,
                        # tag="time",
                        datetime=start_date if start_date else "",
                        data_title=start_date if start_date else "",
                        style=time_style,
                        class_name="tooltip-trigger" if start_date else "",
                    ),
                    style={
                        "display": "flex",
                        "align_items": "center",
                        "color": "#555",
                        "font_size": "0.85rem",
                    },
                ),
                style=header_style,
            ),
            # Footer con resumen
            rx.box(
                rx.text(
                    summary,
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


def experience_section() -> rx.Component:
    """
    Sección completa de experiencia laboral
    """
    return rx.fragment(
        section_component(
            title="Experiencia laboral",
            children=[
                rx.unordered_list(
                    *[experience_item(job) for job in work], style=ul_style
                )
            ],
        ),
        # Estilos CSS para tooltips y responsive
    )


# Estilos definidos como diccionarios
ul_style = list_vertical_style
header_style = item_header_style
time_style = {**time_display_style, "cursor": "default"}


# Versión alternativa con highlights (si los quieres mostrar)
def experience_item_with_highlights(job: dict) -> rx.Component:
    """
    Versión alternativa que incluye highlights/logros
    """
    name = job["name"]
    start_date = job["startDate"]
    end_date = job.get("endDate")
    position = job["position"]
    summary = job["summary"]
    highlights = job.get("highlights", [])
    url = job.get("url")

    start_year = format_date_to_year(start_date)
    end_year = format_date_to_year(end_date)

    if url:
        company_name = rx.link(
            name,
            href=url,
            title=f"Ver {name}",
            target="_blank",
            rel="noopener noreferrer",
            style={
                "color": "#111",
                "text_decoration": "none",
                "_hover": {"text_decoration": "underline"},
            },
        )
    else:
        company_name = rx.text(name, style={"color": "#111"})

    return rx.list_item(
        rx.box(
            # Header
            rx.box(
                rx.box(
                    rx.heading(
                        company_name,
                        level=3,
                        style={"font_weight": "500", "color": "#111", "margin": "0"},
                    ),
                    rx.heading(
                        position,
                        level=4,
                        style={"color": "#222", "font_weight": "400", "margin": "0"},
                    ),
                ),
                rx.box(
                    rx.text(
                        start_year,
                        # tag="time",
                        style=time_style,
                    ),
                    rx.text(" - "),
                    rx.text(
                        end_year,
                        # tag="time",
                        style=time_style,
                    ),
                    style={
                        "display": "flex",
                        "align_items": "center",
                        "color": "#555",
                        "font_size": "0.85rem",
                    },
                ),
                style=header_style,
            ),
            # Footer con resumen y highlights
            rx.box(
                rx.text(
                    summary,
                    style={
                        "color": "#666",
                        "font_size": "0.9rem",
                        "line_height": "1.5",
                        "margin": "0 0 8px 0",
                    },
                ),
                (
                    rx.unordered_list(
                        *[
                            rx.list_item(
                                highlight,
                                style={"color": "#666", "font_size": "0.85rem"},
                            )
                            for highlight in highlights
                        ],
                        style={"margin": "0", "padding_left": "20px"},
                    )
                    if highlights
                    else rx.fragment()
                ),
                # tag="footer",
            ),
            # tag="article",
        )
    )


def experience_section_with_highlights() -> rx.Component:
    """
    Version con highlights incluidos
    """
    return section_component(
        title="Experiencia laboral",
        children=[
            rx.unordered_list(
                *[experience_item_with_highlights(job) for job in work], style=ul_style
            )
        ],
    )
