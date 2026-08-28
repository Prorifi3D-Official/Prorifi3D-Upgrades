FSL Auto Test Portable 2026.08.17
=================================

System requirements
-------------------
- Windows 10 or Windows 11, 64-bit
- USB ports and the Windows drivers required by your Marlin and ESP boards

Start
-----
1. Extract the complete ZIP file to a writable local folder.
2. Double-click "FSL Auto Test.exe".
3. Select the Marlin and ESP serial ports, then click Connect.

Python and Python libraries do not need to be installed. The portable folder
contains the Python 3.11 runtime, Tcl/Tk, pyserial, and all application modules.

Data location
-------------
The default output folder is "output" next to the EXE. Test results, generated
G-code, raw serial logs, charts, and offline-analysis files are written there.

Notes
-----
- Keep the EXE and the _internal folder together.
- Do not run the EXE directly from inside the ZIP file.
- Windows SmartScreen may warn about an unsigned application. Use a trusted
  local copy of this release.
- USB-to-serial hardware drivers are Windows device drivers and are not bundled.

Version: 2026.08.17
Architecture: Windows x64
