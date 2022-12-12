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

    def test_check_nod_6(self):
        self.assertEqual(
            RSA_functions.NOD(59648035252803565764227646564662501437646093662200, 8156951389676008934211584),
            8
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
        # opText = 'Mission planners had two primary goals in deciding on the landing site: to sample lunar highland material older than Mare Imbrium and to investigate the possibility of relatively recent volcanic activity. They therefore selected Taurus-Littrow, where formations that had been viewed and pictured from orbit were thought to be volcanic in nature. Since all three crew members had backed up previous Apollo lunar missions, they were familiar with the Apollo spacecraft and had had more time for geology training.'
        # n = 21583
        # e = 13
        # d = 1637
        opText = 'ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING, BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATIONS'
        n = 1461
        e = 47
        d = 1427
        clText = RSA_functions.encrypt(RSA_functions.get_encrypt_block(opText, n), e, n)
        self.assertEqual(
            RSA_functions.decrypt(RSA_functions.get_decrypt_block(clText, n), d, n),
            opText
        )

    def test_check_encrypt_text_5(self):
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

    def test_check_encrypt_text_6(self):
        opText = 'ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING, BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATIONS'
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

    def test_check_encrypt_text_7(self):
        opText = '''
        ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING, BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATIONS
        ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING, BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATIONS
        ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING, BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATIONS
        ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING, BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATIONS
        ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING, BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATIONS
        ALICE WAS BEGINNING TO GET VERY TIRED OF SITTING BY HER SISTER ON THE BANK AND OF HAVING NOTHING TO DO ONCE OR TWICE SHE HAD PEEPED INTO THE BOOK HER SISTER WAS READING, BUT IT HAD NO PICTURES OR CONVERSATIONS IN IT AND WHAT IS THE USE OF A BOOK THOUGHT ALICE WITHOUT PICTURES OR CONVERSATIONS
        '''
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
    
    def test_check_encrypt_text_8(self):
        opText = '''
        In 1969 NASA announced11 that the backup crew of Apollo 14 would be Gene Cernan Ronald Evans and former X15 pilot Joe Engle1213 This put them in line to be the prime crew of Apollo 17 because the Apollo programs crew rotation generally meant that a backup crew would fly as prime crew three missions later Harrison Schmitt who was a professional geologist as well as an astronaut had served on the backup crew of Apollo 15 and thus because of the rotation would have been due to fly as lunar module pilot on Apollo 1814
        In September 1970 the plan to launch Apollo 18 was cancelled The scientific community pressed NASA to assign a geologist rather than a pilot with nonprofessional geological training to an Apollo landing NASA subsequently assigned Schmitt to Apollo 17 as the lunar module pilot After that NASAs director of flight crew operations Deke Slayton was left with the question of who would fill the two other Apollo 17 slots the rest of the Apollo 15 backup crew Dick Gordon and Vance Brand or Cernan and Evans from the Apollo 14 backup crew Slayton ultimately chose Cernan and Evans11 Support at NASA for assigning Cernan was not unanimous Cernan had crashed a Bell 47G helicopter into the Indian River near Cape Kennedy during a training exercise in January 1971 the accident was later attributed to pilot error as Cernan had misjudged his altitude before crashing into the water Jim McDivitt who was manager of the Apollo Spacecraft Program Office at the time objected to Cernans selection because of this accident but Slayton dismissed the concern After Cernan was offered command of the mission he advocated for Engle to fly with him on the mission but it was made clear to him that Schmitt would be assigned instead with or without Cernan so he acquiesced1516 The prime crew of Apollo 17 was publicly announced on August 13 197117
        When assigned to Apollo 17 Cernan was a 38yearold captain in the United States Navy he had been selected in the third group of astronauts in 1963 and flown as pilot of Gemini 9A in 1966 and as lunar module pilot of Apollo 10 in 1969 before he served on Apollo 14s backup crew Evans 39 years old when assigned to Apollo 17 had been selected as part of the fifth group of astronauts in 1966 and had been a lieutenant commander in the United States Navy Schmitt a civilian was 37 years old when assigned Apollo 17 had a doctorate in geology from Harvard University and had been selected in the fourth group of astronauts in 1965 Both Evans and Schmitt were making their first spaceflights18
        For the backup crews of Apollo 16 and 17 the final Apollo lunar missions NASA selected astronauts who had already flown Apollo lunar missions to take advantage of their experience and avoid investing time and money in training rookies who would be unlikely to ever fly an Apollo mission1920 The original backup crew for Apollo 17 announced at the same time as the prime crew17 was the crew of Apollo 15 David Scott as commander Alfred Worden as CMP and James Irwin as LMP but in May 1972 they were removed from the backup crew because of their roles in an incident known as the Apollo 15 postal covers incident21 They were replaced with the landing crew of Apollo 16 John W Young as backup crew commander Charles Duke as LMP and Apollo 14s CMP Stuart Roosa182223 Originally Apollo 16s CMP Ken Mattingly was to be assigned along with his crewmates but he declined so he could spend more time with his family his son having just been born and instead took an assignment to the Space Shuttle program24 Roosa had also served as backup CMP for Apollo 1625
        For the Apollo program in addition to the prime and backup crews that had been used in the Mercury and Gemini programs NASA assigned a third crew of astronauts known as the support crew Their role was to provide any assistance in preparing for the missions that the missions director assigned then Preparations took place in meetings at facilities across the US and sometimes needed a member of the flight crew to attend them Because McDivitt was concerned that problems could be created if a prime or backup crew member was unable to attend a meeting Slayton created the support crews to ensure that someone would be able to attend in their stead26 Usually low in seniority they also assembled the missions rules flight plan and checklists and kept them updated2728 For Apollo 17 they were Robert F Overmyer Robert A Parker and C Gordon Fullerton29
        Flight directors were Gerry Griffin first shift Gene Kranz and Neil B Hutchinson second shift and Pete Frank and Charles R Lewis third shift30 According to Kranz flight directors during the program Apollo had a onesentence job description The flight director may take any actions necessary for crew safety and mission success31 Capsule communicators CAPCOMs were Fullerton Parker Young Duke Mattingly Roosa Alan Shepard and Joseph P Allen32
        '''
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

    def test_check_encrypt_text_9(self):
        opText = '''
        In 1969 NASA announced11 that the backup crew of Apollo 14 would be Gene Cernan Ronald Evans and former X15 pilot Joe Engle1213 This put them in line to be the prime crew of Apollo 17 because the Apollo programs crew rotation generally meant that a backup crew would fly as prime crew three missions later Harrison Schmitt who was a professional geologist as well as an astronaut had served on the backup crew of Apollo 15 and thus because of the rotation would have been due to fly as lunar module pilot on Apollo 1814
        In September 1970 the plan to launch Apollo 18 was cancelled The scientific community pressed NASA to assign a geologist rather than a pilot with nonprofessional geological training to an Apollo landing NASA subsequently assigned Schmitt to Apollo 17 as the lunar module pilot After that NASAs director of flight crew operations Deke Slayton was left with the question of who would fill the two other Apollo 17 slots the rest of the Apollo 15 backup crew Dick Gordon and Vance Brand or Cernan and Evans from the Apollo 14 backup crew Slayton ultimately chose Cernan and Evans11 Support at NASA for assigning Cernan was not unanimous Cernan had crashed a Bell 47G helicopter into the Indian River near Cape Kennedy during a training exercise in January 1971 the accident was later attributed to pilot error as Cernan had misjudged his altitude before crashing into the water Jim McDivitt who was manager of the Apollo Spacecraft Program Office at the time objected to Cernans selection because of this accident but Slayton dismissed the concern After Cernan was offered command of the mission he advocated for Engle to fly with him on the mission but it was made clear to him that Schmitt would be assigned instead with or without Cernan so he acquiesced1516 The prime crew of Apollo 17 was publicly announced on August 13 197117
        When assigned to Apollo 17 Cernan was a 38yearold captain in the United States Navy he had been selected in the third group of astronauts in 1963 and flown as pilot of Gemini 9A in 1966 and as lunar module pilot of Apollo 10 in 1969 before he served on Apollo 14s backup crew Evans 39 years old when assigned to Apollo 17 had been selected as part of the fifth group of astronauts in 1966 and had been a lieutenant commander in the United States Navy Schmitt a civilian was 37 years old when assigned Apollo 17 had a doctorate in geology from Harvard University and had been selected in the fourth group of astronauts in 1965 Both Evans and Schmitt were making their first spaceflights18
        For the backup crews of Apollo 16 and 17 the final Apollo lunar missions NASA selected astronauts who had already flown Apollo lunar missions to take advantage of their experience and avoid investing time and money in training rookies who would be unlikely to ever fly an Apollo mission1920 The original backup crew for Apollo 17 announced at the same time as the prime crew17 was the crew of Apollo 15 David Scott as commander Alfred Worden as CMP and James Irwin as LMP but in May 1972 they were removed from the backup crew because of their roles in an incident known as the Apollo 15 postal covers incident21 They were replaced with the landing crew of Apollo 16 John W Young as backup crew commander Charles Duke as LMP and Apollo 14s CMP Stuart Roosa182223 Originally Apollo 16s CMP Ken Mattingly was to be assigned along with his crewmates but he declined so he could spend more time with his family his son having just been born and instead took an assignment to the Space Shuttle program24 Roosa had also served as backup CMP for Apollo 1625
        For the Apollo program in addition to the prime and backup crews that had been used in the Mercury and Gemini programs NASA assigned a third crew of astronauts known as the support crew Their role was to provide any assistance in preparing for the missions that the missions director assigned then Preparations took place in meetings at facilities across the US and sometimes needed a member of the flight crew to attend them Because McDivitt was concerned that problems could be created if a prime or backup crew member was unable to attend a meeting Slayton created the support crews to ensure that someone would be able to attend in their stead26 Usually low in seniority they also assembled the missions rules flight plan and checklists and kept them updated2728 For Apollo 17 they were Robert F Overmyer Robert A Parker and C Gordon Fullerton29
        Flight directors were Gerry Griffin first shift Gene Kranz and Neil B Hutchinson second shift and Pete Frank and Charles R Lewis third shift30 According to Kranz flight directors during the program Apollo had a onesentence job description The flight director may take any actions necessary for crew safety and mission success31 Capsule communicators CAPCOMs were Fullerton Parker Young Duke Mattingly Roosa Alan Shepard and Joseph P Allen32
        '''
        # e, n, d = RSA_functions.gen_keys()
        # e = int(e)
        # n = int(n)
        # d = int(d)
        n = 23514627421878329592145898958446898953880545588923
        e = 284227351189514315201777
        d = 32951585898351648982870282376711222397287991360913
        clText = RSA_functions.encrypt(RSA_functions.get_encrypt_block(opText, n), e, n)
        self.assertEqual(
            RSA_functions.decrypt(RSA_functions.get_decrypt_block(clText, n), d, n),
            opText
        )

    def test_check_encrypt_text_10(self):
        opText = 'because of the rotation'
        n = 23514627421878329592145898958446898953880545588923
        e = 284227351189514315201777
        d = 32951585898351648982870282376711222397287991360913
        clText = RSA_functions.encrypt(RSA_functions.get_encrypt_block(opText, n), e, n) # Получает '\x01\x17\x04\x03QE\x17\x85sIË\x187RQr\x8båÕ®ä¡bê\nêùN\x97\x9f$\x9d\x02À\x7fC_§\x00¤ñb'
        # clText = '\x01\x17\x04\x03QE\x17\x85sIË\x187RQr\x8båÕ®ä¡bê\nêùN\x97\x9f$\x9d\x02À\x7fC_§\x00¤ñb' # \r -> \n (переносы строки в dos)
        self.assertEqual(
            RSA_functions.decrypt(RSA_functions.get_decrypt_block(clText, n), d, n),
            opText
        )

if __name__ == '__main__':
    unittest.main() 