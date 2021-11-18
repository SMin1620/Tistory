from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# AbstractUser로 user모델 확장
class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # 필수로 받고싶은 필드를 넣기 위한 소스로 email필드가 들어가야 하지만, 여기서는 로그인을 email로 하기로 하였기 때문에 기입하지 않는다.

    def __str__(self):
        return '{} {}'.format(self.pk, self.email)
