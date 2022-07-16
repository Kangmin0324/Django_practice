from django.urls import path
from polls import views


app_name = 'polls'
urlpatterns = [
    # /polls/ ->클래스형 뷰로 변경
    path('', views.IndexView.as_view(), name='index'),

    # /polls/99/ ->변경
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /polls/99/results/  ->변경
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # /polls/99/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
