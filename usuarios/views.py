from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class RegistrarUsuarioView(View):
	
	template_name= 'registrar.html'
	
	def get(self):
		return render(request,self.template_name)

	def post(self):
		return render(request, self.template_name)