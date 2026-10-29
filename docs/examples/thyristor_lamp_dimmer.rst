Thyristor lamp dimmer (half-wave phase control, three angles)
=============================================================

Script: ``thyristor_lamp_dimmer.py``

Description::

    VAC -> lamp load -> SCR (anode a, cathode k = common return), gate pulse g.
    The pulse fires the SCR at the angle theta after the start of every positive
    half-cycle; the lamp then conducts until the current falls to zero.
    The later the pulse (theta1 < theta2 < theta3) the dimmer the lamp.
      lamp power  P = Vm^2 / (4 pi R) * [(pi - theta) + sin(2 theta) / 2]
    (the lamp is a resistor: R = 800 Ohm, about a 60 W / 220 V lamp).

Code
----

.. literalinclude:: thyristor_lamp_dimmer.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/thyristor_lamp_dimmer.png
   :alt: Thyristor lamp dimmer (half-wave phase control, three angles)
   :align: center

