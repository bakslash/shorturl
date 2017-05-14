from django.db import models

# Create your models here.
class ussurl(models.Model):
	url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15)
    #shortcode = models.CharField(max_length=15, null=True) empty db is ok
    #shortcode = models.CharField(max_length=15, default='marcusdefaultshortcode')
	def __str__(self):
		return str(self.url)
		
	def __unicode__(self):
		return str(self.url)


'''
python manage.py makemigrations
python manage.py migrate
'''