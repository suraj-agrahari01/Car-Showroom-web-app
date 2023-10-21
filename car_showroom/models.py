# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
class CarForSale(models.Model):
    car_for_sale_id = models.IntegerField(primary_key=True)
    manufacturers = models.CharField(max_length=20, blank=True, null=True)
    car_model_code = models.ForeignKey('CarModels', models.DO_NOTHING, db_column='car_model_Code', blank=True, null=True)  # Field name made lowercase.
    asking_price = models.FloatField(blank=True, null=True)
    date_acquired = models.DateTimeField(blank=True, null=True)
    reg_year = models.DateTimeField(blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_for_sale'

    def __str__(self):
        return str(self.car_for_sale_id)


class CarLoan(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    car_sold = models.ForeignKey('CarSold', models.DO_NOTHING, blank=True, null=True)
    finance_company = models.ForeignKey('FinanceCompany', models.DO_NOTHING, blank=True, null=True)
    loan_amount = models.FloatField(blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_loan'

    def __str__(self):
        return str(self.loan_id)


class CarModels(models.Model):
    car_model_code = models.CharField(primary_key=True, max_length=20)
    manufacturer_code = models.CharField(max_length=20, blank=True, null=True)
    model_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_models'

    def __str__(self):
        return self.car_model_code



class CarSold(models.Model):
    car_sold_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    sold_price = models.FloatField(blank=True, null=True)
    sold_date = models.DateTimeField(blank=True, null=True)
    payment = models.FloatField(blank=True, null=True)
    car_for_sale = models.ForeignKey(CarForSale, models.DO_NOTHING, blank=True, null=True)
    purchased_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_sold'

    def __str__(self):
        return str(self.car_sold_id)


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    cell_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    town_city = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=40, blank=True, null=True)

    
    
    

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return str(self.customer_id)


class CustomerPayment(models.Model):
    customer_payment_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    car_sold = models.ForeignKey(CarSold, models.DO_NOTHING, blank=True, null=True)
    customer_payment_date_due = models.DateTimeField(blank=True, null=True)
    customer_payemnt_date = models.DateTimeField(blank=True, null=True)
    customer_payment_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_payment'

    def __str__(self):
        return str(self.customer_payment_id)

class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    salary = models.FloatField(blank=True, null=True)
    joined_date = models.DateTimeField(blank=True, null=True)
    total_leave = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'

    def __str__(self):
        return str(self.employee_id)


class FinanceCompany(models.Model):
    finance_company_id = models.IntegerField(primary_key=True)
    finance_company_name = models.CharField(max_length=20, blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance_company'

    def __str__(self):
        return str(self.finance_company_id)


class InsuranceCompany(models.Model):
    insurance_company_id = models.IntegerField(primary_key=True)
    insurance_company_name = models.CharField(max_length=20, blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_company'

    def __str__(self):
        return str(self.insurance_company_id)


class InsurancePolicies(models.Model):
    policy_id = models.IntegerField(primary_key=True)
    car_sold = models.ForeignKey(CarSold, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    insurance_company = models.ForeignKey(InsuranceCompany, models.DO_NOTHING, blank=True, null=True)
    policy_start_date = models.DateTimeField(blank=True, null=True)
    monthly_payments = models.FloatField(blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_policies'


    def __str__(self):
        return str(self.policy_id)


class Servicing(models.Model):
    servicing_id = models.IntegerField(primary_key=True)
    car_sold = models.ForeignKey(CarSold, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    total_servicing_offered = models.IntegerField(blank=True, null=True)
    servicing_used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicing'


    def __str__(self):
        return str(self.servicing_id)
