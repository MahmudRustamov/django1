from django.urls import path
from pages.views import home_page_view, about_page_view, teacher_page_view

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about_page_view,name='hobby'),
    path('teacher/', teacher_page_view,name='teacher'),
]