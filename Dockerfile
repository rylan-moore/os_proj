FROM arm32v7/ubuntu:latest


ADD timed_dataframe.py /

RUN apt update
RUN apt install default-jdk python3 python3-pip -y
RUN pip3 install pyspark

CMD mkdir /app
WORKDIR /app

COPY . /app/
COPY apat63_99.txt.gz cite75_99.txt.gz /app/
EXPOSE 4040
CMD cd /app && \
    python3 timed_dataframe.py 
# CMD tail -f /dev/null

