from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(help_text="Skill percentage (0 to 100)")
    color = models.CharField(max_length=7, default="#4fcc2a", help_text="Color for progress circle")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']  # Highest skill first
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"
    






class About(models.Model):
    content = models.TextField()  # About text
    image = models.ImageField(upload_to="about/", blank=True, null=True)  # About image
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Section"
    


class TimelineEntry(models.Model):
    ENTRY_TYPE_CHOICES = [
        ("education", "Education"),
        ("experience", "Experience"),
    ]
    entry_type = models.CharField(max_length=16, choices=ENTRY_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True)

    # Keep year nullable in DB (we'll enforce in forms)
    start_year = models.PositiveIntegerField(blank=True, null=True)
    end_year = models.PositiveIntegerField(blank=True, null=True)

    # New optional fields for month/day
    start_month = models.PositiveIntegerField(blank=True, null=True)
    start_day = models.PositiveIntegerField(blank=True, null=True)
    end_month = models.PositiveIntegerField(blank=True, null=True)
    end_day = models.PositiveIntegerField(blank=True, null=True)

    description = models.TextField(blank=True)
    icon_image = models.ImageField(upload_to='timeline_icons/', blank=True, null=True)

    link = models.URLField(blank=True, null=True)
    link_image = models.ImageField(upload_to='timeline_link_images/', blank=True, null=True)

    class Meta:
        ordering = [
            "-end_year", "-end_month", "-end_day",
            "-start_year", "-start_month", "-start_day",
            "-id",  # tiebreaker
        ]

    def __str__(self):
        return f"{self.get_entry_type_display()}: {self.title}"

    def get_start_date_display(self):
        if self.start_day and self.start_month and self.start_year:
            return f"{self.start_day:02d}/{self.start_month:02d}/{self.start_year}"
        if self.start_month and self.start_year:
            return f"{self.start_month:02d}/{self.start_year}"
        if self.start_year:
            return f"{self.start_year}"
        return ""

    def get_end_date_display(self):
        if not self.end_year:
            return "Present"
        if self.end_day and self.end_month:
            return f"{self.end_day:02d}/{self.end_month:02d}/{self.end_year}"
        if self.end_month:
            return f"{self.end_month:02d}/{self.end_year}"
        return f"{self.end_year}"

    



class Profile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/')
    cta_text = models.CharField(max_length=100, default="Let's get started →")
    cta_link = models.URLField(blank=True, null=True)  # Optional link for button

    def __str__(self):
        return self.name

class Internship(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='internship_logos/')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name
    


class Project(models.Model):
    title = models.CharField(max_length=255)  # Optional: project title for easy ID
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True, null=True)  # Optional URL to project/demo
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    


    
class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    issue_date = models.DateField()

    certificate_image = models.ImageField(
        upload_to='certificates/',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["-issue_date"]  # ✅ Latest certificate on top

    def __str__(self):
        return f"{self.title} ({self.issuer})"
