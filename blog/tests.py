"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django import test
from django.contrib.auth.models import User

from blog import models

class PostModelTests(test.TestCase):

    def setUp(self):
        self.user = User.objects.create(username="aaron")

    def should_return_title_as_string_representation(self):
        title = "This is my title."
        post = models.Post(title=title)
        self.assertEqual(str(post), title)

    def should_set_slug_field_on_save(self):
        post = models.Post.objects.create(
            author=self.user,
            title="sample post",
            body_text="This is the body",
        )
        self.assertEqual(post.slug, "sample-post")

    def should_set_html_on_save(self):
        post = models.Post.objects.create(
            author=self.user,
            title="sample post",
            body_text="This is the **body**",
        )
        self.assertEqual(post.body_html, "<p>This is the <strong>body</strong></p>")


