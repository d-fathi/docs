Ring oscillator (3 CMOS inverters with RC delay)
================================================

Script: ``ring_oscillator.py``

Description::

             ┌───────────────────────────────────────────────────────────┐
             │      INV1            R1        INV2            R2     INV3│ R3
             └─ g1 ─►o──── o1 ──[R1]── g2 ─►o──── o2 ──[R2]── g3 ─►o─ o3 ─[R3]─┐
                │                     │                    │                   │
               C1                    C2                   C3                   │
                │                     │                    │                   │
               gnd                   gnd                  gnd      (back to g1)┘
    
    Each inverter is a CMOS pair: a P-channel MOSFET from Vdd to the output and an
    N-channel MOSFET from the output to ground, gates tied together.  The output
    of an inverter reaches the next gate through a resistor R, and the capacitor
    C at that gate sets the delay of the stage (the RC network of each stage).
    An odd number of inverting stages has no stable state, so the loop oscillates:
    
        one half period = the signal travels once round the ring
        f ≈ 1 / (2 · N · td),   td ≈ the delay of one stage  (≈ 0.7 · R · C)
    
    The three capacitors differ by 2 % (like real components); a perfectly
    symmetric ring would stay at its unstable balance point, and the supply
    switch-on (uic=True: all nodes start at 0 V) would move the three nodes
    together.

Code
----

.. literalinclude:: ring_oscillator.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/ring_oscillator_result.png
   :alt: Ring oscillator (3 CMOS inverters with RC delay)
   :align: center

