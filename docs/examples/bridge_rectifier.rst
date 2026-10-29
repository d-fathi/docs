Full-wave bridge rectifier fed by a transformer
===============================================

Script: ``bridge_rectifier.py``

Description::

                     T1 (2:1 step-down)                D1        Out
      V1 ──[Rp]── P1 ═╗╔═ A ────────┬───────┬───────►|────────┬────────┐
      50 Hz           ║║            │       └───────►|─┐ D2    │        │
      20 V peak       ║║            D3                 │       C1      R1
                   gnd═╝╚═ B ─┐     ▼                  │      (filter) (load)
                              └─────D4──────────────────┘       │        │
                                     └────────── gnd ───────────┴────────┘
    
    Bridge: D1 A→Out, D2 B→Out, D3 gnd→A, D4 gnd→B.  On each half-cycle two
    diodes conduct, so the load sees |V(A) - V(B)| minus two diode drops, and
    C1 smooths it (ripple ≈ I/(2*f*C)).
    The transformer has L1 = 100 mH, L2 = 25 mH, M = 49.5 mH (k = 0.99), so the
    turns ratio is sqrt(25/100) = 1/2 and the secondary peak is about 10 V.

Code
----

.. literalinclude:: bridge_rectifier.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/bridge_rectifier_result.png
   :alt: Full-wave bridge rectifier fed by a transformer
   :align: center

