## [312.0.0.20261104](https://pypi.org/project/types-pywin32/312.0.0.20261104/) (2026-11-04)

* pywin32 fixes for pywin32's own demos and tests ([#16680](https://github.com/python/typeshed/pull/16680))

    Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## [312.0.0.20261031](https://pypi.org/project/types-pywin32/312.0.0.20261031/) (2026-10-31)

* Type `pscon` property keys as `PyPROPERTYKEY` ([#16656](https://github.com/python/typeshed/pull/16656))

    pywin32 converts a `PROPERTYKEY` to and from an `(IID, pid)` tuple ([source](https://github.com/mhammond/pywin32/blob/b312/com/win32comext/propsys/src/propsys.cpp#L38-L46)), and every `PKEY_*` constant in `pscon` is such a tuple ([source](https://github.com/mhammond/pywin32/blob/b312/com/win32comext/propsys/pscon.py#L153)). This makes `PyPROPERTYKEY` an alias for `tuple[PyIID, int]` and uses it for the 567 `PKEY_*` constants (plus `int` for `GUIDSTRING_MAX`/`PKEYSTR_MAX`), so the constants can be passed to `propsys` functions that take a `PyPROPERTYKEY`.

    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

* Replace `Incomplete` in `win32gui` ([#16651](https://github.com/python/typeshed/pull/16651))

## [312.0.0.20261024](https://pypi.org/project/types-pywin32/312.0.0.20261024/) (2026-10-24)

* Annotate `win32comext.mapi.emsabtags` constants as `int` ([#16601](https://github.com/python/typeshed/pull/16601))

## [312.0.0.20261006](https://pypi.org/project/types-pywin32/312.0.0.20261006/) (2026-10-06)

* Enable Ruff rule RUF036 ([#16477](https://github.com/python/typeshed/pull/16477))

    Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## [312.0.0.20260928](https://pypi.org/project/types-pywin32/312.0.0.20260928/) (2026-09-28)

* Fix win32file.ReadFile return types and overlapped forms ([#16429](https://github.com/python/typeshed/pull/16429))

    ReadFile returns bytes, not str: a new bytes object when no OVERLAPPED
    is passed, the buffer object itself (or a freshly allocated read buffer
    for an int size) when one is. The stub also rejected an OVERLAPPED
    together with an int size and accepted only PyOVERLAPPEDReadBuffer as
    the buffer, while the runtime takes any writable buffer.

## [312.0.0.20260827](https://pypi.org/project/types-pywin32/312.0.0.20260827/) (2026-08-27)

* fixed some typos ([#16273](https://github.com/python/typeshed/pull/16273))

* Improve win32ras ([#16227](https://github.com/python/typeshed/pull/16227))

* Improve pythonwin.dde ([#16221](https://github.com/python/typeshed/pull/16221))

* Import win32ras definitions in pywin32.lib.win2kras ([#16223](https://github.com/python/typeshed/pull/16223))

## [312.0.0.20260820](https://pypi.org/project/types-pywin32/312.0.0.20260820/) (2026-08-20)

* Improve win32crypt ([#16237](https://github.com/python/typeshed/pull/16237))

## [312.0.0.20260818](https://pypi.org/project/types-pywin32/312.0.0.20260818/) (2026-08-18)

* Use Final for win32.lib constants ([#16222](https://github.com/python/typeshed/pull/16222))

## [312.0.0.20260817](https://pypi.org/project/types-pywin32/312.0.0.20260817/) (2026-08-17)

* Improve pythonwin.win32uiole ([#16220](https://github.com/python/typeshed/pull/16220))

* Improve pythonwin.win32ui ([#16214](https://github.com/python/typeshed/pull/16214))

## [312.0.0.20260724](https://pypi.org/project/types-pywin32/312.0.0.20260724/) (2026-07-24)

* Replace `NoReturn` with `Never` ([#16079](https://github.com/python/typeshed/pull/16079))

## 312.0.0.20260609 (2026-06-09)

Fix type errors in pywin32 using types-pywin32 ([#13844](https://github.com/python/typeshed/pull/13844))

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

[pywin32] Update to 312 ([#15871](https://github.com/python/typeshed/pull/15871))

## 311.0.0.20260521 (2026-05-21)

[pywin32] Replace Incomplete win32print types ([#15794](https://github.com/python/typeshed/pull/15794))

- Add the missing `DEVMODEType` and `DEVMODEWType` types, these are
  both aliases to the `PyDEVMODEW` class.
- Merge the `PyDEVMODE` and `PyDEVMODEW` classes, these are the same
  class in reality.
- Fix the type of `TimeType.format` to include the default value for
  the `format` parameter.
- Audit all the types in the win32print module, replacing all
`Incomplete` types with an appropriate `TypedDict`, and using overloads
to reference the correct version of the type.

## 311.0.0.20260518 (2026-05-18)

Upgrade black to 26.5.0 ([#15801](https://github.com/python/typeshed/pull/15801))

## 311.0.0.20260508 (2026-05-08)

Import some items from typing instead of typing_extensions ([#15711](https://github.com/python/typeshed/pull/15711))

Part of #13782

## 311.0.0.20260408 (2026-04-08)

Use dashes instead of underscores for METADATA.toml field names ([#15614](https://github.com/python/typeshed/pull/15614))

## 311.0.0.20260402 (2026-04-02)

Update most test/lint dependencies ([#15582](https://github.com/python/typeshed/pull/15582))

## 311.0.0.20260323 (2026-03-23)

[pywin32] Improve win32com ([#15527](https://github.com/python/typeshed/pull/15527))

## 311.0.0.20260317 (2026-03-17)

[pywin32] Add parameters for incomplete functions ([#15512](https://github.com/python/typeshed/pull/15512))

## 311.0.0.20260316 (2026-03-16)

[pywin32] Mark stub-only NamedTuples as `@type_check_only` ([#15514](https://github.com/python/typeshed/pull/15514))

## 311.0.0.20251008 (2025-10-08)

pywin32: fill in the type of win32.win32pipe.GetNamedPipeInfo ([#14846](https://github.com/python/typeshed/pull/14846))

## 311.0.0.20250915 (2025-09-15)

Add `@disjoint_base` decorator to the third-party stubs ([#14716](https://github.com/python/typeshed/pull/14716))

## 311.0.0.20250914 (2025-09-14)

Update mypy to 1.18.1 ([#14699](https://github.com/python/typeshed/pull/14699))

## 311.0.0.20250822 (2025-08-22)

Add missing defaults to third-party stubs ([#14617](https://github.com/python/typeshed/pull/14617))

## 311.0.0.20250809 (2025-08-09)

Fix dunder-method positional-only parameter discrepancies in third-party stubs ([#14529](https://github.com/python/typeshed/pull/14529))

## 311.0.0.20250801 (2025-08-01)

Split `tool.stubtest.platforms` metadata key ([#13746](https://github.com/python/typeshed/pull/13746))

Co-authored-by: Avasam <samuel.06@hotmail.com>
Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>

## 311.0.0.20250731 (2025-07-31)

Type stub for `win32com.server` ([#14492](https://github.com/python/typeshed/pull/14492))

## 311.0.0.20250728 (2025-07-28)

[pywin32] Update `LookupAccountSid` to accept `None` for `systemName` ([#14484](https://github.com/python/typeshed/pull/14484))

## 311.0.0.20250723 (2025-07-23)

Bump pywin32 to 311.* ([#14437](https://github.com/python/typeshed/pull/14437))

## 310.0.0.20250516 (2025-05-16)

Replace `Incomplete | None = None` in third party stubs ([#14063](https://github.com/python/typeshed/pull/14063))

## 310.0.0.20250429 (2025-04-29)

Improve `pywin32.isapi` ([#13889](https://github.com/python/typeshed/pull/13889))

## 310.0.0.20250428 (2025-04-28)

Fix return type of win32wnet.WNetOpenEnum ([#13890](https://github.com/python/typeshed/pull/13890))

## 310.0.0.20250426 (2025-04-26)

pywin32: Fix various arguments ([#13846](https://github.com/python/typeshed/pull/13846))

## 310.0.0.20250319 (2025-03-19)

Bump pywin32 to 310.* ([#13667](https://github.com/python/typeshed/pull/13667))

## 309.0.0.20250311 (2025-03-11)

Bump pywin32 to 309 ([#13607](https://github.com/python/typeshed/pull/13607))

## 308.0.0.20250128 (2025-01-28)

Have `win32gui.SystemParametersInfo` return `Any` ([#13438](https://github.com/python/typeshed/pull/13438))

## 308.0.0.20250124 (2025-01-24)

pywin32: type `Get*` functions in win32api ([#13430](https://github.com/python/typeshed/pull/13430))

## 308.0.0.20241221 (2024-12-21)

Update to mypy 1.14 ([#13272](https://github.com/python/typeshed/pull/13272))

## 308.0.0.20241128 (2024-11-28)

Add pywin32's isapi.install ([#13119](https://github.com/python/typeshed/pull/13119))

## 308.0.0.20241121 (2024-11-21)

Fix pywin32 GetClipboardData return type ([#13046](https://github.com/python/typeshed/pull/13046))

Fixes #12825

## 308.0.0.20241029 (2024-10-29)

Add `win32com.gen_py` ([#12901](https://github.com/python/typeshed/pull/12901))

## 308.0.0.20241025 (2024-10-25)

Allow pywin32 to use `pywin.mfc.DocTemplate` in lieu of `PyCDocTemplate` ([#12888](https://github.com/python/typeshed/pull/12888))

## 308.0.0.20241015 (2024-10-15)

Bump pywin32 to 308.* ([#12799](https://github.com/python/typeshed/pull/12799))

## 307.0.0.20241009 (2024-10-09)

Bump pywin32 to 307 ([#12742](https://github.com/python/typeshed/pull/12742))

## 306.0.0.20240822 (2024-08-22)

Using precise code for `pyright: ignore` and re-enabling various pyright tests ([#12576](https://github.com/python/typeshed/pull/12576))

## 306.0.0.20240806 (2024-08-06)

Bump mypy to 1.11.1 ([#12463](https://github.com/python/typeshed/pull/12463))

## 306.0.0.20240408 (2024-04-08)

pywin32: Improve SHGetPropertyStoreFromParsingName type definition ([#11654](https://github.com/python/typeshed/pull/11654))

Improve SHGetPropertyStoreFromParsingName type definition

## 306.0.0.20240331 (2024-03-31)

Various pywin32 improvements ([#11616](https://github.com/python/typeshed/pull/11616))

## 306.0.0.20240319 (2024-03-19)

Improved pywin32 error and exception classes ([#11613](https://github.com/python/typeshed/pull/11613))

## 306.0.0.20240313 (2024-03-13)

`pywin32`: Correctly reference `TimeType` aka `pywintypes.datetime` ([#11577](https://github.com/python/typeshed/pull/11577))

* Correctly reference TimeType

* PyUnicode is UnicodeType

## 306.0.0.20240312 (2024-03-12)

Add deprecation decorator and comments for pywin32 ([#11570](https://github.com/python/typeshed/pull/11570))

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 306.0.0.20240310 (2024-03-10)

Bump mypy to 1.9, add to json.encoder, small fixups ([#11549](https://github.com/python/typeshed/pull/11549))

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 306.0.0.20240130 (2024-01-30)

pywin32: Remove reference to stubgen dll analysis issue ([#11323](https://github.com/python/typeshed/pull/11323))

## 306.0.0.20240128 (2024-01-28)

pywin32: Use PEP 570 positional-only argument syntax and fix arguments ([#11321](https://github.com/python/typeshed/pull/11321))

## 306.0.0.20240106 (2024-01-06)

Update typing_extensions imports in third-party stubs ([#11245](https://github.com/python/typeshed/pull/11245))

## 306.0.0.8 (2023-12-19)

pywin32 annotations improvements ([#11177](https://github.com/python/typeshed/pull/11177))

## 306.0.0.7 (2023-12-08)

Fix `pywin32`'s `PyCBitmap.GetBitmapBits` method ([#11108](https://github.com/python/typeshed/pull/11108))

## 306.0.0.6 (2023-10-29)

Type `pywin32`'s `win32.win32print.StartDocPrinter` method ([#10898](https://github.com/python/typeshed/pull/10898))

Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 306.0.0.5 (2023-10-15)

pywin32: Annotate `win32com.client.constants` ([#10888](https://github.com/python/typeshed/pull/10888))

## 306.0.0.4 (2023-08-14)

pywin32: Fix PyNETRESOURCE descriptor members wrongly marked as readonly ([#10574](https://github.com/python/typeshed/pull/10574))

## 306.0.0.3 (2023-07-20)

Add an upstream_repository field to METADATA.toml ([#10487](https://github.com/python/typeshed/pull/10487))

Closes: #10478

## 306.0.0.2 (2023-05-28)

pywin32: add `HANDLEType` class ([#10032](https://github.com/python/typeshed/pull/10032))

per http://timgolden.me.uk/pywin32-docs/PyHANDLE.html these objects actually have methods, they are not ints

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 306.0.0.1 (2023-03-27)

Add default values for third-party stubs beginning with 'P' ([#9957](https://github.com/python/typeshed/pull/9957))

## 306.0.0.0 (2023-03-26)

Bump pywin32 to 306.* ([#9945](https://github.com/python/typeshed/pull/9945))

Release: https://pypi.org/pypi/pywin32/306
Homepage: https://github.com/mhammond/pywin32

## 305.0.0.11 (2023-03-22)

Add missing types to `pywin32.win32api` ([#9920](https://github.com/python/typeshed/pull/9920))

Co-authored-by: Francesc Elies <francesc.elies@mbbm-ast.com>
Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 305.0.0.10 (2023-03-09)

[pywin32] win32gui.FindWindowEx parameters __ClassName and __WindowName are optional ([#9859](https://github.com/python/typeshed/pull/9859))

## 305.0.0.9 (2023-02-21)

Stubtest settings: change `ignore_missing_stub` default to `false` ([#9779](https://github.com/python/typeshed/pull/9779))

If you're reading about this commit from an autogenerated changelog entry, this should have no user-visible impact on how the stubs are interpreted by a type checker; it's just an internal change to how typeshed's tests work.

## 305.0.0.8 (2023-02-15)

Use `typing_extensions.Self` instead of `_typeshed.Self` ([#9702](https://github.com/python/typeshed/pull/9702))

## 305.0.0.7 (2023-01-17)

Reenable flake8-pyi's Y011 and Y015 ([#9551](https://github.com/python/typeshed/pull/9551))

## 305.0.0.6 (2023-01-13)

Allowlist-only fixes for stubtest on Windows ([#9522](https://github.com/python/typeshed/pull/9522))

## 305.0.0.5 (2022-12-28)

Check for unused `pyright: ignore` and differentiate from mypy ignores ([#9397](https://github.com/python/typeshed/pull/9397))

## 305.0.0.4 (2022-12-07)

3rd-party stubtest: run on Python 3.10 ([#9342](https://github.com/python/typeshed/pull/9342))

## 305.0.0.3 (2022-12-06)

More pywin32 stub completion ([#9308](https://github.com/python/typeshed/pull/9308))

Completed based on usage of the following libraries in mypy_primer:
- apprise
- comtypes
As well as some of the most popular libraries that use both pywin32 and mypy (all over 1k stars on github):
- certbot
- anki
- flexget
- monkey
- twisted
- salt

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>

## 305.0.0.2 (2022-11-23)

Mark first argument of `__[get|set|del]attr__` as `str` ([#9245](https://github.com/python/typeshed/pull/9245))

## 305.0.0.1 (2022-11-11)

Add the ability to run third-party stubtest on Windows or MacOS when needed ([#8923](https://github.com/python/typeshed/pull/8923))

Co-authored-by: Alex Waygood <Alex.Waygood@Gmail.com>
Co-authored-by: Jelle Zijlstra <jelle.zijlstra@gmail.com>

## 305.0.0.0 (2022-11-10)

Update pywin32 to 305 ([#9153](https://github.com/python/typeshed/pull/9153))

## 304.0.0.6 (2022-11-10)

Update pywin32 to mypy 0.990 ([#9124](https://github.com/python/typeshed/pull/9124))

## 304.0.0.5 (2022-11-09)

Annotate known magic-method return types ([#9131](https://github.com/python/typeshed/pull/9131))

## 304.0.0.4 (2022-11-05)

pywin32: Improve some types ([#9089](https://github.com/python/typeshed/pull/9089))

## 304.0.0.3 (2022-10-31)

pywin32 stubs update ([#9040](https://github.com/python/typeshed/pull/9040))

boolean methods
win32gui_struct
MonitorFromRect, FindWindow, FindWindowEx, GetWindowPlacement, GetMenuItemRect

## 304.0.0.2 (2022-10-19)

pywin32: Remove IID that doesn't exist at runtime ([#8930](https://github.com/python/typeshed/pull/8930))

Remove IID that doesn't exist at runtime

## 304.0.0.1 (2022-10-07)

pywin32: Complete modules using stubgen & stubtest ([#8866](https://github.com/python/typeshed/pull/8866))

Complete modules using stubgen & stubtest

## 304.0.0.0 (2022-10-03)

Add `pywin32` type stubs from microsoft/python-type-stubs and mhammond/pywin32  ([#8825](https://github.com/python/typeshed/pull/8825))
