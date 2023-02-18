from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from datetime import datetime
from main.models import Release, Article
import pytz


class test_app(LiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(options=chrome_options)

        Article.objects.create(id=1,
                               title='title',
                               description='desc',
                               text='text',
                               date=datetime.utcnow().replace(tzinfo=pytz.utc),
                               number=1)

        Release.objects.create(id=1,
                               title='Выпуск #1',
                               description='desc',
                               text='text',
                               number=1)

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn('Home', self.browser.title)

    def test_home_page_header(self):
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Home', header.text)

    def test_redirect_to_released(self):
        self.browser.get(self.live_server_url)
        released_link = self.browser.find_element(By.LINK_TEXT, 'Released')
        href = released_link.get_attribute('href')

        self.browser.get(href)
        self.assertIn('Released', self.browser.title)

    def test_detile_view_released(self):
        self.browser.get(self.live_server_url)
        released_link = self.browser.find_element(By.LINK_TEXT, 'Released')
        href = released_link.get_attribute('href')

        self.browser.get(href)
        #self.browser.implicitly_wait(5)
        detail_view_link = self.browser.find_element(By.LINK_TEXT, 'Read more')
        href_detail = detail_view_link.get_attribute('href')

        self.browser.get(href_detail)
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Выпуск #1', header.text)

    def test_redirect_to_about_page(self):
        self.browser.get(self.live_server_url)
        about_link = self.browser.find_element(By.LINK_TEXT, 'About')
        href = about_link.get_attribute('href')

        self.browser.get(href)
        self.assertIn('About', self.browser.title)

    def test_redirect_to_about_page_and_return_home(self):
        self.browser.get(self.live_server_url)
        about_link = self.browser.find_element(By.LINK_TEXT, 'About')
        href = about_link.get_attribute('href')

        self.browser.get(href)
        self.assertIn('About', self.browser.title)

        home_link = self.browser.find_element(By.LINK_TEXT, 'Home')
        href = home_link.get_attribute('href')
        
        self.browser.get(href)
        self.assertIn('Home', self.browser.title)
