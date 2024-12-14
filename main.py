from utils import generate_keys, permute, left_shift

# 1
key = '1010000010'
key_1, key_2 = generate_keys(key)

# 2
bloco_de_dados = '11010111'
IP = [2, 3, 1, 5, 7, 4, 6, 0]
bloco_permutado = permute(bloco_de_dados, IP)
print('Bloco ápos a IP:',bloco_permutado)

# 3 
l_bloco, r_bloco = bloco_permutado[:4], bloco_permutado[4:]
print(l_bloco, r_bloco)

