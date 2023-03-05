from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (AbstractUser, PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, avatar, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email), avatar=avatar)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def add_friend(self, friend):
        print(self, friend, 'friends')


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, db_index=True)
    friends = models.ManyToManyField('self', blank=True)
    avatar = models.ImageField(verbose_name='avatar', upload_to='img', blank=True)

    object = UserManager()

    def image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return '/static/img/skins/ak47-asimov.png'


class Requests(models.Model):
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['inviter', 'recipient'], name='name of constraint')
        ]
        verbose_name_plural = 'requests'

    def __str__(self):
        return f'inviter: {self.inviter_id}, recipient_id: {self.recipient_id}'
