import numpy as np
from .rng import rng_pm, rng_usual
import matplotlib.pyplot as plt


def mean_sq_disp(rand_array):
    """Returns mean squared disp
    Args:
        rand_array: np array

    Returns: number
    """
    disp = np.mean(np.square(rand_array))

    return disp

def sign(rand_num):
    """Returns -1 or 1
    """
    temp = rand_num
    if temp <= 0.5:
        return 1
    else :
        return -1
    
def biased_sign(rand_num, bias = 0.8):
    """Returns -1 or 1
    """
    temp = rand_num
    if temp <= bias:
        return -1
    else :
        return 1

def random_walk_1d(seed,num_jumps, start_pos = 0, bias_flag = False, bias = 0.5):
    """Returns a random walk
    Args:
        a: int
        l0: int
        m: int
        num_jumps: int

    
    Returns: trajectory of random walk
    """
    if bias_flag ==  False:
        x = [start_pos]
        # rand_jumps = rng_pm(a, seed, m, num_jumps)
        rand_jumps = rng_usual(seed, num_jumps)
        for jump in rand_jumps:
            temp = sign(jump) # +1 or -1
            x.append(x[-1] + temp)
        
        x_2 = np.square(x)
    
    else:
        x = [start_pos]
        # rand_jumps = rng_pm(a, seed, m, num_jumps)
        rand_jumps = rng_usual(seed, num_jumps)
        for jump in rand_jumps:
            temp = biased_sign(jump, bias = bias) # +1 or -1
            x.append(x[-1] + temp)
        
        x_2 = np.square(x)

    return x, x_2


def random_walk_nd(dim = 2, num_jumps = 1000, seeds = 21, bias_flag = False, bias = 0.5):
    """Returns n dimensional random walk
    
    """
    lis_x = []
    lis_x_sq = []
    disp_sq_sum = []

    if bias_flag == False:
        if type(seeds) == int:
                rand_walk, rand_walk_x_2 = random_walk_1d(seeds, num_jumps)
            
                lis_x.append(rand_walk)# displacemnt : d = a1 + a2 ... + an = rand_walk[-1]
                lis_x_sq.append(rand_walk_x_2)
                disp_sq_sum.append(np.square(rand_walk[-1])) # <d**2> = <(a1 + a2 .... + an)**2> 

        else:
            for i, seed in zip(range(dim), seeds):
                rand_walk, rand_walk_x_2 = random_walk_1d(seed, num_jumps)
            
                lis_x.append(rand_walk)# displacemnt : d = a1 + a2 ... + an = rand_walk[-1]
                lis_x_sq.append(rand_walk_x_2)
                disp_sq_sum.append(np.square(rand_walk[-1])) # <d**2> = <(a1 + a2 .... + an)**2> 

    else:
        if type(seeds) == int:
                rand_walk, rand_walk_x_2 = random_walk_1d(seeds, num_jumps, bias_flag=bias_flag, bias=bias)
            
                lis_x.append(rand_walk)# displacemnt : d = a1 + a2 ... + an = rand_walk[-1]
                lis_x_sq.append(rand_walk_x_2)
                disp_sq_sum.append(np.square(rand_walk[-1])) # <d**2> = <(a1 + a2 .... + an)**2> 

        else:
            for i, seed in zip(range(dim), seeds):
                rand_walk, rand_walk_x_2 = random_walk_1d(seeds, num_jumps, bias_flag=bias_flag, bias=bias)
            
                lis_x.append(rand_walk)# displacemnt : d = a1 + a2 ... + an = rand_walk[-1]
                lis_x_sq.append(rand_walk_x_2)
                disp_sq_sum.append(np.square(rand_walk[-1])) # <d**2> = <(a1 + a2 .... + an)**2> 


    return lis_x, disp_sq_sum,  lis_x_sq



def simulate_collision2d(num_jumps = 1000, seed = 21, grid = 10):
    """Drunk sailor collison
    
    """
    np.random.seed(seed)
    sailor1_traj = np.array([0, 0])
    sailor2_traj = np.array([5, 5])

    for step in range(num_jumps):
        sailor1_traj = (sailor1_traj + np.array([np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])])) % grid # ensures periodic boundary conditions
        #print(sailor1_traj)
        sailor2_traj = (sailor2_traj + np.array([np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])])) % grid # ensures periodic boundary conditions
        #print(sailor2_traj)
        
        if np.allclose(sailor1_traj, sailor2_traj): # check both elements of 2d array's same ==> same position in grid
            return step + 1 # collison at (step + 1)th step, adding 1 because start index is 0 for step

    
    return num_jumps  # ===> nrever collides (cant assign as imfimity so given max value)






    




    

