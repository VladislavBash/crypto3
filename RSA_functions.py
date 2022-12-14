from random import randint
import math
# POW = 20
# MODEL_NUMBER = 10**POW
# MIN_INT = MODEL_NUMBER
# MAX_INT = MODEL_NUMBER * 10**5
# T = 100
# ENCODING_BYTES = 8
POW = 1024
MODEL_NUMBER = 2**POW
MIN_INT = MODEL_NUMBER
MAX_INT = MODEL_NUMBER * 2**100
T = 100
ENCODING_BYTES = 8

def get_random_prime():
    a = randint(MIN_INT, MAX_INT)
    while check_prime(a) == False:
        a = randint(MIN_INT, MAX_INT)
    return a

def check_prime(n):
    if n == 2: # Приплёл для полноты
        return True
    for i in range(T):
        a = randint(2, n-1)
        r = pow_mod(a, n-1, n)
        if r != 1:
            return False
    return True

def extended_euclidean_algorithm(num, mod):
    a = mod
    b = num
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while (b != 0):
        q = a // b
        r = a % b
        x = x2 - q*x1
        y = y2 - q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    return int(y2)

def NOD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def pow_mod(a, k, n):
    b = 1
    if k == 0:
        return b
    k =  bin(k)
    k = k[:1:-1]
    A = a
    if k[0] == '1':
        b = a
    for i in range(1,len(k)):
        A = (A**2) % n
        if k[i] == '1':
            b = (A * b) % n
    return b 

def check_keys(p, q):
    if abs(p - q) > MODEL_NUMBER:
        return True
    else:
        return False

def calc_module(p, q): # Вычисление модуля алгоритма
    return p*q

def calc_Euler_func(p, q): # Вычисление функции Эйлера
    return (p-1)*(q-1)

def calc_exp_encrypt(phi): # Вычисление экспоненты зашифрования
    e = get_random_prime()
    
    while (NOD(e, phi) != 1):
        e /= NOD(e, phi)
    return e

def calc_exp_decrypt(e, phi): # Вычисление экспоненты расшифрования
    return extended_euclidean_algorithm(e, phi)

def encrypt(m, e, n): # Зашифрование
    c = []
    bit_str = ''
    c_str = ''
    len_block = math.floor(math.log2(n)) + 1
    str_len_block = '0' + str(len_block) + 'b'
    for mi in reversed(m):
        num =  pow_mod(mi, e, n)
        bit_str += str(format(num, str_len_block))

    if len(bit_str) % ENCODING_BYTES != 0:
        bit_str = ('0' * (ENCODING_BYTES - (len(bit_str) % ENCODING_BYTES))) + bit_str
    

    for i in range(int(len(bit_str)/ENCODING_BYTES)):
        temp_str = bit_str[ENCODING_BYTES*i:ENCODING_BYTES*(i+1)]
        
        c_str += chr(int(temp_str, 2))
        
    return c_str

def decrypt(c, d, n): # Расшифрование
    bit_str = ''
    c_str = ''
    len_block = math.floor(math.log2(n))
    str_len_block = '0' + str(len_block) + 'b'
    for ci in reversed(c):
        num =  pow_mod(ci, d, n)
        bit_str += str(format(num, str_len_block))

    if len(bit_str) % ENCODING_BYTES != 0:
        bit_str = ('0' * (ENCODING_BYTES - (len(bit_str) % ENCODING_BYTES))) + bit_str

        
    for i in range(int(len(bit_str)/ENCODING_BYTES)):
        temp_str = bit_str[ENCODING_BYTES*i:ENCODING_BYTES*(i+1)]
        
        if temp_str != '00000000':
            c_str += chr(int(temp_str, 2))
        if c_str == 'In 1969 NASA announced11 that the backup crew of Apollo 14':
            pass
            
    return c_str

def gen_keys():
    p = get_random_prime()
    q = get_random_prime()
    while check_keys(p, q) == False:
        p = get_random_prime()
        q = get_random_prime()
    n = calc_module(p, q)
    phi = calc_Euler_func(p, q)
    e = calc_exp_encrypt(phi)
    d = calc_exp_decrypt(e, phi)
    d += phi
    return e, n, d

def get_encrypt_block(text, n):
    block = []
    bit_str = ''
    
    for sym in text:
        bit_str += format(ord(sym), '0' + str(ENCODING_BYTES) + 'b') # Перевод в ENCODING_BYTES-битную строку
    len_block = math.floor(math.log2(n))
    if len(bit_str) % len_block != 0:
        bit_str = ('0' * (len_block - (len(bit_str) % len_block))) + bit_str
        
    for i in range(int(len(bit_str)/len_block)):
        block.append(int(bit_str[len_block*i:len_block*(i+1)], 2))
    block.reverse()
    return block

def get_decrypt_block(text, n):
    block = []
    bit_str = ''
    
    for sym in text:
        bit_str += format(ord(sym), '0' + str(ENCODING_BYTES) + 'b') # Перевод в ENCODING_BYTES-битную строку
    len_block = math.floor(math.log2(n)) + 1
    if len(bit_str) % len_block != 0:
        bit_str = ('0' * (len_block - (len(bit_str) % len_block))) + bit_str
        
    for i in range(int(len(bit_str)/len_block)):
        block.append(int(bit_str[len_block*i:len_block*(i+1)], 2))
    block.reverse()
    return block