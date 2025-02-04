from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from.serializer import UserRegistrationserializer,UserLoginSerializer,UserProfileserializer,UserChangePassserializer,ResetPassEmailSerializer,UserPasswordResetSerializer
from django.contrib.auth import authenticate
from accounts.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegistrationserializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token= get_tokens_for_user(user)
            return Response({'token':token,'MSG':'REGISTRATION SUCCESSFUL!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
       
    
class UserLoginView(APIView):
    
    renderer_classes=[UserRenderer]

    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data) 
        if serializer.is_valid():
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email ,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'MSG':'LOGGED IN SUCCESSFULLY!!'},status=status.HTTP_201_CREATED)
            else:
                return Response({'errors':{'non_field_errors':['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        seraializer=UserProfileserializer(request.user)
        return Response(seraializer.data,status=status.HTTP_200_OK)
    

class UserchangePass(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer= UserChangePassserializer(data=request.data,context={'user':request.user})
        if serializer.is_valid():
            return Response({'MSG':'password changed successfully!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
    
    
class  PassResetPassEmailView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=ResetPassEmailSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'MSG':'password reset lInk send ! Please check your email '},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserPasswordResetView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer=UserPasswordResetSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid():
            return Response({'MSG':'password Reset successfully!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   

    
        
        
    
    
    
    
        
        

           
        
        
        
        
        
            
            
        
       
        
    
    

  
 
 
 