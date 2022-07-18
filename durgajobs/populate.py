import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','durgajobs.settings')

import django
django.setup()

from testapp.models import HydJobs,BngJobs,PuneJobs
from faker import Faker
fake=Faker()

from random import *
def phnogen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project_Manager','Team_Lead','Software_Engineer','Sr.Software_Engineer'))
        feligibility=fake.random_element(elements=('B.TECH','MCA','M.TECH','Phd'))
        faddrs=fake.address()
        femail=fake.email()
        fphno=phnogen()
        hyd_jobs_records=HydJobs.objects.get_or_create(date=fdate,company_name=fcompany,title=ftitle,
        eligibility=feligibility,addrs=faddrs,email=femail,phone_number=fphno)

n=int(input("Enter number of records:"))
populate(n)
