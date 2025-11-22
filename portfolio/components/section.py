from typing import Any, List, Optional, cast

import reflex as rx

from portfolio.components.styles.styles import SectionStyle


def section(children: List) -> rx.Component:
    # merge and cast styles to avoid strict typing errors when unpacking
    merged_style = {
        **cast(dict[str, Any], SectionStyle.section_style),
        **cast(dict[str, Any], SectionStyle.section_style_mobile),
    }
    return rx.box(
        *children,
        **merged_style,
    )
