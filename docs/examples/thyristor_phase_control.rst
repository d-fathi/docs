Thyristor phase control (half-wave, resistive load)
===================================================

Script: ``thyristor_phase_control.py``

Description::

    A 220 V / 50 Hz mains (311 V peak) feeds a 50 Ohm load through an SCR.  A
    200 us gate pulse (5 V through 100 Ohm) fires the SCR at the angle alpha of
    the positive half-cycle; the SCR then conducts until the current falls
    below the holding current at the end of the half-cycle (natural
    commutation).  The delay of the gate pulse is swept with sweep(), i.e. the
    firing angle is 30, 90 and 150 degrees, and the average load voltage is
    compared with the textbook formula  Vavg = Vm (1 + cos alpha) / (2 pi)
    (and with a numerical reference that includes the on-state drop Von, Ron).

Code
----

.. literalinclude:: thyristor_phase_control.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/thyristor_phase_control.png
   :alt: Thyristor phase control (half-wave, resistive load)
   :align: center

