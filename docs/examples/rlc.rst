Series RLC circuit (inductor example)
=====================================

Script: ``rlc.py``

Description::

      In ──[ R1 ]──( L1 )── Out
      (V1)                   │
                           [ C1 ]
                             │
                            gnd
    
    A 5 V pulse drives a series R-L-C circuit.  R = 50 ohm is below the critical
    value 2*sqrt(L/C) = 200 ohm, so the capacitor voltage overshoots and rings at
    about f0 = 1/(2*pi*sqrt(L*C)) = 1.59 kHz, decaying with tau = 2L/R = 0.4 ms.
    The first peak reaches 5 V * (1 + exp(-pi*alpha/wd)) = 7.22 V (simulation: 7.23 V).

Code
----

.. literalinclude:: rlc.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/rlc_result.png
   :alt: Series RLC circuit (inductor example)
   :align: center

