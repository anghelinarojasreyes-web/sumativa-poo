from config.database import Database
from models.proyecto import Proyecto

class ProyectoDAO:
    @staticmethod
    def crear(proyecto):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (?, ?, ?)",
                (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio)
            )
            conn.commit()
            proyecto.id_proyecto = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def convertir(fila):
        return Proyecto(
            fila["nombre"],
            fila["descripcion"],
            fila["fecha_inicio"],
            fila["id_proyecto"]
        )

    @staticmethod
    def obtener_todos():
        conn = Database().get_connection()
        proyectos = []
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM proyecto")
            for fila in cursor.fetchall():
                proyectos.append(ProyectoDAO.convertir(fila))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()
        return proyectos

    @staticmethod
    def obtener_por_id(id_proyecto):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM proyecto WHERE id_proyecto = ?",
                (id_proyecto,)
            )
            fila = cursor.fetchone()
            return ProyectoDAO.convertir(fila) if fila else None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            conn.close()

    @staticmethod
    def actualizar(proyecto):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE proyecto SET nombre=?, descripcion=?, fecha_inicio=? WHERE id_proyecto=?",
                (proyecto.nombre, proyecto.descripcion,
                 proyecto.fecha_inicio, proyecto.id_proyecto)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def eliminar(id_proyecto):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM proyecto WHERE id_proyecto = ?",
                (id_proyecto,)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    @staticmethod
    def asignar_empleado(id_empleado, id_proyecto):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO empleado_proyecto (id_empleado, id_proyecto) VALUES (?, ?)",
                (id_empleado, id_proyecto)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    @staticmethod
    def quitar_empleado(id_empleado, id_proyecto):
        conn = Database().get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM empleado_proyecto WHERE id_empleado = ? AND id_proyecto = ?",
                (id_empleado, id_proyecto)
            )
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def ver_empleados(id_proyecto):
        conn = Database().get_connection()
        empleados = []
        try:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT empleado.id_empleado, empleado.nombre
                FROM empleado
                INNER JOIN empleado_proyecto
                ON empleado.id_empleado = empleado_proyecto.id_empleado
                WHERE empleado_proyecto.id_proyecto = ?""",
                (id_proyecto,)
            )
            empleados = cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()
        return empleados