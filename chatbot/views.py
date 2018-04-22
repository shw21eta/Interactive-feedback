from __future__ import division
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json
import math
from random import randint
from . import sentiment2
import re
from feedback.models import Feedback
from feedback.models import Message
from feedback.models import Teacher
from feedback.models import Student
from .forms import TeacherLoginForm
from .forms import StudentLoginForm
from .forms import TeacherRegisterForm
from .forms import StudentRegisterForm
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#from .summa import summarizer
def dashboard(request):
    #if(request.session['prn']):
    availableCourses = Teacher.objects.all()
    return render(request,'dashboard.html', {'availableCourses':availableCourses})

def home(request):
    #return HttpResponse('Home page')
    #return render(request,'homepage.html')
    courseCode= request.GET.get('code', '')
    request.session['q']=[0,0,0,0,0,0]
    # request.session['prn']=request.session['prn']
    # request.session['courseCode']=request.session['courseCode']
    feedbackObj= Feedback(
        prn=request.session['prn'],
        courseCode=courseCode,
        q1=request.session['q'][0],
        q2=request.session['q'][1],
        q3=request.session['q'][2],
        q4=request.session['q'][3],
        q5=request.session['q'][4],
        q6=request.session['q'][5]
    )
    feedbackObj.save()
    request.session['f_id']=feedbackObj.id
    return render(request, 'index1.html')


def index(request):
    return render(request,'index.html')

def messages(request):
    return render(request,'chat.html')

def student(request):
    return render(request,'student.html')

def teacher(request):
    return render(request,'teacher.html')

def teacherLogin(request):
    if(request.method=='POST'):
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            courseCode=form.cleaned_data['courseCode']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            rec= Teacher.objects.filter(email=email, courseCode=courseCode, password=password)
            if(rec):
                request.session['email']=email
                request.session['courseCode']=courseCode
                return redirect('/feedback/getFeedback/')
            else:
                return JsonResponse({'data':'Fail record'})
                #return render(request,'charts.html')
        return JsonResponse({'data':'Fail form valid'})
    return JsonResponse({'data':'Fail post'})

def teacherRegister(request):
    if(request.method=='POST'):
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            courseCode=form.cleaned_data['courseCode']
            course=form.cleaned_data['course']
            password=form.cleaned_data['password']
            rec= Teacher.objects.filter(email=email, courseCode=courseCode)
            if(rec):
                return JsonResponse({'data':'User exist'})
            else:
                TeacherObj= Teacher(
                    name=name,
                    courseCode=courseCode,
                    course=course,
                    email=email,
                    password=password
                )
                TeacherObj.save()
                request.session['email']=email
                request.session['courseCode']=courseCode
                request.session['course']=course
                request.session['name']=name
                #return JsonResponse({'data':'Insertion successful'})
                return redirect('/feedback/getFeedback/')
        return JsonResponse({'data':'Fail'})
    return JsonResponse({'data':'Fail'})

def studentLogin(request):
    if(request.method=='POST'):
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            prn=form.cleaned_data['prn']
            password=form.cleaned_data['password']
            rec= Student.objects.filter(prn=prn, password=password)
            if(rec):
                request.session['prn']=prn
                availableCourses = Teacher.objects.all()
                print(availableCourses)
                return redirect('/dashboard/', availableCourses=availableCourses)
            else:
                return JsonResponse({'data':'Fail.. rec not found'})
                #return render(request,'charts.html')
        return JsonResponse({'data':'Fail validation'})
    return JsonResponse({'data':'Fail post'})

def studentRegister(request):
    if(request.method=='POST'):
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            prn=form.cleaned_data['prn']
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            rec= Student.objects.filter(prn=prn)
            if(rec):
                return JsonResponse({'data':'User exist'})
            else:
                StudentObj= Student(
                    prn=prn,
                    name=name,
                    email=email,
                    password=password
                )
                StudentObj.save()
                request.session['email']=email
                request.session['prn']=prn
                request.session['name']=name
                availableCourses = Teacher.objects.all()
                #return JsonResponse({'data':'Insertion successful'})
                return redirect('/dashboard/', availableCourses=availableCourses)
        return JsonResponse({'data':'Form Fail'})
    return JsonResponse({'data':'not post'})

