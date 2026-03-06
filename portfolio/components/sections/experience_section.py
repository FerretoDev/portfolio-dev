import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import list_vertical_style
from portfolio.components.sections.helpers import (
    create_item_header,
    create_link_or_text,
    create_text_content,
)
from portfolio.constants import work


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

    # Crear nombre de empresa como link o texto
    company_name = create_link_or_text(name, url, f"Ver {name}")

    return rx.box(
        rx.box(
            create_item_header(
                title=company_name,
                subtitle=position,
                start_date=start_date,
                end_date=end_date,
            ),
            rx.box(
                create_text_content(summary, is_summary=True),
            ),
        )
    )


def experience_section() -> rx.Component:
    """
    Sección completa de experiencia laboral
    """
    return section_component(
        title="Experiencia laboral",
        children=[experience_item(job) for job in work],
        content_style=list_vertical_style,
    )
