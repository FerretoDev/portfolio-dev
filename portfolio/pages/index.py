import reflex as rx
from rich.padding import Padding

from portfolio.components.layout.footer import footer
from portfolio.components.layout.layout import layout
from portfolio.components.sections.about_section import about_section
from portfolio.components.sections.education_section import education_section
from portfolio.components.sections.experience_section import experience_section
from portfolio.components.sections.hero_section import hero_section
from portfolio.components.sections.projects_section import projects_section
from portfolio.components.sections.skills_section import skills_section
from portfolio.components.styles.styles import PageStyle


@rx.page("/", "Portfolio")  # type: ignore
def index() -> rx.Component:

    return layout(
        children=[
            hero_section(),
            about_section(),
            experience_section(),
            education_section(),
            projects_section(),
            skills_section(),
            footer(),
        ],
    )