def getresponse(request):
    print('in response')
    cnt = request.GET.get('count', None)
    print('cnt--'+cnt)
    count=int(cnt)

    response_data = {}

    if(count==12):
        response_data['res'] = 'Okay we are done then...Thank you!! :)'
        fobj= Feedback.objects.get(id=request.session['f_id'])
        msgObj= Message(
        f_id= fobj,
        msg=""+request.GET.get('responseString', ""),
        status=request.session['sentiment']
        )
        msgObj.save()
        feedbackObj = Feedback.objects.get(id=request.session['f_id'])
        feedbackObj.q1 = request.session['q'][0]
        feedbackObj.q2 = request.session['q'][1]
        feedbackObj.q3 = request.session['q'][2]
        feedbackObj.q4 = request.session['q'][3]
        feedbackObj.q5 = request.session['q'][4]
        feedbackObj.q6 = request.session['q'][5]

        feedbackObj.save()                           # this will update only
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    if(count>12):
        response_data['res'] = 'We have collected your feedback... You can exit the window now!! :)'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    row=int(count/2)

    if(count==0):
        response_data['res'] = getQuestion(row, 0)
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    if(count%2==0):
        col=0
        fobj= Feedback.objects.get(id=request.session['f_id'])
        msgObj= Message(
        f_id= fobj,
        msg=""+request.GET.get('responseString', ""),
        status=request.session['sentiment']
        )
        msgObj.save()
    else:
        request.session['lastResponse']= ""+request.GET.get('responseString', "")

        pos,neg = sentiment2.predict(request.session['lastResponse'])
        print('sentiment analysis on--'+ request.session['lastResponse'])

        if(pos>neg):
            request.session['q'][row]=1
            request.session['sentiment'] = 1
            col=1
        else:
            request.session['q'][row]=0
            request.session['sentiment'] = 0
            col=2

    response_data['res'] = getQuestion(row, col)
    #response_data['message'] = 'Some error message'
    #return HttpResponse({'record':'str data'}, content_type='json')
    return HttpResponse(json.dumps(response_data), content_type="application/json")



def summarizeComments(request):
    strength=""
    improvements=""
    courseCode=request.session['courseCode']

    qSet=Feedback.objects.filter(courseCode=courseCode)

    for record in qSet:
    #request.session['f_id']= qSet['id']
    #fobj= Feedback.objects.get(id=request.session['f_id'])
        mSet=Message.objects.filter(f_id=record)

        for rec in mSet:
            #print(rec.status)
            if(rec.status==1):
                strength=strength+rec.msg+".\n"

            else:
                improvements=improvements+rec.msg+".\n"

    #return JsonResponse({'strength': strength, 'improvements': improvements})
    return HttpResponse(json.dumps({"strength":strength, "improvements":improvements}),content_type="application/json")


class SummaryTool(object):

    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")

    def sentences_intersection(self, sent1, sent2):

        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))

        if (len(s1) + len(s2)) == 0:
            return 0

        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)

    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence


    def get_senteces_ranks(self, content):

        sentences = self.split_content_to_sentences(content)

        n = len(sentences)
        values = [[0 for x in range(n)] for x in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])


        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic


    def get_best_sentence(self, paragraph, sentences_dic):
        sentences = self.split_content_to_sentences(paragraph)

        if len(sentences) < 2:
            return ""

        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s
        return best_sentence


    def get_summary(self, title, content, sentences_dic):
        paragraphs = self.split_content_to_paragraphs(content)

        summary = []
        summary.append(title.strip())
        summary.append("")


        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)

