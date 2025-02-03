import reflex as rx


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
            # "Mis Habilidades", style={"text-align": "center", "margin-bottom": "2rem"}
            "Mis Habilidades",
        ),
        rx.hstack(
            *[
                # rx.box(
                #    rx.heading(skill["title"], size="2", margin_bottom="1rem"),
                #    rx.hstack(
                #        *[
                #            rx.badge(tech, margin_x="0.25rem")
                #            for tech in skill["technologies"]
                #        ]
                #    ),
                #    # style={
                #    #    "background": "rgba(31, 41, 55, 0.5)",
                #    #    "border-radius": "0.75rem",
                #    #    "padding": "1.5rem",
                #    #    "transition": "transform 0.3s ease",
                #    #    "hover": {"transform": "translateY(-10px)"},
                #    # },
                # )
                # for skill in skills
            ],
            # width="100%",
            # spacing="4"
        ),
        # display="grid",
        # grid_template_columns="repeat(3, 1fr)",
        # gap="2rem",
    )
