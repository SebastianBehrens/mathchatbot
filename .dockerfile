FROM python:3.12

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD main.py .
ADD .env .

ADD exercises/ ./exercises
ADD logs/ ./logs
ADD cache/ ./cache
ADD configs/ ./configs
ADD scripts/ ./scripts

WORKDIR .


CMD ["python", "./main.py"]
