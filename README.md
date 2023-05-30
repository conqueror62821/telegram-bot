# Telegram Bot Scraper

The project consists of a Telegram bot that interacts with the user through custom commands defined by the user and is able to provide useful information using scraping techniques.

## Requirements

- Python (3.11.3)
- Docker (optional, for running in a container)
## Environment variables

- Create two environment variable configuration files named .env.dev and .env.prod, using the template.env file as a reference

## Installation without docker

- 1. Clone the repository:

```bash
    git clone https://github.com/4lequinn/telegram-bot-scraper.git
```
- 2. Go to project path:

```bash
    cd project-name-path
```
- 3. Virtual environment:

```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
```

- 4. Install requirements:

```bash
    pip install -r docker/development/requirements.txt
```

## Usage

- 1. Run app
```bash
    python app/main.py
```

## Usage with Docker (optional)
- 1. Run docker compose:

```bash
    docker compose up --build
```

## Server

- 2. Open your web browser and access http://localhost:8000 to interact with the application.

## Contribution

If you want to contribute to this project, follow these steps:

- 1. Fork the repository.
- 2. Create a branch for your contribution: git checkout -b feature/new-feature.
- 3. Make your modifications and commit the changes: git commit -am 'Add new feature'.
- 4. Push to your repository: git push origin feature/new-feature.
- 5. Open a pull request in the original repository.

## Credits
- Author: Jorge Quintui
