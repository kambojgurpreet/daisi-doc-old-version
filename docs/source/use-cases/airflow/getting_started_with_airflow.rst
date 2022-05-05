
Getting started with Airflow
===================================


Please refer to the `Airflow documentation <https://airflow.apache.org/docs/>`_ for a comprehensive overview of Airflow.   


Installing Airflow
----------------------------

Simply install Airflow locally with `pip`:   

.. code-block:: shell

    pip install apache-airflow

Configuration
----------------------------

Airflow needs a working directory. By default it is located in `~/airflow`. You can change this setting with:   

.. code-block:: shell

    export AIRFLOW_HOME=<new airflow location>

Initialize the Airflow database with :   

.. code-block:: shell

    airflow db init

Starting Airflow
----------------------------

Start the Airflow webserver on port 8080 (or any other port) with :   

.. code-block:: shell

    airflow webserver -p 8080

In a different terminal, start the airflow scheduler :   

.. code-block:: shell

    airflow scheduler

Open a web browser and navigate to `http://localhost:8080/admin/`   
It will display the Airflow UI and the content of the `$AIRFLOW_HOME/dags` directory which contain the code of your **Directed Acyclic Graphs** (create manually `$AIRFLOW_HOME/dags` if it doesn't exist)

