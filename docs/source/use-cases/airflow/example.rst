
Example
=============

In this example, we will build an Airflow DAG with two tasks:   

1. Task 1 : Fetch news from Google News for a certain query using the daisi `GoogleNews <https://app.daisi.io/daisies/62afa319-4408-49c0-ab64-38563f9cea2a/how-to-use>`_
2. Task 2 : Classify each news title between a *positive* or *negative* category with the daisi `Zero Shot Text Classification <https://app.daisi.io/daisies/237587e0-7c47-4a4f-afad-80370c8e98a4/how-to-use>`_

These daisies are already deployed on the platform and ready to be executed. Check their documentation !

We will use `pydaisi` to call these daisies and pass parameters.
Airflow will orchestrate the sequential excution of these tasks, and schedule them as directed.

Step 1 : Imports and daisies instantiation
--------------------------------------------------------

.. code-block:: python

    from airflow import DAG
    from airflow.decorators import task
    import pydaisi as pyd
    import pendulum
    from airflow.operators.python_operator import PythonOperator

    classify = pyd.Daisi("Classify Labels")
    news = pyd.Daisi("GoogleNews")

Step 2 : Create an Airflow DAG
--------------------------------------------------------

.. code-block:: python

    default_args = {
        'owner': 'daisi-user',
        'depends_on_past': False,
        'start_date': pendulum.datetime(2021, 1, 1, tz="UTC"),
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
    }

    dag = DAG(
        'Daisi-Airflow-process_news',
        default_args=default_args,
        description='Daisi Example',
        schedule_interval=None,
    )

Step 3 : Define the callable objects
--------------------------------------------------------

The first task will fetch news from Google News.
The `GoogleNews <https://app.daisi.io/daisies/62afa319-4408-49c0-ab64-38563f9cea2a/how-to-use>`_ daisi has a `.get_news()` endpoint to fetch news given a certain query.

As for any daisi endpoint, there is the option of calling it asynchronously and not downloading the results, but only the reference to the execution result.
This is desirable in this case since we can skip storing the actual results in the Airflow database, storing only the reference and passing it to the next task which is powered by a daisi.
This is more efficient and allows to pass directly Python objects between tasks. To do so, we will call the asynchronous endpoint and retrieve the `value_id` attribute, instead of `value`.   


.. code-block:: python

    def get_news(query):
        # Note the asynchronous call with the '_' suffix. We retrieve 'value_id'
        # which is the uuid of the execution result

        return news.get_news_(query = "Apple").value_id[0]
    

.. note::
    The `.get_news()` endpoint returns a Pandas Dataframe which will be stored in the Daisi platform database. 
    `.get_news_().value_id` will return a string which is a reference to the execution result. Try it:   

    >>> import pydaisi as pyd
    >>> news = pyd.Daisi("GoogleNews")
    >>> news.get_news_(query = "Apple").value_id[0]
    'lookup:75c78daa-9058-4839-8722-913330a282d8'


The next task will call the `Classify Labels <https://app.daisi.io/daisies/b7d03b62-76e9-4052-a5d9-ccb3e6b7c0ef/how-to-use>`_ daisi which is a wrapper around the `Zero Shot Text Classification <https://app.daisi.io/daisies/237587e0-7c47-4a4f-afad-80370c8e98a4/how-to-use>`_ daisi. It takes in input a Pandas Dataframe and processes strings from 
a given column, to classify them in the categories defined by *candidate_labels*. 

In this case, we want to retrieve the final results so we will call the synchronous endpoint with `.get_labels()`.
The `sentiment()` function takes in input an Airflow `context` dictionary, which contains the value of the previous task, pulled from the Airflow database with XComms.

.. code-block:: python

    def sentiment(**context):
        news_list_ref = context['templates_dict']['news_list']

        # 'news_list_ref' is the UUID of the get_news daisi execution. It can be passed
        # directly as an argument, as if it were the Pandas dataframe 
        # that '.get_labels() expects' !

        sentiments = classify.get_labels(df=news_list_ref,
                                        column="title",
                                        candidate_labels="positive, negative"
                                        ).value
        print(sentiments)
        return sentiments

Step 4 : Define the tasks and the DAG
--------------------------------------------------------

Then it is straightforward to create two tasks with the `PythonOperator` operator and orchestrate them:

.. code-block:: python

    t1 = PythonOperator(
        task_id='Get_news',
        dag=dag,
        python_callable=get_news,
        op_kwargs = {"query" : "Apple"})

    t2 = PythonOperator(
        task_id='Classify',
        dag=dag,
        python_callable=sentiment,
        provide_context=True,  # Need to pass the context
        templates_dict={'news_list': "{{ ti.xcom_pull(task_ids='Get_news') }}" }) #Pulling out task 1 results (simply a reference to t1 execution results in this case)
    
    t1 >> t2

Copy the code below in a Python script that you will save in the `$AIRFLOW_HOM/dags` folder and refresh the Airflow page in your browser.   
Trigger the execution of the *Daisi-Airflow-process_news* DAG wich should complete in a few seconds !   



.. code-block:: python

    from airflow import DAG
    from airflow.decorators import task
    import pydaisi as pyd
    import pendulum
    from airflow.operators.python_operator import PythonOperator

    classify = pyd.Daisi("Classify Labels")
    news = pyd.Daisi("GoogleNews")

    default_args = {
        'owner': 'daisi-user',
        'depends_on_past': False,
        'start_date': pendulum.datetime(2021, 1, 1, tz="UTC"),
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
    }

    dag = DAG(
        'Daisi-Airflow-process_news',
        default_args=default_args,
        description='Daisi Example',
        schedule_interval=None,
    )

    def get_news(query):
        # Note the asynchronous call with the '_' suffix. We retrieve 'value_id'
        # which is the uuid of the execution result

        return news.get_news_(query = "Apple").value_id[0]

    def sentiment(**context):
        news_list_ref = context['templates_dict']['news_list']

        # 'news_list_ref' is the UUID of the get_news daisi execution. It can be passed
        # directly as an argument, as if it were the Pandas dataframe 
        # that '.get_labels() expects' !

        sentiments = classify.get_labels(df=news_list_ref,
                                        column="title",
                                        candidate_labels="positive, negative"
                                        ).value
        print(sentiments)
        return sentiments

    t1 = PythonOperator(
        task_id='Get_news',
        dag=dag,
        python_callable=get_news,
        op_kwargs = {"query" : "Apple"})

    t2 = PythonOperator(
        task_id='Classify',
        dag=dag,
        python_callable=sentiment,
        provide_context=True,  
        templates_dict={'news_list': "{{ ti.xcom_pull(task_ids='Get_news') }}" })
    
    t1 >> t2