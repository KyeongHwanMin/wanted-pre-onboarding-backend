from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("이메일을 입력해 주세요.")
        if not name:
            raise ValueError("이름을 입력해 주세요.")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, password=password, name=name)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        default="", max_length=100, null=False, blank=False, unique=True
    )
    name = models.CharField(default="", max_length=100, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name
