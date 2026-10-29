Charge and discharge of a capacitor (RC circuit)
================================================

Script: ``charge_discharge.py``

Description::

      In ──[ R1 ]── Out
      (V1)           │
                   [ C1 ]
                     │
                    gnd
    
    V1 is a trapezoidal pulse: while it is high the capacitor charges through R1,
    while it is low the capacitor discharges through R1 (time constant R*C = 1 ms).

Code
----

.. literalinclude:: charge_discharge.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/charge_discharge_result.png
   :alt: Charge and discharge of a capacitor (RC circuit)
   :align: center

