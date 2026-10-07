from cryptography.fernet import Fernet

# Generamos la llave maestra de encriptación
LLAVE_SECRETA = Fernet.generate_key()
maquina_encriptadora = Fernet(LLAVE_SECRETA)

class Usuario:
    def __init__(self, dni, nombre):
        self._dni = dni
        self._nombre = nombre
    
    def get_nombre(self):
        return self._nombre

class Paciente(Usuario):
    def __init__(self, dni, nombre, diagnostico):
        super().__init__(dni, nombre)
        # Encriptación real: convertimos a bytes y encriptamos
        self._diagnostico_protegido = maquina_encriptadora.encrypt(diagnostico.encode())
        
    def get_diagnostico(self):
        # Desencriptación real usando la llave
        return maquina_encriptadora.decrypt(self._diagnostico_protegido).decode()

class GestorCentroSalud:
    # Patrón Singleton: Garantiza una única instancia del gestor de datos
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(GestorCentroSalud, cls).__new__(cls)
            cls._instancia.pacientes = [] # Lista de almacenamiento local
        return cls._instancia

class UsuarioFactory:
    # Patrón Factory: Centraliza la creación de usuarios
    @staticmethod
    def crear_usuario(tipo, dni, nombre, extra):
        if tipo == "Paciente":
            return Paciente(dni, nombre, extra)
        return None