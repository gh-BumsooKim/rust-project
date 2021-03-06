import random 

num = random.randint(1,9999)
num_str = str(num)

answer = list()
output = [0,0,0,0]

answer = list(num_str.zfill(4)) if len(num_str)!=4 else list(num_str)
    
input_num = 0
while True:
    input_num+=1
    guess = input()
    mynum = list(guess)
    
    try:
        int(guess)
    except ValueError as e:
        print("Please Input 4 digits Number such as 0000 with ValueError :",e)
        continue
    
    if(len(guess)!=4):
        print("Please Input 4 digits Number such as 0000 with IndexError")
        continue
    
    try:
        for i in range(len(answer)):
            output[i] = 1 if(answer[i]==mynum[i]) else 0
    except IndexError as e:
        print("Please Input 4 digits Number such as 0000 with IndexError :",e)
        continue
        
    s = str(output[0])+str(output[1])+str(output[2])+str(output[3])
    
    if(s == "1111"):
        print("Result :", s, "with", input_num, "times input")
        break
    else:    
        print("Result :", s)
