from django.db import models
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe
# Create your models here.


class Section(models.Model):
    icons=models.CharField(_("Icons"), max_length=50)
    name=models.CharField(_("Section Name"), max_length=50)
    number=models.IntegerField(_("Number of workers"))
    short_description=models.CharField(_("Short description"), max_length=500)
    created_at=models.DateTimeField(_("Created at"), auto_now=False, auto_now_add=True)
    updated_at=models.DateTimeField(_("Updated at"), auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name
class Worker(models.Model):
    section=models.ForeignKey("Section", related_name='workers',verbose_name=_("Sections"), on_delete=models.CASCADE)
    name=models.CharField(_("Name_Surname"), max_length=50)
    phone_number=models.CharField(_("Phone Number"),max_length=20)
    email=models.EmailField(_("Email"), max_length=254)
    adress=models.CharField(_("Adress"), max_length=50)
    salary=models.FloatField(_("Salary"))
    years_of_experience=models.IntegerField(_("Years of experience"))
    data_about_worker=models.TextField(_("Datas about worker"))
    image=models.ImageField(_("Image"), upload_to="workers" )
    def image_tag(self):
        return mark_safe('<img src="%s"  height="50" />' % (self.image.url))
    image_tag.short_description='Image'
    def __str__(self):
        return self.name
class Works(models.Model):
    section=models.ForeignKey("sections.Section",related_name="works",  verbose_name=_("Section"), on_delete=models.CASCADE)
    name=models.CharField(_("Name"), max_length=50)
    main_image=models.ImageField(_("Main Image"), upload_to='works')
    description=models.TextField(_("Description"))
    likes=models.IntegerField(_("Likes"),default=0)
    views=models.IntegerField(_("Views"),default=0)
    def image_tag(self):
        return mark_safe('<img src="%s"  height="50" />' % (self.main_image.url))
    image_tag.short_description='Image'
    def __str__(self):
        return self.name
class Pictures(models.Model):
    works=models.ForeignKey("Works", verbose_name=_("Works"), on_delete=models.CASCADE)
    name=models.CharField(_("Name"), max_length=50)
    image=models.ImageField(_("Image"), upload_to='works')
    def __str__(self):
        return self.name
    def image_tag(self):
        return mark_safe('<img src="%s"  height="50" />' % (self.image.url))
    image_tag.short_description='Image'
class Comment(models.Model):
    author=models.CharField(_("Author"), max_length=50)
    comment=models.TextField(_("Comment"))
    def __str__(self):
        return self.author

