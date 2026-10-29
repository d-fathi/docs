Schmitt trigger with an op-amp (inverting)
==========================================

Script: ``schmitt_opamp.py``

Description::

      Vin ── In ──(-)\
                       >────┬──── Out        R1 = 30 kΩ, R2 = 10 kΩ
               ┌────(+)/     │                β = R2/(R1+R2) = 0.25
               P            [R1]
               ├────────────┘
             [R2]
               │
              gnd
    
    Positive feedback through R1/R2 gives the (+) input the voltage β·Out.  Out is
    at +Vsat or -Vsat, so the switching thresholds are
    
        UTP = +β·Vsat   (input rising: Out falls)   ≈ +3 V
        LTP = -β·Vsat   (input falling: Out rises)  ≈ -3 V
    
    and the circuit is inverting: a high input gives a low output.

Code
----

.. literalinclude:: schmitt_opamp.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/schmitt_opamp_result.png
   :alt: Schmitt trigger with an op-amp (inverting)
   :align: center

.. image:: /_static/examples/schmitt_opamp_transfer.png
   :alt: Schmitt trigger with an op-amp (inverting)
   :align: center

