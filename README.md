# WebScrapper-2.0
This project is an AI-powered web scraper that automates the extraction of data from websites. It uses Selenium and BeautifulSoup for scraping and cleaning website content, and LangChain’s OllamaLLM to extract specific information based on user-provided descriptions. The project is designed to handle CAPTCHA challenges and large datasets efficiently.

## Features

- Automated website content scraping.
- CAPTCHA handling for secure websites.
- Cleans and processes HTML content for structured data extraction.
- Custom parsing logic based on user-provided descriptions to extract relevant information.
- Built to handle large datasets with efficient data parsing.

## Tech Stack

- **Python**
- **Selenium**: Used for automating browser interactions and handling dynamic web content.
- **BeautifulSoup**: Used for parsing and cleaning HTML content.
- **LangChain's OllamaLLM**: Used for processing and extracting structured data from content.
- **Streamlit**: For creating a simple user interface to input URLs and extract data.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Average-Chief/WebScrapper-2.0.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ai-powered-web-scraper
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. **Install ChromeDriver**:  
   Ensure you have ChromeDriver installed and that it is compatible with your version of Google Chrome. You can download it from [ChromeDriver Download](https://chromedriver.chromium.org/downloads). Make sure to add it to your system's PATH.

## Usage

1. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

2. Run the application:
    ```bash
    streamlit run main.py
    ```

3. Open the Streamlit app in your browser, enter the URL of the website you want to scrape, and provide a description of the information you want to extract.
