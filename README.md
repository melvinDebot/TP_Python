
# TP PYTHON

Create a db capable of receiving scrapper values and then design an api capable of interacting with the db : it should be able to ingest / read / update / delete.
Make two test modules
One to check that your script can send the scrapper data to the api and a second one to test that the api can send / read / delete / update / the data
in the database


## Running File

To run file, run the following command

```python
  python3 scrapper.py
```

## scrapping data example

```python
stocks_brut = soup.findAll("p", {'class': "instock availability"})
stocks = [stock.text for stock in stocks_brut]
for i in stocks:
    li_stock = [i.strip('\n ') for i in stocks]
len(li_stock)
```
## API Reference

#### Get all items

```http
  GET http://192.168.1.21:8080/list
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `port` | `string` | **Required**. Your IP |

#### Get item

```http
  POST http://192.168.1.21:8080/add
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `port` | `string` | **Required**. Your IP |

#### Put item

```http
  PUT http://192.168.1.21:8080/update
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `port` | `string` | **Required**. Your IP |

#### Delete item

```http
  DELETE http://192.168.1.21:8080/delete/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `port` | `string` | **Required**. Your IP |



Takes two numbers and returns the sum.

## Test unitaire example

```python
  class Test_Scrappe(unittest.TestCase):
    def setUp(self):
        self.fake_data_scrappe = {'title': 'melvin', 'statut': True}

    
    def get_call_api(self):
        create()
        self.assertTrue(self.fake_data_scrappe['statut'], True)
```
## Tech Stack

**Server:** Python

**Database:** Firebase

## Authors

- [@melvinDebot](https://github.com/melvinDebot?tab=repositories)


