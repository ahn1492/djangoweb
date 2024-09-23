from django.db import models

# Create your models here.
class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    #제목
    title = models.CharField(max_length=200)
    #내용
    contents = models.TextField()
    #조회수
    views = models.IntegerField()
    #생성일
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Program(models.Model):
    id = models.AutoField(primary_key=True)
    #제목
    title = models.CharField(max_length=200)
    #메인텍스트
    maintext = models.TextField()
    #서브텍스트
    subtext = models.TextField()
    #기간
    schdule = models.TextField()
    img =  models.TextField()
    def __str__(self):
        return self.title
