from django.db import models
from django.urls import reverse

# Create your models here.
class CurdOperation(models.Model):
    
    status_code = (
        (1,("In Progress")),
        (2, ("Completed")), 
        (3, ("Pending")),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.IntegerField(choices=status_code, default=1)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={"id":self.id})
