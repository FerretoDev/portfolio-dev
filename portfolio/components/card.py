from dataclasses import dataclass, field

import reflex as rx
from portfolio.components.styles.styles import CardStyle
from typing import Optional, List


def card(title: str, description: str, tag: str):
    return rx.hstack(
        rx.vstack(
            rx.text(title, **CardStyle.title),
            rx.text(
                description,
                **CardStyle.description,
            ),
            **CardStyle.stack,
        ),
        rx.box(**CardStyle.background),
        rx.icon(tag, **CardStyle.icon),
        **CardStyle.base,
    )


def suma(
    title: str,
    description: str,
    tag: str,
    icon: str,
    background: str,
):
    return rx.hstack(
        rx.vstack(
            rx.text(title, **CardStyle.title),
            rx.text(
                description,
                **CardStyle.description,
            ),
            **CardStyle.stack,
        ),
        rx.box(background, **CardStyle.background),
        rx.icon(icon, **CardStyle.icon),
        **CardStyle.base,
    )
    