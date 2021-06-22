bash:
	docker-compose run --rm ecommerce_api_web /bin/bash

bash_test:
	docker-compose -f docker-compose-testing.yml run --rm ecommerce_api_web_testing /bin/bash

black:
	docker-compose run --rm ecommerce_api_web black --line-length=79 --target-version py37 ecommerce_api

build:
	docker-compose build --no-cache

build_test:
	docker-compose -f docker-compose-testing.yml build --no-cache

clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete
	@find . -name ".pytest_cache" -exec rm -rf {} \;

check:
	docker-compose run --rm ecommerce_api_web bash -c "black --line-length=79 --target-version py37 ecommerce_api --check && flake8 ecommerce_api"

run:
	docker-compose up

stop:
	docker-compose stop

stop_all:
	bash -c "docker-compose stop && docker-compose -f docker-compose-testing.yml stop"

test:
	docker-compose -f docker-compose-testing.yml run --rm ecommerce_api_web_testing pytest

test_cov:
	docker-compose -f docker-compose-testing.yml run --rm ecommerce_api_web_testing pytest --cov-report html:cov_html --cov=ecommerce_api -v ecommerce_api/tests/

proto:
	python -m grpc_tools.protoc --python_out=ecommerce_api/core/discount/ --grpc_python_out=ecommerce_api/core/discount/ --proto_path=ecommerce_api/core/discount/proto/ ecommerce_api/core/discount/proto/*.proto
