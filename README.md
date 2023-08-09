# learntunepad

This is the repo for the revamped learn.tunepad.com site!

Developer Environment Setup:

The website is built using HTML/CSS/JS and Python using the Django framework 

If you're not familiar with Django, I highly recommend following the entire w3schools tutorial (https://www.w3schools.com/django/django_intro.php)
Otherwise, just ensure your environment is set up correctly by following only this page https://www.w3schools.com/django/django_create_virtual_environment.php, and installing the most recent version of Django (4.2.3) within your venv.

Rather than starting a new project, you'll need to pull the contents of this repo into that project environment. Essentially your layout should be:

      [yourproject]/
            Include/ 
            Lib/ 
            Scripts/ 
            [thisrepo]/ 
            pyvenv.cfg 

At this point you're just about set up! Most packages are included via CDN except treebeard, which you can find installation instructions and docs for at https://django-treebeard.readthedocs.io/en/latest/install.html

Happy coding!
