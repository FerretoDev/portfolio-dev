from typing import Any, Optional

import reflex as rx

from portfolio.components.styles.styles import SectionStyle


def section(*children: Any, **props: Any | Optional[rx.Style]) -> rx.section:
    return rx.box(
        *children,
        # class_name="section",
        width="100%",
        # **props,
        # **SectionStyle.section_style,
        # **SectionStyle.section_style_mobile,
    )
