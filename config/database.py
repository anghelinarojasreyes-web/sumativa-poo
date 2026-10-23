import sqlite3

class Database:
    _db_path = "ecotech.db"

    def get_connection(self):
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS departamento (
                id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                gerente TEXT
            )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS empleado (
                id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL,
                direccion TEXT,
                telefono TEXT,
                fecha_inicio TEXT,
                salario REAL,
                id_departamento INTEGER,
                FOREIGN KEY(id_departamento) REFERENCES departamento(id_departamento)
            )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS proyecto (
                id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                fecha_inicio TEXT
            )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS registro_tiempo (
                id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                horas_trabajadas REAL,
                descripcion TEXT,
                id_empleado INTEGER,
                id_proyecto INTEGER,
                FOREIGN KEY(id_empleado) REFERENCES empleado(id_empleado),
                FOREIGN KEY(id_proyecto) REFERENCES proyecto(id_proyecto)
            )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS empleado_proyecto (
                id_empleado INTEGER,
                id_proyecto INTEGER,
                PRIMARY KEY (id_empleado, id_proyecto),
                FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado),
                FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto)
            )""")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la base de datos: {e}")
        finally:
            conn.close()
