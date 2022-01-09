from django.test import TestCase
from django.contrib.auth.models import User
from .models import Website, UserProfile

# Create your tests here.
class ProjectTestClass(TestCase):  # Project class test
    def setUp(self):
        # creating a user
        user = User.objects.create(
            username="test_user", first_name="site", last_name="awards"
        )

        self.website = Website(
            author= user,
            title = "Test Site",
            description="Description",
            country = "Kenya",
            landing_page ="image.jpg",
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.website, Website))
    #def test_save_method(self):
    #    self.website.save_website()
    #    websites = Website.objects.all()
    #    self.assertTrue(len(websites) > 0)
    class ProfileTestClass(TestCase):
        def setUp(self):
        
            user = User.objects.create(
                username="test_user", first_name="site", last_name="awards"
            )

            self.profile = UserProfile(
                bio="Test Bio",
                full_name = "Daniel Kariuki",
                user=user,
                profile_pic = "image.jpg",
                followers = ""
            )
        def test_instance(self):
            self.assertTrue(isinstance(self.profile, UserProfile))