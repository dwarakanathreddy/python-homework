from django.shortcuts import render

def index(request):
    user_text = None
    length = None
    uppercase = None
    lowercase = None
    reversed_text = None
    vowel_count = None

    if request.method == 'POST':
        user_text = request.POST.get('user_text', '')

        # ── STUDENT CODE START ──────────────────────────
        length = len(user_text)
        uppercase = user_text.upper()
        lowercase = user_text.lower()
        reversed_text = user_text[::-1]
        vowel_count=0
        for i in range(len(lowercase)):
            if lowercase[i] in ["a","e","i","o","u"]:
                vowel_count = vowel_count + 1

        # ── STUDENT CODE END ────────────────────────────

    context = {
        'user_text': user_text,
        'length': length,
        'uppercase': uppercase,
        'lowercase': lowercase,
        'reversed_text': reversed_text,
        'vowel_count': vowel_count,
    }
    return render(request, 'assignment2/index.html', context)
