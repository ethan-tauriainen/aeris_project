FROM python:3.10.13-bookworm

COPY . /aeris_project/

WORKDIR /aeris_project/

RUN pip install --upgrade pip

ADD requirements.txt .

ADD ./dist/flaskr-1.0.0-py2.py3-none-any.whl .

RUN pip install flaskr-1.0.0-py2.py3-none-any.whl

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask"]

CMD ["--app", "flaskr", "run", "--debug", "--host", "0.0.0.0"]