
FROM python:3.8-slim-buster

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /myapp

COPY requirements.txt /myapp/

RUN pip3 install -r requirements.txt

COPY . .

RUN python3 manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]