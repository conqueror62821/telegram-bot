FROM python:3.11.3
WORKDIR /app
COPY requirements.txt .
RUN pip install pip --upgrade \
    && pip install -r requirements.txt
COPY . .
