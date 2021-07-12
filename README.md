# mcmc
初次試用一下github  
放放看用Metropolis–Hastings algorithm破替代密的python code  
有參考網路上其他篇  
F_ref.txt是reference text 主要用來獲得長度2字串的出現頻率，可以自行更改參考其他referencetext  
rd_encrypt.py是一開始生成隨機decoding function  
MCMC_break_substitution在密文太長時可以切割，切的過短會解不出來，切太長可能會溢位。500不錯、<200可能比較難解出來(可優化)  
也可以調MCMC要跑幾個round，通常6000~10000，再上去是有點難有更動了。
