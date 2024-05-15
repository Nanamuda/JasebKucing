FROM nikolaik/python-nodejs:python3.10-nodejs19

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir -U -r req.txt

CMD bash run
