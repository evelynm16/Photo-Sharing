from django.views.generic import TemplateView

# 让自定义helloWorld view 继承了template view，就可以用templateView里的很多func和attribute

class HelloWorld(TemplateView):
    template_name = 'test.html'
