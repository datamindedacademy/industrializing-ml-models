FROM python:3.9-slim

WORKDIR /app

# Upgrade pip and setuptools
RUN python -m pip install --upgrade pip && \
    python -m pip install --upgrade setuptools

# Put dependencies in their own image layer as a cache, 
# if you change code only the code layer needs to be rebuilt
COPY pyproject.toml pyproject.toml
COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

# Install the application
COPY src ./src
RUN python -m pip install . --no-cache-dir

# Define which cmd will be executed when running this image
ENTRYPOINT ["python", "-m", "titanic.main"]
