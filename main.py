
def permute(key, list_maps):
    """
    Remapeia os index da minha chave.
    
    Ex:

    """
    return ''.join(key[i] for i in list_maps)
    
def left_shift(bits, N=1):
    """
    Move os bits em N vezes para esqueda.
    OBS: N = 1 -> por padrão(vai para)
    
    Ex:
    bits = 10000001
    N = 1 
    return 01000010
    """
    return bits[N:] + bits[:N]


list_permute_8 = [2, 3, 1, 4, 6, 9, 7, 0]
key = '1010101000'
list_permute_10 = [2, 3, 5, 8, 1, 4, 6, 9, 7, 0]
key_10 = permute(key, list_permute_10)
print('Key permutada em 10 bits:',key_10)
l_bits, r_bits = key_10[:5], key_10[5:]

l_bits_ls1 =  left_shift(l_bits, 1)
r_bits_ls1 = left_shift(r_bits, 1)


key_prov = l_bits_ls1 + r_bits_ls1

key_1 = permute(key_prov, list_permute_8)


l_bits_ls2 = left_shift(l_bits_ls1) 
r_bits_ls2 = left_shift(r_bits_ls1)
key_prov_ls2 = l_bits_ls2 + r_bits_ls2

key_2 = permute(key_prov_ls2, list_permute_8) 

print(f'k1: {key_1}\nk2: {key_2}' )


