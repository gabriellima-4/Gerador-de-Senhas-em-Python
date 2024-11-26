################################
## Programa Gerador de Senhas ##
################################

# A senha deve ter no mínimo um número, uma letra e um caracter especial. A senha será uma mistura de todos esses
    # tipos de caracteres, e não poderá ser uma senha de menos de 4 digitos. 

# Além disso, o programa já possui funções para armazenar todas as
    # senhas geradas num arquivo .txt, com o aplicativo/site que se deseja criar uma conta com aquela senha.

# Por fim, é de suma importância relembrar que um arquivo com senhas pessoais jamais deve ser compartilhado
    # ou comentado com terceiros. Oculte ou proteja seus arquivos para que não sejam de fácil acesso.

##################################################################################################################

# Bibliotecas Utilizadas:
import random
import string


# Classes e Métodos:

class Senha:

    def __init__(self):
        self.senha = []
        self.senha_final = ""

    def nome_app(self):
        self.app = input("Digite o nome do aplicativo ou site para qual a senha de login será gerada: ")

    def gerar_senha(self, tamanho):
        if tamanho < 4:
            print("A senha deve ser de pelo menos quatro caracteres.")
            return None
        
        else:
            self.senha = [
                random.choice(string.ascii_letters), # garantindo que a senha terá no mínimo 1 caracter de cada tipo e no mínimo 3 caracteres.
                random.choice(string.digits), # números
                random.choice(string.punctuation), # caracteres especiais
            ]

            caracteres_utilizaveis = string.ascii_letters + string.digits + string.punctuation

            selecao = random.choices(caracteres_utilizaveis, k=(tamanho - 3)) # a quantidade de caracteres sortidos (k) será
                                                                         # o tamanho desejado do usuário menos os 3 já inscritos.
            
            self.senha.extend(selecao) # junção da lista original com a lista "selecao"
            random.shuffle(self.senha) # garantia de que a cada chamada da função, a saída será uma senha diferente.

            self.senha_final = "".join(self.senha) # todos os caracteres são juntados numa string única.

            return self.senha_final
        

    def gravar_senha(self):
        psw = open('nao entre.txt', 'a')
        psw.write("         Senhas p/ login         \n")
        psw.write("----------------------------------\n")
        psw.write("App/Site: {} ".format(self.app) + "\n")
        psw.write("Senha: {}".format(self.senha_final) + "\n")
        psw.write("----------------------------------\n")
        psw.write("\n")
        psw.close()

    def ler_senhas(self):
        with open("nao entre.txt", 'r') as arquivo:
            lista_psw = arquivo.readlines()
        return lista_psw



########################
## Execução do Código ##
########################
s = Senha()
n_aplicativos = int(input("Digite o número de sites ou apps que queira gerar uma senha: "))

for _ in range(n_aplicativos):
    s.nome_app()
    comprimento_senha = int(input("Digite o tamanho (quantos caracteres) que a senha deve ter: "))

    print("Senha gerada! Aqui está: {} ".format(s.gerar_senha(comprimento_senha)))

    s.gravar_senha()

s.ler_senhas()
