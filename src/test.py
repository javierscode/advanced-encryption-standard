#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from main import *


class Test_1_1_AddRoundKey(unittest.TestCase):

    def test_1(self):
        key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
        state = [[0, 17, 34, 51], [68, 85, 102, 119], [136, 153, 170, 187], [204, 221, 238, 255]]
        new_state = [[0, 16, 32, 48], [64, 80, 96, 112], [128, 144, 160, 176], [192, 208, 224, 240]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)

    def test_2(self):
        key = b'\xd6\xaat\xfd\xd2\xafr\xfa\xda\xa6x\xf1\xd6\xabv\xfe'
        state = [[95, 114, 100, 21], [87, 245, 188, 146], [247, 190, 59, 41], [29, 185, 249, 26]]
        new_state = [[137, 216, 16, 232], [133, 90, 206, 104], [45, 24, 67, 216], [203, 18, 143, 228]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)

    def test_3(self):
        key = b'\xb6\x92\xcf\x0bd=\xbd\xf1\xbe\x9b\xc5\x00h0\xb3\xfe'
        state = [[255, 135, 150, 132], [49, 216, 106, 81], [100, 81, 81, 250], [119, 58, 208, 9]]
        new_state = [[73, 21, 89, 143], [85, 229, 215, 160], [218, 202, 148, 250], [31, 10, 99, 247]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)

    def test_4(self):
        key = b'\xb6\xfftN\xd2\xc2\xc9\xbflY\x0c\xbf\x04i\xbfA'
        state = [[76, 156, 30, 102], [247, 113, 240, 118], [44, 63, 134, 142], [83, 77, 242, 86]]
        new_state = [[250, 99, 106, 40], [37, 179, 57, 201], [64, 102, 138, 49], [87, 36, 77, 23]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)

    def test_5(self):
        key = b'G\xf7\xf7\xbc\x955>\x03\xf9l2\xbc\xfd\x05\x8d\xfd'
        state = [[99, 133, 183, 159], [252, 83, 141, 249], [151, 190, 71, 142], [117, 71, 214, 145]]
        new_state = [[36, 114, 64, 35], [105, 102, 179, 250], [110, 210, 117, 50], [136, 66, 91, 108]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)

    def test_6(self):
        key = b'<\xaa\xa3\xe8\xa9\x9f\x9d\xebP\xf3\xafW\xad\xf6"\xaa'
        state = [[244, 188, 212, 84], [50, 229, 84, 208], [117, 241, 214, 197], [29, 208, 59, 60]]
        new_state = [[200, 22, 119, 188], [155, 122, 201, 59], [37, 2, 121, 146], [176, 38, 25, 150]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)

    def test_7(self):
        key = b'^9\x0f}\xf7\xa6\x92\x96\xa7U=\xc1\n\xa3\x1fk'
        state = [[152, 22, 238, 116], [0, 248, 127, 85], [107, 44, 4, 156], [142, 90, 208, 54]]
        new_state = [[198, 47, 225, 9], [247, 94, 237, 195], [204, 121, 57, 93], [132, 249, 207, 93]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)

    def test_8(self):
        key = b'\x14\xf9p\x1a\xe3_\xe2\x8cD\n\xdfMN\xa9\xc0&'
        state = [[197, 126, 28, 21], [154, 155, 210, 134], [240, 95, 75, 224], [152, 198, 52, 57]]
        new_state = [[209, 135, 108, 15], [121, 196, 48, 10], [180, 85, 148, 173], [214, 111, 244, 31]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)

    def test_9(self):
        key = b'GC\x875\xa4\x1ce\xb9\xe0\x16\xba\xf4\xae\xbfz\xd2'
        state = [[186, 160, 61, 231], [161, 249, 181, 110], [213, 81, 44, 186], [95, 65, 77, 35]]
        new_state = [[253, 227, 186, 210], [5, 229, 208, 215], [53, 71, 150, 78], [241, 254, 55, 241]]
        r = uoc_add_round_key(state, key)
        self.assertEqual(r, new_state)


