from django.contrib import admin
from .models import Section,Worker,Works,Pictures,Comment
# Register your models here.

class Pictures(admin.TabularInline):
    model=Pictures
    extra=1 
class WorksAdmin(admin.ModelAdmin):
    
    list_display=['name','section','image_tag','likes','views']
    list_filter=['section']
    readonly_fields=('image_tag',)
    inlines=[
        Pictures
       
        ]
   

admin.site.register(Section)
admin.site.register(Worker)
admin.site.register(Works,WorksAdmin)