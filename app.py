from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

csrf = CSRFProtect(app)  

@app.route("/")
def pagina_inicial():
    return "Entrega Final Solution Sprint 5 G16"

@app.route('/bug')                                                                                                                                
def bad():                                                                                                                                        
    return "teste do bug"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)