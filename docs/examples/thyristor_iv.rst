Thyristor characteristics I(V)
==============================

Script: ``thyristor_iv.py``

Description::

    A DC source with a 10 Ohm series resistor is swept from -50 V up to 200 V and
    back (analysis(mode="dc", param=...)); the thyristor current is plotted
    against its own voltage Vak.
      * Ig = 0   : the SCR blocks (leakage) until the forward breakover voltage
                   Vbo = 100 V, then jumps to the on-state; on the way back it
                   stays on until the current falls below the holding current Ih.
      * Ig = 8 mA (above Igt): it turns on at once, with no breakover.
    The gate current is changed with sweep() (gate source 0 V / 3 V via 300 Ohm).
    The on-state is  Vak = Von + Ron * I.

Code
----

.. literalinclude:: thyristor_iv.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/thyristor_iv.png
   :alt: Thyristor characteristics I(V)
   :align: center

