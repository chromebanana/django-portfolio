from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleAPIView

urlpatterns = [
	path('', ArticleAPIView.as_view()),
	path('<pk>', ArticleAPIView.as_view())
]