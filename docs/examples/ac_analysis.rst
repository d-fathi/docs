AC analysis (small-signal frequency response)
=============================================

Script: ``ac_analysis.py``

Description::

    analysis(mode="ac", start=f1, stop=f2, step=points_per_decade) solves the DC
    operating point, linearises the circuit around it and solves the complex
    system at every frequency.  The ACVoltage source (Vac = 1 V) gives the phasor
    of each output directly as the transfer function.
      1. series RLC band-pass, family in R with sweep()      (analytic reference)
      2. common-emitter BJT amplifier: bias point -> gm, midband gain and corner
         frequencies, checked against hybrid-pi formulas and against a transient
         run with a small sine (the full non-linear model)
      3. op-amp inverting amplifier with a single-pole open loop (gain-bandwidth)

Code
----

.. literalinclude:: ac_analysis.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/ac_analysis.png
   :alt: AC analysis (small-signal frequency response)
   :align: center

.. image:: /_static/examples/ac_rlc.png
   :alt: AC analysis (small-signal frequency response)
   :align: center

