def SaveProfile(request): 
	saved = False 
	if request method ==  "POST": 
		#Get the posted form 
		myprofileForm = profileForm(request.POST.request.FILES)
		
	if MyProfileForm.is_valid(): 
		profile z profile() 
		profile.name = MyProfileForm.cleaned_data["name"] 
		profile.picture = MyProfileForm.cleaned_data["picture"]
		profile.save() 
		saved = True 
	else: 
		MyProfileForm = Profileform() 
		
return render(request, 'saved.html', locals()) 
