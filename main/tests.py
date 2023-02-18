from django.test import TestCase
from main.models import Article, Release
from datetime import datetime
import pytz


class test_magazine(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_released(self):
        response = self.client.get('/released')
        self.assertEquals(response.status_code, 200)

    def test_about(self):
        response = self.client.get('/about')
        self.assertEquals(response.status_code, 200)


class ArticleModelTest(TestCase):
    def test_article_model_save_and_retrive(self):

        # создание статей
        article1 = Article(title='title1',
                           description='desc',
                           text='text',
                           date=datetime.utcnow().replace(tzinfo=pytz.utc),
                           number=1)

        article1.save()

        article2 = Article(title='title2',
                           description='desc',
                           text='text',
                           date=datetime.utcnow().replace(tzinfo=pytz.utc),
                           number=1)
        article2.save()

        #загрузка всех статей из базы
        articles = Article.objects.all()

        # проверка количества статей
        self.assertEqual(len(articles), 2)

        # проверка заголовка первой записи
        self.assertEquals(articles[0].title, article1.title)

        # проверка заголовка второй записи
        self.assertEquals(articles[1].title, article2.title)


class ReleaseModelTest(TestCase):
    def test_model(self):
        release1 = Release(id=1,
                           title='Выпуск #1',
                           description='desc',
                           text='text',
                           number=1)
        release1.save()

        release2 = Release(id=2,
                           title='Выпуск #2',
                           description='desc',
                           text='text',
                           number=1)
        release2.save()

        # загрузка всех статей из базы
        releases = Release.objects.all()

        # проверка количества статей
        self.assertEqual(len(releases), 2)

        # проверка заголовка первой записи
        self.assertEquals(releases[0].title, release1.title)

        # проверка заголовка второй записи
        self.assertEquals(releases[1].title, release2.title)

        
