Simulation (DC, TR, AC)
=======================

The analysis is chosen with ``cir.analysis(mode=...)`` and executed with ``cir.run()``.

.. list-table::
   :header-rows: 1
   :widths: 22 38 40

   * - ``mode``
     - Use it for
     - Main arguments
   * - ``"dc"``
     - operating point
     - –
   * - ``"dc"`` with ``param=``
     - DC sweep (I–V curves, transfer curves)
     - ``param``, ``start``, ``stop``, ``step``
   * - ``"tran"``
     - behavior in time
     - ``start``, ``stop``, ``step`` (seconds)
   * - ``"ac"``
     - small-signal frequency response
     - ``start``, ``stop`` (Hz), ``step`` (points per decade)

DC analysis
-----------

A single DC operating point: capacitors are open, inductors are short circuits, and time-dependent
sources have their value at ``t = start``.

.. code-block:: python

    cir.analysis(mode="dc")
    res = cir.run()
    print(res["A"][0], res["D1.I"][0])

DC sweep
--------

Sweep one parameter (``"Element.Parameter"``) and solve the operating point at every value.
Each point starts from the previous solution, so a sweep costs little more than one operating point.

.. code-block:: python

    cir.analysis(mode="dc", param="V1.Vdc", start=0, stop=5, step=0.05)
    res = cir.run()          # res["sweep"] = swept values, res["D1.I"] = diode current
    cir.plot()

.. image:: /_static/examples/jfet_curves.png
   :align: center
   :alt: DC sweep: JFET output characteristics

A family of curves is obtained with a parametric sweep (below) or by looping over the second parameter in
Python — see :doc:`examples/jfet_curves`.

Transient analysis (TR)
-----------------------

.. code-block:: python

    cir.analysis(mode="tran", start=0, stop=0.06, step=1e-4)
    res = cir.run()           # {'time': ..., 'In': ..., 'Out': ...}
    cir.plot()

``step`` is the time step of a fixed-step run. With ``adaptive=True`` it becomes only the spacing of the
output points (see :doc:`options`).

.. image:: /_static/examples/rlc_result.png
   :align: center
   :alt: Transient response of a series RLC circuit

AC analysis
-----------

PyAMS solves the DC operating point, **linearizes** every element around it, and solves the complex system

.. math::

    \left( G + j\omega C + \frac{Q}{j\omega} \right) x = b

at every frequency. The stimulus comes from the sources that define an AC value
(``ACVoltage``, ``ACCurrent``). With a 1 V stimulus, the phasor of each node *is* the transfer function.

.. code-block:: python

    import numpy as np
    from pyams.lib import circuit
    from pyams.models import ACVoltage, Resistor, Capacitor

    V1 = ACVoltage("In", "0")
    R1 = Resistor("In", "Out");  R1.setParams("R=1KΩ")
    C1 = Capacitor("Out", "0");  C1.setParams("C=1uF")

    cir = circuit()
    cir.addElements({"V1": V1, "R1": R1, "C1": C1})
    cir.setOutPuts("Out")
    cir.analysis(mode="ac", start=1, stop=1e5, step=20)    # 20 points per decade
    res = cir.run()

    f, H = res["freq"], res["Out"]                          # H is complex
    gain_db   = 20 * np.log10(np.abs(H))
    phase_deg = np.angle(H, deg=True)
    cir.plot()                                              # magnitude and phase

.. image:: /_static/examples/rc_ac.png
   :align: center
   :alt: AC response of an RC low-pass filter

``scale="dec"`` (default) and ``"oct"`` give ``step`` points per decade / octave; ``scale="lin"`` gives
``step`` points in total.

Parametric sweep
----------------

``cir.sweep(param, list)`` repeats the *whole* analysis (DC, transient or AC) once for every value of a parameter.
``run()`` then returns a list of result dictionaries, each with the extra key ``"param"``, and ``plot()``
overlays them.

.. code-block:: python

    cir.analysis(mode="ac", start=1, stop=1e5, step=20)
    cir.sweep(param="R1.R", list=[100, 1000, 10000])
    runs = cir.run()                 # one result per resistor value
    cir.plot()

    cir.sweep()                      # switch the parametric sweep off

Results
-------

``run()`` returns plain dictionaries of NumPy arrays (also stored in ``cir.results``):

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Analysis
     - Keys of the result
   * - ``tran``
     - ``"time"``, then one array per output
   * - ``dc`` (point)
     - ``"time"`` (one value), then one value per output
   * - ``dc`` with ``param``
     - ``"sweep"``, ``"Element.Parameter"``, then one array per output
   * - ``ac``
     - ``"freq"``, then one **complex** array per output
   * - with ``sweep()``
     - a list of the dictionaries above, each with the extra key ``"param"``

Showing the results
-------------------

.. code-block:: python

    cir.plot()                              # open a window
    cir.plot("result.png", show=False)      # save to a file

``plot()`` adapts to the analysis: a transient run gets one panel per unit (voltage, current), a DC sweep is plotted
against the swept parameter, an AC run gives magnitude and phase, and a parametric sweep overlays all runs.

For your own figures use the arrays directly:

.. code-block:: python

    import matplotlib.pyplot as plt

    res = cir.run()
    fig, ax = plt.subplots()
    ax.plot(res["time"] * 1e3, res["Out"], label="Out")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.legend()
    fig.savefig("out.png", dpi=150)
