# MCMC
This is "Metropolis–Hastings algorithm to break substitution", referenced to "Applications of MCMC for Cryptography and Optimization".  
### "F_ref.txt"  
It is reference text, we calculate the frequency of each possible pair of english alphabet in it (for calculate the score in MCMC). We can use own reference-text.    
### "rd_encrypt.py"  
It can generate the initial decoding function.    
### "MCMC_break_substitution.py"  

1. Select a decoding function randomly.
2. Duplicate the current decoding function and create a new decoding function by randomly swapping two alphabets.
3. Generate a random (0,1) value, referred to as "dice."
4. If dice is less than the ratio of the score of the new decoding function to the score of the current decoding function, update the decoding function to the new one.
5. Repeat step 2 if the number of rounds is less than the maximum specified rounds.

When dealing with a lengthy ciphertext, there is a risk of overflow during the total score calculation. To mitigate this, consider dividing the ciphertext into smaller parts. However, be cautious, as breaking the ciphertext becomes challenging if it is too short. A length of around 500 alphabets is optimal, whereas fewer than 200 may be too short (adjustments can be made).

Additionally, the number of algorithm rounds can be fine-tuned, typically ranging from 6000 to 10000. Rather than increasing the number of rounds, restarting the process periodically proves to be a more effective strategy.
