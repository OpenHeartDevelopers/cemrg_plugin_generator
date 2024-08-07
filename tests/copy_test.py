import os
import shutil
import argparse
import cemrg_plugin_generator.PluginGenerator as PG
from cemrg_plugin_generator.Constants import PLUGIN_FOLDER, LICENSE_DEFAULT

def get_plugin_generator(args) :
    input_license_ok = args.license != '' or os.path.exists(args.license)
    license_file = LICENSE_DEFAULT if input_license_ok is True else args.license
    
    return PG.PluginGenerator(args.plugin_name, args.symbolic_name, args.view_name, args.vendor, license_file)

def execute_copy(args) : 
    if args.output is None:
        raise ValueError('Output folder is not defined')
    
    plugin_generator = get_plugin_generator(args)
    plugin_generator.copy_template_folder(PLUGIN_FOLDER, args.output)

def execute_names(args) :
    plugin_generator = get_plugin_generator(args)
    plugin_generator.print_self()
    
def main(args) : 
    if args.mode == 'copy':
        execute_copy(args)
    elif args.mode == 'names':
        execute_names(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test copy function')
    parser.add_argument('mode', choices=['copy', 'names'])
    parser.add_argument('-o', '--output', type=str, help='Output folder', default=None)
    parser.add_argument('-pn', '--plugin-name', type=str, help='Plugin name', default='MyPlugin')
    parser.add_argument('-sn', '--symbolic-name', type=str, help='Symbolic name', default='kcl.cemrgapp.myplugin')
    parser.add_argument('-vn', '--view-name', type=str, help='View name', default='MyView')
    parser.add_argument('-v', '--vendor', type=str, help='Vendor', default='MyVendor')
    parser.add_argument('-l', '--license', type=str, help='License file', default='')

    args = parser.parse_args()
    main(args)
