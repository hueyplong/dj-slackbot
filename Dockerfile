FROM python:3.6-slim

# Setup application working directory and copy the code
WORKDIR /app/
ADD . /app/

# Install dependencies and requirements
RUN set -ex \
    && DEPENDENCIES=" \
        python3-dev \
        default-libmysqlclient-dev \
        build-essential \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $DEPENDENCIES \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "--settings=settings.dev"]