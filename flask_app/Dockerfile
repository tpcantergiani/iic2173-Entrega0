FROM python:3.8.10

WORKDIR /python-flask

COPY ./requirements.txt ./

RUN apt-get update -y

RUN apt install libgl1-mesa-glx -y

RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

RUN pip install -r requirements.txt

COPY ./ ./

# CMD ["python3", "run.py"]
# CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "run:app"]