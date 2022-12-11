import unittest
import RSA_functions

class Prime_Test(unittest.TestCase):
    def test_check_prime_1(self):
        self.assertEqual(
            RSA_functions.check_prime(2),
            True
        )
    
    def test_check_prime_2(self):
        self.assertEqual(
            RSA_functions.check_prime(3),
            True
        )

    def test_check_prime_3(self):
        self.assertEqual(
            RSA_functions.check_prime(4),
            False
        )

    def test_check_prime_4(self):
        self.assertEqual(
            RSA_functions.check_prime(5999158576590057802059601),
            True
        )

class Inverse_Number_Test(unittest.TestCase):
    def test_check_inverse_number_1(self):
        self.assertEqual(
            RSA_functions.extended_euclidean_algorithm(21, 13),
            5
        )
    
    def test_check_inverse_number_2(self):
        self.assertEqual(
            RSA_functions.extended_euclidean_algorithm(85, 19),
            -2
        )
    
    def test_check_inverse_number_3(self):
        self.assertEqual(
            RSA_functions.extended_euclidean_algorithm(4061, 991),
            -378
        )

class NOD_Test(unittest.TestCase):
    def test_check_nod_1(self):
        self.assertEqual(
            RSA_functions.NOD(21, 13),
            1
        )
    
    def test_check_nod_2(self):
        self.assertEqual(
            RSA_functions.NOD(85, 19),
            1
        )
    
    def test_check_nod_3(self):
        self.assertEqual(
            RSA_functions.NOD(4061, 991),
            1
        )
    
    def test_check_nod_4(self):
        self.assertEqual(
            RSA_functions.NOD(85, 35),
            5
        )
    
    def test_check_nod_5(self):
        self.assertEqual(
            RSA_functions.NOD(261423, 5241),
            3
        )

class Pow_Mod_Test(unittest.TestCase):
    def test_check_pow_mod_1(self):
        self.assertEqual(
            RSA_functions.pow_mod(45, 6189700196426901110, 618970019642690137449562111),
            453360609069516352365243294
        )

    def test_check_pow_mod_2(self):
        self.assertEqual(
            RSA_functions.pow_mod(564, 52624122, 264654541),
            185434639
        )

    def test_check_pow_mod_3(self):
        self.assertEqual(
            RSA_functions.pow_mod(45645645712534, 94571454, 11231374),
            8705368
        )
    
    def test_check_pow_mod_4(self):
        self.assertEqual(
            RSA_functions.pow_mod(25112, 143637, 216424),
            pow(25112, 143637, 216424)
        )

    def test_check_pow_mod_5(self):
        self.assertEqual(
            RSA_functions.pow_mod(7252971255756, 973645164, 72476745654),
            pow(7252971255756, 973645164, 72476745654)
        )

class Check_Keys_Test(unittest.TestCase):
    def test_check_check_keys_1(self):
        num = 10**3
        self.assertEqual(
            RSA_functions.check_keys(num, num + RSA_functions.MODEL_NUMBER),
            False
        )
    
    def test_check_check_keys_2(self):
        num = 10**3
        self.assertEqual(
            RSA_functions.check_keys(num, num - RSA_functions.MODEL_NUMBER),
            False
        )
    
    def test_check_check_keys_3(self):
        num = 10**3
        self.assertEqual(
            RSA_functions.check_keys(num, num + 1 + RSA_functions.MODEL_NUMBER),
            True
        )
    
    def test_check_check_keys_4(self):
        num = 10**3
        self.assertEqual(
            RSA_functions.check_keys(num, num - 1 - RSA_functions.MODEL_NUMBER),
            True
        )

class Calc_Module_Test(unittest.TestCase):
    def test_check_calc_module_1(self):
        p = RSA_functions.randint(-RSA_functions.MODEL_NUMBER, RSA_functions.MODEL_NUMBER)
        q = RSA_functions.randint(-RSA_functions.MODEL_NUMBER, RSA_functions.MODEL_NUMBER)
        self.assertEqual(
            RSA_functions.calc_module(p, q),
            p*q
        )

class Calc_Euler_Func_Test(unittest.TestCase):
    def test_check_calc_Euler_func_1(self):
        p = RSA_functions.randint(-RSA_functions.MODEL_NUMBER, RSA_functions.MODEL_NUMBER)
        q = RSA_functions.randint(-RSA_functions.MODEL_NUMBER, RSA_functions.MODEL_NUMBER)
        self.assertEqual(
            RSA_functions.calc_Euler_func(p, q),
            (p-1)*(q-1)
        )

class Get_Encrypt_Block_Test(unittest.TestCase):
    def test_check_get_encrypt_block_1(self):
        text = 'CRYPTO'
        n = 21583
        self.assertEqual(
            RSA_functions.get_encrypt_block(text, n), 
            [5199, 9537, 13605, 16]
        )

class Encrypt_Text_Test(unittest.TestCase):
    def test_check_encrypt_text_1(self):
        text = 'CRYPTO'
        n = 21583
        e = 13
        self.assertEqual(
            RSA_functions.encrypt(RSA_functions.get_encrypt_block(text, n), e, n), 
            "-%*d"
        )
    
    def test_check_encrypt_text_2(self):
        opText = 'HELLO'
        n = 21583
        e = 13
        d = 1637
        clText = RSA_functions.encrypt(RSA_functions.get_encrypt_block(opText, n), e, n)
        self.assertEqual(
            RSA_functions.decrypt(RSA_functions.get_decrypt_block(clText, n), d, n),
            opText
        )
    
    def test_check_encrypt_text_3(self):
        text = 'NAME'
        n = 227923
        e = 31
        d = 7319
        self.assertEqual(
            RSA_functions.encrypt(RSA_functions.get_encrypt_block(text, n), e, n), 
            "\x01\x97¬¨>"
        )

    def test_check_encrypt_text_4(self):
        opText = 'HELLO'
        e, n, d = RSA_functions.gen_keys()
        e = int(e)
        n = int(n)
        d = int(d)
        # n = 38809
        # e = 181
        # d = 46269
        clText = RSA_functions.encrypt(RSA_functions.get_encrypt_block(opText, n), e, n)
        self.assertEqual(
            RSA_functions.decrypt(RSA_functions.get_decrypt_block(clText, n), d, n),
            opText
        )
    
    def test_check_encrypt_text_5(self):
        opText = 'HELLO'
        n = 59648035252803565764227662109371319537837522368439
        e = 8156951389676008934211584
        d = 3571970090168332389047108527885612809115816588462
        n = 227923
        e = 31
        d = 7319
        clText = RSA_functions.encrypt(RSA_functions.get_encrypt_block(opText, n), e, n)
        self.assertEqual(
            RSA_functions.decrypt(RSA_functions.get_decrypt_block(clText, n), d, n),
            opText
        )

if __name__ == '__main__':
    unittest.main() 