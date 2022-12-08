from django.db import models


class Team(models.Model):
    # team_id = models.BigAutoField()
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    PROFILES = (
        ('management', 'management'),
        ('finance', 'finance'),
        ('creative', 'creative'),
        ('hr', 'hr'),
        ('development', 'development'),
        ('design', 'design'),
        ('testing', 'testing')
    )
    profile = models.CharField(
        max_length=20,
        choices=PROFILES,
        default='development'
    )
    master_team = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.id} {self.name}"


class Employee(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    position = models.CharField(max_length=255)
    salary = models.IntegerField()
    login = models.CharField(max_length=255, default="")
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True
    )

    @property
    def task_number(self):
        res = 0
        for task in Task.objects.all():
            employees = task.employee.all()
            if self in employees:
                res += 1
        return res

    def __str__(self):
        return f"{self.id} {self.name}"


class Project(models.Model):
    name = models.CharField(max_length=255)
    STATUSES = (
        ('planned', 'planned'),
        ('cancelled', 'cancelled'),
        ('in progress', 'in progress'),
        ('interrupted', 'interrupted'),
        ('closed', 'closed')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default='planned'
    )
    manager = models.OneToOneField(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.id} {self.name}"


class Version(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    release_datetime = models.DateTimeField()
    project = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT,
        null=True
    )

    def __str__(self):
        return f"{self.id} {self.name}"


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT
    )
    version_created = models.ForeignKey(
        Version,
        related_name='version_created',
        on_delete=models.RESTRICT,
        null=True
    )
    version_completed = models.ForeignKey(
        Version,
        related_name='version_completed',
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )
    employee = models.ManyToManyField(Employee)

    def __str__(self):
        return f"{self.id} {self.name}"
