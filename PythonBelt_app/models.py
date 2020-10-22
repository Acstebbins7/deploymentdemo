from django.db import models
import re
import datetime
#-------------------------------------------------------------------------------------------
#add the regex module here
#create manager class here.
class UserManager(models.Manager):
    def registerValidator(self, postData):
        errors = {}
        #name with if statements for each of these
        if len(postData['name']) == 0:
            errors['namereq']= "First name is required"
        #set this here for anything that needs to be a specific length of characters.
        elif len(postData['name']) < 3:
            errors['namereq']= "Name must be more than 3 characters."
        #username
        if len(postData['username']) == 0:
            errors['unamereq']= "User name is required"
        elif len(postData['username']) < 3:
            errors['unamereq']= "Name must be more than 3 characters."
        #password
        if len(postData['pw']) == 0:
            errors['pwreq']= "Password is required"
        elif len(postData['pw']) < 8:
            errors['pwreq']= "Password is required to be more than 8 characters"
        #date hired
        return errors
#login validator needs to have everything below in order to verify that the wrong username and password is correct before being allowed to login. 
    def loginValidator(self, postData):
        errors = {}
        userMatch= User.objects.filter(username= postData['username'])
        #username
        if len(userMatch) != 0:
            
            if postData['pw'] == userMatch[0].password:
                return errors 
            errors['pw']= "The password must match" 
            return errors
        errors['username']= "A username needs to match the registered username." 
        return errors

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
class WishManager(models.Manager):
    def wishValidator(self, postData):
        errors = {}
        
        #name with if statements for each of these
        # Destination
        if len(postData['destination']) == 0:
            errors['destinationreq']= "Destination is required"
        elif len(postData['destination']) < 3:
            errors['destinationreq']= "Destination must be more than 3 characters."
        return errors
        # Description Is Not Needed!
        # if len(postData['description']) == 0:
        #     errors['descriptionreq']= "Description is required"
        # elif len(postData['description']) < 3:
        #     errors['descriptionreq']= "Item name must be more than 3 characters."
        # return errors
        # Travel Date From
        if len(postData['travelStart']) == 0:
            errors['travelStartreq']= "Start Date is required"
        # elif len(postData['travelStart']) < 3:
        #     errors['travelStartreq']= "Item name must be more than 3 characters."
        return errors
        # Travel Date To
        if len(postData['travelEnd']) == 0:
            errors['travelEndreq']= "Return Date is required"
        # elif len(postData['description']) < 3:
        #     errors['descriptionreq']= "Item name must be more than 3 characters."
        return errors
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
class User(models.Model):
    name= models.CharField(max_length=255)
    username= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

#MAKE SURE THIS IS ACCURATE PER THE TABLE

class Wish(models.Model):
    destination= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    travelStart= models.DateField()
    travelEnd= models.DateField()
    #added_by= one to many
    added_by= models.ForeignKey(User, related_name="descriptionUploaded", on_delete= models.CASCADE)
    #likes= many to many 
    likes= models.ManyToManyField(User, related_name="likes")  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = WishManager()

    #don't use the many to many in the User class or the one to many.

