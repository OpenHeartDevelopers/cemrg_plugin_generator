# Create Plugins for CemrgApp with a simple Python script   

##  Quick start 
There is no need to install anythin as the libraries used are common python libraries. 
After cloning the repository 
```bash
git clone https://github.com/OpenHeartDevelopers/cemrg_plugin_generator.git cemrg_plugin_generator
```

and `cd` into the selected folder `cemrg_plugin_generator`, add the folder to the `PYTHONPATH`: 
```bash
export PYTHONPATH=$PYTHONPATH:$PWD
```

The help text is below: 
```python
➜ python scripts/plugin_generator.py -h                                              
usage: plugin_generator.py [-h] [-pn PLUGIN_NAME] [-sn SYMBOLIC_NAME] [-vn VIEW_NAME] [-v VENDOR]
                           [-l LICENSE] [-d] [-ow]

optional arguments:
  -o  / --output  OUTPUT_FOLDER (Output will be in OUTPUT_FOLDER/PLUGIN_NAME )
  -pn / --plugin-name PLUGIN_NAME 
  -sn / --symbolic-name SYMBOLIC_NAME (default = kcl.cemrgapp.myplugin)
  -vn / --view-name VIEW_NAME (View filename )
  -v / --vendor VENDOR (default = KCL)
  -l / --license LICENSE_PATH 
  -d, --debug 
  -ow, --overwrite 
```

## Create a new plugin in CemrgApp
This is an example usage of plugin generator for the Atrial Strain Motion pipeline:

1. Generate the plugin with the following command
```python
python scripts/plugin_generator.py -pn "Cemrg Atrial Strain Motion" -sn kcl.cemrgapp.atrialstrainmotion -vn AtrialStrainMotion
```
2. Move this new pineline to the `Plugin` folder in CemrgApp. But before doing this, it is advisory to create a new branch called `plugin/atrailstrainmotion` from the `development` branch, and checkout to it
```bash
cd ~/Projects/CemrgApp/cemrgapp
git checkout development 
git checkout -b plugin/atrialstrainmotion

cd ~/Repositories/cemrg_plugin_generator
mv ./kcl.cemrgapp.atrialstrainmotion ~/Projects/CemrgApp/cemrgapp/CemrgApp/Plugins/
```
3. Make the CemrgApp aware of it by
   1. adding `kcl.cemrgapp.atrialstrainmotion: ON` in `PluginList.cmake` under `Plugins` folder
   2. The following instructions are done inside the `Plugins/kcl.cemrgapp.mainapp` folder. You can follow the way previous plugins have been added.
       + Create both `.h` and `.cpp` files in the `perspectives` folder. So `QmitkCemrgAtrialStrainMotion.h`, and `QmitkCemrgAtrialStrainMotion.cpp`
       + Change the `kcl_cemrgapp_mainapp_Activator.cpp` to include the new `QmitkCemrgAtrialStrainMotion` files. 
       + Add the new `QmitkCemrgAtrialStrainMotion` files to the `files.cmake`
       + Add the new plugin to the `plugin.xml` file.

4. Compile the CemrgApp to check if the new plugin is in correct format. 




