# Create Plugins for CemrgApp with a simple Python script   

## Quick start 
There is no need to install anythin as the libraries used are common python libraries. 
After cloning the repository 
```
git clone https://github.com/OpenHeartDevelopers/cemrg_plugin_generator.git cemrg_plugin_generator
```

and `cd` into the selected folder `cemrg_plugin_generator`, add the folder to the `PYTHONPATH`: 
```
export PYTHONPATH=$PYTHONPATH:$PWD
```

The help text is below: 
```
➜ python scripts/plugin_generator.py -h                                              
usage: plugin_generator.py [-h] [-pn PLUGIN_NAME] [-sn SYMBOLIC_NAME] [-vn VIEW_NAME] [-v VENDOR]
                           [-l LICENSE] [-d] [-ow]

optional arguments:
  -o  / --output  OUTPUT_FOLDER (Output will be in OUTPUT_FOLDER/PLUGIN_NAME )
  -pn / --plugin-name PLUGIN_NAME 
  -sn / --symbolic-name SYMBOLIC_NAME (default = kcl.cemrgapp.myplugin)
  -vn / --view-name VIEW_NAME (View filename )
  -v / --vendor VENDOR (default = CEMRG)
  -l / --license LICENSE_PATH 
  -d, --debug 
  -ow, --overwrite 
```

