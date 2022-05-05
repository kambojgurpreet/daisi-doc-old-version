
Schedule jobs with Airflow and Daisi
========================================================

`Apache Airflow <https://airflow.apache.org/>`_ is a platform to programmatically author, schedule and monitor workflows.   

Tasks run by Airflow can be executed by daisies.  There is a number of benefits of outsourcing Airflow tasks to daisies :   

- Any deployed daisi is readily actionable as a Airflow task, no need to rewrite code
- The daisies catalog is a straightforward solution to manage tasks and recombine them in different Airflow workflows
- Tasks which are embarrassingly parallel can scale immediately on a lage number of CPUs thanks to the daisi `map` framework
- Tasks can access specific hardware when needed
- The deployment of Airflow is much lighter since most of the compute is performed by daisies on the daisi platform

The easiest way to call a daisi to execute a task is to leverage the Airflow operator `PythonOperator` operator and `pydaisi`

.. toctree::

    airflow/getting_started_with_airflow
    airflow/example

