from typing import Any, List, Optional

import reflex as rx

from portfolio.components.styles.styles import SectionStyle


def section(children: List) -> rx.section:
    return rx.box(
        *children,
        **SectionStyle.section_style,
        **SectionStyle.section_style_mobile,
    )
