#!/bin/bash
#SBATCH --job-name movie_run
#SBATCH --qos=blanca-sol
##SBATCH --partition=shas
#SBATCH --account=blanca-sol
#SBATCH --nodes 1
#SBATCH --ntasks-per-node 24    # grab 72 cores
#SBATCH --time 4:00:00
#SBATCH --mail-type=ALL
#SBATCH --export=NONE
#SBATCH --threads-per-core=1
#SBATCH --output=./output/movie_%j.out
#SBATCH --mail-user=frra1220@colorado.edu

set -e
ml purge

export PATH=/projects/feathern/software/ffmpeg/:$PATH

ffmpeg -y -framerate 6 -i './png_transfer/%*.png' -s:v 900x900 -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p movie_transfer_6.mp4