def main(request):
    title1 = " Strengths listed: "
    title2= " Need to work upon: "
    result = summarizeComments(request)
    strength= json.loads(result.content)['strength']
    #strength=result['strength']
    improvements=json.loads(result.content)['improvements']
    #improvements=result['improvements']

    print(strength)
    print(improvements)
    #strength=strength

    st1 = SummaryTool()
    st2 = SummaryTool()

    sentences_dic1 = st1.get_senteces_ranks(strength)
    sentences_dic2 = st2.get_senteces_ranks(improvements)

    print(sentences_dic1)
    strengthSummary = st1.get_summary(title1,strength,sentences_dic1)
    improvementsSummary = st2.get_summary(title2,improvements,sentences_dic2)
    print(strengthSummary)
    print(improvementsSummary)
    return HttpResponse(json.dumps({"strengthSummary":strengthSummary, "improvementsSummary":improvementsSummary}),content_type="application/json")


"""
    print(summary)
    print("")
    print("Original Length %s" % (len(title) + len(content)))
    print( "Summary Length %s" % len(summary))
    print( "Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content))))))
	"""

def summarizer(request):
    result = summarizeComments(request)
    strength= json.loads(result.content)['strength']
    improvements=json.loads(result.content)['improvements']

    #print(strength)
    #print(improvements)
    response1= requests.post(
        "https://api.deepai.org/api/summarization",
        data={
            'text': strength,
        },
        headers={'api-key': '82a6166c-4134-41da-b1bb-74553a4d03da'}
    )

    response2 = requests.post(
        "https://api.deepai.org/api/summarization",
        data={
            'text': improvements,
        },
        headers={'api-key': '82a6166c-4134-41da-b1bb-74553a4d03da'}
    )

    #print(response1)
    #print(json.loads(response2.text)['output'])

    strengthSummary = json.loads(response1.text)['output']
    improvementsSummary= json.loads(response2.text)['output']

    summary = { 'strengthSummary': strengthSummary , 'improvementsSummary': improvementsSummary}
    return HttpResponse(json.dumps(summary),content_type="application/json")



def getQuestion(row, col):
    #Course objective
    q1=[['Are you satisfied with course objective?','Do you think the mentioned course objectives are proper?','Does the course objectives match your level of expectations?'],['What would you like to add to make course better?','How do you want to make course better?'],['What would you want to include?','What lessons do you think should be excluded from the syllabus of this course?']]

    #Teaching style
    q2=[['Are you satisfied with teaching skill/style?','Do you agree with the teaching style?','Do you get all the things taught in the classroom?'],['What you liked most about teaching?','What is the best part about the teaching style?'],['Then what kind of classes you would like?','What you dont like about teaching?']]
    #,['Suggest some improvements on teaching style.','What kind of teaching you expect for the teachers?']

    #Interactivity
    q3=[['Is teacher taking lectures more interactively?','Does teacher make lectures interesting?','Did you get extra knowledge other than academics?'],['What kind of activities he/she conducts?','Interesting in which way?'],['How do you expect the lectures should be for this course?','What are your expectations about conducting lectures?']]

    #Understanding of studies
    q4=[['Do you understand all the points taught in classroom?','Does teacher clear all of your doubts?','Does teacher arrange extra lectures for you?'],['How teacher conducts extra lectures?','How that lectures worth for your examination?'],['What would you like to change in explaination style?','Can you tell me what points you dont understand in the class?']]
    #,['What are your suggestions about teaching?','Suggest anything about teaching?']

    #Displines
    q5=[['Does teacher maintain discipline in the classroom?','Does class maintains silence while teaching?','Do you feel like sitting in the class is waste of time?'],['What classroom rules does the teacher follows?','How teacher maintains silence?'],['What improvements would you suggest?','According to you, how teacher should handle indisciplines?']]

    #Exams
    q6=[['Do you think exams taken for this course are beneficial?','Do you agree with the examination pattern?','Is there really a need for conducting exams for this course?'],['What different ways for taking the exam can we try?','Tell me different ways of conducting exams?'],['What kind of questions do you expect?','What do you think about the question difficulty level?']]

    questions=[q1,q2,q3,q4,q5,q6]

    rno= randint(0,len(questions[row][col])-1)

    return questions[row][col][rno]
