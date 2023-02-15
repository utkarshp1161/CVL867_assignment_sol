from utils.rng import rng_pm, rng_usual
from utils.random_walk import random_walk_1d, mean_sq_disp, random_walk_nd, simulate_collision2d
import matplotlib.pyplot as plt
import pdb as pdb
import numpy as np
from utils.utils_plot import plot
import pdb as pdb
import fire




def average_mult_sim(seeds, num_jump_lis, bias_flag = False, bias = 0.5):
    """
    Args:
        seeds: list
        num_jump_lis: list 


    returns: list of lists
    """
    lis_jump_seed = []
    for this_many_jump in num_jump_lis:
        lis_seed = []
        for seed in seeds:
            lis_x, disp,  lis_x_sq = random_walk_nd(dim = 1, num_jumps = this_many_jump, seeds = seed, bias_flag=bias_flag, bias=bias)
            lis_seed.append(disp[0])
        lis_jump_seed.append(np.mean(lis_seed))
    
    return lis_jump_seed


# def main_():
#     #rand_array = rng_pm(a = 18, l0= 71, seed = 167, n = 200)
#     #plt.hist(rand_array)
#     #plt.savefig("histogram.png")
#     #print(rand_array)
#     lis_x, disp,  lis_x_sq = random_walk_nd(dim = 2, num_jumps = 1000, seeds = [1,10])
#     plt.plot(lis_x[0], lis_x[1])
#     #plt.plot(rand_walk)
#     #plt.show()
#     #plt.savefig()
#     #plot(rand_walk, c = "mo", label= "x", dim = 2)
#     #print(lis_x[0])
#     #print(disp[0])
#     #print(mean_sq_disp(rand_walk[0]))
#     #print(np.square(rand_walk[0]))
#     #plot_x(rand_walk_x_2, c = "bo")
#     #plot_x_square(rand_walk)
#     #plt.legend()
#     ##plt.show()
#     plt.pause(1)
#     input("<Hit Enter>") # asking for input from user
#     #plt.close()
#     #raw_input("<Hit Enter To Close>")
#     #pdb.set_trace()
#     #avg_multi_sim = average_mult_sim(seeds = [i for i in range(10000)], num_jump_lis = [200, 2000, 1000, 800])
#     #print(avg_multi_sim)
    
from sklearn.metrics import r2_score

