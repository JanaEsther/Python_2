import requests
import json

ico= input("Zadejte IČ subkjektu, který Vás zajímá:\n")
headers = {
    'accept': 'application/json',
}

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")

if response.text and response.status_code == 200:
    data = response.json()
    

obchodniJmeno = data.get('obchodniJmeno')
textovaAdresa = data.get('sidlo', {}).get('textovaAdresa')

print( f"{obchodniJmeno} \n{textovaAdresa}")

nazev = input("Zadejte název subkjektu, který Vás zajímá:\n")


headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = json.dumps({"obchodniJmeno": nazev})
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(res.json(), file)
data = res.json()
print(data)



