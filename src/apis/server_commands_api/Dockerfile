FROM alpine:3.4 
WORKDIR /code
COPY . /code
RUN apk add --update \
	python \
   	py-pip \
    && pip install -r requirements.txt
CMD ["python", "raspi_os_commands.py"]
