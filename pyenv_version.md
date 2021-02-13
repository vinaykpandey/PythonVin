Python version Maintenance status First released End of support Release schedule
https://www.python.org/doc/versions/


https://www.tecmint.com/pyenv-install-and-manage-multiple-python-versions-in-linux/

pyenv
sudo apt install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
vim $HOME/.bashrc 
sudo apt install vim 
vim $HOME/.bashrc 
pyenv global
source $HOME/.bashrc

pyenv install --list | grep " 3\.[678]"
pyenv install --list | grep " 3\.[678]"
pyenv install -l


https://www.tecmint.com/pyenv-install-and-manage-multiple-python-versions-in-linux/

pyenv install 3.6.4
pyenv install 3.9.0

pyenv versions


pyenv install 3.6.4
pyenv install 3.6.5
pyenv versions
pyenv global

pyenv global 3.6.5
pyenv global

pyenv local 3.6.5
pyenv version

pyenv virtualenv 3.6.5 venv_project365

WARNING: pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.


Add the line export PYENV_VIRTUALENV_DISABLE_PROMPT=1 in your $HOME/.bashrc file, where you added other pyenv configs, and source the file to simulate the behavior being emphasized.

pyenv deactivate
pyenv commands


celery rdb



virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt







