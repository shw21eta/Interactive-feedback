from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback
from chatbot.views import summarizer
from chatbot.views import main
import json
# Create your views here.

def messages(request):
    messages=Feedback.objects.filter(username='sayali').order_by('timestamp')
    return render(request, 'feedback/chat.html',{'accounts':accounts})


def getFeedback(request):
    #lets assume we take course from teacher
    courseCode=request.session['courseCode']

    qSet=Feedback.objects.filter(courseCode=courseCode)
    #print(qSet)
    strength=""
    improvements=""
    positive=[0,0,0,0,0,0]
    negative=[0,0,0,0,0,0]
    if(qSet):
        for rec in qSet:
            print(rec)
            if(rec.q1==1):       #set 1
                positive[0]+=1
            else:
                negative[0]+=1

            if(rec.q2==1):       #set 2
                positive[1]+=1
            else:
                negative[1]+=1

            if(rec.q3==1):       #set 3
                positive[2]+=1
            else:
                negative[2]+=1

            if(rec.q4==1):       #set 4
                positive[3]+=1
            else:
                negative[3]+=1

            if(rec.q5==1):       #set 5
                positive[4]+=1
            else:
                negative[4]+=1

            if(rec.q6==1):       #set 6
                positive[5]+=1
            else:
                negative[5]+=1

        print(positive)
        print(negative)

        for i in range(0,6):
            if(positive[i]+negative[i]>0):
                temp=positive[i]
                positive[i]=positive[i]/(positive[i]+negative[i])
                negative[i]=negative[i]/(temp+negative[i])

        print(positive)
        print(negative)
        summary = main(request)
        #summary = summarizer(request)
        strength= json.loads(summary.content)['strengthSummary']
        #strength=result['strength']
        improvements=json.loads(summary.content)['improvementsSummary']

    return render(request,'ChartAnalysis.html',{'positive':positive, 'negative':negative, 'strength': strength, 'improvements': improvements})

    #return render(request,'feedbackChart.html',{'positive':positive, 'negative':negative, 'strength': strength, 'improvements': improvements})
    #return JsonResponse(data)
