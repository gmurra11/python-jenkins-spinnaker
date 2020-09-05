FROM alpine:3.7

RUN apk add --no-cache python3 curl -y
RUN pip3 install Flask, PrometheusMetrics

COPY . /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python3", "./python-ptds.py" ]
