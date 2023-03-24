# Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


upd_name1= name1.lower()
upd_name2= name2.lower()
t1 = upd_name1.count('t')
t2 = upd_name2.count('t')
T = t1 + t2
r1= upd_name1.count('r')
r2= upd_name2.count('r')
R = r1+ r2
u1= upd_name1.count('u')
u2= upd_name2.count('u')
U = u1 + u2
e1= upd_name1.count('e')
e2= upd_name2.count('e')
E = e1 + e2
l1= upd_name1.count('l')
l2= upd_name2.count('l')
L = l1 + l2
o1= upd_name1.count('o')
o2= upd_name2.count('o')
O = o1 + o2
v1= upd_name1.count('v')
v2= upd_name2.count('v')
V = v1 + v2

total1= T+R+U+E
total2= L+O+V+E
total_score = str(total1) + str(total2)
print(total_score)
love_score = int(total_score)
if love_score < 10 or love_score > 90:
  print(f"Your Score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together")
else:
  print(f"Your score is {love_score}.")