from rest_framework import serializers
from .models import User
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from. utils import Utill 



class UserRegistrationserializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True  
    )

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password!=password2 :
          raise serializers.ValidationError("password and confirm password didn't match  ")
       
        return attrs    
    
    # AS WE ARE USING THE CUSTOM MODEL SO WE NEED TO DEFINW THIS    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model=User
        fields=['email','password']
        
 
        
class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','name'] 
        
    
        
        
class UserChangePassserializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)  
    password2=serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)  
    class Meta:
        model=User
        fields=['password','password2']    
        
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        user=self.context.get('user')
        if password!=password2 :
          raise serializers.ValidationError("password and confirm password didn't match  ")
        user.set_password(password)
        user.save()
      
       
        return attrs  
    
    
    
class ResetPassEmailSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model=User
        fields=[ 'email']
    def validate(self, attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exists:
            user=User.objects.get(email=email)
            uid=urlsafe_base64_encode(force_bytes(user.id))
            print('ENCODED UID :',uid)
            print('--------------------------------------')
            token=PasswordResetTokenGenerator().make_token(user)
            print('PASSWORD RESET TOKEN:', token)
            print('-----------------------------------------------')
            link='http://localhost:3000/api/user/reset'+uid+'/'+token
            print('Password reset link',link)
            # SEND EMAIL    
            body='click on the link to reset the password ' +link
            data={
               'subject':'Reset your password',
               'body':  body,
               'to_email':user.email   
            }
            Utill.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError("You are not a registered user")
   
        
      
class UserPasswordResetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)  
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)  

    class Meta:
        model = User
        fields = ['password', 'password2']    

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')

            if password != password2:
                raise serializers.ValidationError("Password and confirm password didn't match")

            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError('TOKEN IS INVALID OR EXPIRED')

            user.set_password(password)
            user.save()

            return attrs

        except DjangoUnicodeDecodeError:
            raise serializers.ValidationError('Token is invalid or expired')
