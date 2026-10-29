Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS
======================================================

Script: ``dependent_sources.py``

Description::

      VCVS(p, n, cp, cn)  v(p,n) = Gain * v(cp,cn)        (SPICE E)
      VCCS(p, n, cp, cn)  i(p->n) = Gm   * v(cp,cn)       (SPICE G)
      CCVS(p, n, cp, cn)  v(p,n) = Rm    * i(cp->cn)      (SPICE H)
      CCCS(p, n, cp, cn)  i(p->n) = Gain * i(cp->cn)      (SPICE F)
    For the current-controlled sources (cp, cn) is a built-in 0 V ammeter: put it
    IN SERIES with the branch that carries the controlling current.
    
    Five checks, each against a formula:
      1. VCVS as an op-amp with finite gain (non-inverting amplifier)
      2. VCCS gyrator: a capacitor looks like an inductor  L = C / gm^2
      3. CCCS + VCVS: ideal transformer (voltage ratio n, current ratio 1/n)
      4. CCVS: transimpedance amplifier  Vout = Rm * Iin  (zero input resistance)
      5. hybrid-pi small-signal amplifier: VCCS (gm vpi) and CCCS (beta ib) are the same

Code
----

.. literalinclude:: dependent_sources.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/dependent_sources.png
   :alt: Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS
   :align: center

