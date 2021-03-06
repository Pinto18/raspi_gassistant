import unittest
import json
import requests
HOST_BASE_URL = 'http://localhost:5000/'

class ClientTestCases(unittest.TestCase):
#    def setup(self):
#        my_app.app.config['TESTING']=True
#        self.app = my_app.app.test_client()

    def test_os_api(self):
        """
        Simple Integration Test For OS Command API
        Input: GET Request to localhost:5000/reboot
        Expected: JSON returned containing 'sudo reboot' command
        """
        #response = self.app.get(HOST_BASE_URL + 'reboot')
        #data = json.loads(response.get_data(as_text=True))
        response = requests.get(HOST_BASE_URL + 'reboot')
        self.assertEqual(response.json(), {'command' : 'sudo reboot'})

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-report'))
