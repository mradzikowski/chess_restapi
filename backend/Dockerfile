FROM python:3.10

# Setting working directory
WORKDIR /usr/src/app

# Environmental variables related to python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
   && apt upgrade -y

# Installing dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

CMD python manage.py
