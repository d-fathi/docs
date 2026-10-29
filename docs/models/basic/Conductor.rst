Conductor
=========

.. code-block:: python

    from pyams.models import Conductor

    X1 = Conductor("p", "n")
    X1.setParams("Rho=1.68e-08 Len=1")

Terminals
---------

``Conductor(p, n, thermal=False)``

Optional constructor arguments: ``thermal`` (default ``False``).

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Rho``
     - 1.68e-08
     - Ω·m
     - Resistivity at T0
   * - ``Len``
     - 1
     - m
     - Length
   * - ``Area``
     - 1e-06
     - m²
     - Cross-section area
   * - ``Alpha``
     - 0.00393
     - 1/K
     - Temperature coefficient of the resistivity
   * - ``T0``
     - 20
     - °C
     - Reference temperature
   * - ``Tamb``
     - 25
     - °C
     - Ambient temperature
   * - ``Rth``
     - 10
     - K/W
     - Thermal resistance to the ambient
   * - ``Cth``
     - 1
     - J/K
     - Heat capacity

Description
-----------

The documentation of the class (``help(Conductor)``)::

    Conductor: a wire, a PCB track, a bus bar, a lamp filament.  Unlike a
    Resistor, the resistance comes from the material and the geometry and it
    follows the temperature:

        R0 = Rho * Len / Area                           (at the reference temperature T0)
        R  = R0 * (1 + Alpha (T - T0))                  (T = temperature of the conductor)
        I  = V / R

    Without self-heating (the default) T is the ambient temperature Tamb.

    Self-heating, ``Conductor(p, n, thermal=True)``: the conductor gets a
    thermal node whose voltage is the temperature rise DT (in kelvin) above the
    ambient, a thermal resistor Rth to the ambient (K/W) and a heat capacity Cth
    (J/K):

        Cth d(DT)/dt = P - DT / Rth,        P = V^2 / R,      T = Tamb + DT

    so the resistance changes with the dissipated power: a copper or tungsten
    wire (Alpha > 0) limits its own current as it heats up; with Alpha < 0 (a
    thermistor) it would run away.  The temperature rise can be plotted with
    ``setOutPuts("W1.DT")``.  The time constant is about Rth * Cth.

    Typical materials (Rho at 20 C in ohm m, Alpha in 1/K):
        copper 1.68e-8, 3.93e-3     silver 1.59e-8, 3.8e-3     gold 2.44e-8, 3.4e-3
        aluminium 2.65e-8, 3.9e-3   tungsten 5.6e-8, 4.5e-3    nichrome 1.1e-6, 4e-4
        constantan 4.9e-7, 1e-5

    Terminals: Conductor(p, n, thermal=False).

    Attributes:
        V (signal): voltage across the conductor.
        I (signal): current p -> n.
        DT (signal): temperature rise node (only with thermal=True).
        Rho (Ω m, 1.68e-8 copper), Len (m, 1), Area (m², 1e-6 = 1 mm²),
        Alpha (1/K, 3.93e-3), T0 (°C, 20), Tamb (°C, 25),
        Rth (K/W, 10) and Cth (J/K, 1): thermal parameters, used only with thermal=True.

Used in the examples
--------------------

* :doc:`Conductor: resistance from geometry, temperature and self-heating </examples/conductor_examples>`

