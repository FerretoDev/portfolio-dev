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
    summary = edu.get("summary", "")

    return rx.box(
        rx.box(
            create_item_header(
                title=institution,
                start_date=start_date,
                end_date=end_date,
            ),
            rx.box(
                create_text_content(area, is_summary=True),
            ),
            *(
                [
                    rx.box(
                        create_text_content(summary, is_summary=True),
                        style={"margin_top": "4px"},
                    )
                ]
                if summary
                else []
            ),
        )
    )


def education_section() -> rx.Component:
    """
    Sección completa de educación
    """
    return section_component(
        title="Educación",
        children=[education_item(edu) for edu in education],
        content_style=list_vertical_style,
    )
