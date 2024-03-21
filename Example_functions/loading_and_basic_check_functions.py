

import numpy as np

from glob import glob


def get_filelist(path_to_master,subfolder,filetype):
    return glob(path_to_master+subfolder+'/*.'+filetype)

def no_atom_run(dataset, index_limit, threshold):
    return np.mean(np.sum(dataset,axis=0)[:index_limit])<threshold
            
def survived(dataset,start_index, thershold):
    return np.mean(np.sum(dataset,axis=0)[start_index:])>=thershold

def load_runs(file, time_bin, max_time, TDC_resolution=6.25e-10):  #all times need to come in same units (base units are [s])
    data=np.loadtxt(file,dtype=int)
    channel_limits = data[:4] # use one variable as list instad of four standalone variables
    channel_limits_index = np.cumsum(channel_limits)[:-1] # used for splitting of counts array
    triggers = data[4:]*TDC_resolution # split imported values to avoid complicated indexing
    assert np.sum(channel_limits) == triggers.shape[0] # sanity check if channel limit matches loaded values

    triggers_channels = np.split(triggers, channel_limits_index) # split triggers to individual arrays
    
    
    run=np.zeros((4,int(max_time/time_bin))) #container for single run
    for ch in range(len(triggers_channels)):
        batch, timebase= np.histogram(triggers_channels[ch],range=(0,max_time),bins=int(max_time/time_bin)) #time stamps converted to counts per timebin
        timebase=np.delete(timebase, 0)
        run[ch]=batch
    return run, timebase
