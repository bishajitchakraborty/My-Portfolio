
from django.contrib import admin
from nested_inline.admin  import NestedModelAdmin,NestedStackedInline
from .models import About,Educations,Skills,Experiernces,Profile,Testimonials,Services,Message,Professions,Category,Images,Portfolio_projects,Contact

class SkillsInline(admin.StackedInline):
    model = Skills
    extra = 1

class ExperierncesInline(admin.StackedInline):
    model = Experiernces
    extra = 1
   
class EducationsInline(admin.StackedInline):
    model = Educations
    extra = 1


class TestimonialsInline(NestedStackedInline):
    model = Testimonials
    extra = 1


class ServiceInline(NestedStackedInline):
    model = Services
    extra = 1

class MessageInline(NestedStackedInline):
    model = Message
    extra = 1

class ProfessionsInline(NestedStackedInline):
    model = Professions
    extra = 1

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1

class ImageInline(NestedStackedInline):
    model = Images
    extra = 1

class Portfolio_projectsInline(NestedStackedInline):  
    model = Portfolio_projects
    extra = 1
    inlines = [ImageInline]
   
    
# class Portfolio_projectsAdmin(NestedStackedInline):
#     inlines = [Portfolio_projectsInline]
#     model=Portfolio_projects

class ProfileAdmin(NestedModelAdmin):
    inlines = [TestimonialsInline,ServiceInline,MessageInline,ProfessionsInline,Portfolio_projectsInline]

    model=Profile

class AboutAdmin(admin.ModelAdmin):
    inlines = [SkillsInline,ExperierncesInline,EducationsInline,]
    class Meta:
        model=About

admin.site.register(Profile,ProfileAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Skills)
admin.site.register(Contact)
admin.site.register(Experiernces)
admin.site.register(Educations)
admin.site.register(Testimonials)
admin.site.register(Services)
admin.site.register(Message)
admin.site.register(Professions)
admin.site.register(Category)
# admin.site.register(Portfolio_projects,Portfolio_projectsAdmin)
admin.site.register(Images)