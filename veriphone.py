import http.client
import json
conn = http.client.HTTPSConnection("api.veriphone.io") # Conection to API

lang = input("select language (en or ru): ")

# Setting lang
if lang == "en":
    phone = input("Type phone number (ex. +1234567890, 1234567890, 80234567890): ")
if lang == "ru":
    phone = input("Введите номер телефона (ex. +1234567890, 1234567890, 80234567890): ")


key = 'YOUR_API_TOKEN' # Key API from https://veriphone.io/cp
default_country = '375' # Default country key
url = '/v2/verify?phone='+phone+'&key='+key+'&default_country='+default_country # URL
conn.request("GET", url) # Get data from URL
res = conn.getresponse() # Data from URL
datajs = res.read() # Read the response
data = json.loads(datajs.decode("utf-8")) # JS datarecodint to UTF-8

# Testing phone in valid
def if_valid_phone(phone):
    key = '2B730D4D8D0645E299A5CABC000F2443'
    default_country = '375'
    url = '/v2/verify?phone='+phone+'&key='+key+'&default_country='+default_country
    conn.request("GET", url)
    res = conn.getresponse()
    datajs = res.read()
    data = json.loads(datajs.decode("utf-8"))
    api_phone_valid = data['phone_valid']

    if api_phone_valid == 'True':
        if lang == "ru":
            response = 'Да'
        if lang == "en":
            response = "Yes"
    else:
        if lang == "ru":
            response = 'Нет'
        if lang == "en":
            response = "No"
    return response

phone_valid_res = if_valid_phone(phone) # Response from testing in valid

# Response
if lang == "ru":
    print(f"Статус запроса: {data['status']}\nНомер: {data['phone']}\nДействителен?: {phone_valid_res}\nТип номера: {data['phone_type']}\nРегион: {data['phone_region']}\nСтрана: {data['country']}\nКод страны: {data['country_code']}\nПрефикс страны: {data['country_prefix']}\nМеждународный номер: {data['international_number']}\nЛокальный номер: {data['local_number']}\nНомер формата e164: {data['e164']}\nОператор: {data['carrier']}")
if lang == "en":
    print(f"Output status: {data['status']}\nNumber: {data['phone']}\nValid?: {phone_valid_res}\nNumber type: {data['phone_type']}\nРегион: {data['phone_region']}\nCountry: {data['country']}\nCountry code: {data['country_code']}\nCountryprefix: {data['country_prefix']}\nInternacional number: {data['international_number']}\nLocal number: {data['local_number']}\nNumber format e164: {data['e164']}\nCarrier: {data['carrier']}")
