

Map parallel executions
====================================

Let's say that we have an embarrassingly parallel task where a long running function needs to be
executed multiple times on a range of inputs. When this function is deployed as a daisi, its execution
can be distributed over a large number of processors.     

For instance :     

.. code-block:: python

    import time

    def long_wait(duration):
        time.sleep(duration)
    


Without any change to this code, we can create a daisi named **Sleeping Daisi** and make it public 
(`"Sleeping Daisi" <https://app.daisi.io/daisies/5dd072cb-9a11-4665-981b-11a4059043bd/how-to-use>`_ is already on app.daisi.io so you can call it immediately).

.. code-block:: python

    import pydaisi as pyd
    my_sleep_daisi = pyd.Daisi("Sleeping Daisi")

The following call takes 1 second + latency:   

.. code-block:: python

    import time
    start = time.time()

    my_sleep_daisi.long_wait(1)

    print(time.time() - start)

It is a blocking call, meaning that your code will wait for the completion of the task to continue.
Instead of calling it sequentially, we can call it asynchronously by adding the suffix ``_async`` to the method name, and trigger multiple executions in parallel:   

.. code-block:: python

    import time
    start = time.time()

    # Prepare 200 async calls
    futures = [my_sleep_daisi.long_wait_async(1) for _ in range(200)] 
    
    # Launch executions and wait for results
    result = Daisi.run_parallel(*futures, nb_procs = 200) 
    
    print(time.time() - start)

Which will return in about 1 second + latency.   

