555 timer, astable multivibrator
================================

Script: ``timer555_astable.py``

Description::

    C charges from Vcc/3 to 2Vcc/3 through R1 + R2 (output high) and discharges
    through R2 into the discharge pin (output low).  THRES and TRIG are tied.
      t_high = (R1 + R2) C ln 2        t_low = R2 C ln 2        f = 1.44 / ((R1 + 2 R2) C)
    Reference below includes the real discharge transistor (Rdis in parallel with R1).

Code
----

.. literalinclude:: timer555_astable.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/timer555_astable.png
   :alt: 555 timer, astable multivibrator
   :align: center

