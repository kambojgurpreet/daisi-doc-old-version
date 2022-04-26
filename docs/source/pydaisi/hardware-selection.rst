
Hardware selection
============================


Daisies workers can operate on a variety of hardware, both CPUs and GPUs, and the choice can be made at run time.
A worker will have access to the full hardware resources, meaning that a daisi code written for multi processing could access 
mutiple cores.

.. code-block:: python

    import pydaisi as pyd
    
    my_daisi = pyd.Daisi("Zero Shot Text Classification")

    my_daisi.set_hardware('gpu')
    
    result = my_daisi.compute(text="Let's go the moon", 
                            candidate_labels = "astronomy, travel")

Will execute the `"Zero Shot Text Classification" <https://app.daisi.io/daisies/237587e0-7c47-4a4f-afad-80370c8e98a4/how-to-use>`_ daisi on GPUs.

The following choice of hardware is available and can be passed as an argument to the ``Daisi.set_hardware()`` method:

.. list-table:: Choice of hardware to execute daisies
   :widths: 25 25
   :header-rows: 1

   * - Command
     - Description
   * - ``cpu``
     - Regular cpu
   * - ``cpu_32``
     - 16 cores, 32Gb RAM
   * - ``cpu_64``
     - 64 cores, 128Gb RAM
   * - ``cpu_128``
     - 128 cores, 256Gb RAM
   * - ``gpu``
     - GPU






