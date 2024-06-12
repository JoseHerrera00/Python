import json
import pandas as pd
import requests
 
# Lista de direcciones IP
ip_list = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1",
    # Agrega más direcciones IP aquí
]
 
# URL de la API de AbuseIPDB
url = 'https://api.abuseipdb.com/api/v2/check'
 
# Crear una lista para almacenar los resultados
results = []
 
# Cabeceras de la solicitud con la clave de la API
headers = {
    'Key': 'c12a56563457163f5ae59aa5c56fd0f246c475edcac2124629e4be46de8ce14a5f8eb3c6d1522692',
    'Accept': 'application/json'
}
 
# Iterar sobre cada dirección IP
for ip_address in ip_list:
    # Parámetros de la solicitud
    querystring = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
 
    # Realizar la solicitud GET
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
 
    # Decodificar la respuesta JSON
    decoded_response = response.json()
 
    # Extraer los valores necesarios
    data = decoded_response['data']
    abuse_confidence_score = data['abuseConfidenceScore']
    country_code = data['countryCode']
    domain = data['domain']
    ip_address = data['ipAddress']
 
    # Agregar los resultados a la lista
    results.append({
        'IP Address': ip_address,
        'Abuse Confidence Score': abuse_confidence_score,
        'Country Code': country_code,
        'Domain': domain
    })

    response = requests.request(method='GET', url=url, headers=headers, params=querystring, verify=False)

 
# Crear un DataFrame de pandas con los resultados
df = pd.DataFrame(results)
 
# Exportar el DataFrame a un archivo Excel
df.to_excel('abuse_ip_results.xlsx', index=False)
 