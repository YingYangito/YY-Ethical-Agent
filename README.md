# YY - Ethical AI Agent
YY is an autonomous AI agent that scans world news, generates Binglish-style commentary, and posts to X (Twitter).

## Features
- Web scraping news (BeautifulSoup)
- Generating commentary with OpenAI's GPT API
- Browser automation with Selenium
- Automated posting to Twitter
- Binglish writing style

## Setup
1. Create a virtual environment and install dependencies:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
2. Update `src/config.py` with your OpenAI API key.

## Running
python src/agent.py
Or schedule via Task Scheduler using `run_yy.bat`.

## License
MIT
