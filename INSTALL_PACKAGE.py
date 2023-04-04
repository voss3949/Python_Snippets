import subprocess

# Define the package you want to install
package = 'numpy'

# Run pip to install the package
subprocess.check_call(['pip', 'install', package])

# Or we can write
import pip

pip.main(['install', 'numpy'])
