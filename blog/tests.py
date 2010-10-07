"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

import datetime
from mock import Mock, patch

from django import test
from django.core.urlresolvers import reverse
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

    @patch.object(models.Post, 'objects')
    def should_get_recent_active_posts(self, query_mock):
        query_mock.filter.return_value = [1]
        posts = models.Post.get_recent_posts()

        self.assertEqual(query_mock.method_calls, [('filter', (), {'active': True})])
        self.assertEqual(posts, [1])

    @patch.object(models.Post, 'objects')
    def should_limit_recent_posts(self, query_mock):
        query_mock.filter.return_value = [1, 2, 3]
        posts = models.Post.get_recent_posts(limit=2)
        self.assertEqual(posts, [1, 2])

    def should_get_absolute_url(self):
        post = models.Post(publish_date=datetime.date(2010,10,5), slug="post-title")
        self.assertEqual(post.get_absolute_url(), reverse("blog:details", kwargs={
            'year': 2010,
            'month': '10',
            'slug': 'post-title',
        }))

class Acceptance(test.TestCase):

    def setUp(self):
        self.client = test.Client()

    def should_hit_index_page(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)

    def should_hit_blog_detail_page(self):
        response = self.client.get(reverse("blog:details", kwargs={
            'year': '2010', 'month': '05',
            'slug': 'this-post'}))
        self.assertEqual(response.status_code, 200)

class BlogIndexTests(test.TestCase):
    def setUp(self):
        self.client = test.Client()

    @patch.object(models.Post, 'get_recent_posts', Mock(return_value=["Post 1", "Post 2"]))
    def should_send_recent_posts_to_template(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.context['recent_posts'], ["Post 1", "Post 2"])

