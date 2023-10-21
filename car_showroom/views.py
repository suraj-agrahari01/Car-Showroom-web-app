from django.http.response import HttpResponse

from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User 
from .models import Employees, Customer, CarModels,CarForSale,CarSold,CustomerPayment, FinanceCompany,InsuranceCompany,InsurancePolicies,CarLoan,Servicing

from django.db import connection


# Create your views here.

def index(request):
    overall_profit = CarSold.objects.raw("SELECT * FROM car_sold")
    profit = 0
    for content in overall_profit:
        profit += content.sold_price - content.purchased_price
        # print(profit)
    return render(request, 'showroom_base.html',{'profit':profit})

def employees(request):
    employees = Employees.objects.all()
    return render(request, 'employees.html', {'employees':employees})


def search_main(request):
   
   
    return render(request,'search_main.html',{})


def customer_search_detail(request,pk):
    
    obj=get_object_or_404(Customer,pk=pk)
    print(obj)
    print("hello this is me")
    return render(request,'customer_search_detail.html',{'obj':obj})
    
    


def search_result(request):
    if request.is_ajax():
        res=None
        customer=request.POST.get('customer')
      
        qs=Customer.objects.filter(customer_name__icontains=customer)
        if len(qs)>0 and len(customer)>0:
            data=[]
            for pos in qs:
                item={
                    'pk':pos.pk,
                    'name':pos.customer_name,
                    'email':pos.email
                }
                data.append(item)
                

            res=data

        else:
            res='No customer found'
      
        return JsonResponse({'data':res})


    return JsonResponse({})


  

def report(request):
    # content=CarForSale.objects.raw('SELECT manufacturers, SUM(asking_price) as price  FROM car_for_sale GROUP BY manufacturers')
    # print(content)
    x_axis=[]
    y_axis=[]
    # for item in content:
    #    x_axis.append(item.manufacturers)
    #    y_axis.append(item.price)

    # print(x_axis)
    
    # return render(request, 'report.html')

    with connection.cursor() as cursor:
        query = """SELECT manufacturers, SUM(asking_price) as price  FROM car_for_sale GROUP BY manufacturers"""
        cursor.execute(query)
        row = cursor.fetchall()
    content=list(row)
    

    for items in content:
        x_axis.append(items[0])
        y_axis.append(items[1])

    
    with connection.cursor() as cursor:
        query=""" SELECT n.car_for_sale_id,n.manufacturers,s.sold_price,s.car_sold_id
            FROM car_for_sale n
            JOIN car_sold s ON s.car_for_sale_id = n.car_for_sale_id;"""

        cursor.execute(query)
        row = cursor.fetchall()
    content=list(row)
    new_content=[]

    for item in content:
        new_content.append(list(item))

    
    with connection.cursor() as cursor:
        query=""" select insurance_company_name , count(*) from (select n.insurance_company_id,n.policy_id,s.insurance_company_name
        from insurance_policies n 
            join insurance_company s on s.insurance_company_id=n.insurance_company_id) as b group by insurance_company_name ;
                                                    """

        cursor.execute(query)
        row = cursor.fetchall()
    
    insurance_company_name=[]
    insurance_times=[]

    for i in row:
        insurance_company_name.append(i[0])
        insurance_times.append(i[1])

    with connection.cursor() as cursor:
        query="""select manufacturers,sum(servicing_used) servicing_used ,sum(total_servicing_offered) servicing_offered  from
        (select p.car_sold_id,p.manufacturers,q.servicing_id,q.total_servicing_offered,q. servicing_used 
            from(select n.car_for_sale_id,n.manufacturers,s.car_sold_id
        from car_for_sale n 
            join car_sold s on s.car_for_sale_id=n.car_for_sale_id ) p
            join servicing q on q.car_sold_id=p.car_sold_id) as b group by manufacturers;

                                                    """

        cursor.execute(query)
        row = cursor.fetchall()
    
    servicng_used_percent=[]
    manufacturers=[]

    for item in row:
        servicng_used_percent.append(int((item[2]-item[1])/item[2]*100))
        manufacturers.append(item[0])

    


    with connection.cursor() as cursor:
        query="""select employee_id,CONCAT(first_name ,  " ", last_name  )as Name,total_leave,salary from employees;

                                                    """

        cursor.execute(query)
        row = cursor.fetchall()
        salary=[]


    customer_id=[]
    total_leave=[]

    for item in row:
        customer_id.append(item[0])
        total_leave.append(item[2])
        salary.append(item[3])

    
    

    

   


    

    return render(request,'report1.html',{'x_axis':x_axis,'y_axis':y_axis,'table_data':new_content,'insurance_company_name':insurance_company_name,'insurance_times':insurance_times,'servicng_used_percent':servicng_used_percent,'manufacturers':manufacturers,'customer_id':customer_id,'total_leave':total_leave,'salary':salary})


    


        



def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html',{'customers':customers})

def car_models(request):
    car_models = CarModels.objects.all()
    return render(request, 'car_models.html',{'car_models':car_models})

def car_for_sales(request):
    car_for_sales = CarForSale.objects.all()

    
    return render(request, 'car_for_sales.html', {'cars_for_sales':car_for_sales})
    
    
def car_sold(request):
    car_sold = CarSold.objects.all()
    return render(request, 'car_sold.html',{'cars_sold':car_sold})

def car_loans(request):
    car_loans = CarLoan.objects.all()
    return render(request, 'car_loans.html', {'car_loans':car_loans})

def customer_payment(request):
    customer_payment = CustomerPayment.objects.all()
    return render(request, 'customer_payment.html', {'customer_payments':customer_payment})

def finance_company(request):
    finance_company = FinanceCompany.objects.all()
    return render(request, 'finance_company.html',{'finance_companies':finance_company})

def insurance_company(request):
    insurance_company = InsuranceCompany.objects.all()
    return render(request, 'insurance_company.html',{'insurance_companies':insurance_company})

def insurance_policies(request):
    insurance_policies = InsurancePolicies.objects.all()
    return render(request, 'insurance_policies.html',{'insurance_policies':insurance_policies})

def servicings(request):
    servicings =  Servicing.objects.all()
    
    return render(request, 'servicings.html',{'servicings':servicings})


def showroom_login(request):
        
    if request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # messages.error(request, f'Welcome To Thapathali Campus, {user.username}')
                return redirect('/admin')
                
            else:
                return redirect('/login')
        # else:
            # print('Invalid User name')
    return render(request, 'showroom_login.html')

def showroom_logout (request):
    logout(request)
    return redirect('/')
    