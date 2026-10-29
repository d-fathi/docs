UJT relaxation oscillator
=========================

Script: ``ujt_oscillator.py``

Description::

    R3 charges C1 from Vs until the emitter voltage reaches the peak voltage
    Vp ~ Eta VBB + Vd; the UJT then conducts, discharges C1 through the emitter
    and B1 until the valley voltage Vv, and switches off again.
      VC1 : sawtooth between Vv and Vp
      VB1 : positive pulse (the discharge current flows through R1)
      VB2 : negative pulse (the same current lowers the voltage on R2)
    Period:  T = R3 C1 ln[(Vs - Vv) / (Vs - Vp)]  (charging)  + the short discharge time
             (integrated from the static branch of the emitter characteristic)
    Vp and Vv are measured on the emitter characteristic Ve(Ie), traced here
    with a current source and a DC sweep.

Code
----

.. literalinclude:: ujt_oscillator.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/ujt_oscillator.png
   :alt: UJT relaxation oscillator
   :align: center

