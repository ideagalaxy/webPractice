from django.db import models

# Create your models here.

#모델 생성
#모델 테이블 마이그레이션
#테이블 생성

#마이그레이션을 해줘야 함
class Question(models.Model):
    quesiton_text = models.CharField(max_length=200) #최대질문 200자까지
    pub_date = models.DateTimeField(auto_now_add=True)

    def was_published_recently(self):
        return self.pub

    def __str__(self) -> str:
        return f"질문 : {self.quesiton_text}, 날짜 : {self.pub_date}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
    
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Person(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.member.username
    
class BankBook(models.Model):
    member = models.ForeignKey(Person, on_delete=models.CASCADE)
    balance_won = models.IntegerField(default = 0)
    balance_dol = models.IntegerField(default = 0)
    balance_yen = models.IntegerField(default = 0)
    balance_pes = models.IntegerField(default = 0)


