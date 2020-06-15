  
FROM hkarhani/p3nb:latest

MAINTAINER Hassan El Karhani <hkarhani@gmail.com>

WORKDIR /notebooks
COPY requirements.txt ./
COPY *.py ./
COPY *.ipynb ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN rm requirements.txt

ARG build_app=app.py
ENV FLASK_APP=$build_app

EXPOSE 8888
EXPOSE 5000

