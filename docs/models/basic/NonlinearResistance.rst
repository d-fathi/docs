Nonlinear Resistance
====================

.. code-block:: python

    from pyams.models import NonlinearResistance

    X1 = NonlinearResistance("p", "n")
    X1.setParams("Mu=1")

Terminals
---------

``NonlinearResistance(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Mu``
     - 1
     - S
     - Nonlinearity coefficient

Description
-----------

The documentation of the class (``help(NonlinearResistance)``)::

    Voltage-controlled nonlinear (cubic) resistance used in the Van der Pol
    oscillator.  Its differential conductance is

        1/R(v) = dI/dV = Mu (v^2 - 1)

    i.e. negative for |v| < 1 (it injects energy) and positive for |v| > 1
    (it dissipates energy).  Integrating gives the current

        I(v) = Mu (v^3 / 3 - v)

    Connected in parallel with a capacitor C and an inductor L the node voltage
    obeys   C v'' + Mu (v^2 - 1) v' + v / L = 0   (Van der Pol equation).

    Terminals: NonlinearResistance(p, n)   current flows p -> n.
    Parameters:
        Mu   nonlinearity / damping coefficient (S)      (1)

Used in the examples
--------------------

* :doc:`Van der Pol oscillator:  C v'' + Mu (v^2 - 1) v' + v/L = 0 </examples/van_der_pol>`
* :doc:`Van der Pol oscillator: parametric sweep of Mu with cir.sweep(param="R1.Mu", list=[...]) </examples/van_der_pol_sweep>`

