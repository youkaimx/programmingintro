import requests
import json
ingrediente = "egg"
r = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={ingrediente}')
respuesta = json.loads(r.text)
print("Toda la respuesta: ")
print(json.dumps(respuesta,indent=2))
print("Todas las comidas:")
for comida in range(0,len(respuesta['meals'])):
  print(f"{comida+1}: {respuesta['meals'][comida]['strMeal']}")