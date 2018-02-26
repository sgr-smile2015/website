from django.test import TestCase
import datetime
from .models import Question
from django.utils import timezone


class QuestionModelTest(TestCase):

    def test_was_publish_with_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future = Question(pub_date=time)
        self.assertIs(future.was_published_recently(), False)
