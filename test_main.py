import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello(self):
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'hello': 'world'})
        
        
    def test_hello_name(self):
        response = self.app.get('/api/hello/ben')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'hello': 'ben'})
        
        #def test_classify(self):
        #response = self.app.get('/classify/[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,82,198,185,213,205,198,197,186,159,134,111,85,86,76,28,0,0,0,0,0,0,0,0,0,0,0,10,0,62,255,249,251,249,248,250,248,243,244,243,237,229,229,110,0,0,0,0,0,0,0,0,0,0,0,9,0,38,241,234,235,231,230,228,223,221,224,216,210,204,198,22,0,0,0,0,0,0,0,0,0,0,0,4,0,36,242,232,235,237,235,234,235,237,234,219,213,211,214,0,0,0,0,0,0,0,0,0,0,0,0,4,0,37,242,234,234,230,225,220,224,226,212,212,204,219,189,0,0,0,0,0,0,0,0,0,0,0,0,4,0,37,242,231,229,226,226,223,223,237,224,220,205,226,177,0,0,0,0,0,0,0,0,0,0,0,0,4,0,31,240,231,230,225,231,230,220,234,214,204,206,230,177,0,0,0,0,0,0,0,0,0,0,0,0,5,0,84,242,222,223,248,232,225,228,224,213,217,217,228,178,0,0,0,0,0,0,0,0,0,0,0,0,2,0,151,247,219,210,124,245,232,217,213,221,225,223,193,220,0,0,0,0,0,0,0,0,0,0,0,0,5,0,107,244,233,197,61,235,222,219,224,215,209,199,203,255,69,0,0,0,0,0,0,0,0,0,0,0,1,0,7,236,229,222,236,229,217,225,226,227,235,227,225,216,169,0,0,0,0,0,0,0,0,0,0,1,0,0,168,240,230,236,233,222,222,226,229,238,244,237,220,203,227,0,0,0,0,0,0,0,0,0,0,5,0,63,255,217,221,209,239,233,227,231,239,240,238,219,183,192,239,47,0,0,0,0,0,0,0,0,0,3,0,42,234,214,227,44,174,242,228,232,238,234,225,185,156,201,232,78,0,0,0,0,0,0,0,0,0,0,0,30,229,222,218,164,216,221,223,237,235,227,210,206,232,215,237,78,0,0,0,0,0,0,0,1,4,0,7,253,239,219,238,240,226,214,234,234,222,224,239,244,226,232,232,15,0,0,0,0,0,2,2,0,3,0,66,247,225,234,237,240,232,230,241,239,232,247,227,190,197,137,27,0,0,0,0,0,0,1,0,1,6,0,41,234,234,181,44,246,238,239,239,235,238,204,190,200,196,81,58,0,0,0,0,0,0,0,0,0,0,0,142,240,234,192,135,247,230,242,238,219,200,213,185,215,210,255,181,0,0,0,0,0,0,3,1,1,0,28,255,236,252,249,253,234,239,239,224,198,239,73,160,225,204,207,116,0,0,0,0,6,0,0,0,0,0,199,255,187,154,249,231,238,236,220,199,255,44,0,200,221,201,211,97,0,0,0,0,0,0,0,36,110,208,201,206,88,126,254,222,230,221,199,245,82,0,6,196,207,201,207,64,0,0,0,0,10,145,200,222,215,167,190,195,233,255,225,220,220,205,245,165,0,0,8,202,207,200,236,37,0,0,0,46,215,237,224,217,217,207,209,211,232,224,226,231,221,211,234,0,0,0,0,185,211,198,236,27,0,0,0,137,254,229,232,235,232,233,229,227,228,230,232,224,209,255,57,0,0,0,0,163,211,197,194,3,0,0,0,0,116,210,242,249,251,255,252,243,242,238,232,234,255,118,0,0,1,0,30,251,213,216,248,4,0,0,0,0,0,0,10,46,65,111,139,171,178,187,198,180,61,0,0,0,0,0,0,157,194,174,141,0,0,0]')
        #self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.json, {"label": "t-shirt", "prediction": 0})
if __name__ == '__main__':
    unittest.main()
