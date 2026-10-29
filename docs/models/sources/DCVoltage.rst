DC Voltage
==========

.. code-block:: python

    from pyams.models import DCVoltage

    X1 = DCVoltage("p", "n")
    X1.setParams("Vdc=5")

Terminals
---------

``DCVoltage(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Vdc``
     - 5
     - V
     - Constant voltage value

Description
-----------

The documentation of the class (``help(DCVoltage)``)::

    This class models a constant (DC) voltage source.

    The voltage is  V = Vdc  at all times, so it is also the supply of
    circuits that need a fixed rail (a battery, Vcc, a bias voltage).

    Attributes:
        V (signal): Output voltage between nodes (p, n); p is the + terminal.
        Vdc (param): Voltage value in Volts (V), default is 5.0 V.

    Methods:
        analog(): Implements the equation V = Vdc.

Used in the examples
--------------------

* :doc:`Voltage divider with a constant voltage source </examples/voltage_divider>`
* :doc:`Zener diode: I(V) characteristic and shunt regulator </examples/zener_regulator>`
* :doc:`AC analysis (small-signal frequency response) </examples/ac_analysis>`
* :doc:`Conductor: resistance from geometry, temperature and self-heating </examples/conductor_examples>`
* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`
* :doc:`JFET output characteristics (Id versus Vds for several Vgs) </examples/jfet_curves>`
* :doc:`JFET common-source amplifier (self bias) </examples/jfet_amplifier>`
* :doc:`MOSFET4: 4-terminal MOSFET, body effect </examples/mosfet4_examples>`
* :doc:`Thyristor characteristics I(V) </examples/thyristor_iv>`
* :doc:`Thyristor I(V) with several gate currents (IG0 ... IG3) </examples/thyristor_iv_family>`
* :doc:`Thyristor I(V) characteristic in the textbook form </examples/thyristor_iv_textbook>`
* :doc:`IGBT chopper (low-side switch, inductive load, freewheel diode) </examples/igbt_chopper>`
* :doc:`Diac relaxation oscillator </examples/diac_relaxation>`
* :doc:`UJT relaxation oscillator </examples/ujt_oscillator>`
* :doc:`Tunnel diode oscillator </examples/tunnel_diode_oscillator>`
* :doc:`BJT astable multivibrator (classic two-transistor circuit) </examples/bjt_astable>`
* :doc:`Schmitt trigger with two BJT transistors (emitter coupled) </examples/schmitt_bjt>`
* :doc:`Comparator: hysteresis loop and RC relaxation oscillator </examples/comparator_demo>`
* :doc:`555 timer, astable multivibrator </examples/timer555_astable>`
* :doc:`555 timer, monostable (one-shot) </examples/timer555_monostable>`
* :doc:`Ring oscillator (3 CMOS inverters with RC delay) </examples/ring_oscillator>`

