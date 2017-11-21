import os 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Protwo.settings")

import django
django.setup()

# Fake pop scripts

import random
from AppTwo.models import Topic,Webpage,AccessRecord

# importinf faker

from faker import Faker
# this function would be used later in the script to 
# generate fake 
# Generatig instant for the faker object named Faker
fakegen = Faker()

# doing topics manually

topics = ['Search', 'Social Network', 'Market Place', 'News', 'Sports']

# f unction to add topics

def add_topic():
# this will retrieve topics if already existing or create new
	t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
	t.save()
	return t

# writing function 
def populate(N =5):
	for entry in range(5):
		# get topics for entry
		top = add_topic()
		#create fake data for that entry
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		# Create new webpage entry
		webpg = Webpage.objects.get_or_create(topic= top,url = fake_url,name = fake_name)[0]

		# create fake access records
		acc_rec = AccessRecord.objects.get_or_create(name=webpg, date= fake_date)[0]

if __name__ == '__main__':
	print("populating scripts")
	populate(20)
	print("populating done")


