from config.database import Database
from models.registro_tiempo import RegistroTiempo
from models.empleado_dao import EmpleadoDAO
from models.proyecto_dao import ProyectoDAO

class RegistroTiempoDAO:
    @staticmethod
    def crear(registro):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO registro_tiempo
                (fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto)
                VALUES (?, ?, ?, ?, ?)""",
                (registro.fecha, registro.horas_trabajadas,
                 registro.descripcion, registro.empleado.id_empleado,
                 registro.proyecto.id_proyecto)
            )
            conn.commit()
            registro.id_registro = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def convertir(fila):
        empleado = EmpleadoDAO.obtener_por_id(fila["id_empleado"])
        proyecto = ProyectoDAO.obtener_por_id(fila["id_proyecto"])
        return RegistroTiempo(
            fila["fecha"],
            fila["horas_trabajadas"],
            fila["descripcion"],
            empleado,
            proyecto,
            fila["id_registro"]
        )

    @staticmethod
    def obtener_todos():
        conn = Database().get_connection()
        registros = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM registro_tiempo")
            for fila in cursor.fetchall():
                registros.append(RegistroTiempoDAO.convertir(fila))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()
        return registros

    @staticmethod
    def obtener_por_id(id_registro):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM registro_tiempo WHERE id_registro = ?",
                (id_registro,)
            )
            fila = cursor.fetchone()
            return RegistroTiempoDAO.convertir(fila) if fila else None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def actualizar(registro):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE registro_tiempo
                SET fecha=?, horas_trabajadas=?, descripcion=?,
                id_empleado=?, id_proyecto=?
                WHERE id_registro=?""",
                (registro.fecha, registro.horas_trabajadas,
                 registro.descripcion, registro.empleado.id_empleado,
                 registro.proyecto.id_proyecto, registro.id_registro)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_registro):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM registro_tiempo WHERE id_registro = ?",
                (id_registro,)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

 