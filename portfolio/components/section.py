from typing import Any

import reflex as rx

from portfolio.components.styles.styles import SectionStyle


def section(*children: Any, **props: Any) -> rx.section:
    return rx.box(
        *children,
        class_name="section",
        # width="100%",
        # **props,
        **SectionStyle.section_style,
        **SectionStyle.section_style_mobile,
    )
