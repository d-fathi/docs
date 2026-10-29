Comparator: hysteresis loop and RC relaxation oscillator
========================================================

Script: ``comparator_demo.py``

Description::

    1) Hysteresis loop: a DC sweep of the input up and then down.  With
       Vhys = 0.4 V the output switches high at +0.2 V and low at -0.2 V.
    2) Relaxation oscillator: the comparator output charges C through R, the
       inverting input is the capacitor voltage and the other input is a 2.5 V
       reference.  With Vhys = 1 V the capacitor swings between 2.0 V and 3.0 V:
           T = 2 (R + Ro) C ln[(Voh - 2.0) / (Voh - 3.0)] = 2 (R + Ro) C ln 1.5

Code
----

.. literalinclude:: comparator_demo.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/comparator_loop.png
   :alt: Comparator: hysteresis loop and RC relaxation oscillator
   :align: center

.. image:: /_static/examples/comparator_oscillator.png
   :alt: Comparator: hysteresis loop and RC relaxation oscillator
   :align: center

