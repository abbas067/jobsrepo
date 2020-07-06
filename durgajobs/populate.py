import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','durgajobs.settings')
django.setup()
from testapp.models import *
from faker import Faker
from random import *
faker=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=faker.date()
        fcompany=faker.company()
        ftitle=faker.random_element(elements=('Project Manager','Team Lead','Software Enginner','DBA'))
        felligibility=faker.random_element(elements=('MCA','B.Teach'))
        feaddress=faker.address()
        femail=faker.email()
        fphoneno=phonenumbergen()
        hyd_record=HydJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=felligibility,address=feaddress,email=femail,phonno=fphoneno)
        Blore_recordt=BloreJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=felligibility,address=feaddress,email=femail,phonno=fphoneno)
        Pune_record=PuneJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=felligibility,address=feaddress,email=femail,phonno=fphoneno)
populate(30)
