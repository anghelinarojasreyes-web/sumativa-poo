from config.database import Database
from controllers.main_controller import MainController

if __name__ == "__main__":
    db = Database()
    db.init_db()
    conn = db.get_connection()
    print("Conexión a la base de datos exitosa")
    conn.close()
    MainController().ejecutar()



