MOSFET (4 terminals)
====================

.. code-block:: python

    from pyams.models import MOSFET4

    X1 = MOSFET4("d", "g", "s", "b")
    X1.setParams("Kp=0.0001 W=1e-05")

Terminals
---------

``MOSFET4(d, g, s, b)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Kp``
     - 0.0001
     - A/V²
     - Transconductance parameter
   * - ``W``
     - 1e-05
     - m
     - Channel width
   * - ``L``
     - 1e-06
     - m
     - Channel length
   * - ``Vth0``
     - 1
     - V
     - Zero-bias threshold voltage (magnitude)
   * - ``Lambda``
     - 0.02
     - 1/V
     - Channel-length modulation
   * - ``Gamma``
     - 0.5
     - √V
     - Body-effect coefficient
   * - ``Phi``
     - 0.7
     - V
     - Surface potential
   * - ``Type``
     - 1
     - –
     - Polarity: 1 = N-channel, -1 = P-channel
   * - ``Is``
     - 1e-14
     - A
     - Bulk junction saturation current
   * - ``N``
     - 1
     - –
     - Bulk junction emission coefficient
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Cgs``
     - 2e-14
     - F
     - Gate-source capacitance
   * - ``Cgd``
     - 2e-14
     - F
     - Gate-drain capacitance
   * - ``Cgb``
     - 1e-14
     - F
     - Gate-bulk capacitance
   * - ``Cbs``
     - 1e-14
     - F
     - Bulk-source junction capacitance
   * - ``Cbd``
     - 1e-14
     - F
     - Bulk-drain junction capacitance

Description
-----------

The documentation of the class (``help(MOSFET4)``)::

    Four-terminal MOSFET (drain, gate, source, bulk): the level-1 square-law
    model of MOSFET with the *body effect* and the bulk junctions.

    Terminals are given in the order (d, g, s, b).

    For an N-channel device (Type = 1), with vgs = V(g,s), vds = V(d,s),
    vbs = V(b,s), beta = Kp W / L:

        Vth = Vth0 + Gamma ( sqrt(Phi - vbs) - sqrt(Phi) )        (body effect)
        vov = vgs - Vth

        vov <= 0                 cut-off       Id = 0
        0 < vds < vov            triode        Id = beta (vov vds - vds^2/2) (1 + Lambda vds)
        vds >= vov > 0           saturation    Id = beta/2 vov^2 (1 + Lambda vds)

    A source that is more positive than the bulk (vbs < 0, "reverse body
    bias") raises the threshold: this is why an N-channel pass transistor
    cannot pass a full high level, and why stacked transistors (NAND, source
    followers) are slower than the 3-terminal model predicts.

    The device is symmetric: if vds < 0 the drain and source change roles and
    the body effect is taken against the new source (vbd).  A P-channel device
    (Type = -1) uses the same equations with all voltages and currents
    sign-reversed, Vth0 being the (positive) magnitude of its threshold.

    Bulk junctions (diodes bulk-source and bulk-drain, forward when the bulk is
    more positive than the channel end for an N device)

        Ibs = Is (exp(vbs / (N Vt)) - 1)        Ibd = Is (exp(vbd / (N Vt)) - 1)

    and constant capacitances Cgs, Cgd, Cgb (gate) and Cbs, Cbd (junctions).

    Attributes:
        Vgs, Vds, Vgd, Vbs, Vbd, Vgb (signal): input voltages.
        Id (signal): output drain-source channel current.
        Ibs, Ibd, Igs, Igd, Igb (signal): junction and capacitor currents.
        Kp (A/V^2, 100 uA/V^2), W, L (10 um, 1 um), Vth0 (1 V), Lambda (0.02 1/V),
        Gamma (body-effect coefficient, 0.5 sqrt(V)), Phi (surface potential, 0.7 V),
        Type (1 N-channel, -1 P-channel), Is (1e-14 A), N (1), Vt (25 mV),
        Cgs, Cgd (20 fF), Cgb (10 fF), Cbs, Cbd (10 fF).

    With Gamma = 0 and the bulk tied to the source the model reduces to MOSFET
    (apart from the junction diodes and the extra capacitances).

Used in the examples
--------------------

* :doc:`MOSFET4: 4-terminal MOSFET, body effect </examples/mosfet4_examples>`

