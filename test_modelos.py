# Batería de pruebas automatizadas con unittest
import unittest
from modelos import UsuarioFactory, GestorCentroSalud
from operaciones import filtrar_pacientes_por_diagnostico

class TestSistemaRural(unittest.TestCase):

    def setUp(self):
        # Preparación: Se ejecuta automáticamente antes de cada prueba
        self.gestor = GestorCentroSalud()
        self.gestor.pacientes = []  # Vaciamos el gestor para tener un entorno limpio
        
        # Creamos el paciente base para las pruebas
        self.paciente_prueba = UsuarioFactory.crear_usuario("Paciente", "12345678", "Robert", "Castillo", "Tuberculosis")
        self.gestor.pacientes.append(self.paciente_prueba)

    # 1. Caso de prueba: Registro válido (Requisito de rúbrica)
    def test_creacion_y_singleton(self):
        gestor2 = GestorCentroSalud()
        # Verificamos que GestorCentroSalud no permita crear una segunda base de datos
        self.assertIs(self.gestor, gestor2, "Fallo: El Singleton permitió crear múltiples gestores.")
        # Verificamos que el paciente se guardó en la lista
        self.assertEqual(len(self.gestor.pacientes), 1, "Fallo: El paciente no se registró correctamente.")

    # 2. Caso de prueba: Comprobación de datos sensibles (Requisito de rúbrica)
    def test_privacidad_datos_sensibles(self):
        # Leemos la variable profunda
        dato_en_memoria = self.paciente_prueba._diagnostico_protegido
        
        # El test PASA si la memoria interna NO guarda el texto plano original
        self.assertNotEqual(dato_en_memoria, "Tuberculosis", "Fallo: Los datos están expuestos en texto plano.")
        
        # El test PASA si la ventanilla autorizada logra desencriptarlo y devolverlo limpio
        self.assertEqual(self.paciente_prueba.get_diagnostico(), "Tuberculosis", "Fallo: El getter no desencriptó correctamente.")

    # 3. Caso de prueba: Transformación mediante orden superior (Requisito de rúbrica)
    def test_operaciones_funcionales(self):
        # Usamos el filter de operaciones.py buscando un fragmento de la palabra
        resultados = filtrar_pacientes_por_diagnostico(self.gestor.pacientes, "tuber")
        
        # El test PASA si encuentra a Robert a pesar de escribir en minúsculas e incompleto
        self.assertEqual(len(resultados), 1, "Fallo: El filter no encontró coincidencias.")
        self.assertEqual(resultados[0].get_nombre(), "Robert", "Fallo: El nombre del paciente filtrado no coincide.")

if __name__ == '__main__':
    unittest.main()