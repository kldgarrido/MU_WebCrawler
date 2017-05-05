import unittest
from core import count_words, validate_word, validate_words
import pandas as pd

class TestCoreMethods(unittest.TestCase):

    def test_validate_words(self):
        exp_result = ['hola']

        words = ['hola', '*/$23 23']
        result= validate_words(words)

        self.assertEqual(exp_result, result)



    def test_validate_word(self):
        word = '*/$23 23'
        self.assertFalse(validate_word(word))

        word = '314159'
        self.assertFalse(validate_word(word))

        word = 'hola'
        self.assertTrue(validate_word(word))


    def test_count_words(self):
        words = 'hello world hello'

        data = {'frecuency': [2 , 1]}
        unique = ['hello','world']
        exp_result = pd.DataFrame(data, index=unique)
        result = count_words(words.split(' '))

        self.assertEqual(exp_result['frecuency'].tolist(), result['frecuency'].tolist())



if __name__ == '__main__':
    unittest.main()