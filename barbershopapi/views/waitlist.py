"""View module for handling requests about events"""
import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from barbershopapi.models import Waitlist, Barber, Customer, Service

class WaitlistView(ViewSet):
    """Barbershop waitlists"""

    def create(self, request):
        """Handle POST operations for waitlists
        Returns:
            Response -- JSON serialized waitlist instance
        """
        waitlist = Waitlist()
        customer = Customer.objects.get(user=request.auth.user)
        waitlist.barber = Barber.objects.get(pk=request.data['barber'])
        waitlist.time = datetime.datetime.now()
        waitlist.customer = customer
        waitlist.is_served = request.data["is_served"]
        

        try:
            waitlist.save()
            waitlist.waitlist_services.set(request.data["waitlist_services"])
            serializer = WaitlistSerializer(waitlist, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        """Handle GET requests to waitlists resource

        Returns:
            Response -- JSON serialized list of waitlists
        """
        # Get the current authenticated user
        waitlists = Waitlist.objects.all()

        serializer = WaitlistSerializer(
            waitlists, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        waitlists = Waitlist.objects.all()

        # Support filtering games by customer
        #    http://localhost:8000/waitlists?customer=1
        #
        # That URL will retrieve all tabletop games
        customer = self.request.query_params.get('customer', None)
        if customer is not None:
            waitlists = waitlists.filter(customer__id=customer)


        serializer = WaitlistSerializer(
            waitlists, many=True, context={'request': request})
        return Response(serializer.data[-1])


class WaitlistUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer's related Django user"""
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class WaitlistBarberSerializer(serializers.ModelSerializer):
    """JSON serializer for event organizer"""
    user = WaitlistUserSerializer(many=False)

    class Meta:
        model = Barber
        fields = ['user']

# class WaitlistServiceSerializer(serializers.ModelSerializer):
#     """JSON serializer for services organizer"""
#     class Meta:
#         model = Waitlist_Service
#         fields = ['service']

class WaitlistSerializer(serializers.ModelSerializer):
    """JSON serializer for Waitlists"""
    barber = WaitlistBarberSerializer(many=False)
    # waitlist_services = WaitlistServiceSerializer(many=True)

    class Meta:
        model = Waitlist
        fields = ('id', 'customer', 'barber',
                  'time', 'waitlist_services', 'is_served')
        depth = 1