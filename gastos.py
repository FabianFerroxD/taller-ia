"""Librería mínima para registrar y totalizar gastos."""

CATEGORIAS_VALIDAS = ("comida", "transporte", "ocio")


def parsear_linea(linea: str) -> dict:
    """Convierte una línea de texto en un gasto.

    El formato esperado es "AAAA-MM-DD,categoria,monto", por ejemplo:
    "2026-03-01,comida,12.50".

    Devuelve un diccionario con las claves "fecha" (str), "categoria" (str)
    y "monto" (float).
    """
    raise NotImplementedError("MISIÓN 1: implementar parsear_linea")


def totalizar(gastos: list[dict]) -> float:
    """Devuelve la suma de los montos de una lista de gastos."""
    return sum(g["monto"] for g in gastos)


def resumen_por_categoria(gastos: list[dict]) -> dict[str, float]:
    """Devuelve el total de gastos agrupado por categoría."""
    raise NotImplementedError("MISIÓN 3: implementar resumen_por_categoria")
