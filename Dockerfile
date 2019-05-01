FROM alpine
LABEL maintener="mateusfrancofs3@gmail.com"
RUN apk update && apk upgrade && \\
apk add mariadb-dev && apk add py-pip && apk add python-dev && apk add build-base
RUN mkdir project
WORKDIR /project
COPY . /project
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
