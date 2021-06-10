from json.decoder import JSONDecodeError

from django.test import TestCase
from rest_framework.test import RequestsClient
from rest_framework import status
import json

chicago = {
    'date': '2019-06-11',
    'lat': 41.8818,
    'lon': -87.6231,
    'city': 'Chicago',
    'state': 'Illinois',
    'temperatures': [24.0, 21.5, 24.0, 19.5, 25.5, 25.5, 24.0, 25.0, 23.0, 22.0, 18.0, 18.0, 23.5, 23.0, 23.0, 25.5, 21.0, 20.5, 20.0, 18.5, 20.5, 21.0, 25.0, 20.5],
}

oakland = {
    "date": "2019-06-12",
    "lat": 37.8043,
    "lon": -122.2711,
    "city": "Oakland",
    "state": "California",
    "temperatures": [24.0, 36.0, 28.5, 29.0, 32.0, 36.0, 28.5, 34.5, 30.5, 31.5, 29.5, 27.0, 30.5, 23.5, 29.0, 22.0, 28.5, 32.5, 24.5, 28.5, 22.5, 35.0, 26.5, 32.5],
}

london = {
    "date": "2019-03-12",
    "lat": 51.5098,
    "lon": -0.1180,
    "city": "London",
    "state": "N/A",
    "temperatures": [11.0, 11.0, 5.5, 7.0, 5.0, 5.5, 6.0, 9.5, 11.5, 5.0, 6.0, 8.0, 9.5, 5.0, 9.0, 9.5, 12.0, 6.0, 9.5, 8.5, 8.0, 8.0, 9.0, 6.5]
}

moscow1 = {
    "date": "2019-03-12",
    "lat": 55.7512,
    "lon": 37.6184,
    "city": "Moscow",
    "state": "N/A",
    "temperatures": [-2.0, -4.5, 1.0, -6.0, 1.0, 1.5, -9.0, -2.5, -3.0, -0.5, -13.5, -9.0, -11.5, -5.5, -5.5, -3.5, -14.0, -9.5, 1.5, -15.0, -6.5, -7.0, -13.5, -14.5]
}

moscow2 = {
    "date": "2018-03-12",
    "lat": 55.7512,
    "lon": 37.6184,
    "city": "Moscow",
    "state": "N/A",
    "temperatures": [-13.5, -15.5, -9.5, -19.5, -9.0, -18.0, -12.5, -18.5, -20.0, -7.0, -19.5, -17.0, -15.5, -12.0, -20.0, -14.0, -18.5, -20.0, -7.5, -14.5, -14.0, -11.0, -13.5, -11.0]
}

moscow_invalid = {
    "date": "2018-03-12",
    "lat": 5555.7512,
    "lon": 37.6184,
    "city": "Moscow",
    "state": "N/A",
    "temperatures": [-13.5, -15.5, -9.5, -19.5, -9.0, -18.0, -12.5, -18.5, -20.0, -7.0, -19.5, -17.0, -15.5, -12.0, -20.0, -14.0, -18.5, -20.0, -7.5, -14.5, -14.0, -11.0, -13.5, -11.0]
}

HOST = 'http://localhost:8000'

class WeatherEndpointWithPOSTTestCase(TestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.url = HOST + '/weather/'
        self.headers = headers = {
          'Content-Type': 'application/json'
        }
        
    def test_with_valid_data(self):
        payload = json.dumps(chicago) #i'm assuming the sender apllication can do this
        # r = requests.request("POST", self.url, headers=self.headers, data=payload)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        data = r.json()
        self.assertIn('id', data)
        self.assertIsInstance(data['id'], int)
        del data['id']
        
    def test_with_invalid_data(self):
        payload = json.dumps(moscow_invalid)
        r = requests.request("POST", self.url, headers=self.headers, data=payload)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        error_message = {'lat': ['Ensure that there are no more than 6 digits in total.']}
        self.assertEqual(r.json(), error_message)

# class WeatherEndpointWithGETSingleTestCase(TestCase):

#     def setUp(self):
#         self.client = RequestsClient()
#         self.url = HOST + '/weather/'ipty
#         try:
#             self.chicago = self.client.post(self.url, data=chicago).json()
#         except JSONDecodeError:
#             self.fail("/weather endpoint for POST request not implemented")

#     def test_with_existing_record(self):
#         r = self.client.get(self.url)
#         data = r.json()
#         self.assertEqual(r.status_code, status.HTTP_200_OK)
#         self.assertIn(chicago, data)

#     def test_with_non_existing_record(self):
#         # implement the rest of the test
#         raise NotImplementedError()


# def compare_payloads(response_payload, request_payload):
