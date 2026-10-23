from config.database import Database
from models.departamento import Departamento

class DepartamentoDAO:
    @staticmethod
    def crear(departamento):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO departamento (nombre, gerente) VALUES (?, ?)", (departamento.nombre, departamento.gerente))
            conn.commit()
            departamento.id_departamento = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_todos():
        conn = Database().get_connection()
        departamentos = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departamento")
            for fila in cursor.fetchall():
                departamentos.append(Departamento(fila['nombre'], fila['gerente'], fila['id_departamento']))
        finally:
            conn.close()
        return departamentos

    @staticmethod
    def obtener_por_id(id_departamento):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departamento WHERE id_departamento = ?", (id_departamento,))
            fila = cursor.fetchone()
            if fila:
                return Departamento(fila['nombre'], fila['gerente'], fila['id_departamento'])
            return None
        finally:
            conn.close()

    @staticmethod
    def actualizar(departamento):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE departamento SET nombre = ?, gerente = ? WHERE id_departamento = ?", (departamento.nombre, departamento.gerente, departamento.id_departamento))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_departamento):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM departamento WHERE id_departamento = ?", (id_departamento,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
