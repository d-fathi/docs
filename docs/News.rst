News
====

PyAMS 0.3.0
-----------

Version 0.3.0 brings a new solver core and many new elements:

* **AC analysis** (small signal): ``circuit.analysis(mode="ac", start=f1, stop=f2, step=N)``
  returns the complex transfer function of every node.
* **DC sweep** of any parameter: ``analysis(mode="dc", param="V1.Vdc", start=0, stop=5, step=0.1)``.
* **Parametric sweep**: ``circuit.sweep(param="R1.R", list=[...])`` repeats any analysis for several values.
* **Better transient solver**: second-order integration (``order=2``) and an adaptive time step (``adaptive=True``).
* **New models**: ``Conductor`` (with temperature and self-heating), ``Thyristor``, ``Diac``, ``UJT``,
  ``TunnelDiode``, ``IGBT``, ``JFET``, ``MOSFET4``, ``Timer555``, ``Comparator``, ``TransmissionLine``,
  ``Transformer``, ``ExpVoltage``/``ExpCurrent`` and ``PWLVoltage``/``PWLCurrent`` sources.
* **New documentation** with a page for every model and 40 ready-to-run examples.

See :doc:`release_history` for the complete list of versions.
