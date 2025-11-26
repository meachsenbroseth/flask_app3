# from app import create_app

# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)

# run.py
from app import create_app
import os

if __name__ == '__main__':
    app = create_app()
    
    # Debug information
    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print(f"Instance path: {app.instance_path}")
    
    app.run(debug=True)