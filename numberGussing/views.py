from django.contrib import messages
import random
from django.shortcuts import redirect, render

from info.models import NumberModer

def index(request):
  if 'number' not in request.session:
    request.session['number'] = random.randint(1,100)
    request.session['nguess'] = 0

  number = request.session['number']
  nguess = request.session['nguess']

  if request.method == 'POST':
    guessNumber_str = request.POST.get('guessNumber')

    if not guessNumber_str:
      messages.info(request,'Please enter a number')
      return redirect('index')
    
    try:
      guessNumber = int(guessNumber_str)
    except ValueError:
      messages.error(request,'Invalid input! Please enter a vlaid number')
      return redirect('index')
    
    guessNumber_model = NumberModer(guessNumber=guessNumber)
    guessNumber_model.save()
    
    nguess +=1
    request.session['nguess'] = nguess

    if(guessNumber > number):
      messages.info(request,'Enter Lower Number')
    elif(guessNumber<number):
      messages.info(request,'Enter Grater Number')
    else:
      messages.success(request, f'Win! You guessed it in {nguess} attempts')
      request.session.flush()
      return redirect('index')
    
  resultOf = NumberModer.objects.all()
  return render(request,"index.html",{'resultOf':resultOf})
