import unittest
import python_repos
import requests
import json

class PythonReposTestCase(unittest.TestCase):
    """Class to test code in python_repos."""

    def setUp(self):
        """Creates and stores a call."""
        url = 'http://api.github.com/search/repositories?q=language:python&sort:stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        self.r = requests.get(url, headers=headers)
        self.response_dict = self.r.json()
        
    def test_status_code_200(self):
        """Verifies that the response status code is 200."""
        status_code = self.r.status_code
        self.assertEqual(status_code, 200)

    def test_total_repositories(self):
        """Verifies that the amount of total repositories is larger than 1 m."""
        total_count = self.response_dict['total_count']
        self.assertGreater(total_count, 1_000_000)

    def test_returned_repositories(self):
        """Verifies that the amount of returned repositories is 30."""
        returned_repos = len(self.response_dict['items'])
        self.assertEqual(returned_repos, 30)

if __name__ == '__main__':
    unittest.main()