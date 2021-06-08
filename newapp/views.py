from builtins import len, range

import requests
from django.shortcuts import render, redirect



def sample(request):

    data=requests.get('https://opentdb.com/api.php?amount=1').json()


    options=[]
    questions = []
    ca=data.get('results')[0]['correct_answer']
    options.append(ca)
    options.extend(data.get('results')[0]['incorrect_answers'])
    options.sort()
    lengthofoption=len(options)
    questions.append(data.get('results')[0]['question'])

    context={'data':questions[0],'options':options,'ca':ca,'len':range(lengthofoption)}
    return render(request,'sample.html',context)