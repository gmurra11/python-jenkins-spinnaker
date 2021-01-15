FROM alpine:3.7

RUN apk upgrade --no-cache \
  && apk add --no-cache \
  python3 \
  curl -y

RUN pip3 install Flask prometheus_flask_exporter --no-cache-dir --upgrade pip \
&& rm -rf /var/cache/* \
&& rm -rf /root/.cache/*

COPY . /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python3", "./python-ptds.py" ]
