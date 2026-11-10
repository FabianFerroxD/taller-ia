import unittest

from gastos import (
    CATEGORIAS_VALIDAS,
    parsear_linea,
    resumen_por_categoria,
    totalizar,
)


class TestGastos(unittest.TestCase):
    def test_categorias_validas(self):
        self.assertEqual(CATEGORIAS_VALIDAS, ("comida", "transporte", "ocio"))

    def test_totalizar_con_montos_numericos(self):
        gastos = [{"monto": 12.5}, {"monto": 7.5}]
        self.assertEqual(totalizar(gastos), 20.0)

    def test_parsear_linea_devuelve_diccionario(self):
        self.assertEqual(
            parsear_linea("2026-03-01,comida,12.50"),
            {"fecha": "2026-03-01", "categoria": "comida", "monto": 12.5},
        )

    def test_parsear_linea_convierte_monto_a_float(self):
        gasto = parsear_linea("2026-03-02,transporte,3")
        self.assertIsInstance(gasto["monto"], float)
        self.assertEqual(gasto["monto"], 3.0)

    def test_totalizar_convierte_montos_de_texto(self):
        gastos = [{"monto": "12.50"}, {"monto": "7.50"}]
        self.assertEqual(totalizar(gastos), 20.0)

    def test_resumen_por_categoria(self):
        gastos = [
            {"categoria": "comida", "monto": 10.0},
            {"categoria": "comida", "monto": 2.5},
            {"categoria": "ocio", "monto": 5.0},
        ]
        self.assertEqual(
            resumen_por_categoria(gastos),
            {"comida": 12.5, "ocio": 5.0},
        )


if __name__ == "__main__":
    unittest.main()
