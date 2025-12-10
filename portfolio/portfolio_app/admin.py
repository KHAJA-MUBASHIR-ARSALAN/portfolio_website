from django.contrib import admin
from .models import Skill,About,TimelineEntry,Profile,Internship,Project,Certificate


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'color')
    list_editable = ('percentage', 'color')
    search_fields = ('name',)
    list_filter = ('percentage',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('content', 'updated_at')

@admin.register(TimelineEntry)
class TimelineEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'entry_type', 'organization','start_day','start_month', 'start_year', 'end_day','end_month','end_year')
    list_filter = ('entry_type',)
    search_fields = ('title', 'organization', 'description')



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_order')
    ordering = ('display_order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)





@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issue_date')  # Show these columns in admin list view [1][2]
    search_fields = ('title', 'issuer')              # Enable search for these fields [2]