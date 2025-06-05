from models import storage
from models.state import State

def tast_db():
    s = State(name="Calif")
    print(s)
    s.save()

if __name__ == "__main__":
    tast_db()
