import reflex as rx

from portfolio.components.section import section_component
from portfolio.components.sections.common_styles import list_vertical_style
from portfolio.components.sections.helpers import (
    create_item_header,
    create_text_content,
)
from portfolio.constants import education


def education_item(edu: dict) -> rx.Component:
    """
    Componente individual para cada educación
    """
    institution = edu["institution"]
    start_date = edu["startDate"]
    end_date = edu.get("endDate")
    area = edu["area"]

    return rx.list_item(
        rx.box(
            create_item_header(
                title=institution,
                start_date=start_date,
                end_date=end_date,
            ),
            rx.box(
                create_text_content(area, is_summary=True),
            ),
        )
    )


def education_section() -> rx.Component:
    """
    Sección completa de educación
    """
    return section_component(
        title="Educación",
        children=[
            rx.unordered_list(
                *[education_item(edu) for edu in education],
                style=list_vertical_style,
            )
        ],
    )
