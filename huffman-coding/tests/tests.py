import unittest
import sys

sys.path.append("/Users/onuchukwu/Documents/Projects/daily-challenges/huffman-coding")

from huffman import Huffman, get_frequencies

class CompressionTestOne(unittest.TestCase):
    def setUp(self):
         with open("./tests/test-1.txt") as file:
            text =  file.read()
            h = Huffman(text)
            self.h = h
            self.text = text
            
    def test_frequency_count(self):
        self.assertEqual(3, self.h.frequencies["h"])
        self.assertEqual(4, self.h.frequencies["t"])

    def test_text_encoding(self):
        self.assertEqual("11110110010010100011110011111011001100111110000", self.h.encode())

    def test_text_decoding(self):
        decoded_text = self.h.decode(self.h.encode())
        self.assertEqual(self.text, decoded_text)
        

class CompressionTestTwo(unittest.TestCase):
    def setUp(self):
         with open("./tests/135-0.txt") as file:
            text =  file.read()
            h = Huffman(text)
            self.h = h
            self.text = text
            get_frequencies(text)

    def test_frequency_count(self):
        self.assertEqual(333, self.h.frequencies["X"])
        self.assertEqual(223000, self.h.frequencies["t"])

    def test_text_decoding(self):
        self.assertEqual(self.text, self.h.decode(self.h.encode()))
            

if __name__ == "__main__":
    unittest.main()