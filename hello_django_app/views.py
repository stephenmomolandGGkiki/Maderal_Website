from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "Favorite Quote",
                "message": "Other times we come downstairs feeling sunny already. Those are great days!"}
        return data
    
class AboutPageView (TemplateView):
    template_name = "resume.html"
    def get_context_data(self):
        data = {"message_title" : "W E B S I T E",
                "message1": "j&S HIGH SCHOOL: Camarines Sur National High School",
                "message": "Elementary: Milaor Central School"}
        return data

class ContactInfoPageView (TemplateView):
    template_name = "contactInfo.html"
    def get_context_data(self):
        data = {"message_title" : "Zaldy Maderal  ",
                "message1": "Address: Milaor Camarines Sur",
                "message2": "Email: maderalzaldy03@gmail.com",               
                "message3": "Mobile No. 09485828165"}
        return data

