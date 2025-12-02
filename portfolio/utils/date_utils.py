"""Utilidades para manejo de fechas"""

from datetime import datetime
from typing import Optional


def format_date_to_year(date_string: Optional[str]) -> str:
    """
    Convierte una fecha en formato string a año.

    Args:
        date_string: Fecha en formato "YYYY-MM-DD" o None

    Returns:
        Año como string o "Actual" si la fecha es None o inválida
    """
    if date_string is None:
        return "Actual"
    try:
        return str(datetime.strptime(date_string, "%Y-%m-%d").year)
    except Exception:
        return "Actual"
