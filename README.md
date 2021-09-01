# mcmc
Try to use github.  
This is "Metropolis–Hastings algorithm to break substitution", referenced to "Applications of MCMC for Cryptography and Optimization".  
### "F_ref.txt"  
It is reference text, we calculate the frequency of each possible pair of english alphabet in it(for calculate the score in MCMC). We can use own referencetext.    
### "rd_encrypt.py"  
It can generate the initial decoding function.    
### "MCMC_break_substitution.py"  

1. Random pick a decoding function.
2. Duplicate the current decoding function and randomly swap two alphabets as a new decoding function.
3. Random pick a (0,1) value ,say dice.
4. If dice < score(new decoding function)/score(decoding function), then change decoding function to new decoding function.
5. Repeat 2. if round < maximum round.

If the cipher text is too long, it could be overflow when we are calculate the total score. So we can split it into several parts, but notice that it's difficult for us to break the ciphertext if it's length is too short. I think 500 alphabet is nice, less than 200 might be too short.(We can optimize it)  
We can also adjust how many round the algorithm will run, usually 6000-10000 is ok. Instead of more rounds, restart is a better way.  
