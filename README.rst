Flask Tensorflow Carcinoma H&E Tissue Image Classifier
======================================================
This project consists of a mixin between `APIConsumer
<https://bitbucket.org/human-forecast/apiconsumer>`_ and `TF-img-api
<https://bitbucket.org/human-forecast/tf-img-api>`_ projects, in their
master branch flavour (HF style for ``APIConsumer`` and H&E Stained
Tissue Image Carcinoma Classifier for ``TF-img-api``). In addition, a
watchdog-like python script has been added.

::

  SCOPE:     [Demo]
  STATUS:    [Production Ready]

Notes:
------
This project relies on Git submodules, so remember using --recursive tag
when cloning.

In case you want to deploy it with Docker, you should take into account
that this project Dockerfile includes commands for tensorflow compilation,
so build phase will take some time. In case you wanted to modify anything
regarding the deployment phase, maybe you should consider splitting the
Dockerfile, in order to avoid repeating compilation multiple times.
