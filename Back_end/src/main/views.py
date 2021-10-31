import sys
import os
#sys.path.append(r"C:\Users\\User\\Desktop\\Turbo.az\\src")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../..')))
from django.contrib.messages.views import SuccessMessageMixin
from django.http.response import JsonResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from . forms import ContactForm
import features as f


def get_json_car_data(request):
    qs_val=f.brand_json_format_list('Brand')
    return JsonResponse({'data': qs_val})

def get_json_model_data(request, *args, **kwargs):
    selected_car=kwargs.get('car')
    obj_models=f.model_json_format_list(selected_car)
    return JsonResponse({'data': obj_models})

def MainView(request):
    context={
        'fuel_type': f.return_feature_list('FuelType'),
        'ban_type': f.return_feature_list('BanType'),
        'color': f.return_feature_list('Color'),
        'power_engine': f.return_feature_list('EngPow'),
        'transmission': f.return_feature_list('Transmission'),
        'gear_box': f.return_feature_list('Gearbox'),
        'prod_year': f.return_feature_list('ProdYear'),
        'city_name': f.return_feature_list('City'),
        'volume_engine': f.return_feature_list('EngVol'),
    }

    if request.method == 'POST':
        form_list=[]
        initial_list=list(request.POST.items())
        form_list=initial_list[1::]
        print("Final result List: ", form_list)
        context['price_min'], context['price_max']=f.get_price(form_list)
    return render(request, 'index.html', context)


class ContactView(SuccessMessageMixin, FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('contact')
    success_message='Succesfully submitted!'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)






    
