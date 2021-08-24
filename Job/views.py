from django.http import HttpResponseNotFound, Http404, HttpResponse
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from Job.models import Company, Specialty, Vacancy, Application, Resume
from Job.forms import ApplicationForm, CompanyForm, VacancyForm, ResumeForm
from django.views import View

from django.views.generic.base import TemplateView


def custom_handler404(request, exception):
    return HttpResponseNotFound('Что-то сломалось :(')


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.values('code', 'title', 'picture').annotate(amount=Count('vacancies'))
        context['companies'] = Company.objects.values('pk', 'name', 'logo').annotate(amount=Count('vacancies'))
        return context


class VacanciesView(TemplateView):
    template_name = 'vacancies.html'

    def get_context_data(self, **kwargs):
        context = super(VacanciesView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context


class VacanciesSpecView(TemplateView):
    template_name = 'vacancies_spec.html'

    def get_context_data(self, speciality_url, **kwargs):
        context = super(VacanciesSpecView, self).get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.filter(code=speciality_url).values('title')
        if context['specialties'].count() == 0:
            raise Http404
        context['vacancies'] = Vacancy.objects.filter(specialty__code=speciality_url)
        return context


class CompanyView(TemplateView):
    template_name = 'company.html'

    def get_context_data(self, company_id, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.filter(id=company_id)
        if context['company'].count() == 0:
            raise Http404
        context['vacancies'] = Vacancy.objects.filter(company__id=company_id)
        return context


class ApplicationView(View):

    def get(self, request, vacancy):
        context = {
            'vacancy': Vacancy.objects.get(id=vacancy),
            'form': ApplicationForm,
        }
        return render(request, 'vacancy.html', context=context)

    def post(self, request, vacancy):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            application = Application.objects.create(
                written_username=data['written_username'],
                written_phone=data['written_phone'],
                written_cover_letter=data["written_cover_letter"],
                vacancy=Vacancy.objects.get(id=vacancy),
                user=request.user                                  # If User exist!!!
            )
            return render(request, 'send.html')
        return render(request, 'vacancy.html', {'form': form})


class CompanyStartView(View):

    def get(self, request):
        context = {}
        return render(request, 'company-create.html', context=context)


class MyCompanyView(View):

    def get(self, request):
        if len(Company.objects.filter(owner=request.user)) == 0:        # Null is object?
            return redirect('/mycompany/letsstart/')
        else:
            form = CompanyForm(
                initial={
                    'name': request.user.my_company.first().name,
                    'location': request.user.my_company.first().location,
                    'logo': request.user.my_company.first().logo,
                    'description': request.user.my_company.first().description,
                    'employee_count': request.user.my_company.first().employee_count,
                    'owner': request.user,
                }
            )
            context = {
                'form' : form
            }
            return render(request, 'company-edit.html', context=context)

    def post(self, request):
        company = request.user.my_company.first()
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('/mycompany/')
        return render(request, 'company-edit.html', {'form': form})


class MyCompanyCreateView(View):

    def get(self, request):
        context = {
            'form': CompanyForm,
        }
        return render(request, 'company-new.html', context=context)

    def post(self, request):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            company = Company.objects.create(
                name=data['name'],
                location=data['location'],
                logo=data['logo'],
                description=data["description"],
                employee_count=data["employee_count"],
                owner=request.user  # If User exist!!!
            )
            return redirect('/mycompany/')
        return render(request, 'company-new.html', {'form': form})


class CompanyVacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.filter(company=request.user.my_company.first())
        user = request.user
        context = {
            'vacancies' : vacancies,
            'user' : user,
        }
        return render(request, 'vacancy-list.html', context=context)


class VacanciesCreateView(View):

    def get(self, request):
        context = {
            'form': VacancyForm,
        }
        return render(request, 'vacancy-create.html', context=context)

    def post(self, request):
        form = VacancyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            vacancy = Vacancy.objects.create(
                title=data['title'],
                specialty=data['specialty'],
                skills=data['skills'],
                description=data["description"],
                salary_min=data["salary_min"],
                salary_max=data["salary_max"],
                company=request.user.my_company.first()
            )
            return redirect('/mycompany/vacancies/')
        return render(request, 'vacancy-create.html', {'form': form})


class VacancyEditView(View):

    def get(self, request, vacancy_id):
        applications = request.user.my_company.first().vacancies.get(id=vacancy_id).applications.all()
        form = VacancyForm(
            initial={
                'title': request.user.my_company.first().vacancies.get(id=vacancy_id).title,
                'specialty': request.user.my_company.first().vacancies.get(id=vacancy_id).specialty,
                'skills': request.user.my_company.first().vacancies.get(id=vacancy_id).skills,
                'description': request.user.my_company.first().vacancies.get(id=vacancy_id).description,
                'salary_min': request.user.my_company.first().vacancies.get(id=vacancy_id).salary_min,
                'salary_max': request.user.my_company.first().vacancies.get(id=vacancy_id).salary_max,
            }
        )
        context = {
            'form' : form,
            'applications' : applications,
        }
        return render(request, 'vacancy-edit.html', context=context)

    def post(self, request, vacancy_id):
        vacancy = request.user.my_company.first().vacancies.get(id=vacancy_id)
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('/mycompany/vacancies/')
        return render(request, 'vacancy-edit.html', {'form': form})


class ResumeStartView(View):

    def get(self, request):
        if len(Resume.objects.filter(user=request.user)) != 0:        # Null is object?
            return redirect('/myresume/')
        context = {}
        return render(request, 'resume-create.html', context=context)


class ResumeCreateView(View):

    def get(self, request):
        if len(Resume.objects.filter(user=request.user)) != 0:        # Null is object?
            return redirect('/myresume/')
        context = {
            'form': ResumeForm,
        }
        return render(request, 'resume-new.html', context=context)

    def post(self, request):
        form = ResumeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resume = Resume.objects.create(
                user=request.user,         # If user exist!
                name=data['name'],
                surname=data['surname'],
                status=data['status'],
                salary=data['salary'],
                specialty=data['specialty'],
                grade=data['grade'],
                education=data['education'],
                experience=data['experience'],
                portfolio=data['portfolio'],
            )
            return redirect('/myresume/')
        return render(request, 'resume-new.html', {'form': form})


class ResumeView(View):

    def get(self, request):
        if len(Resume.objects.filter(user=request.user)) == 0:        # Null is object?
            return redirect('/myresume/letsstart/')
        else:
            form = ResumeForm(
                initial={
                    'user': request.user,
                    'name': request.user.my_resume.name,
                    'surname': request.user.my_resume.surname,
                    'status': request.user.my_resume.status,
                    'salary': request.user.my_resume.salary,
                    'specialty': request.user.my_resume.specialty,
                    'grade': request.user.my_resume.grade,
                    'education': request.user.my_resume.education,
                    'experience': request.user.my_resume.experience,
                    'portfolio': request.user.my_resume.portfolio,
                }
            )
            context = {
                'form' : form
            }
            return render(request, 'resume-edit.html', context=context)

    def post(self, request):
        resume = request.user.my_resume
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('/myresume/')
        return render(request, 'resume-edit.html', {'form': form})


def search_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Vacancy.objects.filter(Q(title__icontains=search_query) | Q(skills__icontains=search_query))
    else:
        posts = Vacancy.objects.all()
    context = {
        'posts' : posts,
        'search_query' : search_query,
    }
    return render(request, 'search.html', context=context)


class ProfileView(View):

    def get(self, request):
        context = {}
        return render(request, 'profile.html', context=context)