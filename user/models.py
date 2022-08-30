from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self, email, nickname, address, password):

        if not email:
            raise ValueError('must have user email')

        if not nickname:
            raise ValueError('must have user nickname')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            address=address
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, email, nickname, address, password):
        user = self.create_user(
            email,
            nickname=nickname,
            address=address,
            password=password
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, address, password):
        user = self.create_user(
            email,
            nickname=nickname,
            address=address,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(
        max_length=100,
        unique=True
    )
    nickname = models.CharField(
        max_length=50,
        unique=True
    )
    address = models.CharField(
        max_length=200,
    )
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'address']

    objects = UserManager()

    class Meta:
        db_table = 'users'
