from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

from .form import EmpForm
from rest_framework.decorators import api_view
from .serializers import AppraisalSerializer
from .models import Appraisal,manager
from employee.models import Employee


@api_view(['GET', 'POST', 'DELETE'])
def getappraisal(request):
    if request.method == 'POST':
        data=request.POST
        employee=Employee.objects.filter(manager_ID=data['manager_id'])
        appraisal=Appraisal.objects.filter(employee_ID__in=employee)
        data=[]
        for item in appraisal:
            temp={}
            temp['appraisal_id']=item.appraisal_ID
            temp['objective']=item.objective
            temp['review_year']=item.review_year
            temp['department_name']=item.department_ID.department_name
            temp['employee_name']=item.employee_ID.first_name+" "+item.employee_ID.last_name
            temp['rating']=item.rating
            data.append(temp)
        return JsonResponse(data,safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def getfs104(request):
    if request.method == 'POST':
        data=request.POST
        appraisal=Appraisal.objects.filter(employee_ID=data['employee_id'])
        data=[]
        for item in appraisal:
            temp={}
            temp['appraisal_id']=item.appraisal_ID
            temp['objective']=item.objective
            temp['review_year']=item.review_year
            temp['department_name']=item.department_ID.department_name
            temp['employee_name']=item.employee_ID.first_name+" "+item.employee_ID.last_name
            temp['rating']=item.rating
            data.append(temp)
        return JsonResponse(data,safe=False)

def appraisaldetail(request,id=None):
    appraisal=None

    if request.method=="POST":
        appraisalform=EmpForm(request.POST,instance=appraisal)
        if appraisalform.is_valid():
            data=request.POST
            appr=Appraisal.objects.filter(appraisal_ID=request.session.get('appraisalid')).update(
                objective=data['objective'],
                review_year=data['review_year'],
                department_ID=data['department_ID'],
                rating=data['rating']
            )
            return redirect('/appraisaldetail?id='+request.session.get('appraisalid'))
    if request.GET.get('appraisalid', ''):
        request.session['appraisalid']=request.GET.get('appraisalid', '')

        apprid=request.GET.get('appraisalid', '')
        appraisal = Appraisal.objects.get(appraisal_ID=apprid)
        appraisalform=EmpForm(instance=appraisal)
        return render(request,'editappraisal.html',{'form':appraisalform})

    id = request.GET.get('id', '')
    appraisal = Appraisal.objects.get(appraisal_ID=id)
    temp = {}
    temp['appraisal_id'] = appraisal.appraisal_ID
    temp['objective'] = appraisal.objective
    temp['review_year'] = appraisal.review_year
    temp['department_name'] = appraisal.department_ID.department_name
    temp['employee_name'] = appraisal.employee_ID.first_name + " " + appraisal.employee_ID.last_name
    temp['rating'] = appraisal.rating
    context=temp
    return render(request,'appraisaldetail.html',context)





def index(request):
    return render(request,'index.html')