Simulation Options
==================

Options are passed as keyword arguments of ``analysis()``:

.. code-block:: python

    cir.analysis(mode="tran", start=0, stop=6e-3, step=1e-6,
                 adaptive=True, order=2, reltol=1e-6)

An unknown option raises an error that lists the valid ones. The current values are in ``cir.options``.

Transient options
-----------------

.. list-table::
   :header-rows: 1
   :widths: 18 14 68

   * - Option
     - Default
     - Meaning
   * - ``order``
     - ``1``
     - integration method of ``ddt()``: ``1`` = backward Euler (robust, first order);
       ``2`` = variable-step BDF2 (second order, still stable on stiff, switching circuits)
   * - ``adaptive``
     - ``False``
     - ``True``: the solver picks its own step (tiny at fast edges, large in between) from an estimate of the local
       error; ``step`` then only sets the spacing of the output points, which are interpolated.
       It has an effect only when some model uses ``ddt()``
   * - ``lte``
     - ``1e-4``
     - relative local-error tolerance of the adaptive step
   * - ``lte_abs``
     - ``1e-6``
     - absolute local-error tolerance (volts)
   * - ``max_step``
     - ``20 * step``
     - largest internal step. A pulse much shorter than ``max_step`` can be stepped over: lower it then
   * - ``uic``
     - ``False``
     - ``True``: start the transient from an all-zero state instead of the DC operating point
   * - ``progress``
     - ``False``
     - ``True``: show a text progress bar; or pass a function ``fn(fraction, t)``

AC options
----------

.. list-table::
   :header-rows: 1
   :widths: 18 14 68

   * - Option
     - Default
     - Meaning
   * - ``scale``
     - ``"dec"``
     - frequency sweep: ``"dec"`` / ``"oct"`` = ``step`` points per decade / octave, ``"lin"`` = ``step`` points in all

Solver (Newton–Raphson) options
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 14 68

   * - Option
     - Default
     - Meaning
   * - ``reltol``
     - ``1e-6``
     - relative convergence tolerance of the Newton iteration
   * - ``vntol``
     - ``1e-9``
     - absolute tolerance of the node voltages (volts)
   * - ``abstol``
     - ``1e-12``
     - absolute tolerance of the branch currents (amperes)
   * - ``gmin``
     - ``1e-12``
     - minimum conductance added from every node to ground; it helps the convergence of floating nodes
   * - ``maxiter``
     - ``50``
     - maximum number of Newton iterations per solution
   * - ``vlimit``
     - ``1.0``
     - largest change of a node voltage per iteration when the solver falls back to limited steps

Convergence strategy
--------------------

The Newton iteration starts as a plain iteration. If it fails, it is retried with limited node-voltage steps
(``vlimit``), then with *gmin stepping*; in a transient run a failing time step is bisected.
After a run, ``cir.stats`` reports the number of accepted and rejected steps of an adaptive transient.

Tips
----

* Circuits with fast switching, relaxation oscillators or stiff dynamics: use ``adaptive=True, order=2``.
* A short pulse can be missed by the adaptive step: set ``max_step`` smaller than the pulse width.
* A circuit that does not converge in DC: check for floating nodes and, if needed, raise ``gmin`` slightly.
