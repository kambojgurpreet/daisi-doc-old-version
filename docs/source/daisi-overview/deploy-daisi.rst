
Your first daisi
==============================

From Python code to a deployed serveless function in one click
-----------------------------------------------------------------

Let's start by creating a simple *Print Hello* daisi.   

The Python code is just a regular Python function:

.. code-block:: python

   def hello(name = "World"):

    return "Hello " + str(name)

Turning this code into a deployed serverless function only requires two steps:   

#. Step 1 : Push the code to a Github repository.    

#. Step 2 : Register the code in the Daisi platform   

Connect to `app.daisi.io <https://app.daisi.io>`_ and log in or sign up with your Github account.   

Click on the **Create a new daisi** button, give the daisi a name (*Print Hello* for instance) and enter the address to the Github repository.

On the next screen, confirm the branch to use, the folder in the repository and the Python script containing the function. Then click on **Create**.

The Daisi platform will automatically parse the requirements, create a virtual environment and generate an endpoint for every function in the code.

Open the card corresponding to the new *Print Hello* daisi and go to the 
"How to" tab. Our code contains simply one function, so only one endpoint has
been created. In case that multiple functions are present in the main script, 
there will be one endpoint per function.   

*Print Hello* can be called from various clients, including with a regular HTTP request (see the *CURL* tab).   
At the moment, the Python client pyDaisi is the most developed. 


Calling daisies remotely from Python
-----------------------------------------------------

