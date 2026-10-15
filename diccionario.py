#=== DICCIONARIO ===
cliente = {
    "nombre": "Ana Garcia",
    "edad": 29,
    "telefonos": {"123456" , "789012"} 
    "direccion": {"calle": "Av. Principal","numero":123,"ciudad":
     "Madrid"},
    }
cliente["activo"] = True        #agregar una clave nueva
cliente["edad"] =29             #modificar una clave existente

for clave, valor in  cliente.items():
    print(f"{clave} : {valor}")

if cliente ["edad"] > 30:
    print("cliente mayor de 30")
else:
    print("cliente de 30 o menos")
