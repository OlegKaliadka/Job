
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from Job.views import MainView, VacanciesView, VacanciesSpecView, CompanyView, ApplicationView, CompanyStartView, MyCompanyView, MyCompanyCreateView, CompanyVacanciesView, VacanciesCreateView, VacancyEditView, ResumeStartView, ResumeCreateView, ResumeView, search_view, ProfileView, search_word_view
from Application.views import register
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('cat/vacancies/<str:speciality_url>/', VacanciesSpecView.as_view(), name='vacancies_spec'),
    path('companies/<int:company_id>/', CompanyView.as_view(), name='company'),
    path('mycompany/letsstart/', CompanyStartView.as_view(), name='company_start'),
    path('mycompany/', MyCompanyView.as_view(), name='company_edit'),
    path('mycompany/create', MyCompanyCreateView.as_view(), name='company_create'),
    path('mycompany/create/send/', MyCompanyCreateView.as_view()),
    path('vacancies/<int:vacancy>/', ApplicationView.as_view(), name='vacancy'),
    path('vacancies/<int:vacancy>/send/', ApplicationView.as_view()),
    path('mycompany/vacancies/', CompanyVacanciesView.as_view(), name='company_vacancies'),
    path('mycompany/vacancies/create', VacanciesCreateView.as_view(), name='vacancy_create'),
    path('mycompany/vacancies/<int:vacancy_id>/', VacancyEditView.as_view(), name='vacancy_edit'),
    path('myresume/letsstart', ResumeStartView.as_view(), name='resume_start'),
    path('myresume/create', ResumeCreateView.as_view(), name='resume_create'),
    path('myresume/create/send/', ResumeCreateView.as_view()),
    path('myresume/', ResumeView.as_view(), name='resume_edit'),
    path('search/', search_view, name='search'),
    path('search/<str:search_word>/', search_word_view, name='search_word'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('', include("django.contrib.auth.urls")),
    path('logout', LogoutView.as_view()),
    path('register', register, name='register'),
]