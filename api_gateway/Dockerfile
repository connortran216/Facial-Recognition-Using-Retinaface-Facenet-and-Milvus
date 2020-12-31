FROM python:3.6.8

COPY . /api
WORKDIR /api

RUN apt-get update && apt-get install -y \
	tk-dev apt-utils python3-pip tzdata locales

# create alias
RUN cd /usr/bin \
  && ln -sf python3 python \
  && ln -sf pip3 pip


RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y


#COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

RUN pip install uvicorn
RUN pip install fastapi
RUN pip install requests
RUN pip install python-multipart
EXPOSE 8888

# command to run on container start
CMD [ "python", "api_gateway.py" ]