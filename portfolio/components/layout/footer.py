import datetime

import reflex as rx

from portfolio import constants
from portfolio.components.sections.common_styles import link_style
from portfolio.components.styles.styles import FooterStyle
from portfolio.utils.icons import github_social_icon, linkedin_icon, twitter_icon


def media(name: str, link: str) -> rx.Component:
    return rx.link(
        rx.text(name),
        href=link,
        style=FooterStyle.link,
    )


def footer() -> rx.Component:
    """Pie de página."""
    current_year = datetime.date.today().year
    return rx.vstack(
        rx.hstack(
            rx.link(
                github_social_icon(),
                href=constants.GITHUB_URL,
                style=link_style,
                aria_label="GitHub Profile",
            ),
            rx.link(
                linkedin_icon(),
                href=constants.LINKEDIN_URL,
                style=link_style,
                aria_label="LinkedIn Profile",
            ),
            rx.link(
                twitter_icon(),
                href=constants.TWITTER_X_URL,
                style=link_style,
                aria_label="X/Twitter Profile",
            ),
            spacing="3",
        ),
        rx.text(
            f"© 2024-{current_year} {constants.basics['name']}",
            style={
                "color": rx.color("slate", 11),
                "font_size": "0.8rem",
                "text_align": "center",
                "overflow_wrap": "break-word",
                "word_break": "break-word",
            },
        ),
        rx.text(
            "Always learning, building and exploring the intersection between mathematics and technology.",
            style={
                "color": rx.color("slate", 11),
                "font_size": "0.8rem",
                "text_align": "center",
                "overflow_wrap": "break-word",
                "word_break": "break-word",
            },
        ),
        width="100%",
        align="center",
        padding_y="2.5rem",
        spacing="4",
    )


