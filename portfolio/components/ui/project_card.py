"""Tal vez se utilice este fichero"""

import reflex as rx


def project_card(title: str, description: str, tags: List[str]) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(title, size="1"),
            rx.text(
                description,
                color=rx.color_mode_cond(
                    light=rx.color("slate", 7),
                    dark=rx.color("slate", 3),
                ),
            ),
            rx.wrap(
                *[
                    rx.badge(
                        tag,
                        color_scheme="cyan",
                        # variant="subtle",
                        margin="0.2em",
                    )
                    for tag in tags
                ],
            ),
            align_items="start",
            spacing="1",
        ),
        padding="1.5em",
        border_radius="xl",
        background=rx.color_mode_cond(
            light="rgba(255, 255, 255, 0.8)",
            dark="rgba(0, 0, 0, 0.3)",
        ),
        backdrop_filter="blur(12px)",
        border=rx.color_mode_cond(
            light="1px solid rgba(0,0,0,0.1)",
            dark="1px solid rgba(255,255,255,0.1)",
        ),
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-5px)",
            "box_shadow": rx.color_mode_cond(
                light="0 20px 25px -5px rgba(8, 145, 178, 0.1)",
                dark="0 20px 25px -5px rgba(6, 182, 212, 0.1)",
            ),
        },
    )
