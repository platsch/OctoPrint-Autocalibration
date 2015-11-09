# OctoPrint-Autocalibration

This plugin calibrates your printers [backlash](https://en.wikipedia.org/wiki/Backlash_%28engineering%29) for the X, Y or Z-axis.

## How does it work?

Make sure your printer is running and connected to OctoPrint before you start the calibration process. The axis moves to home to find the endstop and then slowly away from the endstop to find the point where the backlash is compensated by the moving pulley. Do not interrupt the process, otherwise the backlash would remain 0 regardless of the original value.

## Requirements and Pitfalls

* The Firmware must be Repetier based with active EEPROM-option.
* If the printer has multiple extruders with offset configured in the firmware, the home-position is usually not directly at the endstop. You must set all extruder offsets to 0 before running the calibration. This might be improved in coming versions.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

  pip install https://github.com/platsch/OctoPrint-Autocalibration/archive/master.zip


This work is based on the [OctoPrint-EEprom-Repetier](https://github.com/Salandora/OctoPrint-EEPROM-Repetier) plugin by Salandora.
