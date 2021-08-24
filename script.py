import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()


from Job.models import Company, Specialty, Vacancy
from Job import data

if __name__ == '__main__':
 #   i = 1
 #   for company in data.companies:
 #       one_company = Company.objects.filter(id=i).update(
 #           name=company['title'],
 #           location=company['location'],
 #           description=company["description"],
 #           employee_count=company["employee_count"]
 #       )
 #       i += 1
 #   i = 1
 #   for specialty in data.specialties:
 #       one_specialty = Specialty.objects.filter(id=i).update(
 #           code=specialty['code'],
 #           title=specialty['title'],
 #       )
 #       i += 1
   # i = 1
   # for job in data.jobs:
   #     one_job = Vacancy.objects.filter(id=i).update(
   #         title=job['title'],
    #        specialty=Specialty.objects.get(code=job['specialty']),
     #       company=Company.objects.get(id=job['company']),
    #        skills=job["skills"],
    #        description=job["description"],
    #        salary_min=job["salary_from"],
    #        salary_max=job["salary_to"],
    #        published_at=job["posted"],
   #     )
   #     i += 1
    kek = Vacancy.objects.all()
    print(kek)




