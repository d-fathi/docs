Thyristor I(V) characteristic in the textbook form
==================================================

Script: ``thyristor_iv_textbook.py``

Description::

    The classic SCR curve: reverse blocking and reverse breakdown (-V, -I),
    forward blocking up to the breakover voltage, the (unmeasurable) negative
    resistance part (dashed), the holding current and the ON state, and the
    gate-triggered turn-on.  The currents are EXAGGERATED on purpose (leakage of
    hundreds of mA, Roff = 500 Ohm) so that the blocking region is visible
    next to the ON state, as in a textbook drawing; with datasheet values see
    thyristor_iv.py.  Every branch is produced by DC sweeps of a source with a
    series resistor (Rs); the up/down sweeps run through the latch hysteresis.

Code
----

.. literalinclude:: thyristor_iv_textbook.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/thyristor_iv_textbook.png
   :alt: Thyristor I(V) characteristic in the textbook form
   :align: center

