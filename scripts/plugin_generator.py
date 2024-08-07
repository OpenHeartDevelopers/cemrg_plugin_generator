import os
import shutil
import argparse
import cemrg_plugin_generator.PluginGenerator as PG
from cemrg_plugin_generator.Constants import PLUGIN_FOLDER, LICENSE_DEFAULT

def get_plugin_generator(args) :
    input_license_ok = args.license != '' or os.path.exists(args.license)
    license_file = LICENSE_DEFAULT if input_license_ok is False else args.license

    
    return PG.PluginGenerator(args.plugin_name, args.symbolic_name, args.view_name, args.vendor, license_file, args.overwrite)

def execute_copy(args) : 
    if args.output is None:
        raise ValueError('Output folder is not defined')
    
    plugin_generator = get_plugin_generator(args)
    plugin_generator.copy_template_folder(PLUGIN_FOLDER, args.output)

def execute_names(args) :
    plugin_generator = get_plugin_generator(args)
    plugin_generator.print_self()
    
def main(args) : 
    if args.plugin_name is None:
        raise ValueError('Plugin name (--plugin-name) is not defined')
    
    plugin_generator = get_plugin_generator(args)
    
    if args.debug is True:
        plugin_generator.print_self()
        
    plugin_generator.create_plugin(plugin_generator.output_name())



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new plugin')
    parser.add_argument('-o', '--output', type=str, help='Output folder', default='.')
    parser.add_argument('-pn', '--plugin-name', type=str, help='Plugin name')
    parser.add_argument('-sn', '--symbolic-name', type=str, help='Symbolic name', default='kcl.cemrgapp.myplugin')
    parser.add_argument('-vn', '--view-name', type=str, help='View name', default='MyView')
    parser.add_argument('-v', '--vendor', type=str, help='Vendor', default='CEMRG')
    parser.add_argument('-l', '--license', type=str, help='License file', default='')
    parser.add_argument('-d', '--debug' , action='store_true', help='Debug mode')
    parser.add_argument('-ow', '--overwrite' , action='store_true', help='Overwrite mode')

    args = parser.parse_args()
    main(args)
