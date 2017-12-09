FROM ubuntu:latest 
WORKDIR /code
COPY . /code
RUN apt-get update -y \
    && apt-get install -y python-pip \
	python-dev \
	build-essential \	
    && pip install -r requirements.txt
CMD ["python", "raspi_os_commands.py"]
