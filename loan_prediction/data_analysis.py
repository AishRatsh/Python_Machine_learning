#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np 
import matplotlib as plt

df = pd.read_csv("train.csv")
print df.describe()