day = int(input("Enter your date of birth: "))
if (day < 1 or day > 31):
    print("The day you enter is invalid.")
    print("-----")
else:
    month = int(input("Enter your birth month: "))
    if ((month == 2 and day > 29) or ((month == 4 or month == 6 or month == 9 or month == 11) and day > 30)):
        print("The day you entered is invalid.")
        print("-----")
    elif (month < 1 or month > 12):
        print("The month you entered is invalid.")
        print("-----")
    else:
        if ((month == 3 and day >= 21) or (month == 4 and day <= 19)):
            print("Your zodiac sign is Aries (Ram)")
        if ((month == 4 and day >= 20) or (month == 5 and day <= 20)):
            print("Your zodiac is Taurus (Bull)")
        if ((month == 5 and day >= 21) or (month == 6 and day <= 21)):
            print("Your zodiac is Gemini (Twins)")
        if ((month == 6 and day >= 22) or (month == 7 and day <= 22)):
            print("Your zodiac is Cancer (Crab)")
        if ((month == 7 and day >= 23) or (month == 8 and day <= 22)):
            print("Your zodiac is Leo (Lion)")
        if ((month == 8 and day >= 23) or (month == 9 and day <= 22)):
            print("Your zodiac is Virgo (Virgin)")
        if ((month == 9 and day >= 23) or (month == 10 and day <= 23)):
            print("Your zodiac is Libra (Balance)")
        if ((month == 10 and day >= 24) or (month == 11 and day <= 21)):
            print("Your zodiac is Scorpius (Scorpion)")
        if ((month == 11 and day >= 22) or (month == 12 and day <= 21)):
            print("Your zodiac is Sagittarius (Archer)")
        if ((month == 12 and day >= 22) or (month == 1 and day <= 19)):
            print("Your zodiac is Capricornus (Goat)")
        if ((month == 1 and day >= 20) or (month == 2 and day <= 18)):
            print("Your zodiac is Aquarius (Water Bearer)")
        if ((month == 2 and day >= 19) or (month == 3 and day <= 20)):
            print("Your zodiac is Pisces (Fish)")
print("--- *** ---") 
