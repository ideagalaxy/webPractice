from django.db import models

# Create your models here.

#모델 생성
#모델 테이블 마이그레이션
#테이블 생성

#마이그레이션을 해줘야 함
class Question(models.Model):
    quesiton_text = models.CharField(max_length=200) #최대질문 200자까지
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"질문 : {self.quesiton_text}, 날짜 : {self.pub_date}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text