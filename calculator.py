import math

def display_menu():
    print('Please select from the following options:\n')
    print('1)  Compute BMI')
    print('2)  Compute YMCA Index')
    print('3)  Compute Navy Index')
    print('4)  Compute All')

def compute_ymca(gender, waist, weight):
    if gender == 'M':
        return (-98.42 + 4.15*waist-(.082 * weight))/weight
    elif gender == 'F':
        return (-76.76 + 4.15*waist-(.082 * weight))/weight
    else:
        print('Invalid Input')
        quit()

def compute_navy_male(abdomen, neck, height):
    return (495/(1.0324-.19077*math.log10(abdomen-neck)+.15456*math.log10(height*2.54))-450)*.01

def compute_navy_female(abdomen, hip, neck, height):
    return (495/(1.29579-.35004*math.log10(abdomen+hip-neck)+.22100*math.log10(height*2.54))-450)*.01

def compute_bmi(weight, height):
    BMI_OFFSET = 703
    return (BMI_OFFSET * weight)/height**2

def assess_bmi(bmi):
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <= 24.99:
        return 'Normal Weight'
    elif bmi <= 29.99:
        return 'Overweight'
    elif bmi <= 34.99:
        return 'Obesity (Class 1)'
    elif bmi <= 39.99:
        return 'Obesity (Class 2)'
    else:
        return 'Morbid Obesity'

def assess_bodyfat(fat, gender):
    if gender == 'F':
        if fat <= .13:
            return 'Essential Fat'
        elif fat <= .2:
            return 'Athlete'
        elif fat <= .24:
            return 'Fitness'
        elif fat < .32:
            return 'Acceptable'
        else:
            return 'Obese'
    elif gender == 'M':
        if fat <= .05:
            return 'Essential Fat'
        elif fat <= .13:
            return 'Athlete'
        elif fat <= .17:
            return 'Fitness'
        elif fat < .25:
            return 'Acceptable'
        else:
            return 'Obese'

def main():
    display_menu()
    choice = int(input('\nWhich option?  '))
    if choice < 1 or choice > 4:
        print('invalid input')
        quit()
    print()
    #gather inputs
    weight = float(input('What is your weight?  '))
    if choice == 1 or choice == 3 or choice == 4:
        height = float(input('What is your height in inches?  '))
    if choice == 2 or choice == 4:
        waist = float(input('What is your waist?  '))
    if choice == 2 or choice == 3 or choice == 4:
        gender = input('What is your gender (M/F)?  ')
    if choice == 3 or choice == 4:
        abdomen = float(input('What is your abdomen in inches?  ')) * 2.54
        neck = float(input('What is your neck in inches?  ')) * 2.54
        if gender == 'F':
            hip = float(input('What is your hip measurement in inches?  ')) * 2.54
            navyfat = compute_navy_female(abdomen, hip, neck, height)
        else:
            navyfat = compute_navy_male(abdomen, neck, height)

    print('Here is your analysis of your data:\n')

    if choice == 1 or choice == 4:#BMI
        print('BMI Results')
        bmi = compute_bmi(weight, height)
        print('Your BMI is:  ' + str(bmi))
        print('Your BMI classification is:  ' + assess_bmi(bmi) + '\n')
    if choice == 2 or choice == 4:  #YMCA
        print('YMCA Results')
        ymcafat = compute_ymca(gender, waist, weight)
        print('Your YMCA body fat % is ' + str(ymcafat))
        print('YMCA Fat Mass:  ' + str(weight * ymcafat))
        print('YMCA Lean Mass:  ' + str(weight * (1 - (ymcafat))))
        print('YMCA Classification:  ' + assess_bodyfat(ymcafat, gender) + '\n')
    if choice == 3 or choice == 4:  #NAVY
        print('Navy Results')
        print('Your Navy body fat % is ' + str(navyfat))
        print('Navy Fat Mass:  ' + str(weight * navyfat))
        print('Navy Lean Mass:  ' + str(weight * (1 - (navyfat))))
        print('Navy Classification:  ' + assess_bodyfat(navyfat, gender) + '\n')

main()
