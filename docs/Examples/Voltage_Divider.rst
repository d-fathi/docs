Voltage divider with a constant voltage source
==============================================

Script: ``voltage_divider.py``

Description::

      In ──[ R1 ]── Out ──[ R2 ]── gnd
      (V1)
    
    V1 is a 12 V DC source.  With R1 = 2 kΩ and R2 = 1 kΩ the output is
    Out = 12 * R2 / (R1 + R2) = 4 V.

Code
----

.. literalinclude:: voltage_divider.py
   :language: python
   :linenos:

Result
------

A DC operating point has no curve to plot; the script prints the node voltages::

    V(In)  = 12.0000 V
    V(Out) = 4.0000 V   (expected 4 V)

