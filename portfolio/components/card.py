from dataclasses import dataclass, field

import reflex as rx
from portfolio.components.styles.styles import CardStyle


def card():
    return rx.hstack(
        rx.vstack(
            rx.text("Interactive User Logins", **CardStyle.title),
            rx.text(
                "Explore our intuitive and secure user login system, designed to streamline the authentication process.",
                **CardStyle.description,
            ),
            **CardStyle.stack,
        ),
        rx.box(**CardStyle.background),
        rx.icon(tag="puzzle", **CardStyle.icon),
        **CardStyle.base,
    )
