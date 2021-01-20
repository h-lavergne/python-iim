FROM python:3.6
RUN mkdir /usr/src/api/
COPY . /usr/src/api/
WORKDIR /usr/src/api/
EXPOSE 5000
RUN pip install -r requirements.txt
RUN pip install redis
CMD ["python", "api.py"]