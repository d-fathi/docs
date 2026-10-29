Zener diode: I(V) characteristic and shunt regulator
====================================================

Script: ``zener_regulator.py``

Description::

    1) I(V) of the zener: forward knee at ~0.6 V and reverse breakdown at -Vz.
    2) Shunt regulator  Vin -- Rs -- (zener || RL):
         line regulation  : Vout against Vin (DC sweep), one curve per load RL
         load regulation  : Vout against RL at Vin = 12 V
         ripple rejection : 12 V + 2 V (100 Hz) ripple, attenuation
                            (rz || RL) / (Rs + rz || RL),  rz = dynamic resistance
    Reference: the same I(V) equation written independently in numpy and the
    regulator solved with brentq; rz is the numerical derivative at the operating point.

Code
----

.. literalinclude:: zener_regulator.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/zener_regulator.png
   :alt: Zener diode: I(V) characteristic and shunt regulator
   :align: center

