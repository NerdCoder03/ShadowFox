#for loop

#using for loop simulate rolling of a six-sided die multiple times
import random
count_6=0
count_1=0
consecutive_6=0
previous_num=None
rolls=int(input("Enter the number of times you want to roll the dice:"))
for i in range(rolls):
    num=random.randint(1,6)
    if num==6:
        count_6+=1
    if num==1:
        count_1+=1
    if previous_num==6 and num==6:
        consecutive_6 +=1
    previous_num = num
print("Let's see the results!")
print(f"You got {count_6} 6's")
print(f"You got {count_1} 1's")
print(f"You got two 6's consecutively {consecutive_6} times")
print("*******************-*******************")

#workout routine using for loop
print("Jumping Jacks, Let's GO!!")
completed=0
remaining=100
for completed in range(10,101,10):
    choice1=input("Type Done to confirm you have done 10 jumping jacks\n"
                  "If you can't complete the next 10, your count will be fixed till the last 10 you did!\n"
                  "In that case press any key to continue:")
    if choice1=='Done':
        print(f"You have completed {completed} jumping jacks.")
        remaining-=10
        print(f"{remaining} jumping jacks remaining! Keep grinding!")
        if completed == 100:
            print("Congratulations! You completed your workout routine.")
            break
        reply1=input("Are you tired?(Yes/No):")
        if reply1=='Yes':
            reply2=input("Do you want to skip the remaining sets?(Yes/No):")
            if reply2=='Yes':
                print(f"You completed a total of {completed} jumping jacks")
                break
            elif reply2=='No':
                continue
            else:
                print("Invalid input! Try again")

        elif reply1=='No':
            continue
        else:
            print("Invalid input! Try again")

    else:
        print(f"You have completed {completed-10} jumping jacks.")
        break
