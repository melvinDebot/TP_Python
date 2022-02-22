
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
  GET /list
```

#### Get item

```http
  POST /add
```

#### Put item

```http
  PUT /update
```

#### Delete item

```http
  DELETE /delete
```

## Running Test

To run test, run the following command

```python
  python3 scrapper_test.py
```

## Test unitaire example

```python
  def test_read_api(self):
    with app.test_client() as client:
      # send data as POST form to endpoint
      sent = {"note": "One", "test": "53.74", "stock": "7"}
      result = client.get(
        '/list',
        data=sent 
      )
      # check result from server with expected data
      print(json.dumps(sent))
      self.assertEqual(
        result.data,
        json.dumps(sent)
      )
```
## Tech Stack

**Server:** Python

**Database:** Firebase

## Authors

- [@melvinDebot](https://github.com/melvinDebot?tab=repositories)


