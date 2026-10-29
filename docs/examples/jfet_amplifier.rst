JFET common-source amplifier (self bias)
========================================

Script: ``jfet_amplifier.py``

Description::

                            Vdd (12 V)
                             │
                           [ RD 4.7k ]
                             │
               Cin           ├──── Cout ──── Out
      Vin ──────||───── G ──┤D
      (1 kHz)    1uF     │   J1  (N-channel)
                       [RG]   S
                       1M │   │
                         gnd  ├── [ RS 1k ] ── gnd
                              │
                             [ CS 100uF ]  (bypass)
                              │
                             gnd
    
    The gate draws no current, so RG holds it at 0 V and the drain current Id
    makes the source rise by Id·RS: the gate-source voltage is negative
    (Vgs = -Id·RS), the bias a JFET needs, with a single supply (self bias).
    
    With Beta = 0.5 mA/V², Vto = -2 V:   Id = Beta (Vgs - Vto)²   and   Vgs = -Id RS
        (with Lambda = 0.01:  Id = 0.789 mA, Vgs = -0.789 V, VD = 12 - Id RD = 8.29 V)
    Small-signal gain (CS short-circuits RS at 1 kHz):  Av = -gm (RD || RL || ro),
        gm = 2 Beta (Vgs - Vto)(1 + Lambda Vds) = 1.30 mS  ->  Av ≈ -5.7 (inverting).

Code
----

.. literalinclude:: jfet_amplifier.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/jfet_amplifier_result.png
   :alt: JFET common-source amplifier (self bias)
   :align: center

