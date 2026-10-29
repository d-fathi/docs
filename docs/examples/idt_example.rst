idt() example: an inductor written with the integral
====================================================

Script: ``idt_example.py``

Description::

    idt(x, ic) = ic + integral of x dt.   The inductor  v = L di/dt  can be
    written either with the derivative  (Inductor model: v = L ddt(i))  or with
    the integral  i = I0 + (1/L) integral v dt  :
    
          self.I += idt(self.V, self.I0 * self.L) / self.L
    
    Both models are put in the same series RLC circuit and compared.

Code
----

.. literalinclude:: idt_example.py
   :language: python
   :linenos:

Result
------

.. image:: /_static/examples/idt_example_result.png
   :alt: idt() example: an inductor written with the integral
   :align: center

