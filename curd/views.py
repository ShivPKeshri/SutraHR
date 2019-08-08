from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import CurdOperation
from .curd_form import CurdForm
from django.db.models import Q
from djqscsv import render_to_csv_response


def get_all(request):
	if request.user.is_staff or request.user.is_superuser:
		queryset = CurdOperation.objects.all()
		query = request.GET.get('q')
		if query:
			queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query)).distinct()

		return render(request,'all_records.html', {'data':queryset})

	else:
		queryset = CurdOperation.objects.all().filter(is_deleted=False)
		return render(request,'non_admin_records.html', {'data':queryset})
		


	


def get_selected(request, id=None):

	instance = get_object_or_404(CurdOperation, id=id)
	if instance.is_deleted:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	context={'inst':instance}

	return render(request, 'records.html', context)


#Create a new employee
@csrf_exempt
def create(request):

	form=CurdForm(request.POST or None)
	if form.is_valid():
		inst=form.save(commit=False)
		inst.save()
		return HttpResponseRedirect(inst.get_absolute_url())

	context={"form":form}
	return render(request, 'curd_form.html', context)

#Update employee details
@csrf_exempt
def update(request, id=None):

	inst=get_object_or_404(CurdOperation, id=id)
	form = CurdForm(request.POST or None, instance=inst)
	if form.is_valid():
		inst=form.save(commit=False)
		inst.save()
		return HttpResponseRedirect(inst.get_absolute_url())

	context={"form":form, 'inst':inst}

	return render(request, 'curd_form.html', context)

def download_csv(request):
	print('here?')
	# queryset = ''
	if request.user.is_staff or request.user.is_superuser:
		queryset = CurdOperation.objects.all()
		# import pdb
		# pdb.set_trace()
		query = request.GET.get('q')
		if query:
			queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query)).distinct()
		return render_to_csv_response(queryset)
	else:
		return render(request,'404.html',{})
