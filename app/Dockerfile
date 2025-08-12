FROM python:3.13


WORKDIR /application


COPY ./requirements.txt /application/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /application/requirements.txt


COPY . /application


CMD ["python3", "main.py"]