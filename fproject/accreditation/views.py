from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from accreditation.models import School
# Create your views here.
def school_detail(request):
	posts = School.objects.all().order_by('-institution_state')
	paginator = Paginator(posts, 50) 
	page = request.GET.get('page')
	
	try:
		changes = paginator.page(page)
	except PageNotAnInteger:
		changes = paginator.page(1)
	except EmptyPage:
		changes = paginator.page(paginator.num_pages)

	query = request.GET.get('q')
	if query:
		posts = posts.filter(
			Q(institution_id__icontains = query)|
			Q(institution_name__icontains = query)|
			Q(institution_state__icontains = query)|
			Q(institution_city__icontains = query)|
			Q(accreditation_status__icontains = query)
			)
    



	context ={'schools': posts, 'changes': changes}
	return render(request, 'accreditation.html',context)