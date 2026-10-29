Capacitor
=========

.. code-block:: python

    from pyams.models import Capacitor

    X1 = Capacitor("p", "n")
    X1.setParams("C=1e-06")

Terminals
---------

``Capacitor(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``C``
     - 1e-06
     - F
     - Capacitor value

Description
-----------

The documentation of the class (``help(Capacitor)``)::

    This class implements a Capacitor model.

    A capacitor stores electrical energy in an electric field and its current
    is proportional to the rate of change of voltage across it.

    Attributes:
        V (signal): Input voltage signal across the capacitor, defined between nodes (p, n).
        I (signal): Output current signal through the capacitor, defined between nodes (p, n).
        C (param): Capacitance value in Farads (F), default is 1.0e-6 F.

    Methods:
        analog(): Defines the capacitor behavior using the equation:
                  I = C * dV/dt

Used in the examples
--------------------

* :doc:`Full-wave bridge rectifier fed by a transformer </examples/bridge_rectifier>`
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
* :doc:`JFET common-source amplifier (self bias) </examples/jfet_amplifier>`
* :doc:`MOSFET4: 4-terminal MOSFET, body effect </examples/mosfet4_examples>`
* :doc:`Diac relaxation oscillator </examples/diac_relaxation>`
* :doc:`UJT relaxation oscillator </examples/ujt_oscillator>`
* :doc:`Tunnel diode oscillator </examples/tunnel_diode_oscillator>`
* :doc:`Astable multivibrator (two NPN BJT transistors) </examples/astable>`
* :doc:`BJT astable multivibrator (classic two-transistor circuit) </examples/bjt_astable>`
* :doc:`Op-amp astable multivibrator (relaxation oscillator) </examples/opamp_multivibrator>`
* :doc:`Comparator: hysteresis loop and RC relaxation oscillator </examples/comparator_demo>`
* :doc:`555 timer, astable multivibrator </examples/timer555_astable>`
* :doc:`555 timer, monostable (one-shot) </examples/timer555_monostable>`
* :doc:`Ring oscillator (3 CMOS inverters with RC delay) </examples/ring_oscillator>`
* :doc:`Chua's circuit with op-amps (double-scroll chaotic oscillator) </examples/chua_opamp>`

