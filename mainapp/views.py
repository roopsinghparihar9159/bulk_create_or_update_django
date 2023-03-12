from django.shortcuts import render
from .models import Customer
import pandas as pd
from datetime import datetime

# Create your views here.
def index(request):
    
    return render(request,'mainapp/index.html')

def dateformatechange(datechannge):
    print(type(datechannge))
    result_datechange = datetime.strptime(datechannge, "%Y-%m-%d")
    print(result_datechange)
    return 

def csv_upload(request):
    if request.method =="POST":
        df = pd.read_csv(request.FILES['file'],delimiter=',')
        # list_of_csv = [list(row) for row in df.values]
        df['Transaction_date'] = df['Transaction_date'].astype('datetime64[ns]')
        
        customer_create = list()
        customer_update = list()
    
        count = 0
        for df_data in df.to_dict(orient='records'):
            exist_transid = Customer.objects.filter(transid=df_data['Transaction_ID'])
            count = count+1
            if exist_transid.exists():
                print("Record available")
                exist_transid = exist_transid.get()
                exist_transid.transdate = df_data.get('Transaction_date')
                exist_transid.gender = df_data.get('Gender')
                exist_transid.age = df_data.get('Age')
                exist_transid.maritalstatus = df_data.get('Marital_status')
                exist_transid.statenames = df_data.get('State_names')
                exist_transid.employeestatus = df_data.get('Employees_status')
                exist_transid.segment = df_data.get('Segment')
                exist_transid.paymentmode = df_data.get('Payment_method')
                exist_transid.referal = df_data.get('Referal')
                exist_transid.amountspent = df_data.get('Amount_spent')
                customer_update.append(exist_transid)
            else:
                print("Record not available")
                customer_create.append(
                Customer(transid=df_data['Transaction_ID'],
                    transdate=df_data['Transaction_date'],
                    gender=df_data['Gender'],
                    age=df_data['Age'],
                    maritalstatus=df_data['Marital_status'],
                    statenames=df_data['State_names'],
                    employeestatus=df_data['Employees_status'],
                    segment=df_data['Segment'],
                    paymentmode=df_data['Payment_method'],
                    referal=df_data['Referal'],
                    amountspent=df_data['Amount_spent']
                ))
        print(count)

        if customer_create:
            Customer.objects.bulk_create(customer_create)

        if customer_update:
            Customer.objects.bulk_update(customer_update, ['transdate', 'gender', 'age', 'maritalstatus', 'statenames', 'employeestatus', 'segment', 'paymentmode', 'referal','amountspent'])

    return render(request,'mainapp/success.html')
