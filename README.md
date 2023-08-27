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

The previous command will install all necessary dependencies. To run the app locally execute the following:
```
$ flask --app flaskr run --debug
```

## Testing
To run the test suite:
```
$ pytest
```

## Docker Commands
If you would like to run this application within a Docker container, execute the following commands from within the root of the project:
```
$ docker image build -t aeris_project .
$ docker run -p 5000:5000 -d aeris_project
```
