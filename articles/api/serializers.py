from rest_framework import serializers

from articles.models import Professional, Qualification

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Professional
		fields = ("__all__")
	
class QualificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qualification
		fields = ("__all__")