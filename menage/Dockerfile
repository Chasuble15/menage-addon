FROM python:3.11-slim

RUN pip install flask

COPY run.sh /run.sh
COPY webserver.py /webserver.py
COPY storage.json /storage.json.template
RUN chmod +x /run.sh

CMD ["/run.sh"]