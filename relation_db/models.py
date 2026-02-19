from django.db import models


class Type(models.Model):
    types = models.CharField(max_length=100)

    def __str__(self):
        return self.types

 
class Person(models.Model):
    personName = models.CharField(max_length=100, verbose_name='Введите имя для регистрации')
    typePerson = models.ManyToManyField(Type, blank=True)



    def __str__(self):
        return f'{self.personName}  {', '.join(i.types for i in self.typePerson.all())}'

class TourPerson(models.Model):
    tour = models.OneToOneField(Person, on_delete=models.CASCADE)
    registered = models.CharField(max_length=100)

    def __str__(self):
        return self.registered
    

class ReviewPerson(models.Model):
    REVIEW = (
        ('Отличный Тур', 'Отличный Тур'),
        ('Хороший Тур', 'Хороший Тур'),
        ('Нормальный Тур', 'Нормальный Тур'),
        ('Ожидал большего', 'Ожидал большего'),
        ('Ужасный Тур', 'Ужасный Тур'),
    )
    revPerson = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='review')
    gradeRev = models.CharField(max_length=100, choices=REVIEW)
    data_rev = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.revPerson}  Отценка {self.gradeRev}'