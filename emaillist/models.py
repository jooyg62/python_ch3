from django.db import models


# 모든 모델은 기본적으로 models.Model을 상속받는다.
class Emaillist(models.Model):
    first_name = models.CharField(max_length=50)    # 모델 정의: 장고가 varchar 로 만들어 준다.
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    # 디버깅을 위해서
    def __str__(self):
        return f'Emaillist({self.first_name}, {self.last_name}, {self.email})'

