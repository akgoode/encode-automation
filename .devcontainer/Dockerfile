FROM mcr.microsoft.com/devcontainers/python

WORKDIR /code/

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src