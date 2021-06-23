# e-commerce API
An API do process cart products.

## Requirements

* [Docker](https://www.docker.com/get-started)
* [Docker-Compose](https://docs.docker.com/compose/install/)

## Running local

```
make run
```

Then, the api will be available at [http://localhost:5000](http://localhost:5000).


## Code Style

The project adopts [black](https://github.com/psf/black) and [flake8](https://flake8.pycqa.org/en/latest/) to keep a consistent code style. The commands you might to know in advance:

**Format code:**

```
make black
```

**Check code style:**

```
make check
```

## Configuration

If you need to change/add env vars, check `env/` directory.

## Tests

You can run all tests at once...

```
make test
```

...and obtain a coverage report:

```
make test_cov
```

## Useful Commands

Useful commands are available at [Makefile](./Makefile).

## Endpoints

**Authorization:**

All endpoints requires an Api Key. The [development.env](env/development.env) file configures one for local environment.

**Response:**

In order to ease the integration process, all responses follow the same template:


```
{
    "code": null,
    "data": { ... },
    "message": null,
    "success": true
}
```

#### Process Cart

```
POST /api/v1/cart/
Content-Type: application/json
X-API-KEY: Apikey <api-key>
{
	"products": [
		{
			"id": 1,
			"quantity": 2
		},
		{
			"id": 2,
			"quantity": 2
		}
	]
}
```

For example:

```
curl --request POST \
  --url http://localhost:5000/api/v1/cart/ \
  --header 'Content-type: application/json' \
  --header 'X-API-KEY: Apikey QMlX5CPNCqUmjeAM9ISw' \
  --data '{
	"products": [
		{
			"id": 1,
			"quantity": 2
		},
		{
			"id": 2,
			"quantity": 2
		}
	]
}'
```
