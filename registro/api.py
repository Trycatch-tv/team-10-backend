from rest_framework.response import Response
from .serializers import *
#from rest_framework.views import APIView
#from rest_framework import status
from rest_framework import viewsets, permissions

# class UserAPI(APIView):
#     def post(self,request):
#         serilizer=UserSerializer(data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
       
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=CategoriaUser.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = CategoriaSerializer        
            
class UserViewSet(viewsets.ModelViewSet):
    queryset=UserPersonalizado.objects.all()
    permission_classes = [permissions.AllowAny] 
    serializer_class = UserSerializer  