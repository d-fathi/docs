IGBT chopper (low-side switch, inductive load, freewheel diode)
===============================================================

Script: ``igbt_chopper.py``

Description::

    A 100 V bus feeds an R-L load (5 Ohm, 0.5 mH) through an IGBT that is
    switched at 20 kHz, duty cycle ~50 %, by a 15 V gate driver (Rg = 10 Ohm).
    The diode in anti-parallel with the load carries the load current while the
    IGBT is off.  What to look for:
      * Vce(on) of a few volts while the IGBT conducts (diode drop + channel),
      * the collector current follows the load current (ripple around ~9 A),
      * at turn-off Vce jumps to Vbus + Vf (diode clamps) and the collector
        current does not drop to zero at once: the "tail current" of the stored
        base charge (Tau).

Code
----

.. literalinclude:: igbt_chopper.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/igbt_chopper_result.png
   :alt: IGBT chopper (low-side switch, inductive load, freewheel diode)
   :align: center

