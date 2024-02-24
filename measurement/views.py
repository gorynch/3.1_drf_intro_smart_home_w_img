from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer
from rest_framework.parsers import JSONParser

# опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    

class SensorIdView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        json_response=JSONParser().parse(request)
        editing_object=Sensor.objects.get(id=pk)
        editing_object.update(**json_response)
        if editing_object.is_valid():
            ser = editing_object
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    


class MeasurmentView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            meas_data = serializer.save()
            serializer = MeasurementSerializer(meas_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)