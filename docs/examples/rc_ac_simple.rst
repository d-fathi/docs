RC low-pass: how to use analysis(mode="ac")
===========================================

Script: ``rc_ac_simple.py``

Description::

           in o---[ R ]---+---o out
                          |
                         [ C ]
                          |
                         gnd
    Cut-off frequency  fc = 1 / (2 pi R C) = 1 kHz  for R = 1 kOhm, C = 159.155 nF

Code
----

.. literalinclude:: rc_ac_simple.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/rc_ac_simple.png
   :alt: RC low-pass: how to use analysis(mode="ac")
   :align: center

