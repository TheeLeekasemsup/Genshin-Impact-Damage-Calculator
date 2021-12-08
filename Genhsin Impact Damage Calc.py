import math as m
import random as r

print("█▀▀ █▀▀ █▄░█ █▀ █░█ █ █▄░█   █ █▀▄▀█ █▀█ ▄▀█ █▀▀ ▀█▀   █▀▄ ▄▀█ █▀▄▀█ ▄▀█ █▀▀ █▀▀   █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█")
print("█▄█ ██▄ █░▀█ ▄█ █▀█ █ █░▀█   █ █░▀░█ █▀▀ █▀█ █▄▄ ░█░   █▄▀ █▀█ █░▀░█ █▀█ █▄█ ██▄   █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄")
def dmgCalc():
    global vape_dps
    global vape_dps_crit
    print("Please enter your total atk:")
    Atk = float(input(""))
    print("Please enter your total Elemental Mastery")
    Em = float(input(""))
    vape_bonus = (-0.000000000013885 * (Em))** 4 + (0.000000060870867 * (Em))**3 - (0.000127973809274 * (Em))**2 + 0.196821095573654 * (Em) + 0.024542903165184
    print("Please Enter your total Crit Rate:")
    cr = float(input(""))
    crit_rate = cr / 100
    print("Please Enter Your Crit Damage:")
    cd = float(input(""))
    crit_damage = cd / 100
    print("Please enter your total damage bonus:")
    total_dmg_bonus = float(input('')) / 100
    raw_dmg = Atk
    print("Please enter your talent multiplier:")
    talent_multiplier = float(input(""))
    talent = talent_multiplier / 100
    raw_crit_dmg = Atk * crit_damage
    if Em <= 0:
        raw_damage_vape = (Atk * talent) * 1.5
        damage_vape_crit_raw = (((Atk * crit_damage) + Atk) * talent) * 1.5
        damage_vape_crit_bonus = (((Atk * crit_damage) + Atk) * talent) * 1.5 * total_dmg_bonus
    elif Em > 0:
        raw_damage_vape = (Atk * talent) * 1.5 * (vape_bonus/100)
        damage_vape_crit_raw = (((Atk * crit_damage) + Atk) * talent) * 1.5 * (vape_bonus/100) 
        damage_vape_crit_bonus = (((Atk * crit_damage) + Atk) * talent) * 1.5 * (vape_bonus/100) * total_dmg_bonus
    print("this is your raw damage:{}".format(round(raw_dmg)))
    print("this is your raw CRIT damage:{}".format(round(raw_crit_dmg)))
    print("this is your raw vaporize damage:{}".format(round(raw_damage_vape)))
    print("this is your CRIT vaporize damage:{}".format(round(damage_vape_crit_raw)))
    print("this is your CRIT vaporize damage with elemental bonus:{}".format(round(damage_vape_crit_bonus)))
    for i in range(60):
        if m.floor(r.uniform(0, 1/(1-crit_rate))):
            vape_dps_crit = 0 + damage_vape_crit_raw
        else:
            vape_dps = 0 + raw_damage_vape
    total_vape_dps = vape_dps_crit + vape_dps / 60
    print("This is your vape dps:{}".format(round(total_vape_dps)))
while True:
    dmgCalc()
    re_calc = input("want to calculate again? y/n")
    if(re_calc.lower() == "n"):
        break

