# csse473
Student-facing materials for CSSE/MA 473 Design and Analysis of Algorithms

## Python Environment Setup Instructions
(with thanks to Dr. Kyle Wilson for some tips, such as `virtualenvwrapper`)
1. Clone the `csse473` repository into an appropriate local (not OneDrive) directory. 
2. Install Python 3.10+. Feel free to use pip or conda, whichever you prefer. 
3. (Recommended) Create a virtual Python environment for this course. Consider using `virtualenvwrapper`. Install instructions are [here](https://virtualenvwrapper.readthedocs.io/en/latest/). This gives you easy-to-remember commands such as:
```
mkvirtualenv [envname] # new python environment
deactivate [envname] # leave the virtual environment
rmvirtualenv [envname] # delete a virtual environment
workon [envname] # load (or switch to) an environment
```
4. Install the necessary Python libraries from `requirements.txt`. Using pip, this might look like 
```
pip3 install -r ./requirements.txt
```
5. If something seems buggy about your environment it's easy to get a fresh slate: 
- deactivate your virtual environment
- delete it
- create a new blank one 
- install the requirements.txt file
