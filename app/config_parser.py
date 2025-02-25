import configparser
from pathlib import PosixPath

def read_config(configfile: str | PosixPath) -> dict | configparser.ConfigParser:
    '''
    read_config(configfile)
    Reads .ini configuration file in configfile and outputs the configuration parameters stated in the file.
    '''
    config = configparser.ConfigParser(
        converters={
            'csv': lambda x: [el.strip().strip('\'') for el in x.split(',')], # read list of comma separated values
            }
    )
    config.read(configfile)

    params = {}
    params['data_dir'] = config.get('Paths','data_dir', fallback='./')
    params['output_dir'] = config.get('Paths', 'output_dir', fallback='./')
    params['gdb_bld_path'] = config.get('Paths', 'gdb_bld_path', fallback='./')

    
    # root_folder = config['Paths']['root_folder']  

    return params
