from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name='index'),
    # # polls/5
    # path('<int:question_id>/', views.detail, name='detail'),
    # # polls/5/results
    # path('<int:question_id>/results/', views.results, name='results'),
    # # polls/5/vote
    # path('<int:question_id>/vote/', views.vote, name='vote')

    # using generic views
    # generic view requires the primary key captured from the URL to be called as "pk"
    # so changed <int:question_id> -> <int:pk>
    path('', views.IndexView.as_view(), name='index'),
    # polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote')
]
