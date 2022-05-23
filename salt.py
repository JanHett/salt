import sys
from src.mvc.session import SessionController

if __name__ == "__main__":

    session = SessionController(sys.argv)

    sys.exit(session.exec())
