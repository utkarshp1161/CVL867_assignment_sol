import numpy as np

# Define the Lennard-Jones potential function
def lj_potential(r, eps, sigma):
    """
    Args:
        r (float): 
        eps (float): 
        sigma (float): 
        
    Returns: float
    """
    attraction = (sigma / r)**12
    repulsion = (sigma / r)**6
     
    return 4 * eps * (attraction - repulsion)






# Define the total potential energy function for the system
def total_lj_potential(positions, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc):
    """
    Args:
        positions (float): 
        species (float): 
        box_length (float): 
        eps_AA (float): 
        eps_AB (float): 
        eps_BB (float): 
        sigma_AA (float): 
        sigma_AB (float):
        sigma_BB (float): 
        rc (float): 
    
    Returns: float
    """
    N = len(positions)
    potential_energy = 0.0
    
    for i in range(N): # total atoms
        for j in range(i+1,N):
            # Calculate the distance between the particles, accounting for periodic boundaries
            dx = positions[i][0] - positions[j][0]
            dy = positions[i][1] - positions[j][1]
            dz = positions[i][2] - positions[j][2]
            
            # impose boundary conditions
            dx -= box_length * np.round(dx / box_length)
            dy -= box_length * np.round(dy / box_length)
            dz -= box_length * np.round(dz / box_length)
            
            r = np.sqrt(dx*dx + dy*dy + dz*dz)
             
            # Calculate the Lennard-Jones potential energy between the particles
            if species[i] == 0 and species[j] == 0:
                eps = eps_AA
                sigma = sigma_AA
            elif species[i] == 0 and species[j] == 1:
                eps = eps_AB
                sigma = sigma_AB
            elif species[i] == 1 and species[j] == 0:
                eps = eps_AB
                sigma = sigma_AB
            elif species[i] == 1 and species[j] == 1:
                eps = eps_BB
                sigma = sigma_BB

            if r < rc:    
                potential_energy += lj_potential(r, eps, sigma)
            
            else:
                potential_energy += 0.0
    
    return potential_energy


def gradient_of_lj_potential(r, eps, sigma):
    """
    Args:
        r (float): 
        eps (float): 
        sigma (float): 
   
    Returns: float
    """
    return -(4 * eps * ((12 * sigma**12) / r**13 - (6 * sigma**6) / r**7))



# Define the gradient of the total potential energy function for the system
def total_lj_potential_gradient(positions, species, box_length, eps_AA, eps_AB, eps_BB, sigma_AA, sigma_AB, sigma_BB, rc):
    """
    Args:
        positions (float): 
        species (float): 
        box_length (float): 
        eps_AA (float): 
        eps_AB (float): 
        eps_BB (float): 
        sigma_AA (float): 
        sigma_AB (float):
        sigma_BB (float): 
        rc (float): 
        
    Returns: float
    """   
    N = len(positions)
    gradient = np.zeros((N,3))
    
    def gradient_of_lj_potential(r, eps, sigma):
        """
        Args:
            r (float):
            eps (float):
            sigma (float):
        
        Returns: float
        """
        attraction_gradient = (12 * sigma**12) / r**13
        repulsion_gradient = (6 * sigma**6) / r**7
        return -(4 * eps * (attraction_gradient - repulsion_gradient))

    
    for i in range(N):
        for j in range(i+1,N):
            # Calculate the distance between the particles, accounting for periodic boundaries
            dx = positions[i][0] - positions[j][0]
            dy = positions[i][1] - positions[j][1]
            dz = positions[i][2] - positions[j][2]
            
            # impose boundary conditions
            dx -= box_length * np.round(dx / box_length)
            dy -= box_length * np.round(dy / box_length)
            dz -= box_length * np.round(dz / box_length)
            
            r = np.sqrt(dx*dx + dy*dy + dz*dz)
            
            # Calculate the Lennard-Jones potential energy between the particles
            if species[i] == 0 and species[j] == 0:
                eps = eps_AA
                sigma = sigma_AA
            elif species[i] == 0 and species[j] == 1:
                eps = eps_AB
                sigma = sigma_AB
            elif species[i] == 1 and species[j] == 0:
                eps = eps_AB
                sigma = sigma_AB
            elif species[i] == 1 and species[j] == 1:
                eps = eps_BB
                sigma = sigma_BB
                
            
            if r < rc*sigma:
                # Calculate the gradient of the Lennard-Jones potential energy between the particles
                dV_dr = gradient_of_lj_potential(r, eps, sigma)
            
            else:
                dV_dr = 0
            
            # for ith particle
            gradient[i][0] += dV_dr * dx / r # gradient in x direction
            gradient[i][1] += dV_dr * dy / r # gradient in y direction
            gradient[i][2] += dV_dr * dz / r # gradient in z direction
            
            # for jth particle
            gradient[j][0] -= dV_dr * dx / r # gradient in x direction
            gradient[j][1] -= dV_dr * dy / r # gradient in y direction
            gradient[j][2] -= dV_dr * dz / r # gradient in z direction
    
    return gradient     # Return the gradient of the total potential energy function    
