from django.db import models
from django.contrib.auth.models import User
from conf.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR,
                             height_field='height_field',
                             width_field='width_field',
                             )
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_company", null=True)

    def __str__(self):
        return f'name={self.name}, company={self.id}, employee_count={self.employee_count}'


class Specialty(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR,
                                height_field='height_field',
                                width_field='width_field',
                                )      # changes
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'name={self.title}'


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'name={self.title}, company={self.company}, specialty={self.specialty}'


class Application(models.Model):
    written_username = models.CharField(max_length=100)
    written_phone = models.CharField(max_length=100)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications", null=True)


class Resume(models.Model):
    STATUS = [
        (1, "I'm not looking for a job"),
        (2, "I'm looking for a job"),
        (3, "I am currently sifting through offers"),
    ]
    GRADE = [
        (1, "Trainee"),
        (2, "Junior"),
        (3, "Middle"),
        (4, "Senior "),
        (5, "Lid"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="my_resume")
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    status = models.PositiveSmallIntegerField(choices=STATUS)
    salary = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="resume")
    grade = models.PositiveSmallIntegerField(choices=GRADE)
    education = models.CharField(max_length=100)
    experience = models.TextField()
    portfolio = models.TextField()
