Inductor with Initial Current
=============================

.. code-block:: python

    from pyams.models import InductorIc

    X1 = InductorIc("p", "n")
    X1.setParams("L=0.001 Ic=0")

Terminals
---------

``InductorIc(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``L``
     - 0.001
     - H
     - Inductance
   * - ``Ic``
     - 0
     - A
     - Initial current

Description
-----------

The documentation of the class (``help(InductorIc)``)::

    Inductor with an initial current (SPICE ``L ... IC=``).

        I(t) = Ic + (1/L) integral(V dt)          (I flows p -> n)

    Written in integral form, so at the start of the transient (operating
    point) the inductor carries exactly Ic and then evolves freely.  Use it
    with a normal transient analysis (not ``uic=True``).

    Terminals: InductorIc(p, n)
    Parameters:
        L    inductance (H)            (1 mH)
        Ic   initial current p -> n (A)    (0)

Used in the examples
--------------------

* :doc:`Van der Pol oscillator:  C v'' + Mu (v^2 - 1) v' + v/L = 0 </examples/van_der_pol>`
* :doc:`Van der Pol oscillator: parametric sweep of Mu with cir.sweep(param="R1.Mu", list=[...]) </examples/van_der_pol_sweep>`

