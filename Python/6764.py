# Sounds fishy! - https://www.acmicpc.net/problem/6764
fish = [0, 0, 0, 0]
for i in range(4):
    fish[i] = int(input())
if (fish[0] < fish[1] and fish[1] < fish[2]) and fish[2] < fish[3]:
    print("Fish Rising")
elif (fish[0] > fish[1] and fish[1] > fish[2]) and fish[2] > fish[3]:
    print("Fish Diving")
elif (fish[0] == fish[1] and fish[1] == fish[2]) and fish[2] == fish[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")