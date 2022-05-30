FROM ufoym/deepo:pytorch-py38-cpu as base

COPY . /app
RUN pip3 install -r /app/api/requirements.txt

WORKDIR /app/

CMD [ "python3", "api/main.py" ]