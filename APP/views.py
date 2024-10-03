from django.shortcuts import render, redirect
from . models import UserPredictModel
from . forms import UserPredictForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import pandas as pd



#from tensorflow import keras
from PIL import Image, ImageOps
from . import forms

import pickle

def Landing_0(request):
    return render(request, '1_Landing.html')


def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login1')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

# def input(request):
#     return render(request, 'input.html')
def login1(request):
    return render(request,"upload_file.html")
def predit(request):
    return render(request,"predition.html")



def handle_uploaded_file(f):
    print('check',f)
    # You can implement different logic here based on the file extension if needed
    # For simplicity, assuming all uploaded files are CSVs
    df = pd.read_csv(f)
    # df = pd.read_csv(f, encoding='utf-8', errors='ignore')
    return df
df=None
def upload_file(request):
    global df, df_list
 
    print("inside upload------------------------------------------------------------------------")
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        df = handle_uploaded_file(uploaded_file)
        df_list = df.to_dict(orient='records')
        #print('check df',df_list)

        # Print the DataFrame (for demonstration purposes)
        #print(df)

        # Render the DataFrame in a template (optional)
        return render(request, 'dataFrame.html', {'dataframe': df_list})
    return render(request, 'upload_file.html')

def output(request):
    
    print("inside file------------------------------------------------------------------------")
    global df,df_list
    print("qqq4444qqqq")
    #df_list1 = None
    print("qqqqqqq")
    if len(df.columns) == 4:
    # Drop the last column
        df = df.iloc[:, :-1]

    rf = pickle.load(open("rf_model.pkl", 'rb'))
    #df_list1=df_list
    #print(df)
    test = np.array(df)
    print("111111111111111")
    #print(test)
    #test = np.reshape(test, (1, -1))
    print(test.shape)
    y_pred = rf.predict(test)
    #print(y_pred)
    data=list(y_pred)
    result = [{'State Of Health': value*100} for value in data]
    #print("11222222222222222222222222222222222",result)
    #print("ooooooooooooooooooooooooggffff2",df_list)
   
    merged_data = []

    for d1 in df_list:
        for d2 in result:
            d = d1.copy()
            d.update({'State Of Health': round(d2['State Of Health'], 2)})
            merged_data.append(d)
    # merged_df = df_list + result
    # # merged_data = {**df_list, **result}
    print(merged_data)

    return render(request, 'dataframe1.html', {'dataframe': merged_data})

def output1(request):
    temp= request.POST.get('temp')
    chr= request.POST.get('chr')
    vol= request.POST.get('vol')

    data=[float(temp),float(chr),float(vol)]
    rf = pickle.load(open("rf_model.pkl", 'rb'))
    print(data)
    test=np.array(data)
    test = np.reshape(test, (1, -1))
    print(test.shape)
    y_pred = rf.predict(test)
    print(y_pred)
    if y_pred is not None and len(y_pred) > 0:
        value = y_pred[0]
        value = format(value*100, ".3f")
  
    return render(request,'output.html',{'out':value})








    


def Logout(request):
    logout(request)
    return redirect('Login_3')
