from django.shortcuts import HttpResponse

data=f"<hr><a href='/'>Home</a>\t<a href='signin'>Sign in</a>\t<a href='/signup'>Sign up</a>"

def index(req):
    return HttpResponse(f"<center><h1>Welcome to my page!{data}</h1></center>")

def signup(req):
    global username
    username=input("enter username=")
    return HttpResponse(f"<center><h1>Sign up Page{data}</h1></center>")

def signin(req):
    chkusername=input("enter username to sign in=")
    if chkusername==username:
        next=f"<hr><h1><a href='/'>Logout</a>"
        return HttpResponse(f"<center><h1>Sign in Page{chkusername}!!!{next}</h1></center>")
    else:
        msg=f"<center><h1>Incorrect Username! Try again</h1></center>"
        next=f"<hr><h1><a href='/'>Click here to go back</a>"
        return HttpResponse(f"{msg}{next}")