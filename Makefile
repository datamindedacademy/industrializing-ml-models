CONTAINER_IMAGE = titanic-survival-predictor:v1
S3_BUCKET = industrializing-ml-models

requirements:
	. .venv/bin/activate && \
	pip-compile --output-file=requirements.txt pyproject.toml && \
	pip-compile --extra=dev --constraint=requirements.txt --output-file=dev-requirements.txt pyproject.toml && \
	pip install -r requirements.txt && \
	pip install -r dev-requirements.txt && \
	pip install --editable .

format:
	. .venv/bin/activate && \
	black src tests && \
	isort src tests

test:
	. .venv/bin/activate && \
	pytest tests

notebook:
	. .venv/bin/activate && \
	jupyter-lab

container.build:
	docker build . --tag $(CONTAINER_IMAGE)

container.run:
	docker run --env-file=.env $(CONTAINER_IMAGE) \
		--bucket=$(S3_BUCKET) \
		--train=titanic/train.csv \
		--test=titanic/test.csv \
		--output=titanic/results.csv

tracking.start:
	. .venv/bin/activate && \
	mlflow server --port 5001
