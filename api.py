import os 
import requests
from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route("/<conve>")
def ok(conve):

    converte = int(conve)


    if converte == 61:
        return jsonify({
        "Estado": "DF",
    })
    elif converte == 62 | converte == 64:
        return jsonify({
        "Estado": "GO",
    })
    elif converte == 65 | converte == 66:
        return jsonify({
        "Estado": "MT",
    })
    elif converte == 67:
        return jsonify({
        "Estado": "MS",
    })
    elif converte == 82:
        return jsonify({
        "Estado": "AL",
    })
    elif converte == 71 | converte == 73 | converte == 74 | converte == 75 | converte == 77:
        return jsonify({
        "Estado": "BA",
    })
    elif converte == 85 | converte == 87:
        return jsonify({
        "Estado": "CE",
    })
    elif converte == 98 | converte == 99:
        return jsonify({
        "Estado": "MA",
    })
    elif converte == 83:
        return jsonify({
        "Estado": "PB",
    })
    elif converte == 81 | converte == 87:
        return jsonify({
        "Estado": "PE",
    })
    elif converte == 86 | converte == 89:
        return jsonify({
        "Estado": "PI",
    })
    elif converte == 84:
        return jsonify({
        "Estado": "RN",
    })
    elif converte == 79:
        return jsonify({
        "Estado": "SE",
    })
    elif converte == 68:
        return jsonify({
        "Estado": "AC",
    })
    elif converte == 96:
        return jsonify({
        "Estado": "AP",
    })
    elif converte == 92 | converte == 97:
        return jsonify({
        "Estado": "AM",
    })
    elif converte == 91 | converte == 93 | converte == 94:
        return jsonify({
        "Estado": "PA",
    })
    elif converte == 69:
        return jsonify({
        "Estado": "RO",
    })
    elif converte == 95:
        return jsonify({
        "Estado": "RR",
    })
    elif converte == 63:
        return jsonify({
        "Estado": "TO",
    })
    elif converte == 96:
        return jsonify({
        "Estado": "AP",
    })
    elif converte == 27 | converte == 28:
        return jsonify({
        "Estado": "ES",
    })
    elif converte == 31 |converte == 32 |converte == 33 | converte == 34 | converte == 35 | converte == 37 | converte == 38:
        return jsonify({
        "Estado": "MG",
    })
    elif converte == 21 | converte == 22 | converte == 24:
        return jsonify({
        "Estado": "RJ",
    })
    elif converte == 11 | converte == 12 |  converte == 13 |  converte == 14 |  converte == 15 | converte == 16 | converte == 17 | converte == 18 | converte == 19:
        return jsonify({
        "Estado": "SP",
    })
    elif converte ==41 | converte == 42 | converte == 43 | converte == 44 | converte == 45 | converte == 46:
        return jsonify({
        "Estado": "PR",
    })
    elif converte == 51 | converte == 53 | converte == 54 | converte == 55:
        return jsonify({
        "Estado": "RS",
    })
    elif converte == 47 | converte == 48 | converte == 49:
        return jsonify({
        "Estado": "SC",
    })
    else:
        return jsonify({
        "Estado": "NENHUMA UF ENCONTRADA",
    })

app.run(host ="0.0.0.0",port = 2000, debug = False)