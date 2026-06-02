from app import create_app, myDB
from app.models import User

app = create_app()

with app.app_context():
    myDB.create_all()

print("Database created!")