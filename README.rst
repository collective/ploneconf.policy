.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

================
Ploneconf policy
================

A policy package for Ploneconf site

Features
--------

Custom content-types:

- Person (a trainer or speaker)
- Talk
- Training
- Time Slot
- Scheduled Talk

Submit proposal
---------------

There are two plone.restapi endpoints to allow users submit their talk proposals:

- @talk-proposal: an endpoint that returns a list of fields for submitting proposal form.
- @submit-proposal: an endpoint (that accept only POST) that creates a Talk and Person object with form data.

This form only works if there are the following folders:

- /site-id/proposals
- /site-id/proposals/talks
- /site-id/proposals/speakers

To allow anonymous users to create contents in this folder, you also need to:

- Publish these folders
- Set "ploneconf.policy: Add Person" and "ploneconf.policy: Add Talk" to "/site-id/proposals" folder from "manage_access" view.


Installation
------------

Install ploneconf.policy by adding it to your buildout::

    [buildout]

    ...

    eggs =
        ploneconf.policy


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/ploneconf.policy/issues
- Source Code: https://github.com/collective/ploneconf.policy


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
