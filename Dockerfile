FROM python:3.9

COPY . .

COPY setup.sql /docker-entrypoint-initdb.d/
RUN mysql -u root -p root < /docker-entrypoint-initdb.d/setup.sql

RUN pip install -U pip
RUN pip install -r requirements.txt

