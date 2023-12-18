import random

from data.data import Person
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + ' ' + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(18, 59),
        salary=random.randint(10000, 100000),
        department=faker_en.job(),
        email=faker_en.email(),
        current_address=faker_en.street_address(),
        permanent_address=faker_en.street_address(),
    )
