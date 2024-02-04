from pythonforandroid.toolchain import Recipe, shprint, current_directory
from os.path import exists, join
import sh
import glob


class BCSFEimplement(Recipe):
    # This could also inherit from PythonRecipe etc. if you want to
    # use their pre-written build processes

    version = '2.7.62'
    url = 'https://files.pythonhosted.org/packages/a3/a5/6b4d6e350f7eea4511249387463bb0d3d15e4f7fded32b4a0aaa66d99f4d/bcsfe-discord-2.7.62.tar.gz'
    #url = 'https://files.pythonhosted.org/packages/d1/c7/4f43241259a669200cfa0a7e29e6049c04433c4b1dec680814123bd3a8bc/bcsfe-discord-{version}.tar.gz'
    name = 'bcsfe-discord'
    # {version} will be replaced with self.version when downloading
    site_packages_name = 'BCSFE_Python_Discord'
    depends = ['python3', 'numpy', 'colored', 'tk', 'python-dateutil', 'requests', 'pyyaml', 'aiohttp', 'kivy', 'setuptools']  # A list of any other recipe names
                                    # that must be built before this
                                    # one

    conflicts = []  # A list of any recipe names that cannot be built
                    # alongside this one

    
        


recipe = BCSFEimplement()
