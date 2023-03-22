import matplotlib.pyplot as plt
import numpy as np
from .lj_pot import total_lj_potential_gradient

def two_plots(x1, x2, y1, y2, x_label, y1_label, y2_label, title):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(x1, y1, 'g-')
    ax2.plot(x2, y2, 'b-')
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label, color='g')
    ax2.set_ylabel(y2_label, color='b')
    #plt.title(title)
    plt.savefig(title)
    
    
def total_kinetic_energy(velocities):
    """
    Args:
        velocities (array):

    Returns:
    """
    masses = 1
    return 0.5 * np.sum(masses * np.sum(velocities ** 2, axis=1)) 

def assign_velocities(positions, temperature):
    """
    Args:
        positons (array):
        temperature (float):

    Returns:
    """
    masses = 1
    num_particles = len(positions)
    k_b = 1.38064852e-23  # Boltzmann constant
    std_dev = np.sqrt(k_b * temperature / masses)
    velocities = np.random.normal(loc=0, scale=std_dev, size=(num_particles, 3))
    return velocities

def velocity_histogram_subplot(velocities, title):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    ax[0].hist(velocities[:, 0], bins=20)
    ax[0].set_xlabel('x velocity')
    ax[0].set_ylabel('Frequency')
    #ax[0].set_title(title)
    ax[1].hist(velocities[:, 1], bins=20)
    ax[1].set_xlabel('y velocity')
    ax[1].set_ylabel('Frequency')
    #ax[1].set_title(title)
    ax[2].hist(velocities[:, 2], bins=20)
    ax[2].set_xlabel('z velocity')
    ax[2].set_ylabel('Frequency')
    #ax[2].set_title(title)
    plt.savefig(title)
    
"""Write a function to calculate force and acceleration on each particle for the given LJ interaction and perform one step of NVE simulation, using velocity-verlet algorithm."""       
def velocity_verlet(pos, vel, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, dt, rc):
    """
    Args:
        pos (array):
        vel (array):
        species (array):
        box_length (float):
        eps_AA (float):
        eps_AB (float):
        eps_BB (float):
        sigma_AA (float):
        sigma_AB (float):
        sigma_BB (float):
        dt (float):
        rc (float):
    
    Returns: 
    """
    acc = -total_lj_potential_gradient(pos, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc) / 1.0
    pos += vel * dt + 0.5 * acc * dt**2 # full time step
    vel += 0.5 * acc * dt # half time step
    acc = -total_lj_potential_gradient(pos, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc) / 1.0
    vel += 0.5 * acc * dt # half time step
    return pos, vel

def save_xyz_trajectory(trajectory, filename):
    """
    Args:
        trajectory (array): 
        filename (str): 
        
    Returns: 
    """
    with open(filename, 'w') as f:
        num_timesteps, num_particles, _ = trajectory.shape
        for t in range(num_timesteps):
            f.write(str(num_particles) + '\n')
            f.write('Generated by Ovito\n')
            for i in range(num_particles):
                particle_data = trajectory[t, i]
                position = particle_data[:3]
                velocity = particle_data[3:]
                f.write(' '.join(str(x) for x in position) + ' ' + ' '.join(str(x) for x in velocity) + '\n')
                
        
        