=============
Developpement
=============

Description
-----------

Le site, basé sur Django, est **basé sur trois apps:**

.. code-block:: bash

   oc-lettings-site
   ├── app:home
   │   └── views.py
   │       ├── index
   │       ├── custom_404
   │       ├── custom_500
   │       └── error_generating
   ├── app:profiles
   │   ├── models.py
   │   │   └── Profile
   │   └── views.py
   │       ├── index
   │       └── profile
   ├── app:lettings
   │   ├── models.py
   │   │   ├── Address
   │   │   └── Letting
   │   └── views.py
   │       ├── index
   │       └── letting
   ├── config:oc_lettings_site
       └── settings.py


.. warning::

    Dans l'attente de nouvelles instructions,
    la **base de données, en sqlite, est versionnée**.

    Prenez donc en considération que les modifications sur la base
    auront un impact sur les bases des collaborateurs
    et celle de la production, en cas de push.


Modifications
-------------

1. En local

* Créer une nouvelle branche

.. code-block:: bash

    git checkout dev
    git branch <type-de-modif>/<nature-de-la-modif>

* Effectuer le test pep8

.. code-block:: bash

    source venv/bin/activate
    flake8

* Effectuer la suite de tests

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    pytest --cov=.


.. note::

    La suite de tests intègre la génération d'une erreur 500.
    En cas d'activation de Sentry (cf paragraphe Sentry), une erreur
    est envoyée à chaque execution des tests.

* Activer le logging sur Sentry

Ajouter en local un fichier .env à la racine du projet:

.. code-block:: python

    # .env

    SENTRY_KEY=<clé sentry>

Puis accéder au
`rapport d'errurs <https://sentry.io/organizations/daguincicode/projects/python-django/?project=4506503864451072>`_

* Tester la dernière image docker stable (correspondant à la production)

.. code-block:: bash

     docker run -it --rm -p 8000:8000 $DOCKER_USERNAME/REPO:TAG


* Tester les rapports d'erreur sur Sentry

2. Exécuter la pipeline

3. Deploiement