class Test_1_2_ByteSub(unittest.TestCase):

    def test_1(self):
        state = [[0, 16, 32, 48], [64, 80, 96, 112], [128, 144, 160, 176], [192, 208, 224, 240]]
        new_state = [[99, 202, 183, 4], [9, 83, 208, 81], [205, 96, 224, 231], [186, 112, 225, 140]]
        r = uoc_byte_sub(state, False)
        self.assertEqual(r, new_state)

    def test_2(self):
        state = [[137, 216, 16, 232], [133, 90, 206, 104], [45, 24, 67, 216], [203, 18, 143, 228]]
        new_state = [[167, 97, 202, 155], [151, 190, 139, 69], [216, 173, 26, 97], [31, 201, 115, 105]]
        r = uoc_byte_sub(state, False)
        self.assertEqual(r, new_state)

    def test_3(self):
        state = [[73, 21, 89, 143], [85, 229, 215, 160], [218, 202, 148, 250], [31, 10, 99, 247]]
        new_state = [[59, 89, 203, 115], [252, 217, 14, 224], [87, 116, 34, 45], [192, 103, 251, 104]]
        r = uoc_byte_sub(state, False)
        self.assertEqual(r, new_state)

    def test_4(self):
        state = [[250, 99, 106, 40], [37, 179, 57, 201], [64, 102, 138, 49], [87, 36, 77, 23]]
        new_state = [[45, 251, 2, 52], [63, 109, 18, 221], [9, 51, 126, 199], [91, 54, 227, 240]]
        r = uoc_byte_sub(state, False)
        self.assertEqual(r, new_state)

    def test_5(self):
        state = [[122, 159, 16, 39], [137, 213, 245, 11], [43, 239, 253, 159], [61, 202, 78, 167]]
        new_state = [[189, 110, 124, 61], [242, 181, 119, 158], [11, 97, 33, 110], [139, 16, 182, 137]]
        r = uoc_byte_sub(state, True)
        self.assertEqual(r, new_state)

    def test_6(self):
        state = [[84, 17, 244, 181], [107, 217, 112, 14], [150, 160, 144, 47], [161, 187, 154, 161]]
        new_state = [[253, 227, 186, 210], [5, 229, 208, 215], [53, 71, 150, 78], [241, 254, 55, 241]]
        r = uoc_byte_sub(state, True)
        self.assertEqual(r, new_state)

    def test_7(self):
        state = [[62, 23, 80, 118], [182, 28, 4, 103], [141, 252, 34, 149], [246, 168, 191, 192]]
        new_state = [[209, 135, 108, 15], [121, 196, 48, 10], [180, 85, 148, 173], [214, 111, 244, 31]]
        r = uoc_byte_sub(state, True)
        self.assertEqual(r, new_state)

    def test_8(self):
        state = [[180, 21, 248, 1], [104, 88, 85, 46], [75, 182, 18, 76], [95, 153, 138, 76]]
        new_state = [[198, 47, 225, 9], [247, 94, 237, 195], [204, 121, 57, 93], [132, 249, 207, 93]]
        r = uoc_byte_sub(state, True)
        self.assertEqual(r, new_state)


