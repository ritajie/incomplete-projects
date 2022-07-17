FROM rackspacedot/python37

LABEL maintainer="1551755561@qq.com"

COPY ./requirements.txt /requirements.txt

RUN apt update
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 1236

COPY . /root/incomplete_projects/

WORKDIR /root/incomplete_projects/

CMD ["/bin/bash", "bin/run.sh"]
