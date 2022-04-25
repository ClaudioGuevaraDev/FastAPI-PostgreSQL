#!/bin/sh

conda create --name fastapi python=3.10 -y

conda activate fastapi

conda install -c conda-forge fastapi -y
conda install -c conda-forge uvicorn -y
conda install -c conda-forge tortoise-orm -y