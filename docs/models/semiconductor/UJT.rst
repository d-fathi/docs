Unijunction Transistor (UJT)
============================

.. code-block:: python

    from pyams.models import UJT

    X1 = UJT("e", "b1", "b2")
    X1.setParams("RBB=5000 Eta=0.6")

Terminals
---------

``UJT(e, b1, b2)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``RBB``
     - 5000
     - Ω
     - Inter-base resistance
   * - ``Eta``
     - 0.6
     - –
     - Intrinsic stand-off ratio
   * - ``Rsat``
     - 20
     - Ω
     - Lower bar resistance at high Ie
   * - ``Imod``
     - 0.00015
     - A
     - Conductivity-modulation current
   * - ``Is``
     - 1e-13
     - A
     - Emitter diode saturation current
   * - ``N``
     - 1
     - –
     - Emitter diode emission coefficient
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Cbar``
     - 2e-12
     - F
     - Bar capacitance (internal node to B1)

Description
-----------

The documentation of the class (``help(UJT)``)::

    Unijunction transistor: a silicon bar with two base contacts (B1, B2) and a
    p-n emitter junction on the bar (E).

                 B2 o----[ RB2 = (1-Eta) RBB ]----o A ----[ RB1 ]----o B1
                                                   |
                                                  >|  emitter diode
                                                   |
                                                   o E

    Between the bases the bar is a resistance RBB = RB1 + RB2 (inter-base
    resistance) and Eta = RB1 / RBB is the intrinsic stand-off ratio, so that
    with the emitter open the point A sits at  V(B1) + Eta (V(B2) - V(B1)).

    The emitter is a diode  Ie = Is (exp(Vea / N Vt) - 1)  into the point A.
    It conducts only when V(E) exceeds V(A) by about a diode drop, i.e. at the
    peak voltage  Vp ~ Eta (V(B2) - V(B1)) + Vd.  The holes it injects lower
    the resistance of the lower part of the bar (conductivity modulation),

        RB1 = Rsat + (Eta RBB - Rsat) / (1 + (Ie / Imod)^2),

    so after the peak the emitter voltage FALLS while the emitter current
    grows: the emitter characteristic Ve(Ie) has a negative-resistance region
    (peak point -> valley point), which makes the relaxation oscillator work.
    The resistance modulation is a smooth function of the emitter current, so
    no latch state is needed.

    Terminals: UJT(e, b1, b2).

    Parameters:
        RBB (ohm)   inter-base resistance with the emitter open (default 5 k)
        Eta         intrinsic stand-off ratio (default 0.6)
        Rsat (ohm)  lower bar resistance at high emitter current (default 20)
        Imod (A)    emitter current at which the modulation is halved
                    (default 0.15 mA, sets the valley point)
        Is (A), N, Vt (V)  emitter diode (1e-13 A, 1, 25 mV)
        Cbar (F)    small capacitance of the bar (internal node - B1, 2 pF): it
                    gives the internal node a time constant, which the solver
                    needs to follow the switching (like the pole of the OpAmp)

Used in the examples
--------------------

* :doc:`UJT relaxation oscillator </examples/ujt_oscillator>`

