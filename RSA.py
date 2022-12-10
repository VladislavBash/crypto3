import RSA_functions
choose = input('Введите:  \n 1 для ввода открытого и закрытого ключей  \n 2 для генерации открытого и закрытого ключей  \n')

# while True:

if choose == '1':
    e, n = input('Введите открытый ключ (e, n) ').split()
    d = input('Введите закрытый ключ  ')
elif choose == '2':
    # open_key = get_random() # TO_DO FOR BIG NUMBERS
    # close_key = get_random() # TO_DO FOR BIG NUMBERS
    e, n, d = RSA_functions.gen_keys()
e = int(e)
n = int(n)
d = int(d)

    # if check_keys(open_key, close_key):
    #     break
    # elif choose == '1':
    #     print('Ключи не подходят\n')


file_name_choose = input('Введите:  \n 1 для чтения из open_text.txt (зашифрования) \n 2 для чтения из close_text.txt (расшифрования)  \n')
if 1:
    fr = open('open_text.txt')
    text = fr.read()
    fw = open('close_text.txt', 'w')
    m = RSA_functions.get_encrypt_block(text, n)
    for sym in RSA_functions.encrypt(m, e, n):
        fw.write(str(sym))
elif 2:
    fr = open('close_text.txt')
    text = fr.read()
    fw = open('open_text.txt', 'w')
    c = RSA_functions.get_decrypt_block(text, n)
    for sym in RSA_functions.decrypt(c, d, n):
        fw.write(str(sym))
fr.close()
fw.close()