import unittest
from ValidateURL import ValidateURL

class TestValidateURL(unittest.TestCase):

    def test_is_valid(self):
        self.assertTrue(ValidateURL.is_valid('https://musicasparamissa.com.br/musica/123'))
        self.assertTrue(ValidateURL.is_valid('https://www.letras.mus.br/abc'))
        self.assertFalse(ValidateURL.is_valid('https://invalidurl.com'))

    def test_get_host_name(self):
        self.assertEqual(ValidateURL.get_host_name('https://musicasparamissa.com.br/musica/123'), 'musicasparamissa')
        self.assertEqual(ValidateURL.get_host_name('https://www.letras.mus.br/abc'), 'letrasmus')
        self.assertIsNone(ValidateURL.get_host_name('https://invalidurl.com'))

if __name__ == '__main__':
    unittest.main()