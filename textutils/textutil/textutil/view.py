from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    #check check values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')

    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!@#$%^&*()_-[]{};:"'<>.,\/?|~'''
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze=analyze+char

        params={'purpose' : 'remove punctuation','analyze_text' : analyze}
        djtext=analyze

    if(fullcaps=='on'):
        analyze=""
        for char in djtext:
            analyze=analyze+char.upper()
        params = {'purpose': 'UPPER CASE', 'analyze_text': analyze}
        djtext=analyze


    if(newlineremover=='on'):
        analyze=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyze=analyze+char
        params={'purpose':'New Line Remove','analyze_text':analyze}
        djtext=analyze
    if(charcount == 'on'):
        analyze=""
        count=0
        for i in djtext:
            count +=1
            analyze=count
        params = {'purpose':'charcount','count':'your count=', 'analyze_text' : analyze}

    if (spaceremover == "on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1]==" "):
                 analyze = analyze + char
            # if char.replace("   "," "):
            #     analyze=analyze+char
        params = {'purpose': ' Space Remove', 'analyze_text': analyze}
        djtext=analyze
        # params={'purpose':'Character Count','count':'your count', 'analyze_text':analyze}
    # if(removepunc != "on"):
    return render(request,'analyze.html',params)
    if(removepunc != "on" and newlineremover != "on" and spaceremover != "on" and fullcaps != "on" and charcount!="on"):
        return HttpResponse("please select any operation and try again")
    return render(request,'analyze.html',params)



    # else:
    #     return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("newline remove")
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("character count")
# # def index(request):
# #     params =  {'name':'suraiya','place':'mars'}
#     return render(request,'index.html', params)
