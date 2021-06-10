## Environment:
- Python version: 3.7
- Django version: 3.0.6
- Django REST framework version: 3.11.0

## Description
API to enable create and fetch informations on weather of a certain city, with details of latitude, longitude and temperature.

## Data:
Example of a weather data JSON object:
```
{
   "id": 1,
   "date": "1985-01-01",
   "lat": 36.1189,
   "lon": -86.6892,
   "city": "Nashville",
   "state": "Tennessee",
   "temperatures": [17.3, 16.8, 16.4, 16.0, 15.6, 15.3, 15.0, 14.9, 15.8, 18.0, 20.2, 22.3, 23.8, 24.9, 25.5, 25.7, 24.9, 23.0, 21.7, 20.8, 29.9, 29.2, 28.6, 28.1]
}
```

## Methods:

POST request to `/weather/`:

- creates a new weather data record
- expects a valid weather data object as its body payload

GET request to `/weather/`:

- returns an array of matching records, ordered by their ids in increasing order
- accepts an optional query string parameter, date, in the format YYYY-MM-DD, for example /weather/?date=2019-06-11
- accepts an optional query string parameter, city. Case insensitive, so "London" and "london" are equivalent. Moreover, it might contain several values, separated by commas (e.g. city=london,Moscow),
- accepts an optional query string parameter, sort, that can take one of two values: either "date" or "-date". If the value is "date", then the ordering is by date in ascending order. If it is "-date", then the ordering is by date in descending order. If there are two records with the same date, the one with the smaller id must come first.


GET request to `/weather/<id>/`:

- returns a record with the given id
