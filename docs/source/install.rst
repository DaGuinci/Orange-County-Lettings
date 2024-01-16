============
Installation
============

1. Description

Afin d'installer le site en local, voici les étapes à suivre.

2. Cloner le repertoire git

.. code-block:: bash

    cd /path/to/put/project/in
    git clone https://github.com/DaGuinci/Orange-County-Lettings.git

3. Créer l'environnement virtuel

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    python -m venv venv

* Activer l'environnement

.. code-block:: bash

    source venv/bin/activate


* Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel

.. code-block:: bash

    which python


* Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure

.. code-block:: bash

    python --version


* Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel

.. code-block:: bash

    which pip


* Pour désactiver l'environnement

.. code-block:: bash

    deactivate


4. Exécuter le site

.. code-block:: bash

    cd /path/to/Python-OC-Lettings-FR
    source venv/bin/activate
    pip install --requirement requirements.txt
    python manage.py runserver

* Aller sur `http://localhost:8000` dans un navigateur.

