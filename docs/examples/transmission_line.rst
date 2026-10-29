Transmission line: pulse, reflections and the load resistance
=============================================================

Script: ``transmission_line.py``

Description::

    A 3.3 V pulse (Rs = 20 Ohm) drives a 50 Ohm line with a delay of 1 ns.
    The load resistance RL is swept with sweep(): matched (50 Ohm, no echo),
    high (200 Ohm, positive reflection) and open (1 MOhm, full reflection).
    The reflection coefficient at the load is  G_L = (RL - Z0) / (RL + Z0)  and
    at the source  G_S = (Rs - Z0) / (Rs + Z0) = -0.43, so the echoes bounce
    between the two ends every 2 ns (Td = 1 ns each way).

Code
----

.. literalinclude:: transmission_line.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/transmission_line_result.png
   :alt: Transmission line: pulse, reflections and the load resistance
   :align: center

