=============
Developpement
=============

Description
-----------

Le site, basé sur Django, **contient trois apps:**

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

Travailler en local
^^^^^^^^^^^^^^^^^^^

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
`rapport d'erreurs <https://sentry.io/organizations/daguincicode/projects/python-django/?project=4506503864451072>`_

* Tester la dernière image docker stable (correspondant à la branche dev)

.. code-block:: bash

    docker run -it --rm -p 8000:8000 daguinci/oc-letting

* Créer une image en local pour test

.. code-block:: bash

    docker build -t daguinci/oc-letting:<nom-de-votre-commit> .

* Envoyer une nouvelle image sur le dépôt docker-hub

.. code-block:: bash

    docker push daguinci/oc-letting:<nom-de-votre-commit>

.. warning::

    Pour les deux étapes précédentes,
    attention à bien mentionner le nom du commit, sous peine d'écraser
    latest, la dernière image stable.

* Mettre à jour la documentation

La documentation est gérée par **ReadTheDocs et Sphinx**.
Les fichiers se trouvent dans le dossier /docs/source.

Une fois aopportées les modifications de la documentation, tester avec:

.. code-block:: bash

    cd docs
    make html

Puis ouvrir le fichier ``docs/_build/html/index.html``

Exécuter la pipeline
^^^^^^^^^^^^^^^^^^^^

CircleCi exécute la pipeline de tests pour chaque commit soumis sur
chaque branche du dépôt Git. Ainsi, pour exécuter cette pipeline:

.. code-block:: bash

    git push origin <nom-de-votre-branche>

Une fois la pipeline terminée avec succès, merger sur dev

.. code-block:: bash

    git checkout dev
    git fetch
    git merge <nom-de-votre-branche>

Á ce stade, la documentation est mise à jour sur
`<https://daguinci-orange-county-lettings.readthedocs.io/en/docs-setup-readthedocs/source/dev.html>`_

Deploiement
-----------

Le déploiement se réalise automatiquement à travers CircleCi,
en cas de commit sur la branche master.

Ainsi, pour déployer:

.. code-block:: bash

    git checkout master
    git fetch
    git merge dev

Après quelques minutes, le site est visible sur
`Render <https://oc-orange-county-letting.onrender.com/>`_
