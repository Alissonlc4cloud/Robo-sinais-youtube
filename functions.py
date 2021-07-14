from iqoptionapi.stable_api import IQ_Option

class Functions():

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def conectar(self):
        self.API = IQ_Option(self.email, self.password)
        self.API.connect()
        if (self.API.check_connect()) == True: print("Conectado!")
        else: print("Dados incorretos!")

    def comprar_binario(self, valor, ativo, acao, expiracao):
        status, id = self.API.buy(valor, ativo, acao, expiracao)
        if status == True: 
            print(self.API.check_win_v3(id))
        else: print("Não foi possível executar a operação.")

    def comprar_digital(self, valor, ativo, acao, expiracao):
        status, id = self.API.buy_digital_spot(ativo,valor,acao,expiracao)
        if status == True: 
            while True:
                check, valor = (self.API.check_win_digital_v2(id))
                if check == True: break
                print(check)
            print(valor)
        else: print("Não foi possível executar a operação.")        