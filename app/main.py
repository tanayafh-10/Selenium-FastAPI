from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Selenium + FastAPI is running!"}

@app.get("/run-test")
def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "113.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities,
        options=chrome_options
    )

    driver.get("https://example.com")
    title = driver.title
    driver.quit()
    return {"title": title}

