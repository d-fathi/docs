Astable multivibrator (two NPN BJT transistors)
===============================================

Script: ``astable.py``

Description::

                       Vcc
         ┌───────┬───────┼───────┬───────┐
        Rc1     Rb1     Rb2     Rc2      │
         │       │       │       │       │
         ├──C1───┼───────┤       │       │    C1 : Out1 → B2
         │       │       └───C2──┤       │    C2 : Out2 → B1
       Out1     B1       B2    Out2
         │  Q1 ──┘       └── Q2  │
         └── c ─ e ─ gnd ─ e ─ c ┘
    
    Each transistor is switched on in turn; the base resistors recharge the
    coupling capacitors and set the period  T ≈ ln2 · (Rb1·C2 + Rb2·C1)
    (≈ 0.65 ms by this rule of thumb; the full model gives 0.678 ms because it
    includes Vbe and the saturation voltage).  The supply ramps up like a real
    power switch-on, and Rc2 is a little larger than Rc1 (component tolerance):
    a perfectly symmetric circuit stays at its unstable balance point and never
    starts (a real one is started by noise).
    
    The BJT model includes its junction capacitances (Cje, Cjc).  Without them a
    regenerative circuit like this one has no capacitance on some nodes and the
    equations jump when a transistor switches, so the solver cannot follow it.
    
    Time step: the edges of this circuit take nanoseconds while the base
    capacitors recharge over hundreds of microseconds, so a fixed step is either
    slow or wrong (step=1e-7 takes about 10 s; step=1e-6 is fast but the circuit
    starts about 0.1 ms late).  adaptive=True lets the solver choose its own step
    (tiny at the edges, tens of microseconds in between) and order=2 selects a
    second-order method; `step` is then only the spacing of the output points.
    The result agrees with a reference ODE solution to 0.07 us on every edge and
    0.001 % on the period, in about 1.5 s.

Code
----

.. literalinclude:: astable.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/astable_result.png
   :alt: Astable multivibrator (two NPN BJT transistors)
   :align: center

