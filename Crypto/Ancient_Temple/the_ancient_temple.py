s, C = [], [] 
l = 1337
M = 7777771


n=[]
flag = "REDACTED"

#map converts to int
#join: joins all digit of bin(ord(i)) in a single string, separated by spaces
# [2:] discards the 0b_____
# Finally, split separates each digit of the binary number, and creates a list of digits (0s and 1s)
binary_rep_flag = [list(map(int, list(' '.join(bin(ord(i))[2:]).split()))) for i in flag]


def num_gen(first, last):

   o = [[1]]                       
   cnt = 1                            
   while cnt <= last:
       if cnt >= first:
           yield o[-1][0]           
       row = [o[-1][-1]]            
       for b in o[-1]:
        row.append(row[-1] + b)  
       cnt += 1                       
       o.append(row)


#for i in num_gen(7, 13):
#       s.append(i)

#res of num_gen 
s = [203,877,4140,21147,115975,678570,4213597]


#for i in range(len(s)):
for i in range(7): 
    ni = ((l*s[i]) % M)           
    n.append(ni)

#result of loop is:
n = [271411, 1172549, 5535180, 4940226, 7280926, 5026654, 2472985]

#binary_rep_flag is in format [ [0,0,1,1,0,1], [], [], ...  ]
for binary_char in binary_rep_flag:
    C_curr = []
    for (bit_0_1,y) in zip(binary_char, n):
        C_ = bit_0_1*y
        C_curr.append(C_)
    C += [sum(C_curr)]

#print(M, s, l, C, n)


