from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,state, password = None):
        if not email:
            raise ValueError("Users must have an email adress")
        if not username:
            raise ValueError("User must have a username")
        if not state:
            raise ValueError("User must have a state")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            state = state,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,state,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username= username,
            password = password,
            state=state,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser= True
        user.save(using = self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length= 60, unique= True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add= True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default= False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    state = models.CharField(max_length=2)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email','state']

    objects = MyAccountManager()
    def __str__(self):
        return self.email
    def has_perm(self,perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "complete": self.complete,
        }

class Score(models.Model):
    score = models.IntegerField(default=0)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.score

    class Meta:
        ordering = ['score']

    def serialize(self):
        return {
            "id": self.id,
            "score": self.score,
        }