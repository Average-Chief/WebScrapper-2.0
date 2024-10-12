from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

#add your Bright Data Web Socket link here
SBR_WebDriver = "***************************************************************"
def scrape_website(website):
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WebDriver, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html

def extract_body(html_content):
    soup = BeautifulSoup(html_content,'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,'html.parser')
    for script_style in soup(["script","style"]):
        script_style.extract()
    clean_content = soup.get_text(separator="\n")
    clean_content = "\n".join(line.strip() for line in clean_content.splitlines() if line.strip())
    return clean_content

def split_content(dom_content,max_length =6000):
    return [dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)]

