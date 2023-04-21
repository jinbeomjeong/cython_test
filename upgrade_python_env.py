import os


upgrade_pip = "python -m pip install --upgrade pip"
upgrade_setuptools = "python -m pip install --upgrade setuptools"
upgrade_wheel = "python -m pip install --upgrade wheel"

commands = [upgrade_pip, upgrade_setuptools, upgrade_wheel]

for command in commands:
    os.system(command)

print("")
print("python environment is upgraded!")
