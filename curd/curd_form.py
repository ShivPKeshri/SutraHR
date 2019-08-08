from django import forms
from .models import CurdOperation

class CurdForm(forms.ModelForm):
	class Meta:
		model = CurdOperation
		fields = [	'id',
					'title',
					'description',
					'status',
					'is_deleted',
				]
