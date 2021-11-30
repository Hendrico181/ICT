from django.shortcuts import render
import datetime
from .models import Participant

# Create your views here.
def participant_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        workout1_time = datetime.timedelta(minutes=int(request.POST.get('workout1_minutes')), seconds=int(request.POST.get('workout1_seconds')))
        workout2_time = datetime.timedelta(minutes=int(request.POST.get('workout2_minutes')), seconds=int(request.POST.get('workout2_seconds')))
        workout3_time = datetime.timedelta(minutes=int(request.POST.get('workout3_minutes')), seconds=int(request.POST.get('workout3_seconds')))
        workout4_time = datetime.timedelta(minutes=int(request.POST.get('workout4_minutes')), seconds=int(request.POST.get('workout4_seconds')))
        Participant.objects.create(name=name, workout1_time=workout1_time, workout2_time=workout2_time, workout3_time=workout3_time, workout4_time=workout4_time)
    context = {}
    scoring()
    return render(request, 'leaderboard/create.html', context=context)


def scoring():
    participant_workout1_scoring = Participant.objects.order_by('workout1_time')
    participant_workout1_scoring.update(points=4)
    participant_workout2_scoring = Participant.objects.order_by('workout2_time')
    participant_workout3_scoring = Participant.objects.order_by('workout3_time')
    participant_workout4_scoring = Participant.objects.order_by('workout4_time')

    last_score = 0
    for k, participant_workout_scoring in enumerate([participant_workout1_scoring, participant_workout2_scoring, participant_workout3_scoring, participant_workout4_scoring]):
        for i, participant in enumerate(participant_workout_scoring):
            #create a dynamic filter to get participant score
            _filter = {f'workout{k+1}_time': getattr(participant, f'workout{i+1}_time')}
            participant_query = Participant.objects.filter(**_filter).exclude(id=participant.id)

            if participant_query.exists(): #check for tie
                participant.points += last_score
                setattr(participant, f'workout{k+1}_score', last_score+1)
            
            else:
                last_score = i
                participant.points += i
                setattr(participant, f'workout{k+1}_score', i+1)
            
            participant.save()

