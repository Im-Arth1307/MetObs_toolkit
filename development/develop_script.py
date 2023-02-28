#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:25:02 2022
@author: thoverga
"""

# import vlinder_toolkit
import os, sys
import pandas as pd
import numpy as np
from pathlib import Path


lib_folder = Path(__file__).resolve().parents[1]
sys.path.append(str(lib_folder))
print(str(lib_folder))

import vlinder_toolkit

# % Import

testdatafile = os.path.join(str(lib_folder), 'tests', 'test_data',  'testdata_okt_small.csv')

static_data =  os.path.join(str(lib_folder), 'static_data', 'vlinder_metadata.csv')




# #% Setup dataset
settings = vlinder_toolkit.Settings()
settings.update_settings(input_data_file=testdatafile,
                          input_metadata_file=static_data,
#                           output_folder='/home/thoverga/Documents/VLINDER_github/vlinder_toolkit'
                          )


dataset = vlinder_toolkit.Dataset()
dataset.import_data_from_file(coarsen_timeres=True)



dataset.get_physiography_data(types=['elevation'])






print(dataset.metadf.head())


