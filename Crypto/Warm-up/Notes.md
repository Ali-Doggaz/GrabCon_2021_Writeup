This challenge was pretty fun!

# Understanding the challenge 

When I saw the encrypted string, I immediately saw the "=" sign at the end of the string. That is a good indicator that the string is either encoded in base64 or in base32. Moreover, in the prompt text, we can read " ... his drink was 64 rupees and 32 rupees cigarette ..." 

==> That confirmed my theory! We were dealing with a string, encoded multiple times in a row, alternatively by a base64 encoding then a base32 encoding.

# Decryption process

You can use your terminal, or you can go to these online tools:
https://www.base64decode.org/
https://emn178.github.io/online-tools/base32_decode.html

Decode the string in base64, then decode the result in base32, then decode the result in base64, then ......... 

 # Congrats! We're hackers now. Call Elliot, we'll need some help for the next challenges.
