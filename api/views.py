from django.shortcuts import render
# admin : username = api pass= 12345api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def get_logs(request):
    logs = Log.objects.all()
    serializer = LogSerializer(logs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_logs(request):
    serializer = LogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.error, status=400)

@api_view(['GET'])
def get_log(request,hp):
    try:
        log = Log.objects.get(pk=hp)
        serializer = LogSerializer(log)
        return Response(serializer.data)
    except Log.DoesNotExist:
        return Response({'error':"Log not found"},status=404)



@api_view(['PUT','PATCH'])
def update_log(request, hp):
    try:
        log = Log.objects.get(pk=hp)
    except Log.DoesNotExist:
        return Response({"error":"log not found"},status=404)
    
    serializer = LogSerializer(log,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error, status=400)    
    
@api_view(['DELETE'])
def delete_log(request, hp):
    try:
        log = Log.objects.get(pk=hp)
        log.delete()
        return Response({"message":'Log deleted successfully'},status=204)
    except Log.DoesNotExist:
        return Response({"error":"log not found"},status=404)
    
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.utils.timezone import now, timedelta

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        ip = request.META.get('REMOTE_ADDR')
        device = request.META.get('HTTP_USER_AGENT')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            Log.objects.create(user=user,event='login_success',ip=ip,device=device,timestamp=now(),message='user logged in successfully',severity='low')
            return JsonResponse({'message':'Login successful'})
        else:
            recent_attempts = Log.objects.filter(event='login_failed',ip=ip,timestamp__gte=now() - timedelta(minutes=10))

            attempt_count = recent_attempts.count()

            if attempt_count >= 10:
                severity = 'critical'
            elif attempt_count >= 5:
                severity = 'high'
            else:
                severity = 'medium'

            Log.objects.create(event='login_failed',ip=ip,device=device,timestamp=now(),message=f'Failed login attempt for user : {username}',severity = severity)
        return JsonResponse({'error':'Invalid credentials'},status=401)
    return JsonResponse({'error':'Only POST requests are allowed'}, status=405)



from django.contrib.auth import logout
csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        ip = request.META.get('REMOTE_ADDR')
        device = request.META.get('HTTP_USER_AGENT')
        user = request.user if request.user.is_authenticated else None

        logout(request)

        Log.objects.create(user=user,event='logot_success',ip=ip,device=device,timestamp=now(),message='user logged out successfully',severity='low')
        return JsonResponse({'message':'Logout successful'})
    return JsonResponse({'error':'Only POST requests are allowed'},status=405)


from rest_framework import viewsets

class LogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Log.objects.all()
    serializers_class = LogSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        event = request.query_params.get('event')
        severity = request.query_params.get('severity')
        ip = request.query_params.get('ip')
        user = request.query_params.get('user')

        if event : 
            queryset = request.filter(event=event)
        if severity:
            queryset = request.filter(severity=severity)
        if ip : 
            queryset = request.filter(ip=ip)
        if user : 
            queryset = request.filter(user=user)
        return queryset
    

from django.db.models import Count

@api_view(['GET'])
def log_summary_view(request):
    summary = (
        Log.objects.values('severity')
        .annotate(severity_count=Count('id'))
        .order_by('severity')
        )
    
    result = {entry['severity']: entry['severity_count'] for entry in summary}
    return Response(result)

@api_view(['GET'])
def recent_logs_view(request):
    recent_logs = Log.objects.order_by('-timestamp')
    serializer = LogSerializer(recent_logs,many=True)
    return Response(serializer.data)


# def home(request):
#     return render(request,'home.html')