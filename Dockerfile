FROM python:alpine
RUN apk update && apk upgrade
WORKDIR /APP
COPY . ./ 
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","flask_server.py"]
