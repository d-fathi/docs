Tunnel diode oscillator
=======================

Script: ``tunnel_diode_oscillator.py``

Description::

    The tunnel diode is biased in the middle of its negative-resistance region
    through Rl and L; C is in parallel with the diode.  The negative conductance
    -g cancels the losses of the tank (Rl): oscillation starts when
          |g| > Rl C / L
    and grows until the nonlinearity of I(V) limits the amplitude.
    Frequency ~ 1 / (2 pi sqrt(L (C + Cj))).
    Check: the same circuit integrated with scipy (solve_ivp) from I(V) written
    independently, and the frequency from the FFT.

Code
----

.. literalinclude:: tunnel_diode_oscillator.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/tunnel_diode_oscillator.png
   :alt: Tunnel diode oscillator
   :align: center

