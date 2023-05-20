FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install pip --upgrade \
    && pip install -r requirements.txt
COPY . .
