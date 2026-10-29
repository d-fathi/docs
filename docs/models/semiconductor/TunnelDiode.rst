Tunnel Diode
============

.. code-block:: python

    from pyams.models import TunnelDiode

    X1 = TunnelDiode("p", "n")
    X1.setParams("Ip=0.005 Vp=0.1")

Terminals
---------

``TunnelDiode(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Ip``
     - 0.005
     - A
     - Peak current
   * - ``Vp``
     - 0.1
     - V
     - Peak voltage
   * - ``Ix``
     - 0.0001
     - A
     - Excess current scale
   * - ``Vx``
     - 0.35
     - V
     - Excess current voltage offset
   * - ``Kex``
     - 15
     - 1/V
     - Excess current exponent
   * - ``Is``
     - 1e-12
     - A
     - Thermal saturation current
   * - ``N``
     - 1
     - –
     - Emission coefficient
   * - ``Vt``
     - 0.025
     - V
     - Thermal voltage
   * - ``Cj``
     - 1e-11
     - F
     - Junction capacitance

Description
-----------

The documentation of the class (``help(TunnelDiode)``)::

    Tunnel (Esaki) diode: a heavily doped p-n junction whose I(V) curve has a
    negative-resistance region between the peak (Vp, Ip) and the valley.

        I(V) = Itunnel + Iexcess + Ithermal + Cj dV/dt

        Itunnel  = Ip (V / Vp) exp(1 - V / Vp)             peak exactly at (Vp, Ip)
        Iexcess  = Ix (exp(Kex (V - Vx)) - exp(-Kex Vx))   trap-assisted tunnelling,
                                                           it makes the valley
        Ithermal = Is (exp(V / N Vt) - 1)                  ordinary diode injection

    The current is a single-valued function of the voltage, so the diode can be
    swept with a voltage source (it is an "N-type" negative resistance: stable
    when driven by a voltage source, unstable with a high-impedance parallel
    inductor-capacitor circuit -> oscillator).

    Terminals: TunnelDiode(p, n)   (anode, cathode).

    Parameters:
        Ip (A), Vp (V)    peak current and peak voltage    (5 mA, 0.1 V)
        Ix (A), Vx (V)    excess current scale and offset  (0.1 mA, 0.35 V)
        Kex (1/V)         excess current exponent          (15)
        Is (A), N, Vt     thermal diode                    (1e-12 A, 1, 25 mV)
        Cj (F)            junction capacitance             (10 pF)

Used in the examples
--------------------

* :doc:`Tunnel diode oscillator </examples/tunnel_diode_oscillator>`