class Test_1_3_ShiftRow(unittest.TestCase):

    def test_1(self):
        state = [[99, 202, 183, 4], [9, 83, 208, 81], [205, 96, 224, 231], [186, 112, 225, 140]]
        new_state = [[99, 83, 224, 140], [9, 96, 225, 4], [205, 112, 183, 81], [186, 202, 208, 231]]
        r = uoc_shift_row(state, False)
        self.assertEqual(r, new_state)

    def test_2(self):
        state = [[167, 97, 202, 155], [151, 190, 139, 69], [216, 173, 26, 97], [31, 201, 115, 105]]
        new_state = [[167, 190, 26, 105], [151, 173, 115, 155], [216, 201, 202, 69], [31, 97, 139, 97]]
        r = uoc_shift_row(state, False)
        self.assertEqual(r, new_state)

    def test_3(self):
        state = [[59, 89, 203, 115], [252, 217, 14, 224], [87, 116, 34, 45], [192, 103, 251, 104]]
        new_state = [[59, 217, 34, 104], [252, 116, 251, 115], [87, 103, 203, 224], [192, 89, 14, 45]]
        r = uoc_shift_row(state, False)
        self.assertEqual(r, new_state)

    def test_4(self):
        state = [[45, 251, 2, 52], [63, 109, 18, 221], [9, 51, 126, 199], [91, 54, 227, 240]]
        new_state = [[45, 109, 126, 240], [63, 51, 227, 52], [9, 54, 2, 221], [91, 251, 18, 199]]
        r = uoc_shift_row(state, False)
        self.assertEqual(r, new_state)

    def test_5(self):
        state = [[122, 213, 253, 167], [137, 239, 78, 39], [43, 202, 16, 11], [61, 159, 245, 159]]
        new_state = [[122, 159, 16, 39], [137, 213, 245, 11], [43, 239, 253, 159], [61, 202, 78, 167]]
        r = uoc_shift_row(state, True)
        self.assertEqual(r, new_state)

    def test_6(self):
        state = [[84, 217, 144, 161], [107, 160, 154, 181], [150, 187, 244, 14], [161, 17, 112, 47]]
        new_state = [[84, 17, 244, 181], [107, 217, 112, 14], [150, 160, 144, 47], [161, 187, 154, 161]]
        r = uoc_shift_row(state, True)
        self.assertEqual(r, new_state)

    def test_7(self):
        state = [[62, 28, 34, 192], [182, 252, 191, 118], [141, 168, 80, 103], [246, 23, 4, 149]]
        new_state = [[62, 23, 80, 118], [182, 28, 4, 103], [141, 252, 34, 149], [246, 168, 191, 192]]
        r = uoc_shift_row(state, True)
        self.assertEqual(r, new_state)

    def test_8(self):
        state = [[180, 88, 18, 76], [104, 182, 138, 1], [75, 153, 248, 46], [95, 21, 85, 76]]
        new_state = [[180, 21, 248, 1], [104, 88, 85, 46], [75, 182, 18, 76], [95, 153, 138, 76]]
        r = uoc_shift_row(state, True)
        self.assertEqual(r, new_state)


class Test_2_1_GenKey(unittest.TestCase):

    def test_1(self):
        r = uoc_aes_genkey()
        self.assertEqual(len(r), 16)

    def test_2(self):
        r = uoc_aes_genkey()
        self.assertEqual(isinstance(r, bytes), True)


