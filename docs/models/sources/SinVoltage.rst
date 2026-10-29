Sinusoidal Voltage
==================

.. code-block:: python

    from pyams.models import SinVoltage

    X1 = SinVoltage("p", "n")
    X1.setParams("Fr=100 Va=10")

Terminals
---------

``SinVoltage(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Fr``
     - 100
     - Hz
     - Frequency of sine wave
   * - ``Va``
     - 10
     - V
     - Amplitude of sine wave
   * - ``Ph``
     - 0
     - °
     - Phase of sine wave
   * - ``Voff``
     - 0
     - V
     - Voltage offset

Description
-----------

The documentation of the class (``help(SinVoltage)``)::

    This class models a Sinusoidal Voltage Source.

    The voltage waveform follows the equation:
        V(t) = Va * sin(2π * Fr * t + Ph) + Voff

    Attributes:
        V (signal): Output voltage.
        Fr (param): Frequency of the sine wave (Hz).
        Va (param): Amplitude of the sine wave (V).
        Ph (param): Phase shift in degrees (°).
        Voff (param): Voltage offset (V).

    Methods:
        analog(): Implements the sinusoidal voltage equation.

Used in the examples
--------------------

* :doc:`Half wave rectification circuit </examples/half_wave_rectifier>`
* :doc:`Full-wave bridge rectifier fed by a transformer </examples/bridge_rectifier>`
* :doc:`Zener diode: I(V) characteristic and shunt regulator </examples/zener_regulator>`
* :doc:`AC analysis (small-signal frequency response) </examples/ac_analysis>`
* :doc:`Elliptic (Cauer) RLC low-pass filter </examples/elliptic_filter>`
* :doc:`idt() example: an inductor written with the integral </examples/idt_example>`
* :doc:`JFET common-source amplifier (self bias) </examples/jfet_amplifier>`
* :doc:`Thyristor phase control (half-wave, resistive load) </examples/thyristor_phase_control>`
* :doc:`Thyristor lamp dimmer (half-wave phase control, three angles) </examples/thyristor_lamp_dimmer>`
* :doc:`Schmitt trigger with two BJT transistors (emitter coupled) </examples/schmitt_bjt>`
* :doc:`Schmitt trigger with an op-amp (inverting) </examples/schmitt_opamp>`

