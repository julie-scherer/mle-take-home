FROM python:3.10

RUN pip3 install --upgrade pip

WORKDIR /mle-take-home

COPY ./requirements.txt /mle-take-home/requirements.txt

RUN pip3 install --no-cache-dir -r /mle-take-home/requirements.txt

COPY ./app /mle-take-home/app
COPY ./run.py /mle-take-home

EXPOSE "5000"

CMD ["python3", "run.py", "--host", "0.0.0.0", "--port", "5000"]