Trapezoid (Pulse) Voltage
=========================

.. code-block:: python

    from pyams.models import TrapezoidVoltage

    X1 = TrapezoidVoltage("a", "b")
    X1.setParams("V0=1 V1=1")

Terminals
---------

``TrapezoidVoltage(a, b)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``V0``
     - 1
     - V
     - Initial voltage
   * - ``V1``
     - 1
     - V
     - Peak voltage
   * - ``Td``
     - 0
     - Sec
     - Initial delay time
   * - ``Tr``
     - 0
     - Sec
     - Rise time
   * - ``Tw``
     - 0.05
     - Sec
     - Pulse-width
   * - ``Tf``
     - 0
     - Sec
     - Fall time
   * - ``T``
     - 0.1
     - Sec
     - Total period of the waveform
   * - ``Voff``
     - 0
     - V
     - Offset voltage

Description
-----------

The documentation of the class (``help(TrapezoidVoltage)``)::

    This class models a Trapezoidal Waveform Voltage Source.

    The voltage waveform follows a trapezoidal shape with:
    - An initial delay (Td)
    - A rising edge (Tr)
    - A constant peak (Tw)
    - A falling edge (Tf)
    - A periodic repetition (T)

    Attributes:
        V (signal): Output voltage.
        V0 (param): Initial voltage.
        V1 (param): Peak voltage.
        Td (param): Initial delay time.
        Tr (param): Rise time.
        Tw (param): Pulse-width (high duration).
        Tf (param): Fall time.
        T (param): Total period of the waveform.
        Voff (param): Offset voltage.

    The voltage waveform is defined as:

    - **Before initial delay (t ≤ Td):**
      V = V0 + Voff

    - **During the rising edge (0 ≤ t ≤ Tr):**
      V = ((V1 - V0) / Tr) * t + V0 + Voff

    - **During the high state (Tr ≤ t ≤ Tr + Tw):**
      V = V1 + Voff

    - **During the falling edge (Tr + Tw ≤ t ≤ Tr + Tw + Tf):**
      V = ((V0 - V1) / Tf) * (t - Tr - Tw) + V1 + Voff

    - **During the low state (t > Tr + Tw + Tf):**
      V = V0 + Voff

    Methods:
        analog(): Defines the trapezoidal waveform equation.

Used in the examples
--------------------

* :doc:`Charge and discharge of a capacitor (RC circuit) </examples/charge_discharge>`
* :doc:`Series RLC circuit (inductor example) </examples/rlc>`
* :doc:`Conductor: resistance from geometry, temperature and self-heating </examples/conductor_examples>`
* :doc:`Transmission line: pulse, reflections and the load resistance </examples/transmission_line>`
* :doc:`MOSFET4: 4-terminal MOSFET, body effect </examples/mosfet4_examples>`
* :doc:`Thyristor phase control (half-wave, resistive load) </examples/thyristor_phase_control>`
* :doc:`Thyristor lamp dimmer (half-wave phase control, three angles) </examples/thyristor_lamp_dimmer>`
* :doc:`IGBT chopper (low-side switch, inductive load, freewheel diode) </examples/igbt_chopper>`
* :doc:`Tunnel diode oscillator </examples/tunnel_diode_oscillator>`
* :doc:`Astable multivibrator (two NPN BJT transistors) </examples/astable>`
* :doc:`555 timer, monostable (one-shot) </examples/timer555_monostable>`

