import os
import shutil 
from cemrg_plugin_generator.Constants import PLUGIN_FOLDER

class PluginGenerator:
    def __init__(self, plugin_name, symbolic_name, view_name, vendor, license_file, overwrite=False) :
        self.plugin_name = plugin_name
        self.symbolic_name = symbolic_name
        self.view_name = view_name
        self.vendor = vendor
        self.license_file = license_file
        self.destination_folder = None
        self.overwrite = overwrite
    
        self.fill_placeholder_variables()

        self.file_names = {
            'mitkPluginActivator' : self.replacements['activator-class-name'],
            'QmitkTemplateView': self.replacements['view-class-name']
        }

    def output_name(self) :
        return self.plugin_name.replace(' ', '_')
    
    def walk(self, folder) :
        list_of_files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                list_of_files.append(os.path.join(root, file))
        
        return list_of_files
    
    def fill_placeholder_variables(self) : 
        self.replacements  = {
            'plugin-target' : self.symbolic_name.replace('.', '_'),
            'plugin-symbolic-name' : self.symbolic_name, 
            'plugin-name' : self.plugin_name.replace(' ', ''),
            'plugin-export-directive' : self.symbolic_name.split(".")[-1].upper() + "_EXPORT",
            'activator-file-name' : self.symbolic_name.replace('.', '_') + '_Activator',
            'activator-class-name' : self.symbolic_name.replace('.', '_') + '_Activator',
            'view-file-name' : f'{self.view_name}View',
            'view-class-name': f'{self.view_name}View',
            'vendor' : self.vendor,
            'view-id' : f'org.mitk.views.{self.view_name.lower()}view',
            'view-name' : self.view_name,
            'license' : self.get_license_text()
        }

    def print_self(self) :
        for key, value in self.replacements.items():
            print(f'{key}: {value}')

    def copy_template_folder(self, src, dest):
        if os.path.exists(dest) and self.overwrite is True: 
            print(f'Overwriting {dest}')
            shutil.rmtree(dest)

        shutil.copytree(src, dest)

    def rename_file(self, src, dest) :
        shutil.move(src, dest)

    def get_license_text(self) :
        res = '/*========================================================================='
        with open(self.license_file, 'r') as file:
            res += file.read()
        res += '\n=========================================================================*/\n\n'

        res += '/*=========================================================================\n'
        res += '*\n'
        res += f'* CemrgApp Plugin - {self.plugin_name}\n'
        res += '*\n'
        res += '* Cardiac Electromechanics Research Group\n'
        res += '* http://www.cemrgapp.com\n'
        res += '* info@cemrgapp.com \n'
        res += '*\n'
        res += '* This software is distributed WITHOUT ANY WARRANTY or SUPPORT!\n'
        res += '* \n'
        res += '=========================================================================*/\n\n'

        return res
    
    def create_plugin(self, dest_folder) :
        self.copy_template_folder(PLUGIN_FOLDER, dest_folder)
        self.destination_folder = os.path.abspath(dest_folder)

        list_of_files = self.walk(self.destination_folder)
        for file_path in list_of_files:
            if not file_path.endswith('.png') : 
                print(f'Processing {file_path}')
                self.replace_placeholder(file_path)
        
        src_dir = os.path.join(self.destination_folder, 'src', 'internal')
        classes_files = os.listdir(src_dir)
        for file in classes_files:
            for key, value in self.file_names.items():
                if key in file:
                    new_name = file.replace(key, value)
                    self.rename_file(os.path.join(src_dir, file), os.path.join(src_dir, new_name))
    
    def replace_placeholder(self, file_path) :
        with open(file_path, 'r') as file:
            filedata = file.read()
                
        for key, value in self.replacements.items():
            filedata = filedata.replace(f'$({key})', value)
        
        with open(file_path, 'w') as file:
            file.write(filedata)


    
