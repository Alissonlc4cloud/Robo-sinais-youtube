from iqoptionapi.stable_api import IQ_Option

API = IQ_Option("wmieky.m@vlvstech.com", "12345678")
API.connect()
if (API.check_connect()) == True: print("Conectado!")
else: print("Dados incorretos!")