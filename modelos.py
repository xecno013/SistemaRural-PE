# Aplicación estricta de POO y protección de datos
from cryptography.fernet import Fernet

# Generamos la llave maestra de encriptación
LLAVE_SECRETA = Fernet.generate_key()
maquina_encriptadora = Fernet(LLAVE_SECRETA)

class Usuario:
    def __init__(self, dni, nombre, apellido):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
    
    def get_nombre(self):
        return self._nombre
        
    def get_apellido(self):
        return self._apellido

class Paciente(Usuario):
    def __init__(self, dni, nombre, apellido, diagnostico):
        super().__init__(dni, nombre, apellido)
        self._diagnostico_protegido = maquina_encriptadora.encrypt(diagnostico.encode())
        
    def get_diagnostico(self):
        return maquina_encriptadora.decrypt(self._diagnostico_protegido).decode()

class GestorCentroSalud:
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(GestorCentroSalud, cls).__new__(cls)
            cls._instancia.pacientes = [] 
        return cls._instancia

class UsuarioFactory:
    @staticmethod
    def crear_usuario(tipo, dni, nombre, apellido, extra):
        if tipo == "Paciente":
            return Paciente(dni, nombre, apellido, extra)
        return None