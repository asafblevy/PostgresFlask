FROM python:3.8
LABEL "Maintainer"="Asaf Bein Levy"
LABEL version="1.0.0"
LABEL description="Simple flask application"

EXPOSE 80
RUN mkdir /app
WORKDIR /app
ADD app/ .
RUN pip install -r requirements.txt

CMD ["python", "/app/app.py"]