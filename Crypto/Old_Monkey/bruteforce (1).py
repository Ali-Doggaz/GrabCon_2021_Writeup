import codecs

#Decode the string
enc1 = b'\x07A[\x06\\\r\x15\t\x04\x07\x18VG]U]@\x02\x08&9&%\' 41".;'



#Use this to get the i (first char)
print(enc1[0]):



#initialize i for the FIRST 1st enc. I don't know why, but i isn't equal to the ord of the first char. It's equal to ord(first_char)-1.
i=6;

#init x
x = "hjlgyjgyj10hadanvbwdmkw00OUONBADANKHM;IMMBMZCNihaillm"  #len(x) = 53

out=""
for char in enc1:
    out += chr(char ^ ord(x[i]))
    i = (i + 1)%79 


print(out)


#enc     ||||  d817letmein40986728ilikeapples
#enc1    |||| d817letmein40986728ilikeapples
#enc2    ||||  d817letmein40986728ilikeapples