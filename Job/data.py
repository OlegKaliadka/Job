""" vacancies """

jobs = [

    {"id": "1", "title": "Python Developer", "specialty": "backend", "company": "3", "salary_from": "3000",
     "salary_to": "3500", "posted": "2020-03-11", "skills": "Python, Nginx, Git, Django, Docker, Kubernetes", "description": "Office in the city center with a terrace and hookah, tea, buns and whiskey always available. Possible free work schedule. Minimum requirements are:  Have 3 or more years of commercial development experience. Ability to write Unit tests on your code. Technical background, especially math and radio engineering. Knowledge of Django, Django Rest Framework and Celery. Knowledge in cluster deployment. Willingness to learn video data technology. Bonuses: The official registration of the TC. Office in the center of the city. Flexible schedule. Training and conferences at the company's expense. VHI. Would be an advantage: Experience with Docker. Experience in writing services on Asyncio. Skill in using the Linux/UNIX command line. Ability to work with Git. Salary is decent, to be discussed on a personal basis at the interview, based on competency level."},
    {"id": "2", "title": "Developer for Django project", "specialty": "backend", "company": "6", "salary_from": "2500",
     "salary_to": "2900", "posted": "2020-03-11", "skills": "Python, Django, PostgreSQL", "description": "We have been working in the web development market for more than 10 years. The main direction is custom development of web services and development of our own startups. We are a good match if: you know Python and Django well, have at least 3 years experience, have been involved in at least several projects, worked in a team. You want to work in a company of like-minded Django developers. You're interested in working on startups, taking part in their formative life. You understand that before submitting the task to the tester you need to check it out. You understand that you need to keep a balance between the quality of the code and duration of development. You like sharing knowledge and are not afraid to ask your colleagues for help. What we offer: Stable remote work. Project work/Official employment. Hourly wages/Pay per month. Negotiated number of working hours per month (100-200). Regular payments (2 times a month). Loyal work schedule, starting time no later than 10 am Moscow time. Interesting projects, complex tasks, work with modern technology."},
    {"id": "3", "title": "Middle SWIFT-developer", "specialty": "backend", "company": "1",
     "salary_from": "3300", "salary_to": "3500", "posted": "2020-03-11", "skills": "Swift, CoreData, Git, OOP, Databases", "description": "Developing an app for learning Chinese words and characters. Good in content and design, but lacking the right developer/developers. Our goal is to make a world leading Chinese language learning service. As such, we are looking for a full-time or part-time remote Senior/Middle iOS developer. Technology stack: Swift, Combine, CoreData, UI Constraints, Git. What we expect from you: senior students and Computer Science graduates; understanding of OOP principles; fluency in English (Intermediate minimum); willingness to work in a team; initiative, responsibility and ability to plan your time; ability to understand the current tasks of the company. We offer a good market salary."},
    {"id": "4", "title": "Middle Python Developer", "specialty": "backend", "company": "7", "salary_from": "2600",
     "salary_to": "2900", "posted": "2020-03-11", "skills": "Python, Docker, MySQL", "description": "What we expect from the candidate: 3 years experience in Python development, participation in a completed commercial project, the ability to describe it competently; Django / Flask.Experience with 3D models and underlying libraries (such as Open3D) would be an advantage; Experience with the standard libraries NumPy, SciPy, OpenCV (trimesh, open3d, pyvista); SQL at a basic level; Understanding of the main machine learning algorithms (linear regression, random forest, catboost, neural networks, etc.); Mathematical knowledge, experience in mathematical modeling; Experience with the project management tools.  What you will do: Optimizing existing virtual fitting methods and developing new ones; Improving the speed and accuracy of virtual fitting (from SLA and above); Using libraries and frameworks numpy, pandas, scikit-learn, tensorflow, catboost, LightGBM, opencv; Developing neural network methods of virtual fitting. Conditions: The official registration according to LC RF; Work with the latest equipment, the ability to travel abroad on a variety of IT-seminars; Work schedule 5 / 2 from 9-00 to 18-00 (work in the office, not remotely); friendly team and modern office; Opportunities for further career development. The final salary level is discussed after the interview."},
    {"id": "5", "title": "Skilled Python Developer", "specialty": "backend", "company": "8", "salary_from": "3200",
     "salary_to": "3500", "posted": "2020-03-11", "skills": "Python, Django, PostgreSQL, Git", "description": "Our main areas: e-commerce, geoservices, messengers, image recognition, automation, telephony, and startups. The customers are large financial, IT, and product companies in England. We are looking for an experienced full-time python developer to work on projects of our company. Experience in commercial Python/Django development for at least 2 years; SQL skills (Postgres); experience in writing client-server applications; skills in estimating deadlines and scope of work; Git, bug tracking systems. What you will do: Participate in the whole development process - from design to launch. Optimize the performance of the application. Benefits: Salary from 3000 pounds on hand; Remote collaboration with lined processes; Ambitious projects, interesting tasks from a professional point of view; Team of professionals. In the response must be a cover letter, why exactly you are suitable for this vacancy."}

]

