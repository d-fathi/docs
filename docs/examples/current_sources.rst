Current sources: DCCurrent, SinCurrent, TrapezoidCurrent
========================================================

Script: ``current_sources.py``

Description::

    Each source feeds a parallel R || C (R = 1 kOhm, C = 1 uF, tau = 1 ms).
    A positive current flows through the source from p ("0") to n, so it is
    pushed into the RC node:   C dv/dt + v/R = i(t).
      DC        : v = Idc R (1 - exp(-t/tau))
      Sine      : low-pass filter of the current, |Z| = R / sqrt(1 + (w tau)^2)
      Trapezoid : the voltage follows the integral of the current pulse.

Code
----

.. literalinclude:: current_sources.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/current_sources_result.png
   :alt: Current sources: DCCurrent, SinCurrent, TrapezoidCurrent
   :align: center

