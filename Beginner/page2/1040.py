scores = list(map(float, input().split()))

average = (scores[0] * 2 + scores[1] * 3 + scores[2] * 4 + scores[3] * 1)/10


if (average >= 7):
    print('Media: ' + '%.1f' % average)
    print('Aluno aprovado.')
elif (average < 5):
    print('Media: ' + '%.1f' % average)
    print('Aluno reprovado.')
else:
    score_extra = float(input())
    print('Media: ' + '%.1f' % average)
    print('Aluno em exame.')
    print('Nota do exame: ' + '%.1f' % score_extra)
    new_average = (average + score_extra) / 2

    if (new_average > 5):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    
    print('Media final: ' + '%.1f' % new_average)
        