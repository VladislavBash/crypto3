import RSA_functions
choose = input('Введите:  \n 1 для ввода открытого и закрытого ключей  \n 2 для генерации открытого и закрытого ключей  \n')

# while True:

if choose == '1':
    e, n = input('Введите открытый ключ (e, n) ').split()
    d = input('Введите закрытый ключ d  ')
elif choose == '2':
    # open_key = get_random() # TO_DO FOR BIG NUMBERS
    # close_key = get_random() # TO_DO FOR BIG NUMBERS
    e, n, d = RSA_functions.gen_keys()
    fw = open('keys.txt', 'w', encoding='utf-8')
    fw.write('e     ' + str(e) +'\n')
    fw.write('n     ' + str(n) +'\n')
    fw.write('d     ' + str(d) +'\n')
    fw.close()
    print("e - ", e)
    print("n - ", n)
    print("d - ", d)
e = int(e)
n = int(n)
d = int(d)

    # if check_keys(open_key, close_key):
    #     break
    # elif choose == '1':
    #     print('Ключи не подходят\n')


file_name_choose = input('Введите:  \n 1 для чтения из open_text.txt (зашифрования) \n 2 для чтения из close_text.txt (расшифрования)  \n')
if file_name_choose == '1':
    fr = open('open_text.txt', encoding='utf-8')
    text = []
    while True:
        letter = fr.read(1)
        if not letter:
            break
        text.append(letter)
    fw = open('close_text.txt', 'w', encoding='utf-8')
    m = RSA_functions.get_encrypt_block(text, n)
    # sym = RSA_functions.encrypt(m, e, n)
    # fw.write(sym) 
    for sym in RSA_functions.encrypt(m, e, n):
        fw.write(sym)
elif file_name_choose == '2':
    fr = open('close_text.txt', encoding='utf-8')
    text = []
    while True:
        letter = fr.read(1)
        if not letter:
            break
        text.append(letter)
    fw = open('open_text.txt', 'w', encoding='utf-8')
    c = RSA_functions.get_decrypt_block(text, n)
    for sym in RSA_functions.decrypt(c, d, n):
        fw.write(sym)
fr.close()
fw.close()