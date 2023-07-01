
import csv
from django.shortcuts import render
from .models import Dish

from thefuzz import fuzz , process
import json


# Create your views here.


def HomePage(request):
    d = Dish.objects.get(id=2)

    d = json.loads(d.detail)

    print(d['user_rating']['aggregate_rating'])
    print(d['location']['city'])

    return render(request ,"home.html")



def searchFood(request):
    if request.method=='POST':
        data = request.POST['foodName']

    allMatchingFood = []
    
    dish = Dish.objects.all()
    for d in dish:
        
        item=  json.loads(d.items) 
        d_id = d.id 

        list_of_food = list(item.keys())
        
        list_of_food = process.extract(data , list_of_food , limit=1)

        for i in range(len(list_of_food)):
            p = item[list_of_food[i][0]]
            list_of_food[i]= [list_of_food[i][0],list_of_food[i][1],p,d_id]
            
            
        allMatchingFood.extend(list_of_food)

    allMatchingFood.sort(key= lambda x:(-x[1],x[2]))

    goodMatchingFood = allMatchingFood[:20]

    for i in range(len(goodMatchingFood)):
        
        resName = Dish.objects.get(id= goodMatchingFood[i][3])
        goodMatchingFood[i][3]= resName.restaurantName

        if resName.detail:
            detailsRes = json.loads(resName.detail)
            goodMatchingFood[i][1]= detailsRes['user_rating']['aggregate_rating']
            
            if detailsRes['location']['city'] and detailsRes['location']['address']:
                goodMatchingFood[i].append(detailsRes['location']['city'] +", "+ detailsRes['location']['address']) 
            else: 
                goodMatchingFood[i].append(resName.location)

        else:
            goodMatchingFood[i][1]= 'Not Avaulable'
            goodMatchingFood[i].append(resName.location)

    return render(request ,'foodSearch.html' , {
        "searched":data,
        "goodMatchingFood": goodMatchingFood,
    })



    



# def CreateDbFromCSV(request):
#     print("Start th job ################")

#     # opening the CSV file
#     with open('../restaurants_small.csv', mode ='r') as file:   
        
#         # reading the CSV file
#         csvFile = csv.DictReader(file)
 
#         # displaying the contents of the CSV file
        
#         for lines in csvFile:
#             dish = Dish(dishId=lines['id'] , restaurantName= lines['name'] ,location= lines['location'] , items= lines['items'] , lat_long= lines['lat_long'] , detail=lines['full_details'])
#             dish.save()
        

#     return render(request , 'home.html')