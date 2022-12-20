import RSA_functions
import math
choose = input('Введите:  \n 1 для ввода открытого и закрытого ключей  \n 2 для генерации открытого и закрытого ключей  \n')


if choose == '1':
    e, n = input('Введите открытый ключ (e, n) ').split()
    d = input('Введите закрытый ключ (d)  ')
elif choose == '2':
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



file_name_choose = input('Введите:  \n 1 для чтения из open_text.txt (зашифрования) \n 2 для чтения из close_text.txt (расшифрования)  \n')
open_text = input('Введите название файла с открытым текстом  ')
close_text = input('Введите название файла с шифротекстом  ')
if file_name_choose == '1':
    # fr = open('open_text.pdf', encoding='utf-8')
    fr = open(open_text, 'rb')
    open_file_type = open_text[-3:]
    close_file_type = close_text[-3:]
    # full_let = fr.read()
    text = []
    
    if (open_file_type == 'txt'):
        while True:
            letter = fr.read(1)
            if not letter:
                break
        text.append(letter)
    else:
        text = fr.read()
        
    # fw = open('close_text.pdf', 'w', encoding='utf-8')
    fw = open(close_text, 'wb')
    m = RSA_functions.get_encrypt_block(text, n, open_file_type)
    
    
    # for sym in RSA_functions.encrypt(m, e, n, close_file_type):
    #     fw.write(bytes(sym, encoding='utf-8'))
    bin_lst = RSA_functions.encrypt(m, e, n, close_file_type)
    # result = [bytes(bin_lst[i:8+i], encoding='utf-8') for i in range(0, len(bin_lst), 8)]
    bin_lst = [int(bin_lst[i:8+i], 2) for i in range(0, len(bin_lst), 8)]
    fw.write(bytes(bin_lst))
    # for sym in result:
    #     fw.write(chr(int(sym, 2)))
        

elif file_name_choose == '2':
    # fr = open('close_text.pdf', encoding='utf-8')
    fr = open(close_text, 'rb')
    open_file_type = open_text[-3:]
    close_file_type = close_text[-3:]
    text = []
    
    if (open_file_type == 'txt'):
        while True:
            letter = fr.read(1)
            if not letter:
                break
        text.append(letter)
    else:
        text = fr.read()
        
    # fw = open('open_text.pdf', 'w', encoding='utf-8')
    fw = open(open_text, 'wb')
    c = RSA_functions.get_decrypt_block(text, n, open_file_type)
    # for sym in RSA_functions.decrypt(c, d, n, close_file_type):
    #     fw.write(bytes(sym, encoding='utf-8'))
    bin_lst = RSA_functions.decrypt(c, d, n, close_file_type)
    # result = [bytes(bin_lst[i:8+i], encoding='utf-8') for i in range(0, len(bin_lst), 8)]
    bin_lst = [int(bin_lst[i:8+i], 2) for i in range(0, len(bin_lst), 8)]
    # fw.write(bytes(bin_lst))
    string = ''
    string_lst = []
    for i in reversed(bin_lst):
        string += format(i, '0'+str(math.floor(math.log2(n)))+'b')[::-1]
    for i in range(int(len(string)/8)):
            temp_str = string[8*i:8*(i+1)]
            temp_str = temp_str[::-1]
            string_lst.append(temp_str)
    string_lst = string_lst.reverse()
    fw.write(bytes(string_lst))
    # for sym in result:
    #     fw.write(chr(int(sym, 2)))

fr.close()
fw.close()