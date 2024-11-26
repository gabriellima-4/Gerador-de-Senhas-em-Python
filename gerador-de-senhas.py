################################
## Programa gerador de senhas ##
################################

# A senha deve ter no mínimo um número, uma letra e um caracter especial. A senha será uma mistura de todos esses
    # tipos de caracteres, e não poderá ser uma senha de menos de 4 digitos. 


# Bibliotecas Utilizadas:
import random
import string


# Função Principal:
def gerar_senha(tamanho):
    if tamanho < 4:
        print("A senha deve ser de pelo menos quatro caracteres.")
        return None
    
    else:
        senha = [
            random.choice(string.ascii_letters), # garantindo que a senha terá no mínimo 1 caracter de cada tipo e no mínimo 3 caracteres.
            random.choice(string.digits),    # números
            random.choice(string.punctuation),   # caracteres especiais
        ]

        caracteres_utilizaveis = string.ascii_letters + string.digits + string.punctuation

        selecao = random.choices(caracteres_utilizaveis, k=(tamanho - 3))  # a quantidade de caracteres sortidos (k) será
                                                                            # o tamanho desejado do usuário menos os 3 já inscritos.
        
        senha.extend(selecao) # junção da lista original com a lista "selecao"
        random.shuffle(senha) # garantia de que a cada chamada da função, a saída será uma senha diferente.

        senha_final = "".join(senha) # todos os caracteres são juntados numa string única.

        return senha_final


########################
## Execução do Código ##
########################

comprimento_senha = int(input("Digite o tamanho (quantos caracteres) que a senha deve ter: "))

print(gerar_senha(comprimento_senha))
