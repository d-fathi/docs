JFET output characteristics (Id versus Vds for several Vgs)
===========================================================

Script: ``jfet_curves.py``

Description::

    Inner loop : DC sweep of Vd (Vds) from 0 to 10 V       -> analysis(param=...)
    Outer loop : one curve for every Vgs in the list       -> sweep(param, list)
    Both are done by a single run().

Code
----

.. literalinclude:: jfet_curves.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/jfet_curves.png
   :alt: JFET output characteristics (Id versus Vds for several Vgs)
   :align: center

