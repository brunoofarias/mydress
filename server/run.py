from app import manager, db

if __name__ == "__main__":
    manager.run()
    db.create_all()
    