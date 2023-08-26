# aeris_project
Take home project assignment for Ethan Tauriainen.

## Build and Install
Find the resulting `.whl` file here: `dist/flaskr-1.0.0-py2.py3-none-any.whl`
```
$ pip -m build --wheel
```

Install the application:
```
$ pip install flaskr-1.0.0-py2.py3-none-any.whl
```

## Docker Commands
```
$ docker image build -t aeris_project .
$ docker run -p 5000:5000 -d aeris_project
```
