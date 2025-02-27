from django.db import models

# Create your models here.
class Profile(models.Model):
    # Basic Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    # Professional Summary
    summary = models.TextField()

    # Education
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    graduation_year = models.IntegerField()
    gpa = models.FloatField(null=True, blank=True)

    # Work Experience
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    # Skills
    skills = models.TextField()

    # Projects
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    technologies = models.CharField(max_length=200)
    project_link = models.URLField(null=True, blank=True)

    # Certifications
    certification = models.CharField(max_length=100)
    organization = models.CharField(max_length=150)
    completion_date = models.DateField()

    # Languages
    languages = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
   
