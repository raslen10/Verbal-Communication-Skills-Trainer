from app.utils import init_db
from app.interface import launch_interface

if __name__ == "__main__":
    init_db()
    launch_interface()