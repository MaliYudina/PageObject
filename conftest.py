import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, fr, zh-ch, es or others")


@pytest.fixture(scope="function")
def browser(request):
    chrome_path = r'/Users/Mali/Downloads/chromedriver'
    # pdb.set_trace()
    language = request.config.getoption('language')
    if language == "ru":
        print("\nStart chrome languages ru for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        browser = webdriver.Chrome(options=options, executable_path=chrome_path)
    elif language == "es":
        print("\nStart chrome languages en for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        browser = webdriver.Chrome(options=options, executable_path=chrome_path)
    elif language == "fr":
        print("\nStart chrome languages en for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        browser = webdriver.Chrome(options=options, executable_path=chrome_path)
    elif language == "zh-ch":
        print("\nStart chrome languages en for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'zh-ch'})
        browser = webdriver.Chrome(options=options, executable_path=chrome_path)
    else:
        print(f'Language "{language}" is not available. Please choose ru, es, fr or zh-ch.')
    yield browser
    time.sleep(3)
    print("\nQuit browser..")
    browser.quit()
