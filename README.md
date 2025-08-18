# Do VLMs Have Bad Eyes? Diagnosing Compositional Failures via Mechanistic Interpretability

This repository contains code, data and results for the paper "Do VLMs Have Bad Eyes? Diagnosing Compositional Failures via Mechanistic Interpretability" accepted at the [Explainable Computer Vision: Quo Vadis?](https://excv-workshop.github.io/) workshop at the International Conference on Computer Vision (ICCV) 2025.

The python notebooks in order will take you through steps for the CLIP MLP Neuron Activation Analysis (Sec 3.4) described in the paper. This repository contains all the necessary code and data to reproduce the experiments and results presented in the paper.

`data_gen.py` is the script used to create the toy shapes dataset in `generated_images`.

**To setup the environment:**
1. Install packages listed in `requirements.txt`: `pip install -r requirements.txt`
2. Install [ViT-Prisma](https://github.com/Prisma-Multimodal/ViT-Prisma).

**Authors:**
- Ashwath Vaithinathan Aravindan (vaithina@usc.edu)
- Abha Jha (abhajha@usc.edu)
- Mihir Kulkarni (mkulkarn@usc.edu)