from Topology import *
from RCSA import RCSA
from Simulation_NetworkLoad import Simulation_NetworkLoad
from Grafics import Grafics
import multiprocessing as mp
import time

def main():

        # --------------------------------------- Simualtion Types ---------------------------------------

        print('\n1 - Network load variation with fixed number of calls  \n2 - Network load variation with fixed number of blockages \n3 - Percentage variation on the network traffic load \n4 - BER variation \n5 - Intercore Crosstalk x Distance')
        simualtion_type = int(input('\n>>> Define a simulation to run: '))
        if simualtion_type == 1 or simualtion_type == 2 or simualtion_type == 3 or simualtion_type == 4 or simualtion_type == 5:
                pass
        else:
                raise ValueError('Invalid simualtion type.')

        # --------------------------------------- Topologies ---------------------------------------

        if simualtion_type != 5:
                print('\n1 - Simple topology \n2 - Topology 1 \n3 - European \n4 - German \n5 - NSFNet \n6 - PacificBell \n7 - US Backbone')
                topology = int(input('\n>>> Select a network topology: '))
                if topology == 1:
                        n_nodes = len(adj01)
                        A = adj01
                        links = links01
                elif topology == 2:
                        n_nodes = len(adjTop1)
                        A = adjTop1
                        links = linksTop1
                elif topology == 3:
                        n_nodes = len(adjEuropean)
                        A = adjEuropean
                        links = linksEuropean
                elif topology == 4:
                        n_nodes = len(adjGerman)
                        A = adjGerman
                        links = linksGerman
                elif topology == 5:
                        n_nodes = len(adjNSFNet)
                        A = adjNSFNet
                        links = linksNSFNet
                elif topology == 6:
                        n_nodes = len(adjPacificBell)
                        A = adjPacificBell
                        links = linksPacificBell
                elif topology == 7:
                        n_nodes = len(adjUSBackbone)
                        A = adjUSBackbone
                        links = linksUSBackbone
                else:
                        raise ValueError('Invalid network topology.')

        # --------------------------------------- Network Types ---------------------------------------
        if simualtion_type != 5:
                print('\n1 - WDM  \n2 - EON')
                network_type = int(input('\n>>> Select a network type: '))
                if network_type == 1:
                        n_cores = int(input('\n>>> Enter the number of cores (1 | 7 | 12 | 19): '))
                        if n_cores == 1 or n_cores == 7 or n_cores == 12 or n_cores == 19:
                                pass
                        else:
                                raise ValueError('The option entered is invalid.')
                        wavelength_bandwidth = int(input('\n>>> Enter the wavelength bandwidth in GHz: '))
                        if wavelength_bandwidth < 0:
                                raise ValueError('The wavelength bandwidth must be positive.')
                        consider_ase_noise = int(input('\n>>> Consider ASE noise? (0 - No | 1 - Yes): '))
                        if consider_ase_noise == 0 or consider_ase_noise == 1:
                                pass
                        else:
                                raise ValueError('The option entered is invalid.')        
                        damp = float(input('\n>>> Enter the distance between inline amplifiers in Km: '))
                        if damp < 0:
                                raise ValueError('The distance between inline amplifiers must be positive.')        
                        consider_xt = int(input('\n>>> Consider multicore crosstalk? (0 - No | 1 - Yes): '))
                        if consider_xt == 0 or consider_xt == 1:
                                pass
                        else:
                                raise ValueError('The option entered is invalid.')                       
                elif network_type == 2:
                        n_cores = int(input('\n>>> Enter the number of cores (1 | 7 | 12 | 19): '))
                        if n_cores == 1 or n_cores == 7 or n_cores == 12 or n_cores == 19:
                                pass
                        else:
                                raise ValueError('The option entered is invalid.')
                        wavelength_bandwidth = None
                        consider_ase_noise = int(input('\n>>> Consider ASE noise? (0 - No | 1 - Yes): '))
                        if consider_ase_noise == 0 or consider_ase_noise == 1:
                                pass
                        else:
                                raise ValueError('The option entered is invalid.')                       
                        damp = float(input('\n>>> Enter the distance between inline amplifiers in Km: '))
                        if damp < 0:
                                raise ValueError('The distance between inline amplifiers must be positive.')
                        consider_xt = int(input('\n>>> Consider multicore crosstalk? (0 - No | 1 - Yes): '))
                        if consider_xt == 0 or consider_xt == 1:
                                pass
                        else:
                                raise ValueError('The option entered is invalid.')        
                else:
                        raise ValueError('Invalid network type.')

        # ---------------------------------------  Parameters and Simulation  --------------------------------------- 
        if simualtion_type != 5:
                rcsa = RCSA()
                mcf = rcsa.Generate(n_nodes, n_cores, links)
                slots, times = mcf.genemcf()
                N = slots.copy()
                T = times.copy()
        simulation = Simulation_NetworkLoad()
        grafics = Grafics()
        load_bp = []
        pool = mp.Pool(mp.cpu_count())               

        if simualtion_type == 1 or simualtion_type == 2 or simualtion_type == 4:
                min_traffic_load = int(input('\n>>> Enter the min. traffic load: '))    
                if min_traffic_load < 0:
                        raise ValueError('Invalid network load.')
                max_traffic_load = int(input('\n>>> Enter the max. traffic load: '))
                if max_traffic_load < 0 or max_traffic_load < min_traffic_load:
                        raise ValueError('Invalid network load.')                
                traffic_load_step = int(input('\n>>> Enter the traffic load step: '))
                if traffic_load_step < 0:
                        raise ValueError('Invalid network load.')
        elif simualtion_type == 3:
                traffic_load = int(input('\n>>> Enter the traffic load: '))
                if traffic_load < 0:
                        raise ValueError('Invalid network load.')
                min_percentage = int(input('\n>>> Enter the min. percentage variation: '))
                if min_percentage < 0:
                        raise ValueError('Invalid percentage.')
                max_percentage = int(input('\n>>> Enter the max. percentage variation: '))
                if max_percentage < 0:
                        raise ValueError('Invalid percentage.')
                percentage_step = int(input('\n>>> Enter the percentage step: '))
                if percentage_step < 0:
                        raise ValueError('Invalid percentage.')
        else:
                n_cores = int(input('\n>>> Enter the number of cores (7 | 12 | 19): '))
                if n_cores == 7 or n_cores == 12 or n_cores == 19:
                        pass
                else:
                        raise ValueError('The option entered is invalid.')
                min_dist = int(input('\n>>> Enter the min. distance: '))
                if min_dist < 0:
                        raise ValueError('Invalid distance')
                max_dist = int(input('\n>>> Enter the max. distance: '))
                if max_dist < 0 or max_dist < min_dist:
                        raise ValueError('Invalid distance')
                dist_step = int(input('\n>>> Enter the distance step: '))
                if dist_step < 0:
                        raise ValueError('Invalid distance.')

        if simualtion_type == 1:
                n_calls = int(input('\n>>> Enter the number of calls: '))
                if n_calls < 0:
                        raise ValueError('Invalid number of calls.')
                print('\nSimulation in progress...\n')
                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                        r = pool.apply_async(simulation.FixedCalls, args=(load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp, n_cores, mcf, consider_xt), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()
                # grafics.plot_blocking_probability(load_bp)
        elif simualtion_type == 2:
                n_blockages = int(input('\n>>> Enter the number of blocked calls: '))        
                if n_blockages < 0:
                        raise ValueError('Invalid number of blockages.')
                print('\nSimulation in progress...\n')
                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                        r = pool.apply_async(simulation.FixedBlockages, args=(load, n_blockages, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp, n_cores, mcf, consider_xt), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()    
                grafics.plot_blocking_probability(load_bp)
        elif simualtion_type == 3:
                n_calls = int(input('\n>>> Enter the number of calls: '))
                print('\nSimulation in progress...\n')                
                t1 = time.time()
                for percentage in range(min_percentage, max_percentage, percentage_step):                        
                        r = pool.apply_async(simulation.LoadVariation, args=(percentage, traffic_load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp, n_cores, mcf, consider_xt), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()
                # simulation.SaveResults(sorted(load_bp))
        elif simualtion_type == 4:
                n_calls = int(input('\n>>> Enter the number of calls: '))
                print('\nSimulation in progress...\n')                
                t1 = time.time()
                for load in range(min_traffic_load, max_traffic_load, traffic_load_step):
                        r = pool.apply_async(simulation.BERVariation, args=(load, n_calls, n_nodes, links, A, N, T, network_type, wavelength_bandwidth, consider_ase_noise, damp, n_cores, mcf, consider_xt), callback=load_bp.append)
                pool.close()
                pool.join()            
                t2 = time.time()   
                grafics.plot_BER_variation(sorted(load_bp), n_calls)
        else:
                t1 = time.time()
                for distline in range(min_dist, max_dist, dist_step):
                        r = pool.apply_async(simulation.xtdistance, args=(distline, n_cores), callback=load_bp.append)
                pool.close()
                pool.join()
                t2 = time.time()
                grafics.plot_crosstalk_distance(load_bp)

        # ---------------------------------------  Results --------------------------------------- 

        simulation.ShowResults(sorted(load_bp), simualtion_type)
        print('\nTime taken =', t2-t1, 'seconds')

if __name__ == '__main__':
    main()
