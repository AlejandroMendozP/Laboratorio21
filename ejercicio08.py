import json

lista = [
    {
        "nombre": "Barcelona",
        "pais": "Espana",
        "nivelAtaque": 100,
        "nivelDefensa": 100
    },
    {
        "nombre": "Man United",
        "pais": "Inglaterra",
        "nivelAtaque": 70,
        "nivelDefensa": 30
    },
    {
        "nombre": "Bayern Munich",
        "pais": "Alemania",
        "nivelAtaque": 100,
        "nivelDefensa": 80
    }
]

texto = json.dumps(lista, indent=5)
print(texto)