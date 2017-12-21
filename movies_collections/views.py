from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movies
from .forms import SearchingForm
from xlrd import open_workbook
import os
from django.conf import settings

results = ""

def index(request):
    # return 'success'
    return render(request,'base.html',{})


def displayAll(request):
    """ to display total data """
    results = Movies.objects.all()
    return render(request,'results.html',{'results':results})

def language_filter(request):
    """ to filter as per language basis """
    # results1 = ''
    results = Movies.objects.filter(language='english')
    return render(request,'results.html',{'results':results})
    # print results1
    # return render(request,'language_results.html',{'language_selection_result':results1})
    if request.method == "GET":
        lan = request.GET.get('lan')
        lan = str(lan).lower()
        print lan
        results = Movies.objects.filter(language='english')
        print results
        return render(request,'results.html',{'results':results})
    else:
        print "else"
        pass

    

def year_filter(request):
    """ to filter as per language basis """
    results = Movies.objects.filter(releaseyear='2017')
    return render(request,'results.html',{'results':results})

    if request.method == "GET":
        lan = request.GET.get('lan')
        lan = str(lan).lower()
        print lan
        results = Movies.objects.filter(releaseyear='2017')
        print results1
        return render(request,'results.html',{'results':results1})
    else:
        print "else"
        pass
    
    



def data_inserting(request):
    """ Exce data feeding into database model """    
    
    sheet_name = "movies"
    wb = open_workbook(os.path.join(settings.MEDIA_ROOT, "insert_data.xlsx"))
    if sheet_name == "movies":
        tasks = wb.sheet_by_name(sheet_name)   
        for row in range(1, tasks.nrows):           

            number_of_rows = tasks.nrows
            number_of_columns = tasks.ncols
            values = []
            for column in range(tasks.ncols):                    
                value  = (tasks.cell(row,column).value)                    
                values.append(value)
            Movies.objects.create(language=values[0],movie_name=values[1],typeofmovie=values[2],releaseyear=int(values[3]))
        return render(request, 'insert_log.html', {'message':'Records Inserted Successfully'})

    # Movies.objects.create(language='telugu',movie_name='Ninnukori',typeofmovie='romantic',releaseyear='2017')
    # Movies.objects.create(language='english',movie_name='Notebook',typeofmovie='romantic',releaseyear='2009')
    # return HttpResponse('one record inserted')

def search_filter(request):
    print "search_view"
    form = SearchingForm()
    results = ''
    year_data = '' 
    language_data = ''
    movies_data = ''
    if request.method == "GET":
        form = SearchingForm(request.GET)
        searching_word = request.GET.get('search_text')
        year_data = Movies.objects.filter(releaseyear__icontains=searching_word)
        print ">>>>>>>>",year_data
        language_data = Movies.objects.filter(language__icontains=searching_word)
        movies_data = Movies.objects.filter(movie_name__icontains=searching_word)

        print searching_word
    else:
        results = Movies.objects.all()        
    return render(request,'results.html',{'years_result':year_data,'languages_result':language_data,'titles_result':movies_data, 'results':results})
def gettingids(request):
    year_data=language_data=movies_data =""
    if request.method=="GET":

        language_value = request.GET.get('languages')
        year_value = request.GET.get('year')
        print language_value,year_value

        filter_data = Movies.objects.filter(releaseyear__icontains=year_value,language__icontains=language_value)
        print "--------------------------",filter_data
        print 
        pass

        return render(request,'results1.html',{'filter_data':filter_data,'years_result':year_data,'languages_result':language_data,'titles_result':movies_data, 'results':results})
    else:
        pass





