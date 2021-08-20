FROM python:3.8

RUN mkdir -p /opt/services/survey
WORKDIR /opt/services/survey

RUN mkdir -p /opt/services/survey/requirements

ADD requirements.txt /opt/services/survey/

COPY . /opt/services/survey/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--chdir", "src", "--bind", ":8000", "survey.wsgi:application"]