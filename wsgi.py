import os
from app import create_app

app = create_app()
host = os.getenv('HOST')
port = os.getenv('PORT')

if __name__ == "__main__":
    app.run(host=host, port=port)