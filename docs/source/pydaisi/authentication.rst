
####################
Authentication
####################

An access token is required to execute private daisies on `app.daisi.io <https://app.daisi.io>`_.   
Private daisies are any daisi which have not been made "Public".    
They can be daisies that you own and visible only to you or daisies which have been shared in a team you belong to.   

An access token might be required to execute public daisies if:   

* The quotas of the Community edition of the platform have been exceeded for the day
* You want to access specific hardware which is not available in the Community edition   


.. note::

    Public daisies don't require a token to be executed, within the limit of the quotas
    of the Community edition


Generate an access token
==============================


Once you are logged on the platform :   

#. click on your account settings (top right) and select **Personal Access Tokens**
#. click on **Generate a New Token** and fill in the form
#. copy the newly generated token and store it in a secret file

.. note::

    This is the only time this token will be visible in the platform. 
    Daisi doesn't store your tokens.   
    You can have multiple tokens. The **Personal Access Tokens** page allows to manage them.


Remote authentication
===========================


In Python
-------------------

In your Python code, an iPython console or a Jupyter notebook, set the ACCESS_TOKEN
environment variable as follow:

.. code-block:: python

    import os
    os.environ["ACCESS_TOKEN"] = <your access token>


With a Shell environment variable
----------------------------------------

Define a *ACCESS_TOKEN* environment variable.    

In a *sh* type shell (sh, bash, ksh, zsh, ...):   

.. code-block:: shell

    export ACCESS_TOKEN=<your access token>

In a *csh* type shell (csh, tcsh, ...):

.. code-block:: shell

    setenv ACCESS_TOKEN <your access token>


With an .env file
-----------------------
