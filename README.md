# capcad 🔨

a website to generate cad models of capacitors at arbitrary dimensions for use in EDA software, because im sick of making cylinders in freecad

## setup

```
# Install to ~/mambaforge
curl -L -o mambaforge.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash mambaforge.sh -b -p $HOME/mambaforge
```

```
# Activate
source $HOME/mambaforge/bin/activate
```

make environment

```
conda create -n cq231
conda activate cq231
mamba install cadquery=2.3.1
mamba install flask
```

## todo:

- [ ] setup a proper dev env (npm or some other web dev trash) because this is pain to do manually and my ide has no completions
- [ ] make code gooder, lot of LLM junk in here
- [ ] make the model actually look like a cap
- [ ] let user actually download the model
- [ ] make it not eye cancer
- [ ] profit
