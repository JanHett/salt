Architecture
============

On the topmost level, Salt is split into two parts:

* The Model, View and Controller (collectively referred to as MVC)
* The image processing library

The former is concerned with state management and representing this state to the user. This also means that the MVC layer manages serialisation.

The latter implements the image processing operations and while it is called upon by the MVC layer, it should remain largely independent of it.

The MVC layer
-------------

..:ref:`mvc-layer-reference`
:doc:`reference/mvc/index`

The image processing library
----------------------------
