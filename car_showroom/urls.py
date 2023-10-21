from django.urls import path
from. import views

from .views import search_result

urlpatterns = [
    path('',views.index),
    path('employees/',views.employees),
    path('customers/',views.customers),
    path('car_models/',views.car_models),
    path('car_sold/',views.car_sold),
    path('car_for_sales/',views.car_for_sales),
    path('customer_payment/',views.customer_payment),
    path('finance_company/',views.finance_company),
    path('insurance_policies/',views.insurance_policies),
    path('insurance_company',views.insurance_company),
    path('car_loans/',views.car_loans),
    path('servicings/',views.servicings),
    path('login/',views.showroom_login),
    path('logout/',views.showroom_logout),
    path('report/',views.report),
    path('search_result/',views.search_result),
     path('<int:pk>/',views.customer_search_detail),
    path('search_main/',views.search_main),
]