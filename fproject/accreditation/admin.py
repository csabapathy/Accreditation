from django.contrib import admin

# Register your models here.

from .models import School

class SchoolAdmin(admin.ModelAdmin):
	list_display = ('institution_id', 'institution_name', 'institution_state', 'institution_city', 'program_name', 'accreditation_type')
	search_fields = ('institution_id', 'institution_name', 'institution_city')
	list_display_links = ('institution_id', 'institution_name')


admin.site.register(School, SchoolAdmin)