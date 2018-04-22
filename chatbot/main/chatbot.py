from textblob import TextBlob
from random import randint
import sentiment2
import summary

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

answers=[]
analyse = ""
for set in range(len(questions)):
	stage = []
	print("\nnew set:")
	current=questions[set]
	#print(current)

	#for index in range(len(current)):
	index=0
	r=randint(0,len(current[index])-1)
	#print(r)
	#print(current[index][r])
	ans=input()
	pos,neg = sentiment2.predict(ans)
	#print("\nPositive: "+pos+"\nnegative: "+neg)
	answers.append(ans)
	stage.append(ans)
    
	if(pos>neg):
		r2=randint(0,len(current[index+1])-1)
		print(current[index+1][r2])
		ans2=input()
		answers.append(ans2)
		stage.append(ans2)

	else:
		r3=randint(0,len(current[index+2])-1)
		print(current[index+2][r3]) 
		ans3=input()
		answers.append(ans3)
		stage.append(ans3)

	
	stage = ' '.join(stage)
	pos,neg = sentiment2.predict(stage)
	#print("\nPositive: "+pos+"\nnegative: "+neg)

answers = '\n'.join(answers)
summary.main(answers)