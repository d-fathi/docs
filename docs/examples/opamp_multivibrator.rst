Op-amp astable multivibrator (relaxation oscillator)
====================================================

Script: ``opamp_multivibrator.py``

Description::

             ┌────────[ R ]────────┐
             │                     │
             N ──(-)\              │
             │       >──────┬──────┴── Out        R1 = 35 kΩ, R2 = 30 kΩ
           [ C ]  ┌─(+)/    │                    β = R2/(R1+R2) = 0.462
             │    P       [ R1 ]
            gnd   ├────────┘
                  │
                [ R2 ]
                  │
                 gnd
    
    The output saturates at +Vcc or -Vcc.  The divider R1/R2 feeds back a fraction
    β of the output to the (+) input, which sets the switching thresholds
    ±β·Vsat, and R charges / discharges C towards the output.  Each time the
    capacitor voltage crosses a threshold the output flips, so
    
        T = 2·R·C·ln((1 + β) / (1 - β))      (= 2RC for β = 0.462, since ln(e) = 1)
        f = 1 / T = 1 kHz  for R = 50 kΩ, C = 0.01 µF
    
    The 1 mV input offset of the op-amp starts the oscillation (an ideal
    symmetric circuit stays at its unstable balance point at 0 V).

Code
----

.. literalinclude:: opamp_multivibrator.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/opamp_multivibrator_result.png
   :alt: Op-amp astable multivibrator (relaxation oscillator)
   :align: center

