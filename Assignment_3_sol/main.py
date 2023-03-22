from utils.lj_pot import total_lj_potential, total_lj_potential_gradient
from utils.gradient_descent import gradient_descent
import numpy as np
from utils.utils_ import two_plots, assign_velocities, velocity_histogram_subplot, velocity_verlet, save_xyz_trajectory, total_kinetic_energy
import matplotlib.pyplot as plt
from tqdm import tqdm

def main():
    pos = np.load("data/LJ_A80B20_3D_100_pos.npy")
    species = np.load("data/LJ_A80B20_3D_100_species.npy")
    
    
    print("Initial PE", total_lj_potential(pos, species, box_length=4.3679, 
                             eps_AA=1, eps_AB=1.5, eps_BB=0.5, 
                             sigma_AA=1, sigma_AB=0.8, sigma_BB=0.88, rc=2.5))
    final_positions, energy_lis, grad_lis_norm = gradient_descent(positions=pos, species=species, 
                                                                  box_length=4.3679, eps_AA=1, eps_AB=1.5, eps_BB=0.5, sigma_AA=1, 
                                                                  sigma_AB=0.8, sigma_BB=0.88, rc = 2.5, 
                                                                  grad_func=total_lj_potential_gradient, step_size=0.001, num_steps=1000)
    
    
    # two_plots(x1=range(len(energy_lis)), x2=range(len(grad_lis_norm)), y1=energy_lis, y2=grad_lis_norm, 
    #         x_label='Number of steps', y1_label='Energy', y2_label='Gradient', title='Energy vs Gradient')
    
    vel = assign_velocities(positions=pos, temperature=2)
    
    #velocity_histogram_subplot(velocities=vel, title='Velocity Histogram')
    
    num_steps = 1000
    trajectory = []
    p_energy_lis = [total_lj_potential(pos, species, box_length=4.3679, 
                                     eps_AA=1, eps_AB=1.5, eps_BB=0.5,
                                     sigma_AA=1, sigma_AB=0.8, sigma_BB=0.88, rc=2.5)]
    k_energy_lis = [total_kinetic_energy(vel)]
    for i in tqdm(range(num_steps)):
        trajectory.append(np.hstack((pos, vel, species.reshape(-1,1))))
        pos, vel = velocity_verlet(pos, vel, species, box_length=4.3679, 
                                   eps_AA=1, eps_AB=1.5, eps_BB=0.5, sigma_AA=1, 
                                   sigma_AB=0.8, sigma_BB=0.88, dt=0.003, rc=2.5)
        p_energy_lis.append(total_lj_potential(pos, species, box_length=4.3679, 
                                             eps_AA=1, eps_AB=1.5, eps_BB=0.5, 
                                             sigma_AA=1, sigma_AB=0.8, sigma_BB=0.88, rc=2.5))
        k_energy_lis.append(total_kinetic_energy(vel))
    
    energy_lis = np.array(p_energy_lis) + np.array(k_energy_lis)
    
    plt.plot(range(num_steps+1), energy_lis, label='Total Energy')
    plt.plot(range(num_steps+1), p_energy_lis, label='Potential Energy')
    #plt.plot(range(num_steps+1), k_energy_lis, label='Kinetic Energy')
    plt.legend(loc='lower right')
    plt.xlabel('Number of steps')
    plt.ylabel('Energy')
    #plt.title('Energy vs Number of steps')
    plt.savefig('energy_vs_steps_md.png')
    trajectory = np.array(trajectory)
    # Assuming your trajectory array is named "trajectory"
    save_xyz_trajectory(trajectory, 'trajectory.xyz')
    np.save('trajectory.npy', trajectory)
    
if __name__ == "__main__":
    main()