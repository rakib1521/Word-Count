from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    #ls=["Rakib Hossain Rifat", 24, 'AUST']
    return render(request,'home.html')

def Count(request):
    #getting the text from text input via url
    input_text=request.GET['input_text']
    #print(input_text)
    #spliting the text by space
    input_text_list= input_text.split()
    #print(input_text_list)
    #print(len(input_text_list))
    #creating empty dictonary
    word_dict={}
    #looking if a word is multiple time in the dictonary
    for word in input_text_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] =1


    #print(word_dict)
    #sorting and converting dictonary to a list
    sorted_list= sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
    #print(word_dict)

    return render(request,'count.html',{'input_text':input_text,'input_text_list':len(input_text_list),'sorted_list':sorted_list})


def about(request):
    return render(request,'about.html')
