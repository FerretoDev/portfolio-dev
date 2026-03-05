"""Helpers reutilizables para componentes de secciones"""

import reflex as rx

from portfolio.components.sections.common_styles import (
    date_box_style,
    item_header_style,
    item_link_style,
    item_subtitle_style,
    item_text_style,
    item_title_style,
    time_display_style,
)
from portfolio.utils.date_utils import format_date_to_year


def create_item_header(
    title: str | rx.Component,
    subtitle: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> rx.Component:
    """
    Crea un header estándar para items con título, subtítulo y fechas.

    Args:
        title: Título principal (puede ser un componente Link o Text)
        subtitle: Subtítulo opcional
        start_date: Fecha de inicio en formato "YYYY-MM-DD"
        end_date: Fecha de fin en formato "YYYY-MM-DD" o None para "Actual"

    Returns:
        Componente de header con el formato estándar
    """
    # Formatear fechas si se proporcionan
    years_display = None
    if start_date is not None:
        start_year = format_date_to_year(start_date)
        end_year = format_date_to_year(end_date)
        years_display = f"{start_year} - {end_year}"

    # Crear contenido del título
    title_content = []

    # Si title es un string, crear un heading, si no, usarlo directamente
    title_component = rx.heading(title, level=3, style=item_title_style)

    title_content.append(title_component)

    # Agregar subtítulo si existe
    if subtitle:
        title_content.append(rx.heading(subtitle, level=4, style=item_subtitle_style))

    # Crear box del título/subtítulo
    title_box = rx.box(*title_content)

    # Crear box de fechas si existe
    if years_display:
        date_box = rx.box(
            rx.text(
                years_display,
                datetime=start_date if start_date else "",
                data_title=start_date if start_date else "",
                style=time_display_style,
                class_name="tooltip-trigger" if start_date else "",
            ),
            style=date_box_style,
        )

        return rx.box(title_box, date_box, style=item_header_style)

    return title_box


def create_text_content(text: str, is_summary: bool = False) -> rx.Component:
    """
    Crea un componente de texto con estilo estándar.

    Args:
        text: Contenido del texto
        is_summary: Si es un resumen (usa estilo específico)

    Returns:
        Componente de texto formateado
    """
    base_style = {
        "color": rx.color_mode_cond(light="#666", dark="#d4d4d4"),
        "line_height": "1.5",
        "margin": "0",
    }

    if is_summary:
        base_style["font_size"] = "0.9rem"

    return rx.text(text, style=base_style)


def create_link_or_text(
    text: str,
    url: str | None = None,
    title: str | None = None,
) -> rx.Component:
    """
    Crea un link si hay URL, o texto simple si no.

    Args:
        text: Texto a mostrar
        url: URL opcional
        title: Título del link (hover text)

    Returns:
        Componente Link o Text según corresponda
    """
    if url:
        return rx.link(
            text,
            href=url,
            title=title or f"Ver {text}",
            target="_blank",
            rel="noopener noreferrer",
            style=item_link_style,
        )
    return rx.text(text, style=item_text_style)
