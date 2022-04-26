
Executing a daisi with pydaisi
==================================

Executing a daisi remotely with ``pydaisi`` takes three steps:   

#. Authentication, which is optional to execute public daisies

#. Instantiation of a local Daisi object, making reference to the remote daisi

#. Calling the endpoint of the daisi


An example daisi
------------------------

Let's work with the following python code as an example:   

.. code-block:: python

    import numpy as np

    def stack_arrays(a, b):
        # a, b are 1D numpy arrays

        a += 1
        b += 2

        return np.vstack((a, b))

Without any change to this code, user **User1** creates a daisi named **Example Daisi** and make it public 
(`"Example Daisi" <https://app.daisi.io/daisies/e4a03d4b-8530-4a39-98d8-42e9a7bc6e94/how-to-use>`_ is already on app.daisi.io so you can call it immediately).   

The function ``stack_arrays`` has now and endpoint which can be called remotely, directly with an HTTP request or using
the Python pyDaisi package.    

This function takes as arguments two Numpy arrays. Calling it with the pyDaisi package removes the need to serialize the data.
Actually any Python object can be passed as an argument to a daisi with pyDaisi.

Authentication
-------------------

See the **Authentication** section     


Instantiation of a local Daisi object
-------------------------------------------

The ``Daisi`` class contains methods to trigger the execution of a remote daisi.    
It is instantiated as follows:    

.. code-block:: python

    import pydaisi as pyd
    my_daisi = pyd.Daisi("Example Daisi")

or    

.. code-block:: python

    import pydaisi as pyd
    my_daisi = pyd.Daisi("User1/Example Daisi")

.. note::  

    Specifying the owner of the daisi is safer as nothing prevents several daisies to share the same name.
    However, a user can't create two daisies with the same name.

Calling endpoints : Execution and returns
-------------------------------------------

``stack_arrays`` is now available as a method of the ``my_daisi`` object. 

Parameters can be simply passed as arguments. 

.. code-block:: python

    import numpy as np

    a = np.zeros((10,))
    b = np.ones((10,))
    result = my_daisi.stack_arrays(a=a, b=b)

``result`` is DaisiExecution object. It has attributes which contain the execution status, 
any log or print returned as well as the return of the ``stack_arrays`` execution.   

By default, the return is not downloaded but kept remote so it can be passed directly to a next daisi.   

We can download it and print its value with:   

>>> result.value
array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [3., 3., 3., 3., 3., 3., 3., 3., 3., 3.]])

>>> result.value.shape
(2, 10)

``result`` can be passed immediately as an argument to a next daisi (or to the same daisi in this example):

.. code-block:: python

    result = my_daisi.stack_arrays(a=result, b=b)

>>> result.value
array([[2., 2., 2., 2., 2., 2., 2., 2., 2., 2.],
       [4., 4., 4., 4., 4., 4., 4., 4., 4., 4.],
       [3., 3., 3., 3., 3., 3., 3., 3., 3., 3.]])

>>> result.value.shape
(3, 10)

Exceptions and stack traces
-------------------------------------------

If we pass two arrays with different shapes, the *np.vstack* function will return an exception. The stack trace is sent back
directly to the ``pydaisi`` client :   

.. code-block:: python

    a = np.zeros((10,))
    b = np.ones((8,))
    result = my_daisi.stack_arrays(a=a, b=b)

>>> result.value
return np.vstack((a, b))   
File "<__array_function__ internals>", line 180, in vstack   
File "/usr/local/lib/python3.8/site-packages/numpy/core/shape_base.py", line 282, in vstack   
return _nx.concatenate(arrs, 0)   
File "<__array_function__ internals>", line 180, in concatenate   
ValueError: all the input array dimensions for the concatenation axis must match exactly,    
but along dimension 1, the array at index 0 has size 10 and the array at index 1 has size 8   







