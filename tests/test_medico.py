import unittest
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.medico = Medico("Dr. Juan Pérez", "12345678")
        self.especialidad1 = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.especialidad2 = Especialidad("Cardiología", ["martes", "jueves"])

    def test_agregar_especialidad(self):
        self.medico.agregar_especialidad(self.especialidad1)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Pediatría")
        self.medico.agregar_especialidad(self.especialidad2)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("martes"), "Cardiología")

    def test_obtener_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "12345678")

    def test_str(self):
        self.medico.agregar_especialidad(self.especialidad1)
        self.assertIn("Pediatría", str(self.medico))

if __name__ == "__main__":
    unittest.main()
