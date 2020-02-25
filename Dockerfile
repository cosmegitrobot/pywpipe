FROM continuumio/miniconda3:4.7.12

RUN mkdir -p /app

ADD tests /app/tests
ADD . /app/pywpipe
WORKDIR /app
RUN pip install pytest
RUN pip install git+https://github.com/cosmegitrobot/pywpipe.git
#RUN pip install ./pywpipe
CMD ["pytest", "tests"]