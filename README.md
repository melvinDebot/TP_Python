
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

#### GET all items
`GET /list`
#### Request
```json
  [
    {
        "note": "One",
        "price": "50.10",
        "stock": "In stock",
        "title": "Soumission"
    },
    {
        "note": "six",
        "price": "42.80",
        "stock": "inStock",
        "title": "Max"
    },
]
```

#### POST item
`POST /add`
#### Request
```json
  {
        "note": "huit",
        "price": "50.10",
        "stock": "In stock",
        "title": "test"
    },
```

#### Put item

`PUT /update`
#### Request
```json
  {
        "note": "huit",
        "price": "50.10",
        "stock": "In stock",
        "title": "test568"
    },
```

#### Delete item
delete() : Delete a document from Firestore collection

## Running Test

To run test, run the following command

```python
  python3 scrapper_test.py
```

## Test unitaire example

```python
  def test_get_api(self):
        with app.test_client() as client:
            result = client.get(
                '/list',
            )
            # Check the status of the call if it is a 200
            self.assertEqual(result.status_code, 200)
```
## Tech Stack

**Server:** Python

**Database:** Firebase

## Authors

- [@melvinDebot](https://github.com/melvinDebot?tab=repositories)


