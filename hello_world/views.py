from datetime import date
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . models import UserDetail
from . serializers import UserSerializer


class UserView(generics.RetrieveUpdateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_name'

    # def update(self, *args, **kwargs):
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        content = data['user_name']
        if data['dateOfBirth'][5:] == date.today().strftime("%m-%d"):
            response = ("Hello, %s! Happy birthday!" % content)
            return Response({'message': response}, status=status.HTTP_200_OK)
        else:
            bday = data['dateOfBirth']
            bday_ar = bday.split('-')
            today_date = date.today().strftime("%Y-%m-%d")
            today_ar = today_date.split('-')
            bdate = date(2017, int(bday_ar[1]), int(bday_ar[2]))
            tdate = date(2017, int(today_ar[1]), int(today_ar[2]))
            diff = bdate - tdate
            day = diff.days
            if day < 0:
                bdate = date(2020, int(bday_ar[1]), int(bday_ar[2]))
                tdate = date(2019, int(today_ar[1]), int(today_ar[2]))
                day = (tdate-bdate).days
                response = ("Hello, %s! Your birthday is in %i days!" % (content, abs(day)))
                return Response({'message': response}, status=status.HTTP_200_OK)
            response = ("Hello, %s! Your birthday is in %i days!" % (content, day))
        return Response({'message': response}, status=status.HTTP_200_OK)
