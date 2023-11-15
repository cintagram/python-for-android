from pythonforandroid.toolchain import Recipe, shprint, current_directory
from os.path import exists, join
import sh
import glob


class BCSFEimplement(Recipe):
    # This could also inherit from PythonRecipe etc. if you want to
    # use their pre-written build processes
    #https://files.pythonhosted.org/packages/0c/db/3b5637d34fd231121ba6e4034d6f81e9c9977e4b59ea427ce8d37f4e5f81/bcsfe-discord-2.7.55.tar.gz
    version = '2.7.55'
    url = 'https://files.pythonhosted.org/packages/0c/db/3b5637d34fd231121ba6e4034d6f81e9c9977e4b59ea427ce8d37f4e5f81/bcsfe-discord-2.7.55.tar.gz'
    name = 'bcsfe-discord'
    # {version} will be replaced with self.version when downloading
    site_packages_name = 'BCSFE_Python_Discord'
    depends = ['python3', 'numpy', 'colored', 'tk', 'python-dateutil', 'requests', 'pyyaml', 'aiohttp', 'kivy', 'setuptools']  # A list of any other recipe names
                                    # that must be built before this
                                    # one

    conflicts = []  # A list of any recipe names that cannot be built
                    # alongside this one

    
        


recipe = BCSFEimplement()