import sys
sys.dont_write_bytecode = True

from src.infrastractures.flask_handler import app

if __name__ == '__main__':
    app.run(debug=True)
    