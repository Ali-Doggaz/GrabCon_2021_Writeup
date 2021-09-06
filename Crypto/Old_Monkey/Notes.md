# Understanding the challenge

So first, we start by taking a look at the source code.

We immediately see that a "REDACTED" string (which is supposed to contain the flag), is encoded with the encode() function.

Taking a look at that function, we see that it first defines a cst:    
x = "hjlgyjgyj10hadanvbwdmkw00OUONBADANKHM;IMMBMZCNihaillm"

Then we see that a random number 'i' is generated. Then, we see that the "out" string, which will contain the final encrypted string, will start with chr(i). 
out = chr(i)

So now we can get i from the first char of our encrypted string. Yay!

After figuring out how to get i, we take a look at the next step, which is a loop that goes through our flag, and xor it with the iTH character of x

        for c in text:
            out += chr(ord(c) ^ ord(self.x[i]))
            i = (i + 1)%79   
            
How do we reverse a xor operation ? OH YES I KNOW THIS ONE! WE XOR IT AGAIN!
So once we have i, we just have to repeat that encryption process and we will get the flag! yay!
