import numpy as np
from .lj_pot import total_lj_potential

def gradient_descent(positions, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc, 
                        grad_func, step_size, num_steps):
    """
    Args:
        positions (array): 
        species (array): 
        box_length (float): 
        eps_AA (float): 
        eps_AB (float): 
        eps_BB (float): 
        sigma_AA (float): 
        sigma_AB (float): 
        sigma_BB (float): 
        rc (float): 
        grad_func (function): 
        step_size (float): 
        num_steps (int): 
    Returns: int array of new positions, list of energies, list of gradient norms
    """
    new_positions = positions.copy()
    
    print("Initial potential energy: {}".format(total_lj_potential(new_positions, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc)))
    energy_lis = [total_lj_potential(new_positions, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc)]
    grad_lis_norm = []
    i = 0
    while True:
        grad = grad_func(new_positions, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc)
        if i == num_steps: # condition for convergence
            break
        print(np.linalg.norm(grad))
        grad_lis_norm.append(np.linalg.norm(grad))
        new_positions -= step_size * grad# Take a step opposite of the gradient descent
        print("Step {} potential energy: {}".format(i+1, total_lj_potential(new_positions, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc)))
        energy_lis.append(total_lj_potential(new_positions, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc))
        i += 1
    
    return new_positions, energy_lis, grad_lis_norm