#Base image, Python 3
FROM python:3 

#Copy our server files
COPY hello.py /
COPY requirements.txt /

#Install our prereqs
RUN pip install -r requirements.txt

#Run the server on startup
EXPOSE 5000
CMD ["python", "hello.py"]