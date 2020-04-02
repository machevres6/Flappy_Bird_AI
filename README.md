# Flappy Bird NEAT Project

I will be following the tutorial by Tech With Tim called [AI Plays Flappy Bird - NEAT Python](https://www.youtube.com/watch?v=MMxFDaIOHsE&list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2)

I'll be taking notes as it goes and keeping tab of my progress through it.  I'm excited to build something 
that I have played before and to create an AI that would actually solve it.  

Lets see if it works. 


For the NN we are going to use: 
* Input: Try to eliminate one of these in the future and see how it works 
    * Bird Y direction
    * Top Pipe Location
    * Bottom Pipe Location
* Output: 
    * Jump or Do not Jump
* Activation Function: We can let NEAT pick activation function for hidden layers
    * We are going to use 'TanH' for this problem 
        * TanH will give results b/w -1 and 1. So we will check if the value is above 0.5 and when it is we will 
        tell the bird to jump
* Population Size: How many birds are going to be going through it. 
    * Gen 0: 100 Birds
    * Gen 1: the best of Gen 0 + x until it equals 100
* Fitness Function: 
    * The birds that get further in the level have better fitness
    * Distance! 
* Max Generations: 
    * 30
    * If the program does not work after 30 itterations then lets change the hyperparameters and try again. 
    
    
THIS THING WORKED MOFOSSSSS!!!!!! 
I changed a couple of the hyperparameters such as: 

* pop_size = 15

I also want to start messing around with activation functions and a bunch of other hyperparameters
