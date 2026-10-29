Thyristor I(V) with several gate currents (IG0 ... IG3)
=======================================================

Script: ``thyristor_iv_family.py``

Description::

    The textbook characteristic of an SCR with a family of gate currents:
      forward blocking (blocage direct), reverse blocking (blocage inverse),
      reverse breakdown (claquage inverse), the breakover voltage VBo that falls
      as the gate current grows IG0 < IG1 < IG2 < IG3, the threshold voltage VT,
      the holding current IH and the latching current IL of the ON state (passant).
    
    Every solid branch is a DC sweep of a source with a series resistor; the
    gate current comes from a DCCurrent source and is changed with sweep().
    The negative-resistance part between breakover and the ON state cannot be
    measured by a voltage sweep (the latch jumps over it): it is drawn as a
    smooth dashed curve between the two measured ends.  The currents are
    exaggerated (Roff = 2 kOhm) and the axes compressed (linear near the
    origin, logarithmic farther away), as in a textbook drawing.

Code
----

.. literalinclude:: thyristor_iv_family.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/thyristor_iv_family.png
   :alt: Thyristor I(V) with several gate currents (IG0 ... IG3)
   :align: center

