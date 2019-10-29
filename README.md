# AI-clustering
This repository contains implementations for three clustering algorithms:
- K-means
- Single-linkage
- Average-linkage

# TL;DR
This is an attempt to parallelize 3 algorithms aiming performance only.

# What we already got here?
Some of them are working perfectly (avg-link might need some adjusts) but, for now, they are very slow.
I decided to minimize function calls to give a brake for the sys stack, it resulted in a 20% per iteration in single-link, for example.
But 

# Milestones
In order to optimize execution time the main goal is implement all three algorithm in parallel, following the priorities:
- 1st --> NVIDIA Cuda
- 2nd --> CPU (many logical cores as viable)
- 3rd --> CPU (physical cores only)

Parallel execution using CPU cores was done only in "execution.py".
