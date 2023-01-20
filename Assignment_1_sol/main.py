from pyriodic_table.chemelements import Element
from utils.max_val import max_value_algo1, max_value_algo2
import random
from utils.corr import  compute_pearson, compute_spearman
from utils.sorting_ import bubble_sort_lis, merge_sort_lis, selection_sort_lis
import time
import matplotlib.pyplot as plt



def make_property_list(n, seed=42):
    random.seed(seed)
    random_atomic_number_list = random.sample(range(1, 82), n)
    print("sampling elements done================================================================")
    lis_elements = []
    for atomic_num in random_atomic_number_list:
        #print(atomic_num)
        i = Element(atomic_num)
        element_prop = [i.name, i.atomic_number, i.atomic_mass, i.density, i.melting_point_k, i.boiling_point_k]
        #print(i.name)
        lis_elements.append(element_prop)

    # craete data
    element_name_lis = [i[0] for i in lis_elements]
    atomic_number_lis = [i[1] for i in lis_elements]
    atomic_mass_lis = [i[2] for i in lis_elements] # amu
    element_density_lis = [i[3] for i in lis_elements] # g/cm^3
    melting_pt_lis = [i[4] for i in lis_elements] # kelvin
    boiling_pt_lis = [i[5] for i in lis_elements] # kelvin

    properties = {"atomic_numbers":atomic_number_lis, "mass_numbers": atomic_mass_lis, "densities": element_density_lis, "melting_pt": melting_pt_lis, "boiling_pt": boiling_pt_lis}

    return properties

def main(n, seed = 42):
    properties = make_property_list(n, seed)
   
    print("properties============================================================================")
    for i in properties.keys():
        print(f"{i}_sampled", properties[i].copy(), "\n")

    print("Maximum value of each properties================================================")
    for i in properties.keys():
        print(f"maximum_{i}_algo1", max_value_algo1(properties[i].copy())[0],"\n")
        print(f"maximum_{i}_algo2", max_value_algo2(properties[i].copy())[0], "\n")


    print("Sorted list of properties=========================================================")
    for i in properties.keys():
        print(f"bubble_sort_{i}", bubble_sort_lis(properties[i].copy())[0],"\n")
        print(f"merge_sort_{i}", merge_sort_lis(properties[i].copy())[0],"\n")
        print(f"selection_sort_{i}", selection_sort_lis(properties[i].copy())[0],"\n")



    print("correlation========================================================================")

    print(properties["mass_numbers"])
    print("pearson_corr_mass_density", compute_pearson(properties["mass_numbers"].copy(), properties["densities"].copy()))

    print("spearman_corr_mass_density", compute_spearman(properties["mass_numbers"].copy(), properties["densities"].copy()))

    print("pearson_corr_melting_pt_boiling_pt", compute_pearson(properties["melting_pt"].copy(), properties["boiling_pt"].copy()))

    print("spearman_corr_melting_pt_boiling_pt", compute_spearman(properties["melting_pt"].copy(), properties["boiling_pt"].copy()))


    print("pearson_corr_melting_pt_density", compute_pearson(properties["melting_pt"].copy(), properties["densities"].copy()))

    print("spearman_corr_melting_pt_density", compute_spearman(properties["melting_pt"].copy(), properties["densities"].copy()))







def time_complexity_analysis(list_of_n, seed = 42):
    
    time_max_val_algo1 = []
    time_max_val_algo2 = []
    time_bubble_sort = []
    time_merge_sort = []
    time_selection_sort = []
    for n in list_of_n:
        
        #time_dict[str(counter) 
        
        properties = make_property_list(n, seed)
        print(f"=================Run{n}================================================")
        i = list(properties.keys())[-1]
        time_max_val_algo1.append(max_value_algo1(properties[i].copy())[1])
        print(f"maximum_{i}_algo1_time", time_max_val_algo1[-1],"\n")
        time_max_val_algo2.append(max_value_algo2(properties[i].copy())[1])
        print(f"maximum_{i}_algo2_time", time_max_val_algo2[-1], "\n")
        time_bubble_sort.append(bubble_sort_lis(properties[i].copy())[1])
        print(f"bubble_sort_{i}", time_bubble_sort[-1],"\n")
        time_merge_sort.append(merge_sort_lis(properties[i].copy())[1])
        print(f"merge_sort_{i}",time_merge_sort[-1],"\n")
        time_selection_sort.append(selection_sort_lis(properties[i].copy())[1])
        print(f"selection_sort_{i}",time_selection_sort[-1],"\n")
        

    x_values = list_of_n
    plt.figure(figsize=(8, 8))
    plot_max_val_algo1, = plt.plot(x_values, time_max_val_algo1, "bo")
    plt.plot(x_values, time_max_val_algo1, color='b', linestyle='dashed')
    plot_max_val_algo1.set_label("Find_max_value_in_list_algo_1")
    plot_max_val_algo2, = plt.plot(x_values,time_max_val_algo2, "go")
    plt.plot(x_values,time_max_val_algo2,color='g', linestyle='dashed')
    plot_max_val_algo2.set_label("Find_max_value_in_list_algo_2")
    plot_time_bubble_sort, = plt.plot(x_values,time_bubble_sort, "ro")
    plt.plot(x_values,time_bubble_sort,color='r', linestyle='dashed')
    plot_time_bubble_sort.set_label("Bubble_sort")
    plot_time_merge_sort, = plt.plot(x_values,time_merge_sort, "ko")
    plt.plot(x_values,time_merge_sort, color='k', linestyle='dashed')
    plot_time_merge_sort.set_label("Merge_sort")
    plot_time_merge_sort, = plt.plot(x_values,time_selection_sort, "mo")
    plt.plot(x_values,time_selection_sort, color='m', linestyle='dashed')
    plot_time_merge_sort.set_label("Selection_sort")

    #ax = plt.axes()
    #ax.set_xticklabels(['20_elements', '40_elements', '80_elements'])
    plt.legend()
    plt.xlabel("Run(No. of elements[20, 40, 80])")
    plt.ylabel("Time in seconds")
    plt.title("Time complexity analysis")
    plt.grid()
    plt.savefig("Time_complexity_analysis_plot")







if __name__ == '__main__':
    main(n=20)
    print("Time complexity analysis================================================started")
    time_complexity_analysis([20,40,80])