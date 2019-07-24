FROM python:2.7.16-alpine
COPY src/ /tmp
EXPOSE 8080
CMD [ "python", "./tmp/simpleserver.py" ]
