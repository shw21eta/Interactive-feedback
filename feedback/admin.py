from django.contrib import admin
from .models import Feedback
from .models import Message
from .models import Teacher
from .models import Student
from .models import Questions

# Register your models here.
admin.site.register(Feedback)
admin.site.register(Message)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Questions)
