#!/bin/bash
#SBATCH --job-name clip_run
#SBATCH --qos=blanca-sol
##SBATCH --partition=shas
#SBATCH --account=blanca-sol
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 24    # grab 72 cores
#SBATCH --time 24:00:00
#SBATCH --mail-type=ALL
#SBATCH --export=NONE
#SBATCH --threads-per-core=1
#SBATCH --output=./output/clip_cut_%j.out
#SBATCH --mail-user=frra1220@colorado.edu

set -e
ml purge

ml paraview/5.6.0

#xvfb-run --server-args="-screen 0 1024x768x24" mpiexec -np 4 pvbatch --mesa-llvm clip_paraview_312.py

xvfb-run --server-args="-screen 0 1024x768x24" pvpython --mesa-llvm clip_transfer_update.py