""" Компании """

companies = [

    {"id": "1", "title": "workiro", "logo": "logo1.png", "employee_count": "10", "location": "Liverpool", "description": "We develop mobile applications and services for online learning."},
    {"id": "2", "title": "rebelrage", "logo": "logo2.png", "employee_count": "24", "location": "London", "description": "Mobile services, software, websites, mobile applications."},
    {"id": "3", "title": "staffingsmarter", "logo": "logo3.png", "employee_count": "123", "location": "London", "description": "Online exam monitoring service with artificial intelligence"},
    {"id": "4", "title": "evilthreat h", "logo": "logo4.png", "employee_count": "36", "location": "London", "description": "The leading webinar and video conferencing software in the UK and Western Europe."},
    {"id": "5", "title": "hirey ", "logo": "logo5.png", "employee_count": "21", "location": "Bristol", "description": "Telecommunications and payment services that help businesses around the world grow."},
    {"id": "6", "title": "swiftattack", "logo": "logo6.png", "employee_count": "79", "location": "London", "description": "Development of complex web services and mobile applications"},
    {"id": "7", "title": "troller", "logo": "logo7.png", "employee_count": "230", "location": "Manchester", "description": "A mobile app that allows you to try on shoes and choose the perfect pair in just 3 clicks"},
    {"id": "8", "title": "primalassault", "logo": "logo8.png","employee_count": "13", "location": "London", "description": "We implement projects of any complexity in the digital sphere" }

]

""" Категории """

specialties = [

    {"code": "frontend", "title": "Frontend"},
    {"code": "backend", "title": "Backend"},
    {"code": "gamedev", "title": "Gamedev"},
    {"code": "devops", "title": "Devops"},
    {"code": "design", "title": "Design"},
    {"code": "products", "title": "Products"},
    {"code": "management", "title": "Management"},
    {"code": "testing", "title": "Testing"}

]

""" Статусы в формате Enum """

#
#
# class EducationChoices(Enum):
#     missing = 'Отсутствует'
#     secondary = 'Среднее'
#     vocational = 'Средне-специальное'
#     incomplete_higher = 'Неполное высшее'
#     higher = 'Высшее'
#
#
# class GradeChoices(Enum):
#     intern = 'intern'
#     junior = 'junior'
#     middle = 'middle'
#     senior = 'senior'
#     lead = 'lead'
#
#
# class SpecialtyChoices(Enum):
#     frontend = 'Фронтенд'
#     backend = 'Бэкенд'
#     gamedev = 'Геймдев'
#     devops = 'Девопс'
#     design = 'Дизайн'
#     products = 'Продукты'
#     management = 'Менеджмент'
#     testing = 'Тестирование'
#
#
# class WorkStatusChoices(Enum):
#     not_in_search = 'Не ищу работу'
#     consideration = 'Рассматриваю предложения'
#     in_search = 'Ищу работу'
