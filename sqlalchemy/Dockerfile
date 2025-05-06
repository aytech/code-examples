FROM python:3.9-slim
WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY models /app/models
COPY main.py /app/main.py

CMD ["tail", "-f", "/dev/null"]
#CMD [ "python", "main.py" ]