from multiprocessing import context
from operator import ge

from django.shortcuts import render
from matches.utils import get_points_table

# Create your views here.
def home(request):
    table = get_points_table()
    context ={
        "table":table
    }
    return render(request, "home.html",context)