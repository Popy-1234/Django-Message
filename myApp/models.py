from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer')
    ]
    usertype=models.CharField(choices=USER,max_length=100,null=True)

    def __str__(self) -> str:
        return f"{self.username}-{self.first_name}-{self.last_name}"
    
class ResumeModel(models.Model):
    Gender=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    Designation=models.CharField(max_length=100,null=True)
    Contact_number=models.CharField(max_length=100,null=True)
    Career_Summary=models.TextField(max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    age=models.PositiveIntegerField(null=True)
    gender=models.CharField(choices=Gender,max_length=100,null=True)

    def __str__(self) -> str:
        return self.user.username+ " "+ self.Designation
    
class IntermediateLanguageModel(models.Model):
    
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Language_Name=models.CharField(max_length=100,null=True)

    
    def __str__(self) -> str:
        return self.Language_Name  
    
class LanguageModel(models.Model):
    
    Proficiency_Level_Choices=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('expert','Expert'),
    ]

    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Language_Name=models.CharField(max_length=100,null=True)
    Proficiency_Level=models.CharField(choices=Proficiency_Level_Choices,max_length=100,null=True)
    
    
    class Meta:
        unique_together=['user','Language_Name']
    
    def __str__(self) -> str:
        return self.user.username+ " "+ self.Language_Name
    
class IntermediateLanguageModel(models.Model):
    
    Language_Name=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.Language_Name
    

class SkillModel(models.Model):
    
    
    Skill_Level_Choices=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('expert','Expert'),
    ]
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Skill_Name=models.CharField(max_length=100,null=True)
    Skill_Level=models.CharField(choices=Skill_Level_Choices,max_length=100,null=True)
    
    class Meta:
        unique_together=['user','Skill_Name']
    
    def __str__(self) -> str:
        return self.user.username+ " "+ self.Skill_Name
    
class IntermediateSkillModel(models.Model):
    
    My_Skill_Name=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.My_Skill_Name
    
    
  

