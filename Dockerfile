FROM python:3.10-alpine

COPY . /aeris_project/

WORKDIR /aeris_project/

COPY ./dist/flaskr-1.0.0-py2.py3-none-any.whl /aeris_project/flaskr-1.0.0-py2.py3-none-any.whl

RUN pip install flaskr-1.0.0-py2.py3-none-any.whl

EXPOSE 5000

ENTRYPOINT ["flask"]

CMD ["--app", "flaskr", "run", "--debug", "--host", "0.0.0.0"]