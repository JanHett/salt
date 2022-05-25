Architecture
============

On the topmost level, Salt is split into two parts:

* The Model, View and Controller (collectively referred to as MVC)
* The image processing library

The former is concerned with state management and representing this state to the user. This also means that the MVC layer manages serialisation.

The latter implements the image processing operations and while it is called upon by the MVC layer, it should remain largely independent of it.

:doc:`The MVC layer <reference/mvc/index>`
------------------------------------------

Inside the MVC layer, the responsibilities are as follows

:doc:`Model <reference/mvc/model>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* "Dumb" state management
* The only logic the model should be concerned with is that of correct access

View
~~~~

* "Dumb" visual representation of the state and first-line handling of user input
* The view should only handle logic immediately required for interaction (e.g. modifying UI elements in reaction to user input, updating the UI when the relevant handlers are called, etc.)

:doc:`Controller <reference/mvc/controller>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The link between the model and the view
* A controller may link multiple views to a single model
* Complex logic (e.g. modifying a view only if the model is in a certain state) should live here
* The ``SessionController`` in particular also manages the distinction between graphical and headless mode

:doc:`The image processing library <reference/processing/index>`
----------------------------------------------------------------

Description to follow ASAP
