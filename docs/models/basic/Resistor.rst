Resistor
========

.. code-block:: python

    from pyams.models import Resistor

    X1 = Resistor("p", "n")
    X1.setParams("R=1000")

Terminals
---------

``Resistor(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``R``
     - 1000
     - Ω
     - Resistance

Description
-----------

The documentation of the class (``help(Resistor)``)::

    This class implements a Resistor model.

    A resistor limits current flow according to Ohm's Law, which states that
    the current through a resistor is proportional to the voltage across it
    and inversely proportional to its resistance.

    Attributes:
        V (signal): Input voltage signal across the resistor, defined between nodes (p, n).
        I (signal): Output current signal through the resistor, defined between nodes (p, n).
        R (param): Resistance value in Ohms (Ω), default is 1000 Ω.

    Methods:
        analog(): Defines the resistor behavior using Ohm's Law:
                  I = V / R

Used in the examples
--------------------

* :doc:`Voltage divider with a constant voltage source </examples/voltage_divider>`
* :doc:`Half wave rectification circuit </examples/half_wave_rectifier>`
* :doc:`Full-wave bridge rectifier fed by a transformer </examples/bridge_rectifier>`
* :doc:`Zener diode: I(V) characteristic and shunt regulator </examples/zener_regulator>`
* :doc:`Charge and discharge of a capacitor (RC circuit) </examples/charge_discharge>`
* :doc:`Series RLC circuit (inductor example) </examples/rlc>`
* :doc:`RC low-pass: how to use analysis(mode="ac") </examples/rc_ac_simple>`
* :doc:`AC analysis (small-signal frequency response) </examples/ac_analysis>`
* :doc:`Elliptic (Cauer) RLC low-pass filter </examples/elliptic_filter>`
* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`
* :doc:`Current sources: DCCurrent, SinCurrent, TrapezoidCurrent </examples/current_sources>`
* :doc:`Exponential sources (SPICE EXP): ExpVoltage drives an RC filter, ExpCurrent charges a capacitor </examples/exp_sources>`
* :doc:`PWL sources: arbitrary waveform from (time, value) points </examples/pwl_sources>`
* :doc:`idt() example: an inductor written with the integral </examples/idt_example>`
* :doc:`Transmission line: pulse, reflections and the load resistance </examples/transmission_line>`
* :doc:`JFET common-source amplifier (self bias) </examples/jfet_amplifier>`
* :doc:`MOSFET4: 4-terminal MOSFET, body effect </examples/mosfet4_examples>`
* :doc:`Thyristor characteristics I(V) </examples/thyristor_iv>`
* :doc:`Thyristor I(V) with several gate currents (IG0 ... IG3) </examples/thyristor_iv_family>`
* :doc:`Thyristor I(V) characteristic in the textbook form </examples/thyristor_iv_textbook>`
* :doc:`Thyristor phase control (half-wave, resistive load) </examples/thyristor_phase_control>`
* :doc:`Thyristor lamp dimmer (half-wave phase control, three angles) </examples/thyristor_lamp_dimmer>`
* :doc:`IGBT chopper (low-side switch, inductive load, freewheel diode) </examples/igbt_chopper>`
* :doc:`Diac relaxation oscillator </examples/diac_relaxation>`
* :doc:`UJT relaxation oscillator </examples/ujt_oscillator>`
* :doc:`Tunnel diode oscillator </examples/tunnel_diode_oscillator>`
* :doc:`Astable multivibrator (two NPN BJT transistors) </examples/astable>`
* :doc:`BJT astable multivibrator (classic two-transistor circuit) </examples/bjt_astable>`
* :doc:`Schmitt trigger with two BJT transistors (emitter coupled) </examples/schmitt_bjt>`
* :doc:`Schmitt trigger with an op-amp (inverting) </examples/schmitt_opamp>`
* :doc:`Op-amp astable multivibrator (relaxation oscillator) </examples/opamp_multivibrator>`
* :doc:`Comparator: hysteresis loop and RC relaxation oscillator </examples/comparator_demo>`
* :doc:`555 timer, astable multivibrator </examples/timer555_astable>`
* :doc:`555 timer, monostable (one-shot) </examples/timer555_monostable>`
* :doc:`Ring oscillator (3 CMOS inverters with RC delay) </examples/ring_oscillator>`
* :doc:`Chua's circuit with op-amps (double-scroll chaotic oscillator) </examples/chua_opamp>`

