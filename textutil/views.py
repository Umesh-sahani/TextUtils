# i have created this file - Umesh
from django.http import HttpResponse
from django.shortcuts import render


# video for 7
def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text and checkbox value
    djtext = request.POST.get('text', "default")

    removepunctuation = request.POST.get('removepunctuations', "off")
    uppercase = request.POST.get('uppercase',"off")
    newlineremover = request.POST.get('newlineremover',"off")
    extraspaceremover = request.POST.get('extraspaceremover',"off")
    charactercount = request.POST.get('charactercount',"off")
    wordcount = request.POST.get('wordcount',"off")
       
    #Check the checkbox status
    if removepunctuation == 'on':
        analyze=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$^%&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        param = {'purpose':'Remove Punctuations','before':djtext, 'analyzed_text':analyze}
        djtext=analyze
        # Analyze the text
        # return render(request, 'analyze.html', param)
    if(uppercase=='on'):
        analyze=""
        for char in djtext:
            analyze = analyze + char.upper()
        param = {'purpose':'Change the text to uppercase','before':djtext, 'analyzed_text':analyze}
        djtext=analyze
        # return render(request, 'analyze.html', param)
    if(newlineremover=='on'):
        analyze=""
        analyze=""
        for char in djtext:
            if char != '\n' or char != '\r':
                analyze = analyze + char
        param = {'purpose':'Remove New line','before':djtext, 'analyzed_text':analyze}
        djtext=analyze
        # return render(request, 'analyze.html', param)
    if(extraspaceremover=='on'):
        analyze=""
        for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                analyze = analyze+char            
        param = {'purpose':'Remove Extra Spaces','before':djtext, 'analyzed_text':analyze}
        djtext=analyze
        # return render(request, 'analyze.html', param)    
    if(charactercount=='on'):
        analyze=""
        count=0
        for char in djtext:
            count = count+1
        analyze = f'Number of Character is = {count}'
        param = {'purpose':'Count Your String Character','before':djtext, 'analyzed_text':analyze}
        return render(request, 'analyze.html', param)
    if(wordcount=='on'):
        analyze=""
        if djtext!='':
            word = 1
        else:
            word = 0
        for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]!=' ':
                word=word+1    
        analyze = f'Number of Words = {word}'
        param = {'purpose':'Count Your String word','before':djtext, 'analyzed_text':analyze}
    if(removepunctuation != "on" and uppercase !=  'on' and newlineremover != 'on' and extraspaceremover !=  'on' and charactercount != 'on' and wordcount != 'on'):
        return HttpResponse("<script>alert('Please choose any options')</script>")
    return render(request, 'analyze.html', param)
