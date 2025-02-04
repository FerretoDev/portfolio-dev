from dataclasses import dataclass, field

import reflex as rx

from portfolio.components.styles.styles import GlobalThemeVariables


@dataclass
class SkillsStyle:
    skills_base: dict[str, str] = field(
        default_factory=lambda: {
            "display": "grid",
            "grid_template_columns": "repeat(3, 1fr)",
            "gap": "2rem",
        },
    )
    hero_title: dict[str, str] = field(
        default_factory=lambda: {
            "background": rx.color_mode_cond(
                light=f"linear-gradient(to right, {GlobalThemeVariables.LIGHT.value['--primary']}, {GlobalThemeVariables.LIGHT.value['--secondary']})",
                dark=f"linear-gradient(to right, {GlobalThemeVariables.DARK.value['--primary']}, {GlobalThemeVariables.DARK.value['--secondary']})",
            ),
            # "font_size": "3rem",
            "background_image": "linear-gradient(to right, #06B6D4, #3B82F6)",
            "background_clip": "text",
            "color": "transparent",
            ########################################################################
            "size": "2",
            "margin_bottom": "1rem",
            "": "column",
        },
    )

    hero_text: dict[str, str] = field(
        default_factory=lambda: {
            "color": rx.color_mode_cond(
                light=GlobalThemeVariables.LIGHT.value["--secondary"],
                dark=GlobalThemeVariables.DARK.value["--secondary"],
            ),
            "font-size": "1.2em",
        },
    )


SkillsStyle: SkillsStyle = SkillsStyle()


def skills_section() -> rx.Component:
    """Sección de habilidades."""
    skills = [
        {
            "title": "Desarrollo de Software",
            "technologies": ["Python", "FastAPI", "React", "Docker"],
        },
        {
            "title": "Modelación Matemática",
            "technologies": ["Optimización", "Estadística", "Métodos Numéricos"],
        },
        {
            "title": "Data Science",
            "technologies": ["Machine Learning", "SQL", "Big Data"],
        },
    ]

    return rx.box(
        rx.heading(
            "Mis Habilidades",
            **SkillsStyle.hero_title,
        ),
        rx.hstack(
            *[
                rx.box(
                    rx.heading(
                        skill["title"],
                    ),
                    rx.hstack(
                        *[
                            rx.badge(tech, margin_x="0.25rem")
                            for tech in skill["technologies"]
                        ]
                    ),
                    style={
                        "background": "rgba(31, 41, 55, 0.5)",
                        "border-radius": "0.75rem",
                        "padding": "1.5rem",
                        "transition": "transform 0.3s ease",
                        "hover": {"transform": "translateY(-10px)"},
                    },
                )
                for skill in skills
            ],
            width="100%",
            spacing="4",
        ),
        **SkillsStyle.skills_base,
    )
