Schmitt trigger with two BJT transistors (emitter coupled)
==========================================================

Script: ``schmitt_bjt.py``

Description::

                    Vcc (12 V)
           ┌──────────┬──────────┐
          Rc1        Rc2          │
           │          │           │
           ├──[R1]──┬─┼───── Out  │       Vin ──[Rs]── In ──► Q1 base
           C1       │ │           │
           │       B2 │           │       Q1: c = C1, b = In, e = E
      In ──┤Q1      │ Q2          │       Q2: c = Out, b = B2, e = E
           │       [R2]           │
           E ───────┼─────E───────┘       R1, R2 : feedback divider C1 → B2 → gnd
           │                              Re      : common emitter resistor
          [Re]
           │
          gnd
    
    Low input: Q1 is off, Q2 is on (Out low).  When Vin rises above the upper
    threshold Q1 starts to conduct, its collector falls, Q2 turns off and Out
    jumps high.  The common emitter resistor makes the thresholds different when
    rising (UTP) and falling (LTP): the hysteresis.  The input is a 100 Hz sine,
    0 .. 5 V.

Code
----

.. literalinclude:: schmitt_bjt.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/schmitt_bjt_result.png
   :alt: Schmitt trigger with two BJT transistors (emitter coupled)
   :align: center

.. image:: /_static/examples/schmitt_bjt_transfer.png
   :alt: Schmitt trigger with two BJT transistors (emitter coupled)
   :align: center

