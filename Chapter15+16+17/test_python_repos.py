import unittest
import requests
from python_repos import return_status_code


class MyTestCase(unittest.TestCase):
    def test_something(self):
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        r = requests.get(url)
        return_code = return_status_code(r)
        self.assertEqual(return_code, 200)


if __name__ == '__main__':
    unittest.main()
