import os
import logging
import ray
import json

from Data_generating.data_process.data_concat import Data_Concat
from Data_generating.data_process.data_ready import Data_Ready
from Data_generating.data_process.data_processing import process_all_pdfs
from master.config import *
from master.url_list import url_path_list

#log config setting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("This is an info message.")

# Ray 초기화
if not ray.is_initialized():
    ray.init(num_cpus = config['num_cpus'] , num_gpus = config['num_gpus'])

input_folder = config['input_path']
output_folder = config['output_path']

if url_path_list !=[]:
    for i in range(len(url_path_list)):
        # data_concat
        data_concat = Data_Concat(url_path_list[i], input_folder, output_folder)
        data_concat.gather_files()

        # data_ready
        dr = Data_Ready(input_folder)
        dr.data_ready

        # data_processing
        result = process_all_pdfs(input_folder, output_folder)




