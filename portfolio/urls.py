from django.urls import path
from . import views 
from .views import portfolio_about,portfolio_home,portfolio_portfolio

urlpatterns = [
    path('home/', views.portfolio_home, name='home'),
    path('portfolio/', views.portfolio_portfolio, name='portfolio'),
    path('about/', views.portfolio_about, name='about'),
    path('base/', views.portfolio_base, name='base'),
    path('resume/', views.portfolio_resume, name='resume')
]

# urlpatterns =[
#     path('home/', form_home, name=''),
#     path('portfolio/', form_portfolio, name=''),
#     path('about/', form_about, name=''),
# ]