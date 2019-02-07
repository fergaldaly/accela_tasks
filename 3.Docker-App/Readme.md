# Overview

### Python Flask-based Hello World Docker container;

1. Build the docker image. From the root of the repo:
        `docker build -t fdaly_docker_app .\3.Docker-App`

2. Run it: 			
    `docker run -p 5000:5000 fdaly_docker_app`

3. Connect to http://localhost:5000/

4. Add any name to the URL for a personalised greeting, e.g. http://localhost:5000/Fergal