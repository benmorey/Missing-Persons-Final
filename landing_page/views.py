from django.shortcuts import render
from .models import MissingPersons

# Create your views here.
def landingPageView(request):
    return render(request, 'landing_page/index.html')


# This view requests all of our objects from our MissingPersons class, and calls the name of 
# entire data set "individuals". We then provide context, where we create a dictionary and 
# name each object "the_missing", and each objects set of data as "individuals". We then return
# a table (using html reference) and pass our class data to the table to organize our objects 
# and display object attributes (our missing persons data).
def tableView(request):
    individuals = MissingPersons.objects.all()
    context = {
        "the_missing" : individuals
    }
    return render(request, 'landing_page/table.html', context)


# This view requests all of our objects from our MissingPersons class, and calls the name of 
# entire data set "personsData". We will also use a variable called "id" here to filter our data
# by each objects id. In the table.html, we pull each objects primary key from our online database
# and assign it to our variable "personID". Here, we use that ID when we again request data from 
# our dataset, in order to pull each object (individual) with all of their data. We then
# create a dictionary and name each missing person as "missing_persons", and "personsData" as the 
# collection of information for each object. We then return to the individual html page for each 
# person where it calls the dictionary, and formats it into a table. 
def personView(request, personId):
    personsData = MissingPersons.objects.filter(
        id= personId
    ).get()
    context = {
        'missingpersons': personsData
    }
    return render(request, 'landing_page/individual.html', context)