FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3.8 python3-pip

COPY ./pythonMailApi /app
WORKDIR /app

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