class Test_2_2_ExpandKey(unittest.TestCase):

    def test_1(self):
        key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        subkeys = [b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
                   b'bcccbcccbcccbccc',
                   b'\x9b\x98\x98\xc9\xf9\xfb\xfb\xaa\x9b\x98\x98\xc9\xf9\xfb\xfb\xaa',
                   b'\x90\x974Pil\xcf\xfa\xf2\xf4W3\x0b\x0f\xac\x99',
                   b'\xee\x06\xda{\x87j\x15\x81u\x9eB\xb2~\x91\xee+',
                   b'\x7f.+\x88\xf8D>\t\x8d\xda|\xbb\xf3K\x92\x90',
                   b'\xecaK\x85\x14%u\x8c\x99\xff\t7j\xb4\x9b\xa7',
                   b'!u\x17\x875Pb\x0b\xac\xafk<\xc6\x1b\xf0\x9b',
                   b'\x0e\xf9\x033;\xa9a8\x97\x06\n\x04Q\x1d\xfa\x9f',
                   b'\xb1\xd4\xd8\xe2\x8a}\xb9\xda\x1d{\xb3\xdeLfIA',
                   b'\xb4\xef[\xcb>\x92\xe2\x11#\xe9Q\xcfo\x8f\x18\x8e']
        r = uoc_expand_key(key)
        self.assertEqual(r, subkeys)

    def test_2(self):
        key = b'\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a\x0a'
        subkeys = [b'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',
                   b'lmmmfggglmmmfggg',
                   b'\xeb\xe8\xe8^\x8d\x8f\x8f9\xe1\xe2\xe2T\x87\x85\x853',
                   b'x\x7f+I\xf5\xf0\xa4p\x14\x12F$\x93\x97\xc3\x17',
                   b'\xf8Q\xdb\x95\r\xa1\x7f\xe5\x19\xb39\xc1\x8a$\xfa\xd6',
                   b'\xde|-\xeb\xd3\xddR\x0e\xcank\xcf@J\x91\x19',
                   b'(\xfd\xf9\xe2\xfb \xab\xec1N\xc0#q\x04Q:',
                   b'\x9a,yAa\x0c\xd2\xadPB\x12\x8e!FC\xb4',
                   b'@6\xf4\xbc!:&\x11qx4\x9fP>w+',
                   b'\xe9\xc3\x05\xef\xc8\xf9#\xfe\xb9\x81\x17a\xe9\xbf`J',
                   b'\xd7\x13\xd3\xf1\x1f\xea\xf0\x0f\xa6k\xe7nO\xd4\x87$']
        r = uoc_expand_key(key)
        self.assertEqual(r, subkeys)

    def test_3(self):
        key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'
        subkeys = [b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f',
                   b'\xd6\xaat\xfd\xd2\xafr\xfa\xda\xa6x\xf1\xd6\xabv\xfe',
                   b'\xb6\x92\xcf\x0bd=\xbd\xf1\xbe\x9b\xc5\x00h0\xb3\xfe',
                   b'\xb6\xfftN\xd2\xc2\xc9\xbflY\x0c\xbf\x04i\xbfA',
                   b'G\xf7\xf7\xbc\x955>\x03\xf9l2\xbc\xfd\x05\x8d\xfd',
                   b'<\xaa\xa3\xe8\xa9\x9f\x9d\xebP\xf3\xafW\xad\xf6"\xaa',
                   b'^9\x0f}\xf7\xa6\x92\x96\xa7U=\xc1\n\xa3\x1fk',
                   b'\x14\xf9p\x1a\xe3_\xe2\x8cD\n\xdfMN\xa9\xc0&',
                   b'GC\x875\xa4\x1ce\xb9\xe0\x16\xba\xf4\xae\xbfz\xd2',
                   b'T\x992\xd1\xf0\x85Wh\x10\x93\xed\x9c\xbe,\x97N',
                   b'\x13\x11\x1d\x7f\xe3\x94J\x17\xf3\x07\xa7\x8bM+0\xc5']
        r = uoc_expand_key(key)
        self.assertEqual(r, subkeys)

    def test_4(self):
        key = b'\x0f\x0e\x0d\x0c\x0b\x0a\x09\x08\x07\x06\x05\x04\x03\x02\x01\x00'
        subkeys = [b'\x0f\x0e\r\x0c\x0b\n\t\x08\x07\x06\x05\x04\x03\x02\x01\x00',
                   b'yrnwrxg\x7fu~b{v|c{', b'k\x89OO\x19\xf1(0l\x8fJK\x1a\xf3)0',
                   b'b,K\xed{\xddc\xdd\x17R)\x96\r\xa1\x00\xa6',
                   b'XOo:#\x92\x0c\xe74\xc0%q9a%\xd7',
                   b'\xa7pa(\x84\xe2m\xcf\xb0"H\xbe\x89Cmi',
                   b'\x9dL\x98\x8f\x19\xae\xf5@\xa9\x8c\xbd\xfe \xcf\xd0\x97',
                   b'W<\x108N\x92\xe5x\xe7\x1eX\x86\xc7\xd1\x88\x11',
                   b'\xe9\xf8\x92\xfe\xa7jw\x86@t/\x00\x87\xa5\xa7\x11',
                   b'\xf4\xa4\x10\xe9S\xcego\x13\xbaHo\x94\x1f\xef~',
                   b'\x02{\xe3\xcbQ\xb5\x84\xa4B\x0f\xcc\xcb\xd6\x10#\xb5']
        r = uoc_expand_key(key)
        self.assertEqual(r, subkeys)


