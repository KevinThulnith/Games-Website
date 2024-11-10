from django.contrib.auth.decorators import login_required
from .models import WebGame, Score
from django.shortcuts import render
# Create your views here.

games = WebGame.objects.all()


def saveScore(request, b: int):
    "save player game score"
    pan = [eval(i) for i in request.POST['score'].split('/')]
    if len(Score.objects.filter(game=games[b], player=request.user)) == 0:
        a = Score(player=request.user, game=games[b])
        a.save()
    report = Score.objects.filter(game=games[b], player=request.user)[0]
    report.score += pan[0]
    report.save()
    return pan


@login_required
def home(request):
    "render home page"
    return render(
        request, 'games/index.html', {
            'title': ' - Home',
            'user': request.user,
            'games': games,
            'game1': Score.objects.filter(game=games[0]).order_by('-score'),
            'game2': Score.objects.filter(game=games[1]).order_by('-score'),
            'game3': Score.objects.filter(game=games[2]).order_by('-score'),
            'game4': Score.objects.filter(game=games[3]).order_by('-score')
        })


@login_required
def number(request, n):
    context = {'title': f' - {n}', 'status': 0}
    if n == 'Tik Tak To':

        if request.method == 'POST':
            pans = saveScore(request, 0)

            if len(pans) > 1: context['status'] = pans[1]

        return render(request, 'games/TikTakTo.html', context)

    elif n == 'Rock Paper Scissor':

        if request.method == 'POST':

            pans = request.POST['score'].split('/')
            if len(pans) == 3:
                pans = [eval(pans[0]), pans[1], eval(pans[2])]
            else:
                pans = [eval(pans[0]), eval(pans[1])]

            if len(Score.objects.filter(game=games[2],
                                        player=request.user)) == 0:
                a = Score(player=request.user, game=games[2])
                a.save()

            report = Score.objects.filter(game=games[2],
                                          player=request.user)[0]
            report.score += pans[0]
            report.save()

            if len(pans) > 2: context['status'] = f"{pans[1]}/{pans[2]}"

        return render(request, 'games/RockPaperScissor.html', context)

    elif n == 'Guess The Number':

        if request.method == 'POST':
            pans = saveScore(request, 1)

            if len(pans) > 1: context['status'] = pans[1]

        return render(request, 'games/GuessTheNumber.html', context)

    elif n == 'Hang Man':
        if request.method == 'POST':
            pans = saveScore(request, 3)

            if len(pans) > 1: context['status'] = pans[1]

        return render(request, 'games/HangMan.html', context)


@login_required
def loadProfile(request):
    "render profile page"
    if request.method == 'POST':
        user = request.user
        user.name = request.POST['name']
        user.mobile = request.POST['mobile']
        user.dob = request.POST['dob']

        if len(request.FILES) != 0:
            user.profilePic = request.FILES['profilePic']

        user.save()

    can = request.user.dob
    report = Score.objects.filter(player=request.user).order_by('-score')
    context = {
        'title': ' - User Profile',
        'dob': f'{can}',
        'game1': report,
        'user': request.user
    }
    return render(request, 'games/profile.html', context)

@login_required
def slides(request):
    context = {'title': ' - Animal Slides'}
    return render(request, 'games/slides.html', context)