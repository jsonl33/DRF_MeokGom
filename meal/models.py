from django.db import models

# Create your models here.

# 레시피(Recipe)와 원재료(Groceries) 클래스에서 Meal 클래스에 Foreignkey로 모델을 불러와 식단을 작성시킬 예정
     
class Groceries(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    

# class Recipe(models.Model):
#     name = models.CharField(max_length=100)
#     groceries = models.ForeignKey(Groceries, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name
    
    
    
# class Meal(models.Model):
#     time = models.DateField()
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.time
    


     
