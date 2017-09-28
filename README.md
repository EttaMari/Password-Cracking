# Password Dump Cracking
A password cracking exercise using dumped password hashes from EHarmony, Formspring, and Ashley Madison

## Ashley Madison
These passwords were stored in plaintext. It was simply a matter writing a script to extract them all.

## EHarmony
These passwords were stored with an unsalted md5 hash. 

Before using any specific approaches, I went to the eHarmony site to look for password specifications. The password length range turned out to be between 8 and 14 characters long. A little more digging revealed that these passwords were converted to upper case before being hashed, so I could further refine my approach. 

The first approach I tried was brute force. I used the cartesian product to obtain all combinations of capital letters. Even at a length of 8 brute forcing would be pretty slow, but I just let it run while I focused on other approaches.

A lot of md5 crackers online use lookup tables with millions of entries to quickly crack md5 hashes. I decided to do something similar by finding a few wordlists of common names, words, and passwords. I also tried appending and prepending numbers to each guess. This approach was pretty successful with a handful of passwords. But the effectiveness of this approach relies heavily on the quality of the wordlists used.

I also tried taking the cartesian product of different wordlists, lists of adjectives, etc. with some relative success. With the hashes I had to work with, there were no password cracks, but given a more comprehensive wordlist and a larger hash collection, I think this could also be a viable approach.

## Formspring
These passwords were stored using SHA256, using a random salt ranging from 0-99. 

A little research revealed that formspring has a password length range of 5 to 20 characters long. Furthermore, the passwords were not converted to any specific case before hashing so brute forcing would be much harder. On top of that the random salts (assuming some reasonable level of pseudo-randomness) of 0-99 means each brute force guess would have to be done 100 times to cover all salts. It was much more secure than EHarmony, assuming proper implementation.

While SHA256 is still considered secure, the poor choice of salts makes these password hashes reasonably vulnerable. 

Before applying the same approaches I used for the EHarmony passwords, I tried using the passwords from both Formspring and EHarmony with each possible salt value. This didn't yield any results, but given that people tend to keep identical passwords across multiple sites, this approach would be very useful if the type of people that use EHarmony also use Formspring. Unfortunately this did not seem to be the case here. 

I only got one password out of my attempts. It may not be the case that these password choices are more secure, but due to time and processing power constraints, it was much slower for all approaches because it was necessary to brute force the salts for each guess.

## Thoughts and future work
Some other valid techniques could involve malware, keyloggers, social engineering, and even some reconaissance to determine user information to add to customized wordlists. A lot of passwords people use have to do with names, both human and pet, street names, foods, etc. that are specific to individual people. Though it certainly isn't feasible to apply many of these approaches in this case.

It might be interesting to try these approaches with different wordlists, software like John the Ripper, or GPU Programming at some point...
