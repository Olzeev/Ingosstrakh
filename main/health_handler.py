def health_rating_handler(age, pulse1, pulse2, pulse_prev, pressure1, pressure2, pressure3, pressure4, all_hratings):
    if (age < 1):
        Pnormal = 132
        Pable = 30
    elif (age < 4):
        Pnormal = 124
        Pable = 30
    elif (age < 6):
        Pnormal = 106
        Pable = 20
    elif (age < 8):
        Pnormal = 98
        Pable = 20
    elif (age < 10):
        Pnormal = 88
        Pable = 20
    elif (age < 12):
        Pnormal = 80
        Pable = 20
    elif (age < 15):
        Pnormal = 75
        Pable = 20
    elif (age < 50):
        Pnormal = 70
        Pable = 10
    elif (age < 60):
        Pnormal = 74
        Pable = 10
    else:
        Pnormal = 79
        Pable = 10

    P1 = pulse1
    P2 = pulse2
    Pcurrent = (P1 + P2)/2

    Pdifference = abs(Pcurrent - Pnormal)

    Ppercent = Pdifference * 10 / Pable
    #print("Ваш коэффициент отклонения пульса (если больше 10 - плохо, меньше - все в норме): " + str(Ppercent))

    Pcurrenty = pulse_prev #int(input("Введите ваш вчерашний пульс (в дальнейшем ввод будет автоматически): "))
    Pdelta = abs(Pcurrenty - Pcurrent)
    Pjump = Pdelta * 6 / Pable

    Prating = max(Pjump, Ppercent)
    #print("Ваш рейтинг пульса (максимум из коэффициента скачков пульса и коэффициента отклонения пульса: " + str(Prating))

    if (age < 5):
        BLnormal = 60
        BLable = 15
        BUnormal = 90
        BUable = 15
    elif (age < 6):
        BLnormal = 65
        BLable = 15
        BUnormal = 95
        BUable = 15
    elif (age < 13):
        BLnormal = 70
        BLable = 10
        BUnormal = 105
        BUable = 15
    elif (age < 19):
        BLnormal = 77
        BLable = 4
        BUnormal = 117
        BUable = 12
    elif (age < 24):
        BLnormal = 79
        BLable = 4
        BUnormal = 120
        BUable = 12
    elif (age < 29):
        BLnormal = 80
        BLable = 4
        BUnormal = 121
        BUable = 12
    elif (age < 34):
        BLnormal = 81
        BLable = 4
        BUnormal = 122
        BUable = 12
    elif (age < 39):
        BLnormal = 82
        BLable = 4
        BUnormal = 123
        BUable = 12
    elif (age < 44):
        BLnormal = 83
        BLable = 4
        BUnormal = 125
        BUable = 12
    elif (age < 49):
        BLnormal = 84
        BLable = 4
        BUnormal = 127
        BUable = 12
    elif (age < 54):
        BLnormal = 85
        BLable = 4
        BUnormal = 129
        BUable = 13
    elif (age < 59):
        BLnormal = 86
        BLable = 4
        BUnormal = 131
        BUable = 13
    else:
        BLnormal = 87
        BLable = 4
        BUnormal = 134
        BUable = 13

    BL1 = pressure1
    BL2 = pressure3
    BLcurrent = (BL1 + BL2)/2

    BLdifference = abs(BLcurrent - BLnormal)
    BLpercent = BLdifference * 10 / BLable

    BU1 = pressure2
    BU2 = pressure4
    BUcurrent = (BU1 + BU2)/2

    BUdifference = abs(BUcurrent - BUnormal)
    BUpercent = BUdifference * 10 / BUable

    Brating = max(BUpercent, BLpercent)
    #print("Ваш рейтинг давления (максимум из коэффициента отклонения нижнего давления и верхнего давления: " + str(Brating))

    Hrating = max(Prating, Brating)
    #print("Ваш рейтинг здоровья: " + str(Hrating))

    allHealthRatings = all_hratings

    allHealthRatings.append(Hrating)
    l = min(7, len(allHealthRatings))
    curHealthRatings = [allHealthRatings[i] for i in range(len(allHealthRatings) - l, len(allHealthRatings))]
    #allHealthRatings[len(allHealthRatings)-l:]

    Hsigma = sum(curHealthRatings)
    Hfinal = max(curHealthRatings)

    #print("Ваша сумма рейтингов здоровья: " + str(Hsigma) + ", ваш рейтинг здоровья, на который стоит обратить наибольшее внимание: " + str(Hfinal))

    message = ""
    if (Hrating > 10):
        message = "Вам необходимо срочно обратиться к врачу!"
    elif (Hrating > 8):
        message = "Вам стоит получше следить за своим здоровьем: вероятно, Вам скоро придется сходить к врачу"
    else:
        message = "С Вашим здоровьем все в порядке. Продолжайте за ним следить с помощью нашей платформы!"

    return [message, Hrating]