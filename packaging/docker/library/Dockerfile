FROM python:3.12.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /library/
WORKDIR /library/
COPY ./src/library/ /library/

RUN adduser --disabled-password --gecos "" django
RUN chown -R django:django /library/

USER django
