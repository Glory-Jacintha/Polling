import datetime

from django.test import TestCase
from django.test import Client
from django.utils import timezone

from .models import Question

client = Client()

class QuestionModelTests(TestCase):
    def test_recently_published_with_future_question(self):
        """
        recently_published() returns False for questions whose publish_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(publish_date=time)
        self.assertIs(future_question.recently_published(), False)

    def test_recently_published_with_old_question(self):
        """
        recently_published() returns False for questions whose publish_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(publish_date=time)
        self.assertIs(old_question.recently_published(), False)
    
    def test_recently_published_with_old_question(self):
        """
        recently_published() returns True for questions whose publish_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(publish_date=time)
        self.assertIs(recent_question.recently_published(), True)