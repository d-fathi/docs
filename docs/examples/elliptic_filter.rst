Elliptic (Cauer) RLC low-pass filter
====================================

Script: ``elliptic_filter.py``

Description::

    Passive doubly-terminated LC ladder with an elliptic (Cauer) response:
    equal ripple in the passband AND in the stopband, and transmission zeros
    (infinite attenuation) at finite frequencies, made by parallel L-C branches
    in the series arms.
    
      Vin -- Rs --+-----[L2 || C2]-----+-----[L4 || C4]-----+---- Vout
                  |                    |                    |
                 C1                   C3                   C5      RL
                  |                    |                    |
                 gnd                  gnd                  gnd
    
    Design (done here, from scratch, with no filter-design tables):
      1. scipy gives the prototype |H(jw)|^2 = 1 / (1 + eps^2 R_n^2(w)).
      2. With lossless ladder and Rs = RL:  rho(s) rho(-s) = 1 - H(s) H(-s).
         The reflection zeros are on the jw axis (the ripple minima); the
         polynomial N(s) of rho = N/A is built from them.
      3. Zin(s) = (A + N) / (A - N) (the sign that makes every element positive),
         then a continued-fraction (Cauer) expansion removes, in turn, a shunt C
         such that the rest has a pole at a transmission zero, and that pole as a
         parallel L-C branch.
    The circuit is then simulated with the AC analysis and compared with scipy's
    response; a transient run with a sine checks one passband and one stopband
    point.

Code
----

.. literalinclude:: elliptic_filter.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/elliptic_filter.png
   :alt: Elliptic (Cauer) RLC low-pass filter
   :align: center