class Test_2_3_Cipher(unittest.TestCase):

    def test_1(self):
        # Fips 197
        key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
        plaintext = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
        ciphertext = b'\x69\xc4\xe0\xd8\x6a\x7b\x04\x30\xd8\xcd\xb7\x80\x70\xb4\xc5\x5a'
        new_ciphertext = uoc_aes_cipher(plaintext, key)
        self.assertEqual(new_ciphertext, ciphertext)

    def test_2(self):
        key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        plaintext = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
        ciphertext = b'\xc8\xa31\xff\x8e\xdd=\xb1u\xe1T]\xbe\xfbv\x0b'
        new_ciphertext = uoc_aes_cipher(plaintext, key)
        self.assertEqual(new_ciphertext, ciphertext)

    def test_3(self):
        key = b'\x0a\x0b\x0c\x0d\x0e\x0f\x0a\x0b\x0c\x0d\x0e\x0f\x00\x00\x00\x00'
        plaintext = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
        ciphertext = b'\xb9\xb6\xaex!c\xa8/K\x15\xd12wv,\xb3'
        new_ciphertext = uoc_aes_cipher(plaintext, key)
        self.assertEqual(new_ciphertext, ciphertext)

    def test_4(self):
        key = b'\x0a\x0b\x0c\x0d\x0e\x0f\x0a\x0b\x0c\x0d\x0e\x0f\x00\x00\x00\x00'
        plaintext = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        ciphertext = b'\x90W\x89\x9eo(F\x03\x8b\xae\x13-\x99c\x03\xe0'
        new_ciphertext = uoc_aes_cipher(plaintext, key)
        self.assertEqual(new_ciphertext, ciphertext)


class Test_2_4_Decipher(unittest.TestCase):

    def test_1(self):
        # Fips 197
        key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
        plaintext = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
        ciphertext = b'\x69\xc4\xe0\xd8\x6a\x7b\x04\x30\xd8\xcd\xb7\x80\x70\xb4\xc5\x5a'
        new_plaintext = uoc_aes_decipher(ciphertext, key)
        self.assertEqual(new_plaintext, plaintext)

    def test_2(self):
        key = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        plaintext = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
        ciphertext = b'\xc8\xa31\xff\x8e\xdd=\xb1u\xe1T]\xbe\xfbv\x0b'
        new_plaintext = uoc_aes_decipher(ciphertext, key)
        self.assertEqual(new_plaintext, plaintext)

    def test_3(self):
        key = b'\x0a\x0b\x0c\x0d\x0e\x0f\x0a\x0b\x0c\x0d\x0e\x0f\x00\x00\x00\x00'
        plaintext = b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
        ciphertext = b'\xb9\xb6\xaex!c\xa8/K\x15\xd12wv,\xb3'
        new_plaintext = uoc_aes_decipher(ciphertext, key)
        self.assertEqual(new_plaintext, plaintext)

    def test_4(self):
        key = b'\x0a\x0b\x0c\x0d\x0e\x0f\x0a\x0b\x0c\x0d\x0e\x0f\x00\x00\x00\x00'
        plaintext = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        ciphertext = b'\x90W\x89\x9eo(F\x03\x8b\xae\x13-\x99c\x03\xe0'
        new_plaintext = uoc_aes_decipher(ciphertext, key)
        self.assertEqual(new_plaintext, plaintext)


if __name__ == '__main__':

    # create a suite with all tests

    # test_classes_to_run = [Test_1_1_AddRoundKey,
    #                        Test_1_2_ByteSub,
    #                        Test_1_3_ShiftRow,
    #                        Test_2_1_GenKey,
    #                        Test_2_2_ExpandKey,
    #                        Test_2_3_Cipher,
    #                        Test_2_4_Decipher]
    test_classes_to_run = [Test_1_1_AddRoundKey, Test_1_2_ByteSub, Test_1_3_ShiftRow, Test_2_1_GenKey,Test_2_2_ExpandKey, Test_2_3_Cipher]

    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_tests_suite = unittest.TestSuite(suites_list)

    # run the test suite with high verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)



