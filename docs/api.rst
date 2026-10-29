API reference
=============

The core classes live in ``pyams.lib``:

.. code-block:: python

    from pyams.lib import circuit, model, signal, param, voltage, current, time, ddt, idt

circuit
-------

.. autoclass:: pyams.lib.circuit
   :members: addElements, setOutPuts, analysis, sweep, run, plot

model
-----

.. autoclass:: pyams.lib.model
   :members: analog, getParams, setParams

signal
------

.. autoclass:: pyams.lib.signal

param
-----

.. autoclass:: pyams.lib.param

Errors
------

.. autoclass:: pyams.lib.SimulationError
