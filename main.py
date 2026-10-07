# Módulo principal - Paradigma Orientado a Eventos
import tkinter as tk
from tkinter import ttk, messagebox  # Importamos ttk para las pestañas
from modelos import GestorCentroSalud, UsuarioFactory
from operaciones import contar_total_pacientes, buscar_paciente_por_dni

class InterfazSistema:
    def __init__(self, root):
        self.gestor = GestorCentroSalud()
        self.root = root
        self.root.title("SistemaRural-PE")
        self.root.geometry("350x280") # Un poco más ancha para que se vea elegante
        
        # 1. Crear el controlador de pestañas (Notebook)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill="both")
        
        # --- PESTAÑA 1: REGISTRO ---
        self.frame_registro = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_registro, text="📝 Registrar Paciente")
        
        tk.Label(self.frame_registro, text="DNI:").pack(pady=5)
        self.entry_dni = tk.Entry(self.frame_registro)
        self.entry_dni.pack()
        
        tk.Label(self.frame_registro, text="Nombre:").pack(pady=5)
        self.entry_nombre = tk.Entry(self.frame_registro)
        self.entry_nombre.pack()

        tk.Label(self.frame_registro, text="Apellido:").pack(pady=5)
        self.entry_apellido = tk.Entry(self.frame_registro)
        self.entry_apellido.pack()
        
        tk.Label(self.frame_registro, text="Diagnóstico:").pack(pady=5)
        self.entry_diag = tk.Entry(self.frame_registro)
        self.entry_diag.pack()
        
        self.btn_registrar = tk.Button(self.frame_registro, text="Registrar Paciente", command=self.registrar)
        self.btn_registrar.pack(pady=15)
        
        # --- PESTAÑA 2: BÚSQUEDA ---
        self.frame_busqueda = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_busqueda, text="🔍 Buscar Historial")
        
        tk.Label(self.frame_busqueda, text="Ingrese el DNI del Paciente:").pack(pady=20)
        self.entry_busqueda = tk.Entry(self.frame_busqueda)
        self.entry_busqueda.pack()
        
        self.btn_buscar = tk.Button(self.frame_busqueda, text="Buscar", command=self.ejecutar_busqueda)
        self.btn_buscar.pack(pady=15)

    # Manejador del evento de registro (Se mantiene igual)
    def registrar(self):
        try:
            dni = self.entry_dni.get()
            nombre = self.entry_nombre.get()
            apellido = self.entry_apellido.get() 
            diag = self.entry_diag.get()
            
            if not dni.isdigit() or len(dni) != 8:
                raise ValueError("El DNI debe contener exactamente 8 dígitos (sin letras ni espacios).")
            if not nombre or not apellido or not diag: # Validamos que no esté vacío
                raise ValueError("Todos los campos son obligatorios.")
                
            nuevo_paciente = UsuarioFactory.crear_usuario("Paciente", dni, nombre, apellido, diag)
            self.gestor.pacientes.append(nuevo_paciente)
            
            total = contar_total_pacientes(self.gestor.pacientes)
            
            self.entry_dni.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_diag.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Paciente registrado de forma segura.\nTotal en sistema: {total}")
            
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))

    # Manejador del evento de búsqueda (Se mantiene igual)
    def ejecutar_busqueda(self):
        dni_ingresado = self.entry_busqueda.get()
        
        if not dni_ingresado:
            messagebox.showerror("Error", "Por favor ingrese un DNI para buscar.")
            return

        resultados = buscar_paciente_por_dni(self.gestor.pacientes, dni_ingresado)
        
        if resultados:
            paciente = resultados[0] 
            mensaje = f"¡Paciente Encontrado!\n\nPaciente: {paciente.get_nombre()} {paciente.get_apellido()}\nDiagnóstico: {paciente.get_diagnostico()}"
            messagebox.showinfo("Historial Clínico", mensaje)
        else:
            messagebox.showwarning("Sin resultados", f"No existe un paciente registrado con el DNI: {dni_ingresado}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazSistema(ventana)
    ventana.mainloop()