# Dockerfile to build a flask app
FROM python:3.10.0

WORKDIR /app 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .

CMD [ "python", "-m", "flask", "run"]
