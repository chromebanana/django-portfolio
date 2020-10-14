from django.db import models

class Article(models.Model):
	location = models.CharField(max_length=120)
	date = models.CharField(max_length=120)
	body = models.TextField()

	class Meta:
		abstract = True

class Professional(Article):
	role = models.CharField(max_length=120)
	organisation = models.CharField(max_length=120)

	def __str__(self):
		return self.organisation

class Qualification(Article):
	institution = models.CharField(max_length=120)
	grade = models.CharField(max_length=120) 

	def __str__(self):
		return self.institution