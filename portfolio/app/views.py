from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.


def home(request):
    user1=user.objects.get(name='SanthoshReddy')
    s=skills.objects.filter(host_id = 1)
    cdlangs=coding_languages.objects.filter(host_id = 1)
    servics=services.objects.filter(host_id=1)
    blogs=blog.objects.filter(host_id=1)
    prjcts=projects.objects.filter(host_id=1)
    dict={'user':user1,'skills':s,'coding_languages':cdlangs,'servics':servics,'blogs':blogs,'projects':prjcts}
    if request.method=='POST':
        n=request.POST['name']
        m=request.POST['email']
        p=request.POST['subject']
        q=request.POST['message']
        msg=support.objects.create(name=n,email=m,subject=p,message=q)
        msg.save()
        messages.info(request,'message received,i will reach you shortly!!')
    return render(request,'index.html',dict)
def blogs(request,pk):
    b=blog.objects.get(id=pk)
    blogs=blog.objects.all()
    comments=comment.objects.filter(blog_id=pk)
    replies=reply.objects.filter(commentor__blog__id = pk)
    d={'blog':b,'comments':comments,'replies':replies,'blogs':blogs}
    if request.method =='POST':
        p=request.POST['name']
        q=request.POST['email']
        r=request.POST['message']
        if request.FILES:
            pic=request.FILES['dp']
            cmnt=comment.objects.create(blog=b,name=p,mail=q,comment=r,dp=pic)
            cmnt.save()
            messages.info(request,'comment added')
        else:
            cmnt=comment.objects.create(blog=b,name=p,mail=q,comment=r)
            cmnt.save()
            messages.info(request,'comment added')
    return render(request,'blog-single.html',d)


def replycomment(request,pk):
    cmnt=comment.objects.get(id=pk)
    if request.method=='POST':
        p=request.POST['name']
        r=request.POST['message']
        if request.FILES:
            pic=request.FILES['dp']
            rply=reply.objects.create(reply_name=p,commentor=cmnt,reply=r,dpic=pic)
            rply.save()
            messages.info(request,'reply sent')
            return redirect('blogs'+'/'+cmnt.blog.id+'/')
        else:
            rply=reply.objects.create(reply_name=p,commentor=cmnt,reply=r)
            rply.save()
            messages.info(request,'reply sent') 
            return redirect('/blogs'+'/'+str(cmnt.blog.id)+'/')      
    else:
        return render(request,'reply.html',{'cmment':cmnt})    

def portfolio(request,pk):
    project=projects.objects.get(id=pk)
    dict={'project':project}
    return render(request,'portfolio-details.html',dict)


