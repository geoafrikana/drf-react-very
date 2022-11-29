from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category


class Test_Create_Post(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='B*d023W00#'
        )
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Test Post Excerpt', content='post content', author=testuser1
        )

    
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(excerpt, 'Test Post Excerpt')
        self.assertEqual(content, 'post content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), title)
        self.assertEqual(str(post), 'Post Title')
        self.assertEqual(str(cat), 'django')
        self.assertEqual(str(cat), cat.name)
        self.assertEqual(post.category_id, 1)
        

