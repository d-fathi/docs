Chua's circuit with op-amps (double-scroll chaotic oscillator)
==============================================================

Script: ``chua_opamp.py``

Description::

               R           V2
      V1 ──[ R ]────────────┬──────┐
       │                    │      │
     [C1]  [ Chua diode ]  [C2]   [L]
       │         │          │      │
      gnd       gnd        gnd   [R0]  (inductor series resistance)
                                   │
                                  gnd
    
      C1 dV1/dt = (V2 - V1)/R - f(V1)
      C2 dV2/dt = (V1 - V2)/R + iL
      L  diL/dt = -V2 - R0·iL
    
    The Chua diode f(V) is a nonlinear resistor built from two op-amps.  Each
    op-amp is a non-inverting amplifier (gain K = 1 + Rf/Rg) whose (+) input is the
    diode node V1, and a resistor Rn joins V1 to the op-amp output:
    
        inside the linear range    i = (V1 - K·V1)/Rn = -(K-1)/Rn · V1   (negative R)
        when the output saturates  i = (V1 ∓ Vsat)/Rn                    (positive R)
    
    OA1 (K = 9)  saturates first, at |V1| = Vsat/9 = 1 V.
    OA2 (K = 2)  saturates later,  at |V1| = Vsat/2 = 4.5 V.  This gives the three
    slopes of Chua's diode:
        |V1| < 1 V      : Ga = -0.762 mS
        1 V < |V1| < 4.5 V : Gb = -0.416 mS
        |V1| > 4.5 V    : Gc = +0.486 mS   (confines the orbit)
    
    The circuit is chaotic around R = 1.7 kΩ (try 1.6 kΩ ... 2 kΩ: it moves from
    a limit cycle through period doubling to chaos and the double scroll).  The
    oscillation is started by the 1 mV input offset of the op-amps (the origin is an
    unstable equilibrium); uic=True starts the circuit with all capacitors empty.

Code
----

.. literalinclude:: chua_opamp.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/chua_result.png
   :alt: Chua's circuit with op-amps (double-scroll chaotic oscillator)
   :align: center

.. image:: /_static/examples/chua_double_scroll.png
   :alt: Chua's circuit with op-amps (double-scroll chaotic oscillator)
   :align: center

