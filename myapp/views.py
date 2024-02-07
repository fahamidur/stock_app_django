from django.views.generic import ListView
from .models import StockData

class StockListView(ListView):
    model = StockData
    template_name = 'myapp/stock_list.html'  # Specify the template containing your table
    context_object_name = 'stocks'
