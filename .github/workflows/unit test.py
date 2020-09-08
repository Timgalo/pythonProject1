 import unittest
 import unittest

 
 class TestProject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')


    def test_Get(self):
       with patch('project.requests.get') as mocked_get:
           mocked_get.return_value.ok = True
           mocked_get.return_value.text = 'Success!'

if __name__ == '__main__':
    unittest.main()
