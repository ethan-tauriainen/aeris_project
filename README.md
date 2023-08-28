# Aeris LLC Take Home Assignment
Ethan Tauriainen<br>
Denver, CO<br>
734-751-4749

## Overview
This application sets up four endpoints via Flask:
- `/data/get-sum`
- `/data/get-mean`
- `/data/get-std-deviation`
- `/data/get-image`

The endpoints may be accessed via `curl` or some other method by which API endpoints may be tested (such as `Postman`). It should be noted that this document contains instructions for manually testing the above endpoints via `curl` alone.

The application will read data from a `.csv` file, process this data and return a different result depending upon which of the above endpoints is accessed by the client.

## Pre-requisites
Users must have Docker installed. If one needs assistance in this area please follow the official instructions, which can be found here: https://docs.docker.com/engine/install/

If a user would like to run this application locally without the use of a Docker container, this is possible; however, it is advised to create a `venv` within which to build, install, and run the application. If help is desired in this area, please refer to the following documentation: https://docs.python.org/3/library/venv.html

## Build and Install
Install the build command:
```
$ pip install build
```
Find the resulting `.whl` file here: `dist/flaskr-1.0.0-py2.py3-none-any.whl` after running the following command:
```
$ python -m build --wheel
```

Install the application:
```
$ pip install ./dist/flaskr-1.0.0-py2.py3-none-any.whl
```
Install the total requirements:
```
$ pip install -r requirements.txt
```

The previous command will install all necessary dependencies. To run the app locally execute the following:
```
$ flask --app flaskr run --debug
```

## Docker Commands
#### Note: the aforementioned `flaskr-1.0.0-py2.py3-none-any.whl` file MUST be generated. The Dockerfile script relies on this file being present. Remember to execute the following commands prior to running the docker-specific commands below:
```
$ pip install build
$ python -m build --wheel
```

If you would like to run this application within a Docker container, execute the following commands from within the root of the project:
```
$ docker image build -t aeris_project .
$ docker run -p 5000:5000 -d aeris_project
```

## Testing
### Unit Tests
To run the test suite:
```
$ pytest
```

### /data/get-sum
To hit the `/data/get-sum` endpoint:
```
$ curl -v http://localhost:5000/data/get-sum
```
Expected result:
```
*   Trying 127.0.0.1:5000...                                                                                                                                                                
* Connected to localhost (127.0.0.1) port 5000 (#0)                                                                                                                                         
> GET /data/get-sum HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.7 Python/3.10.13
< Date: Sun, 27 Aug 2023 17:34:39 GMT
< Content-Type: application/json
< Content-Length: 36
< Connection: close
<
{
  "sum": "0.000137476137616907"
}

```
### /data/get-mean
To hit the `/data/get-mean` endpoint:
```
$ curl -v http://localhost:5000/data/get-mean
```
Expected result:
```
*   Trying 127.0.0.1:5000...
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /data/get-mean HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.7 Python/3.10.13
< Date: Sun, 27 Aug 2023 17:38:47 GMT
< Content-Type: application/json
< Content-Length: 38
< Connection: close
< 
{
  "mean": "1.414363555729496e-07"
}
```

### /data/get-std-deviation
To hit the `/data/get-std-deviation` endpoint:
```
$ curl -v http://localhost:5000/data/get-std-deviation
```
Expected result:
```
*   Trying 127.0.0.1:5000...
* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /data/get-std-deviation HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.7 Python/3.10.13
< Date: Sun, 27 Aug 2023 17:42:29 GMT
< Content-Type: application/json
< Content-Length: 48
< Connection: close
< 
{
  "std-deviation": "4.5936824115977264e-07"
}
```

### /data/get-image
To hit the `/data/get-image` enpoint:
```
$ curl -v http://localhost:5000/data/get-image -o data.png
```
Expected result:
```
*   Trying 127.0.0.1:5000...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Connected to localhost (127.0.0.1) port 5000 (#0)
> GET /data/get-image HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.3.7 Python/3.10.13
< Date: Sun, 27 Aug 2023 17:46:12 GMT
< Content-Disposition: inline; filename=data.png
< Content-Type: image/png
< Content-Length: 192705
< Last-Modified: Sun, 27 Aug 2023 17:46:12 GMT
< Cache-Control: no-cache
< ETag: "1693158372.7699256-192705-3010071432"
< Date: Sun, 27 Aug 2023 17:46:12 GMT
< Connection: close
< 
{ [8192 bytes data]
100  188k  100  188k    0     0   645k      0 --:--:-- --:--:-- --:--:--  646k
```
Ensure the file downloaded successfully:
```
$ ls
data.png
```
