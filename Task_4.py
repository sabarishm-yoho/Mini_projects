list=list(map(int,input("Enter the value:").split()))
Sum=0
Max=list[0]
Min=list[0]
for i in list:
    Sum += i
    if i > Max:
        Max = i
    if i<Min:
        Min=i
    print(i)
print(f"Total sum:{Sum}\nLargest Number:{Max}\nSmallest Number:{Min}")    

