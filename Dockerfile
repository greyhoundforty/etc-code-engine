FROM python:3.10.10-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
COPY . .
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION python
CMD [ "python", "./main.py" ]
