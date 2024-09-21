from django.shortcuts import render,HttpResponse

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST': 
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        email=email.rstrip()

        if email == '' or password == '' or username == '':
            messages.error(request,"Please fill all the fields.")
            return render(request,"signup.html")
        
        elif User.objects.filter(username=username).exists(): 
            messages.add_message(request, messages.INFO, 'Username already exists.')
            return render(request,"signup.html")
        
        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.INFO, 'Email already exists.')
            return render(request,"signup.html")

        else :
            user = User.objects.create(email=email, username=username, password=make_password(password))
            user.save() 
            auth_login(request, user)    
            messages.add_message(request, messages.INFO, 'You have successfully signed up.')
            return redirect('/create_profile_page')
    else:
        return render(request,"signup.html")