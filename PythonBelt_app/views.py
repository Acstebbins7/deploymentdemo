from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Wish

#-------------------------------------------------------------------------------------------
# Create your views here.
def index(request):
    return redirect("/main")
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def main(request):
    if 'loggedInId' in request.session:
        return redirect("/dashboard")
    return render(request, "main.html")
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def register(request):
    #print(request.POST) to see the terminal response. 
    print(request.POST)
    #in order for the register to work you need to include the resultFromValidator
    resultFromValidator = User.objects.registerValidator(request.POST)
    #print is used to show in the terminal and i can check if this actually works
    print("RESULTS FROM THE VALIDATOR BELOW")
    print(resultFromValidator)

    #if there are any error messages, the length of the resultFromValidator will be greater than 0
    if len(resultFromValidator)>0:
        #for each error message, we are sending the message to the messages framework that allows us to send messages to the html for one refresh
        for key, value in resultFromValidator.items():
            messages.error(request, value)
            #after storing the error messages in the messages framework, redirect them to the route that takes us to the form
        return redirect("/")
    #If they fill the form out properly with no error messages, create a user using the form information. 
    newUser = User.objects.create(name= request.POST['name'], username= request.POST['username'], password=request.POST['pw'])
    #print to see the output in the terminal
    print("Here is the newuser that got awjkerngoaerngoerngoerngakjrgnowerg")
    print(newUser.id)
    #REMEMBER THIS FOR BLACK BELT EXAM!
    request.session['loggedInId'] = newUser.id
    #Now it needs to redirect to the /success page. Create a new "success.html"
    return redirect("/dashboard")
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def login(request):
    #print(request.POST) helps for debugging issues while building the project
    print(request.POST)
    resultFromValidator = User.objects.loginValidator(request.POST)
    print("PRINTING FROM THE VALIDATOR TO WORK")
    print(resultFromValidator)
    #if the length of result is greater than zero, run this for loop.
    #for key, value (pair) in resultsFromValidator.items() 
    if len(resultFromValidator)>0:
        for key, value in resultFromValidator.items():
            messages.error(request, value)
        return redirect("/")

    #if we are here that means the login was valid
    userMatch= User.objects.filter(username= request.POST['username'])
    request.session['loggedInId'] = userMatch[0].id
    return redirect("/dashboard")
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def home(request):
    if 'loggedInId' not in request.session:
        return redirect("/")
    loggedInUser = User.objects.get(id=request.session['loggedInId'])
    likes = Wish.objects.filter(likes= loggedInUser)
    nolike = Wish.objects.exclude(likes= loggedInUser)
    #
    context = {
        'loggedInUser': loggedInUser,
        'likes': likes,
        'nolike': nolike 
    }
    return render(request, "dashboard.html", context)
    #Never forget to add context in the return render(request, "dashboard.html", CONTEXT)
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def logout(request):
    #this will clear the (request.session)
    request.session.clear()
    return redirect('/')
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def addItem(request):
    return render(request, "addItem.html")
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def show(request, wishid):
    context = {
        'wishShow': Wish.objects.get(id=wishid),
        'wishLikes': Wish.objects.get(id=wishid).likes.all(), 
    }
    return render(request, "show.html", context)
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def processItem(request):
    resultFromValidator = Wish.objects.wishValidator(request.POST)
    if len(resultFromValidator)>0:
        for key, value in resultFromValidator.items():
            messages.error(request, value)
        return redirect("/wish_items/create")
    wishCreate= Wish.objects.create(destination= request.POST['destination'], description= request.POST['description'], travelStart= request.POST['travelStart'], travelEnd= request.POST['travelEnd'], added_by=User.objects.get(id=request.session['loggedInId']))
    Wish.objects.get(id=wishCreate.id).likes.add(User.objects.get(id=request.session['loggedInId']))
    print(wishCreate)
    return redirect('/')
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def wishAdd(request, wishid):
    newWish= Wish.objects.get(id=wishid).likes.add(User.objects.get(id= request.session['loggedInId']))
    return redirect('/')
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def removeWish(request, wishid):
    notWish= Wish.objects.get(id=wishid).likes.remove(User.objects.get(id= request.session['loggedInId']))
    return redirect('/')
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
def deleteWish(request, wishid):
    c= Wish.objects.get(id=wishid)
    c.delete()
    return redirect('/dashboard')