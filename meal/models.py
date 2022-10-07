from django.db import models

# 식품(Food) 클래스에서 Meal 클래스에 Foreignkey로 모델을 불러와 식단을 작성시킬 예정
     
class Food(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
# class Meal(models.Model):
#     time = models.DateField()
#     menu = models.ForeignKey(Food, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.time
    


     
