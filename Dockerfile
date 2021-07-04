FROM python:3.8

ADD telbot.py .

RUN pip install python-telegram-bot

CMD ["python", "./telbot.py"]