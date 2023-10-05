# pull official base image
FROM python:3.10-slim as base

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt-get install gcc build-essential -y

# install dependencies
# Install poetry:
RUN pip3 install poetry && \
    poetry config virtualenvs.create false


# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

RUN poetry lock --no-update && \
    poetry install --only main

EXPOSE 8080

#CMD ["sh", "-c", "make run_prod"]
ENTRYPOINT ["./entrypoint.sh"]