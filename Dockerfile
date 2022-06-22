FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app 
#app:app = module_name: flask_object
#The CMD command​ specifies the instruction that is to be executed when a Docker container starts