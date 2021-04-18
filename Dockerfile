FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install -r requirements.txt
RUN pip install -e .
COPY . .
ENV DATABASE="app/data/message.db"
CMD ["app.py"]
ENTRYPOINT ["python3"]