def main(ques = 7):

    def Q1():
        lis_x, disp,  lis_x_sq = random_walk_nd(dim = 1, num_jumps = 1000, seeds = 1)
        plot(lis_x, c = "m", label= "X", dim = 1 )
        #plot(lis_x_sq, c = "b", label= "x_square", dim = 1)
        plt.legend()
        plt.xlabel("Step number")
        plt.ylabel("X")
        plt.savefig("Q1_a")

    def Q1_b():
        lis_x, disp,  lis_x_sq = random_walk_nd(dim = 1, num_jumps = 1000, seeds = 1)
        plot(lis_x_sq, c = "m", label= "X^2", dim = 1 )
        #plot(lis_x_sq, c = "b", label= "x_square", dim = 1)
        plt.legend()
        plt.xlabel("Step number")
        plt.ylabel("X^2")
        plt.savefig("Q1_b")


    def Q2():    
        #avg_multi_sim = average_mult_sim(seeds = [i for i in range(10000)], num_jump_lis = [200, 2000, 1000, 800])
        avg_multi_sim_5 = average_mult_sim(seeds = [i for i in range(5)], num_jump_lis = [200, 800, 1000, 2000 ])
        avg_multi_sim_10 = average_mult_sim(seeds = [i for i in range(10)], num_jump_lis = [200, 800, 1000, 2000 ])
        avg_multi_sim_100 = average_mult_sim(seeds = [i for i in range(100)], num_jump_lis = [200, 800, 1000, 2000 ])
        avg_multi_sim_1000 = average_mult_sim(seeds = [i for i in range(1000)], num_jump_lis = [200, 800, 1000, 2000 ])

        #pdb.set_trace()
        avg_multi = [avg_multi_sim_5, avg_multi_sim_10, avg_multi_sim_100, avg_multi_sim_1000]
        #print(avg_multi)
        plt.figure(figsize=(10,9))
        
        for plot in range(4):
            plot_, = plt.plot( [200, 800, 1000, 2000 ], avg_multi[plot] , "o" )
            r_squared = round(r2_score([200, 800, 1000, 2000 ], avg_multi[plot]), 3)
            plot_.set_label("Number of simulations = " + str([5, 10, 100, 1000 ][plot]) + "\n" + "r_square" + " = " + str(r_squared))
            #plot_.set_label(str(plot))
            #plt.plot([200, 800, 1000, 2000 ], avg_multi[plot] , linestyle='dashed' )
            plt.xlabel("Number of steps")
            plt.ylabel("Mean_squared_displacement")
            plt.legend(fontsize = "x-small")
            #break
            #plt.xlim(xmin = 0, xmax = 1600)
            #plt.annotate("r-squared = {:.3f}".format(r_squared ), (0, 1))
        plt.plot([200, 800, 1000, 2000 ], avg_multi[3] , color = "r", linestyle='dashed' )
        plt.savefig("Q2_alt_multi")


    def Q3():
        plt.figure(figsize=(10,8))
        for bias, c in zip([0.1, 0.2, 0.4, 0.5], ["r", "b", "g", "m" ]):
            avg_multi_sim = average_mult_sim(seeds = [i for i in range(10000)], num_jump_lis = [5, 10, 20, 30], bias_flag = True, bias = bias)
            r_squared = round(r2_score([5, 10, 20, 30], avg_multi_sim), 3)
            plot_, = plt.plot([5, 10, 20, 30],avg_multi_sim , c)
            plot_.set_label("biased probability" + " = " + str(bias) + "\n" + "r_square" + " = "+ str(r_squared))
            plt.legend(fontsize = "x-small")

        plt.ylim(5, 30)
        plt.xlim(5, 30)
        plt.ylabel("Mean squared displacement")
        plt.xlabel("Step number")
        plt.savefig("Q3")
    
    # def Q3b():
    #     plt.figure(figsize=(10,8))
    #     for bias, c in zip([0.1, 0.2, 0.4, 0.5], ["ro", "bo", "go", "mo" ]):
    #         avg_multi_sim = average_mult_sim(seeds = [i for i in range(10000)], num_jump_lis = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170], bias_flag = True, bias = bias)
    #         r_squared = round(r2_score([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170], avg_multi_sim), 3)
    #         plot_, = plt.plot([50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170],np.log(avg_multi_sim) , c)
    #         plot_.set_label("biased probability" + " = " + str(bias) + "\n" + "r_square" + " = "+ str(r_squared))
    #         plt.legend(fontsize = "xx-small")

    #     plt.ylabel("log of Mean squared displacement")
    #     plt.xlabel("Step number")
    #     plt.savefig("Q3_log_plot")

    def Q4():
        plt.figure(figsize=(10,8))
        lis_x, disp,  lis_x_sq = random_walk_nd(dim = 2, num_jumps = 1000, seeds = [1,10])
        plt.plot(lis_x[0], lis_x[1])
        plt.xlabel("x")
        plt.ylabel("y")
        plt.savefig("Q4")

    def Q5():
        plt.figure(figsize=(10,8))
        sim_lis = [10, 100, 200, 500, 1000, 2000, 3000, 4000, 5000]
        collision_steps = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i,sim in enumerate(sim_lis):
            for this_sim in range(sim):
                collision_steps[i] += simulate_collision2d(num_jumps = 100000, seed = sim)
        
        for i in range(len(sim_lis)):
            collision_steps[i] = collision_steps[i]/sim_lis[i]
        
        plt.plot(sim_lis, collision_steps, 'bo')
        plt.ylabel("Mean_steps_to_collide")
        plt.xlabel("number of simulations")
        plt.savefig("Q5")

    def Q6():
            plt.figure(figsize=(10,8))
            period = rng_pm(a = 18, seed = 71, m = 167, n = 300, period_flag=True)
            rand_array = rng_pm(a = 18, seed = 71, m = 167, n = 500)
            print(period)
            plt.plot(rand_array)
            plt.xlabel("time_step")
            #plt.vlines(ymin=0, ymax=180, x= period, colors="r", linestyles="dashed", label= "period")
            plt.axvline( x= period, color="r", linestyle="dashed", label= "period")
            plt.legend()
            #plt.xticks(x = period)
            plt.ylabel("random_number")
            plt.ylim(0, 200)
            plt.xticks([0, period, 120, 200, 300, 400, 500])
            plt.savefig("Q6")

    def Q6_b():
        a_lis = [i for i in range(200)]
        period = []
        for a in a_lis:
            per = rng_pm(a = a, seed = 71, m = 167, n = 300, period_flag=True)
            period.append(per)
        
        plt.figure(figsize=(10, 8))
        max_value = max(period)
        max_index = period.index(max_value)
        plot_, = plt.plot(a_lis, period, "mo")
        #plot_.set_label("minimum a value for max period = " + str(a_lis[max_index]))
        plt.axvline( x= a_lis[max_index], color="r", linestyle="dashed", label= "minimum 'a' for maximum period")
        plt.xlabel("'a' values")
        plt.ylabel("Period")
        plt.xticks([1, 40, 71, 100, 150, 200])
        plt.legend(loc = "upper right", fontsize = "small")
        plt.savefig("Q6_b")
    
    if ques == 1:
        Q1()
        Q1_b()
    elif ques == 2:
        Q2()
    elif ques == 3:
        Q3()
        # Q3b()
    elif ques == 4:
        Q4()
    elif ques == 5:
        Q5()
    elif ques == 6:
        Q6()
        Q6_b()
    else:
        print("please enter value b/w 1 to 6")

    


    #plt.hist(rand_array)
    #plt.savefig("Q6_hist")







if __name__ == '__main__':
    fire.Fire(main)