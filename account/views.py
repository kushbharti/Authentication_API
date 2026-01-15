from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer,SendPasswordResetEmailSerilaizer,UserPasswordResetSerializer
from account.renderers import UserRenderer
from account.utils.tokens import get_tokens_for_user
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'message':'Registration Success','User': serializer.data,"token":token},status=status.HTTP_201_CREATED)
       
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes= [UserRenderer]

    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data.get('user')
            token = serializer.validated_data.get('token')
            
            return Response(
                {'message': 'Login Success',
                 'User':{'name':user.name,
                         'email':user.email,
                         },
                 "token":token
                 },
                status=status.HTTP_200_OK
            )
    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    renderer_classes= [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class UserChangePasswordView(APIView):
    renderer_classes= [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = UserChangePasswordSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(
            {'message': 'Password changed successfully'},
            status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetEmailView(APIView):
    renderer_classes= [UserRenderer]
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerilaizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'Password Reset link sent. Please Check your Email'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer = UserPasswordResetSerializer(data= request.data,context={
            'uid':uid,
            'token':token
        })
        if serializer.is_valid(raise_exception=True):
            return Response({'message':'Password Reset Successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)