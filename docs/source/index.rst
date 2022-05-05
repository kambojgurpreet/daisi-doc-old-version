.. highlight:: python

##########################
Daisi's documentation
##########################

**Daisi** `(app.daisi.io) <https://app.daisi.io>`_ is a distributed Cloud Computing platform running Python serverless functions, named *daisies*.   

Daisi brings the power of cloud computing into the hands of every developer, scientist, engineer by adding endpoints automatically and letting anyone calling it seamlessly from any environment.

Serverless means that there is no need to manage infrastructure, with the ability to scale elastically depending on the demand.   

Daisies can be used to create web services much more easily and rapidly than traditional cloud platforms. 
They can also be used to accelerate compute intensive workloads, especially embarassingly parallel jobs 
where they can scale up instantly to thousands of processes on demand.  

Any regular Python function can be turned into a *daisi* by simply registering it in the Daisi platform, with **no need to write any specific code**. 
The only action needed is to link the Github repository of the code in the platform.   


.. note::

   This project is under active development.


Quick start with the Python pyDaisi package
======================================================

1. Install the *pydaisi* Python package:

.. code-block:: shell

      pip install --upgrade pydaisi

2. In your code, a iPython console or a Jupyter notebook, import *pydaisi*:

>>> import pydaisi as pyd

3. You can now immediately start calling any existing daisi in the platform.
Instantiate locally a Daisi object which will make reference to a remote daisi by passing its name in argument:

>>> my_daisi = pyd.Daisi("Print Hello")

.. note::

   Check this daisi on app.daisi.io : `"Print Hello" <https://app.daisi.io/daisies/2263a2fe-31b1-4af7-9ff8-575cab3c7f0a/how-to-use>`_   

   Instructions on how to call a daisi is documented in the **How to** tab of each daisi page in `(app.daisi.io) <https://app.daisi.io>`_

4. Execute one of the endpoints of this daisi:

>>> result = my_daisi.hello("World")

5. *result* is a Daisi Execution object. Get the returned value with:

>>>  print(result.value)
'Hello World'

