from django.contrib import admin
from car_showroom.models import CarForSale,Customer,CarLoan,FinanceCompany,InsuranceCompany,InsurancePolicies,CarModels,CarSold,CustomerPayment,Employees,Servicing

admin.site.site_title = 'Car Showroom'
admin.site.site_header = 'Car Showroom admin panel'
# Register your models here.
admin.site.register(CarSold)
admin.site.register(CarLoan)
admin.site.register(CarModels)
admin.site.register(CarForSale)
admin.site.register(Customer)
admin.site.register(CustomerPayment)
admin.site.register(Employees)
admin.site.register(FinanceCompany)
admin.site.register(InsuranceCompany)
admin.site.register(InsurancePolicies)
admin.site.register(Servicing)