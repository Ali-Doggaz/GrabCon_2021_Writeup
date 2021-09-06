First, one of my friends googled encryption algorithms similar to RSA and found out about the Paillier cryptosystem! (Lucky us!)
https://en.wikipedia.org/wiki/Paillier_cryptosystem

I recommend this wikipedia article, you'll understand a lot from it.

Now, getting back to our challenge, we clearly see that in our equation, n is replaced with sqrt(n). So let n' = sqrt(n). We'll use n' instead of n in our equation, to clearly see that we are dealing with paillier. 

We also see that we have g = a = n' + 1
And if we look closer at our wikipedia article, we see that this is a special case of the paillier algorithm, that is very easy to decrypt!
"If using p,q of equivalent length, a simpler variant of the above key generation steps would be to set g=n+1. Lambda = phi(n) and mu = inverse(phi(n), n), with phi(n) = (p-1)*(q-1)"

So we need p and q in order to decrypt it. Let's check factordb.com, which is a website containing a huge database for numbers' factorizations.
Luckily, we found p and q of n in factordb!

So now we have everything, we just need to calculate the decryption key (lambda and mu), and then of course decrypt the flag. 

You could do it manually, or you can also use this amazing online tool: https://cryptocalc.giondesign.com.au/paillier-crypto-calc

/!\ Once again, if you are not sure about what I am saying, and don't really understood what lambda and mu are, I recommend you check the wikipedia article again as everything is explained in details there.
/!\ If you ever need to do simple operations involving big numbers, you can use this amazing online tool: https://www.calculator.net/big-number-calculator.html
