from flask import Flask, request, jsonify
from database import DatabaseConnection
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:*******@localhost:5433/api_keys'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_conn = DatabaseConnection(app)
db_conn.init_app()

db_conn.create_api_key_table()

api_key = "testee" ## TODO implementar metodo de cadastro automatico
hashed_key = hashlib.sha1(api_key.encode()).hexdigest()
db_conn.insert_api_keys([hashed_key])

app = Flask(__name__)

uf_por_codigo = {
    61: "DF",
    62: "GO",
    64: "GO",
    65: "MT",
    66: "MT",
    67: "MS",
    82: "AL",
    71: "BA",
    73: "BA",
    74: "BA",
    75: "BA",
    77: "BA",
    85: "CE",
    87: "CE",
    98: "MA",
    99: "MA",
    83: "PB",
    81: "PE",
    86: "PI",
    89: "PI",
    84: "RN",
    79: "SE",
    68: "AC",
    96: "AP",
    92: "AM",
    97: "AM",
    91: "PA",
    93: "PA",
    94: "PA",
    69: "RO",
    95: "RR",
    63: "TO",
    27: "ES",
    28: "ES",
    31: "MG",
    32: "MG",
    33: "MG",
    34: "MG",
    35: "MG",
    37: "MG",
    38: "MG",
    21: "RJ",
    22: "RJ",
    24: "RJ",
    11: "SP",
    12: "SP",
    13: "SP",
    14: "SP",
    15: "SP",
    16: "SP",
    17: "SP",
    18: "SP",
    19: "SP",
    41: "PR",
    42: "PR",
    43: "PR",
    44: "PR",
    45: "PR",
    46: "PR",
    51: "RS",
    53: "RS",
    54: "RS",
    55: "RS",
    47: "SC",
    48: "SC",
    49: "SC"
}

@app.route("/")
def home():
    return "Bem-vindo à API de conversão de códigos de estado!"

@app.route("/<conve>")
def ok(conve):
    api_key = request.headers.get("API-Key")

    if db_conn.verify_api_key(api_key):
        converte = int(conve)
        estado = uf_por_codigo.get(converte, "NENHUMA UF ENCONTRADA")
        return jsonify({"Estado": estado})
    else:
        return jsonify({"error": "Chave de API inválida."}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000, debug=False)