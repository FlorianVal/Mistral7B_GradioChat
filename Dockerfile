FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ARG API_URL
ARG MODEL

ENV API_URL=$API_URL
ENV MODEL=$MODEL

CMD ["python", "app.py"]