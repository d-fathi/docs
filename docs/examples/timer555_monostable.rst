555 timer, monostable (one-shot)
================================

Script: ``timer555_monostable.py``

Description::

    TRIG is held at Vcc; a negative pulse below Vcc/3 sets the flip-flop: the output
    goes high, the discharge transistor opens and C charges from 0 through R towards
    Vcc.  When V(C) reaches 2Vcc/3 the flip-flop is reset: output low, C discharged.
          T = R C ln 3 = 1.0986 R C
    The trigger pulse must end before T (here it is 0.1 ms wide, T ~ 1.1 ms).

Code
----

.. literalinclude:: timer555_monostable.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/timer555_monostable.png
   :alt: 555 timer, monostable (one-shot)
   :align: center

