# Speed fines are not fine! - https://www.acmicpc.net/problem/6763
limit = int(input())
car = int(input())
fine = car - limit

if fine <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= fine <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= fine <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")