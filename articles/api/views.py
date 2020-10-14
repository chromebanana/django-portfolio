from rest_framework.generics import ListAPIView, RetrieveAPIView
from drf_multiple_model.views import ObjectMultipleModelAPIView

from articles.models import Professional, Qualification
from .serializers import ArticleSerializer, QualificationSerializer

class ArticleAPIView(ObjectMultipleModelAPIView):
	querylist = [
		{
			'queryset' : Professional.objects.all(),
			'serializer_class' : ArticleSerializer
		},
		{
			'queryset' : Qualification.objects.all(),
			'serializer_class' : QualificationSerializer
		}
	]

class ArticleListView(ListAPIView):
	queryset = Professional.objects.all()
	serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveAPIView):
	queryset = Professional.objects.all()
	serializer_class = ArticleSerializer

# class QualificationListView(ListAPIView):
# 	queryset = Qualification.objects.all()
# 	serializer_class = QualificationSerializer

# class QualificationDetailView(RetrieveAPIView):
# 	queryset = Qualification.objects.all()
# 	serializer_class = QualificationSerializer