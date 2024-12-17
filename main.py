def permutar(bits, tabela):
    return [bits[i - 1] for i in tabela]

def deslocar_esquerda(bits, deslocamentos):
    return bits[deslocamentos:] + bits[:deslocamentos]

def gerar_chaves(chave):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]  
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]  

    
    chave_p10 = permutar(chave, P10)
    esquerda, direita = chave_p10[:5], chave_p10[5:]

   
    esquerda = deslocar_esquerda(esquerda, 1)
    direita = deslocar_esquerda(direita, 1)
    K1 = permutar(esquerda + direita, P8)

    
    esquerda = deslocar_esquerda(esquerda, 2)
    direita = deslocar_esquerda(direita, 2)
    K2 = permutar(esquerda + direita, P8)

    return K1, K2

chave_10 = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
K1, K2 = gerar_chaves(chave_10)
print("K1:", K1)
print("K2:", K2)

IP = [2, 6, 3, 1, 4, 8, 5, 7]
def permutacao_inicial(dados):
    
    return permutar(dados, IP)


bloco_dados = [1, 1, 0, 1, 0, 1, 1, 1]
IP_dados = permutacao_inicial(bloco_dados)
print("Bloco após Permutação Inicial:", IP_dados)


def xor(bits1, bits2):
    
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def rodada_feistel(esquerda, direita, chave):
   
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    direita_EP = permutar(direita, EP)
    direita_XOR = xor(direita_EP, chave)

    S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    def sbox(bits, caixa):
        linha = int(f"{bits[0]}{bits[3]}", 2)
        coluna = int(f"{bits[1]}{bits[2]}", 2)
        return [int(x) for x in f"{caixa[linha][coluna]:02b}"]

    esquerda_temp, direita_temp = direita_XOR[:4], direita_XOR[4:]
    saida_S = sbox(esquerda_temp, S0) + sbox(direita_temp, S1)
    P4 = [2, 4, 3, 1]
    saida_F = permutar(saida_S, P4)
    nova_esquerda = xor(esquerda, saida_F)
    return direita, nova_esquerda

def permutacao(bits, tabela):
    return [bits[i - 1] for i in tabela]

def deslocamento_circular(bits, deslocamento):
    return bits[deslocamento:] + bits[:deslocamento]

def xor_operador(lista1, lista2):
    return [b1 ^ b2 for b1, b2 in zip(lista1, lista2)]

def aplicar_sbox(bits, sbox):
    linha = int(f"{bits[0]}{bits[3]}", 2)
    coluna = int(f"{bits[1]}{bits[2]}", 2)
    return [int(x) for x in f"{sbox[linha][coluna]:02b}"]

esquerda, direita = IP_dados[:4], IP_dados[4:]
esquerda, direita = rodada_feistel(esquerda, direita, K1)
esquerda, direita = rodada_feistel(esquerda, direita, K2)

print("Saída após rodadas de Feistel:", esquerda + direita)

print("\n### Resultados Finais ###")
print(f"Chave Inicial (10 bits): {chave_10}")

print(f"Chave K1 (8 bits): {K1}")
print(f"Chave K2 (8 bits): {K2}")

print(f"Bloco de Dados Inicial (8 bits): {bloco_dados}")
print(f"Bloco de Dados após Permutação Inicial (IP): {IP_dados}")

saida_final = esquerda + direita
print(f"Saída após as Rodadas de Feistel (8 bits): {saida_final}")

FP = [4, 1, 3, 5, 7, 2, 8, 6]
mensagem_cifrada = permutar(saida_final, FP)
print(f"Mensagem Cifrada (8 bits): {mensagem_cifrada}")

print("\n### Processo de Cifragem Concluído ###")
