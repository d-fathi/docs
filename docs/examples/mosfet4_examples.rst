MOSFET4: 4-terminal MOSFET, body effect
=======================================

Script: ``mosfet4_examples.py``

Description::

    MOSFET4(d, g, s, b): level-1 MOSFET with the body effect
          Vth = Vth0 + Gamma (sqrt(Phi - vbs) - sqrt(Phi))
    and the two bulk-junction diodes.  Checks:
      1. drain current against an independent numpy implementation (N and P,
         random bias points, triode / saturation / reverse operation, body bias)
      2. threshold voltage measured from sqrt(Id) against Vsb  (body effect)
      3. output and transfer curves (family in Vsb)
      4. CMOS inverter: transfer curve and switching threshold Vm, with the bulks
         on the rails
      5. N-channel pass transistor: the high level is Vg - Vth(Vsb), not Vg - Vth0

Code
----

.. literalinclude:: mosfet4_examples.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/mosfet4_examples.png
   :alt: MOSFET4: 4-terminal MOSFET, body effect
   :align: center

