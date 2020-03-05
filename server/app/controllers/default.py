from app import app, db
from app.models.user import User

@app.route("/")
def index():
    user = User("Bruno", "bruno@uol.com", "44417655862", "12345")
    db.session.add(user)
    db.session.commit()
    return "Hello World"
