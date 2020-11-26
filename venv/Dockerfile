FROM python:3.7
RUN pip3 install-r requirements.txt

RUN apt install python3-pip

COPY . .


EXPOSE 5000
ENTRYPOINT ["python", "app.py"]