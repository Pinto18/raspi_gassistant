import unittest
import json
HOST_BASE_URL = 'localhost:5000/'

class ClientTestCases(unittest.TestCase):
    def setup(self):
        my_app.app.config['TESTING']=true
        self.app = my_app.app.test_client()

    def test_os_api():
        """
        Simple Integration Test For OS Command API
        Input: GET Request to localhost:5000/reboot
        Expected: JSON returned containing 'sudo reboot' command
        """
        response = self.client.response(HOST_BASE_URL + 'reboot')
        self.assertIn('reboot', response)
