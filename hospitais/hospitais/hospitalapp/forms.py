from django import forms
from .models import Hospitais

class Hospitalform(forms.ModelForm):
    class Meta:
        model = Hospitais
        fields = '__all__'


#<div>
#	<form action="." method="POST"> {% csrf_token %}
#		{{ form.as_p}}
#		<input type="submit" value="Enviar">
#	</form>
#</div>