FROM python:3.8.1-alpine

COPY . .

ENV FLASK_APP mini_todo

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b 0.0.0.0:8080", "mini_todo:app"]
