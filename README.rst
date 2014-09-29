=====================
PEP 500: Type hinting
=====================

This is a work-in-progress repository for the draft of the Type Hinting
PEP for Python 3.5.

Authors
-------

* Guido van Rossum

* Jukka Lehtosalo

* Łukasz Langa

Random notes from the Skype meeting
-----------------------------------

* just static type checker

* signature will preserve the full expression

* ``typing`` as alias for types from other modules

* aliases with parameters: the type checker has a limited understanding of the
  semantics; has to be able to follow the definitions to understand it. Overly
  dynamic type definitions can confuse the type checker. Expected: left-hand
  side variable, right-hand side typing expression.

* variable typing is the future; for the first iteration we introduce just
  comments

* we should discourage using runtime-dependent annotations; just use type
  expressions directly

* conditions of types: platforms, Python versions, etc.

* constant expressions, compile-time expressions

* syntax section should be enough to implement a compatible parser; the PEP
  should have the complete list of all names importable from the typing module
