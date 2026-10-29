Diac relaxation oscillator
==========================

Script: ``diac_relaxation.py``

Description::

      V1 (60 V) ──[ R1 100k ]──┬───────┬─── Out1
                               │       │
                             [ C1 ]  [ X1 diac ]
                             22 nF    │
                               │      ├─── Out2
                              gnd   [ R2 10 Ω ]
                                      │
                                     gnd
    
    C1 charges through R1 towards 60 V.  When Out1 reaches the breakover voltage
    of the diac (36 V) the diac switches on and C1 discharges through it and R2
    (a short current pulse, seen across R2 as Out2) until the current falls below
    the holding current and the diac turns off again (Out1 ≈ 16 V).  Then C1
    charges again:
    
        first peak : t = R1·C1·ln(60 / (60 - 36))        ≈ 2.0 ms
        period     : T = R1·C1·ln((60 - 16) / (60 - 36)) ≈ 1.33 ms (a bit more
                     because of the diac leakage current)

Code
----

.. literalinclude:: diac_relaxation.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/diac_relaxation_result.png
   :alt: Diac relaxation oscillator
   :align: center

