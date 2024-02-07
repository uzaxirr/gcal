from rest_framework.views import APIView
from rest_framework.response import Response

from mycalendar.models import Event
from mycalendar.serializers import EventSerializer


class EventView(APIView):
    def post(self, request):
        serialized_event = EventSerializer(data=request.data)
        if serialized_event.is_valid():
            serialized_event.save()
            return Response(serialized_event.data, status=201)
        return Response(serialized_event.errors, status=400)

    def put(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=404)

        serialized_event = EventSerializer(event, data=request.data)
        if serialized_event.is_valid():
            serialized_event.save()
            return Response(serialized_event.data)
        return Response(serialized_event.errors, status=400)

    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=404)

        serialized_event = EventSerializer(event)
        return Response(serialized_event.data)


class UserEventsView(APIView):
    def get(self, request, user_id):
        events = Event.objects.filter(createdBy=user_id)
        serialized_events = EventSerializer(events, many=True)
        return Response(serialized_events.data)
