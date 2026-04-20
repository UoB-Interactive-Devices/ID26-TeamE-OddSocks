# Bangle.js 2 Software Reference - Espruino

Toggle navigation [Espruino](/)

-   [Get Espruino](#)
    -   [🇬🇧 Espruino Shop](https://shop.espruino.com)
    -   [🌎 Distributors](/Order)
    -   [Download firmware](/Download)
-   [Donate](/Donate)
-   [Documentation](#)
    -   [Quick Start](/Quick+Start)
    
    -   [API Reference](/Reference#software)
    -   [Tutorials & Examples](/Tutorials)
    -   [Modules](/Modules)
    -   [Tips & Tricks](/Tips+and+Tricks)
    -   [Videos](https://www.youtube.com/user/espruino)
    
    -   [Bangle.js 2](/Bangle.js2)
    -   [Bangle.js 1](/Bangle.js)
    -   [Pixl.js](/Pixl.js)
    -   [Puck.js](/Puck.js)
    -   [Jolt.js](/Jolt.js)
    -   [Espruino WiFi](/WiFi)
    -   [Espruino Pico](/Pico)
    -   [Original Espruino](/Original)
    -   [MDBT42Q Module](/MDBT42Q)
    
    -   [Other Boards](/Other+Boards)
-   [Support](#)
    -   [Forums](http://forum.espruino.com)
    
    -   [Getting Started](/Quick+Start)
    -   [FAQ](/FAQ)
    -   [Troubleshooting](/Troubleshooting)
    
    -   [Bangle.js App Loader](https://banglejs.com/apps/)
    -   [Espruino.js App Loader](/apps)
    
    -   [Espruino for Business](/Business)
    -   [Contact Us](/Contact+Us)
    -   [Press Info](/Press)

    [![](/images/socialtiny_facebook.png)](http://www.facebook.com/sharer.php?u=http://www.espruino.com&t=Espruino+JavaScript+for+Microcontrollers "Share on Facebook") [![](/images/socialtiny_twitter.png)](http://twitter.com/Espruino "Follow us on Twitter") [![Espruino on LinkedIn](/images/socialtiny_linkedin.png)](https://www.linkedin.com/company/espruino "Espruino on LinkedIn") [![YouTube](/images/youtube_tinyw.png)](https://www.youtube.com/user/espruino "YouTube")

# Bangle.js 2 Software Reference

![](img/BANGLEJS2_thumb.jpg)

This is a software reference containing only the functionality available in [Bangle.js 2](Bangle.js2). For a reference showing all available functionality, [click here](Reference).

Version 2v29

## Contents

-   [Globals](#_global)
-   [AES](#AES)
-   [Array](#Array)
-   [ArrayBuffer](#ArrayBuffer)
-   [ArrayBufferView](#ArrayBufferView)
-   [Bangle](#Bangle)
-   [BluetoothDevice](#BluetoothDevice)
-   [BluetoothGATTServer](#BluetoothGATTServer)
-   [BluetoothRemoteGATTCharacteristic](#BluetoothRemoteGATTCharacteristic)
-   [BluetoothRemoteGATTServer](#BluetoothRemoteGATTServer)
-   [BluetoothRemoteGATTService](#BluetoothRemoteGATTService)
-   [Boolean](#Boolean)
-   [console](#console)
-   [crypto](#crypto)
-   [DataView](#DataView)
-   [Date](#Date)
-   [E](#E)
-   [Error](#Error)
-   [Flash](#Flash)
-   [Float32Array](#Float32Array)
-   [Float64Array](#Float64Array)
-   [fs](#fs)
-   [Function](#Function)
-   [Graphics](#Graphics)
-   [heatshrink](#heatshrink)
-   [I2C](#I2C)
-   [Int16Array](#Int16Array)
-   [Int32Array](#Int32Array)
-   [Int8Array](#Int8Array)
-   [InternalError](#InternalError)
-   [JSON](#JSON)
-   [Math](#Math)
-   [Modules](#Modules)
-   [NRF](#NRF)
-   [Number](#Number)
-   [Object](#Object)
-   [OneWire](#OneWire)
-   [Pin](#Pin)
-   [process](#process)
-   [Promise](#Promise)
-   [ReferenceError](#ReferenceError)
-   [RegExp](#RegExp)
-   [Serial](#Serial)
-   [SPI](#SPI)
-   [Storage](#Storage)
-   [StorageFile](#StorageFile)
-   [String](#String)
-   [SyntaxError](#SyntaxError)
-   [tensorflow](#tensorflow)
-   [TFMicroInterpreter](#TFMicroInterpreter)
-   [timer](#timer)
-   [TypeError](#TypeError)
-   [Uint16Array](#Uint16Array)
-   [Uint24Array](#Uint24Array)
-   [Uint32Array](#Uint32Array)
-   [Uint8Array](#Uint8Array)
-   [Uint8ClampedArray](#Uint8ClampedArray)
-   [Unistroke](#Unistroke)
-   [Waveform](#Waveform)

## [Globals](#t__global)

[(top)](javascript:toppos\(\);)

#### Methods and Fields

-   [variable \_\_FILE\_\_](#l__global___FILE__)
-   [function analogRead(pin)](#l__global_analogRead)
-   [function analogWrite(pin, value, options)](#l__global_analogWrite)
-   [variable arguments](#l__global_arguments)
-   [function atob(base64Data)](#l__global_atob)
-   [Bluetooth](#l__global_Bluetooth)
-   [variable BTN](#l__global_BTN)
-   [variable BTN1](#l__global_BTN1)
-   [function btoa(binaryData)](#l__global_btoa)
-   [function changeInterval(id, time)](#l__global_changeInterval)
-   [function clearInterval(id, ...)](#l__global_clearInterval)
-   [function clearTimeout(id, ...)](#l__global_clearTimeout)
-   [function clearWatch(id, ...)](#l__global_clearWatch)
-   [function decodeURIComponent(str)](#l__global_decodeURIComponent)
-   [function digitalPulse(pin, value, time)](#l__global_digitalPulse)
-   [function digitalRead(pin)](#l__global_digitalRead)
-   [function digitalWrite(pin, value)](#l__global_digitalWrite)
-   [function dump()](#l__global_dump)
-   [function echo(echoOn)](#l__global_echo)
-   [function edit(funcName)](#l__global_edit)
-   [function encodeURIComponent(str)](#l__global_encodeURIComponent)
-   [function eval(code)](#l__global_eval)
-   [function getPinMode(pin)](#l__global_getPinMode)
-   [function getSerial()](#l__global_getSerial)
-   [function getTime()](#l__global_getTime)
-   [variable global](#l__global_global)
-   [variable globalThis](#l__global_globalThis)
-   [variable HIGH](#l__global_HIGH)
-   [I2C1](#l__global_I2C1)
-   [variable Infinity](#l__global_Infinity)
-   [function isFinite(x)](#l__global_isFinite)
-   [function isNaN(x)](#l__global_isNaN)
-   [function load(filename)](#l__global_load)
-   [LoopbackA](#l__global_LoopbackA)
-   [LoopbackB](#l__global_LoopbackB)
-   [variable LOW](#l__global_LOW)
-   [variable NaN](#l__global_NaN)
-   [function parseFloat(string)](#l__global_parseFloat)
-   [function parseInt(string, radix)](#l__global_parseInt)
-   [function peek16(addr, count)](#l__global_peek16)
-   [function peek32(addr, count)](#l__global_peek32)
-   [function peek8(addr, count)](#l__global_peek8)
-   [function pinMode(pin, mode, automatic)](#l__global_pinMode)
-   [function poke16(addr, value)](#l__global_poke16)
-   [function poke32(addr, value)](#l__global_poke32)
-   [function poke8(addr, value)](#l__global_poke8)
-   [function print(text, ...)](#l__global_print)
-   [function require(moduleName)](#l__global_require)
-   [function reset(clearFlash)](#l__global_reset)
-   [Serial1](#l__global_Serial1)
-   [Serial2](#l__global_Serial2)
-   [function setBusyIndicator(pin)](#l__global_setBusyIndicator)
-   [function setInterval(function, timeout, args, ...)](#l__global_setInterval)
-   [function setSleepIndicator(pin)](#l__global_setSleepIndicator)
-   [function setTime(time)](#l__global_setTime)
-   [function setTimeout(function, timeout, args, ...)](#l__global_setTimeout)
-   [function setWatch(function, pin, options)](#l__global_setWatch)
-   [function shiftOut(pins, options, data)](#l__global_shiftOut)
-   [SPI1](#l__global_SPI1)
-   [SWDCON](#l__global_SWDCON)
-   [Terminal](#l__global_Terminal)
-   [function trace(root)](#l__global_trace)
-   [variable VIBRATE](#l__global_VIBRATE)

### [variable \_\_FILE\_\_](#t_l__global___FILE__) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L29 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable __FILE__`

#### Returns

The filename of the JavaScript that is currently executing

#### Description

The filename of the JavaScript that is currently executing.

If `[load](#l__global_load)` has been called with a filename (eg `load("myfile.js")`) then `[__FILE__](#l__global___FILE__)` is set to that filename. Otherwise (eg `[load()](#l__global_load)`) or immediately after booting, `[__FILE__](#l__global___FILE__)` is not set.

### [function analogRead](#t_l__global_analogRead) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L168 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function analogRead(pin)`

#### Parameters

`pin` - The pin to use  
You can find out which pins to use by looking at [your board's reference page](#boards) and searching for pins with the `ADC` markers.

#### Returns

The analog value of the `[Pin](#Pin)` between 0(GND) and 1(VCC). See below.

#### Description

Get the analogue value of the given pin.

-   The value is normally greater than or equal to 0, however in some cases nRF52-based boards can produce values less than 0 when the ADC voltage is slightly less than the chip's internal GND.
-   The value returned will always be _less_ than 1, even when the ADC reads full range. For example a 12 bit ADC may return 4095 as a full-range value, but this is divided by 4096 to produce `[analogRead](#l__global_analogRead)`'s output value.

This is different to Arduino which only returns an integer between 0 and 1023

However only pins connected to an ADC will work (see the datasheet)

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset pin's state to `"analog"`

**Note:** [Jolt.js](https://www.espruino.com/Jolt.js) motor driver pins with analog inputs are scaled with a potential divider, and so those pins return a number which is the actual voltage.

### [function analogWrite](#t_l__global_analogWrite) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L194 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function analogWrite(pin, value, options)`

#### Parameters

`pin` - The pin to use  
You can find out which pins to use by looking at [your board's reference page](#boards) and searching for pins with the `PWM` or `DAC` markers.

`value` - A value between 0 and 1

`options` - An object containing options for analog output - see below

#### Description

Set the analog Value of a pin. It will be output using PWM.

Objects can contain:

-   `freq` - pulse frequency in Hz, e.g. `analogWrite(A0,0.5,{ freq : 10 });` - specifying a frequency will force PWM output, even if the pin has a DAC
-   `soft` - boolean, If true software PWM is used if hardware is not available.
-   `forceSoft` - boolean, If true software PWM is used even if hardware PWM or a DAC is available

On nRF52-based devices (Puck.js, Pixl.js, MDBT42Q, etc) hardware PWM runs at 16MHz, with a maximum output frequency of 4MHz (but with only 2 bit (0..3) accuracy). At 1Mhz, you have 4 bits (0..15), 1kHz = 14 bits and so on.

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset pin's state to `"output"`

### [variable arguments](#t_l__global_arguments) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L52 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable arguments`

#### Returns

An array containing all the arguments given to the function

#### Description

A variable containing the arguments given to the function:

```

function hello() {
  console.log(arguments.length, JSON.stringify(arguments));
}
hello()        // 0 []
hello("Test")  // 1 ["Test"]
hello(1,2,3)   // 3 [1,2,3]
```

**Note:** Due to the way Espruino works this is doesn't behave exactly the same as in normal JavaScript. The length of the arguments array will never be less than the number of arguments specified in the function declaration: `(function(a){ return arguments.length; })() == 1`. Normal JavaScript interpreters would return `0` in the above case.

### [function atob](#t_l__global_atob) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L373 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function atob(base64Data)`

#### Parameters

`base64Data` - A string of base64 data to decode

#### Returns

A string containing the decoded data

#### Description

Decode the supplied base64 string into a normal string

**Note:** This is not available in devices with low flash memory

### [Bluetooth](#t_l__global_Bluetooth) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L711 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`Serial`](#Serial)

#### Description

The Bluetooth Serial port - used when data is sent or received over Bluetooth Smart on nRF51/nRF52 chips.

**Note:** This is only available in devices with Bluetooth LE capability

### [variable BTN](#t_l__global_BTN)

[(top)](javascript:toppos\(\);)

#### Call type:

`variable BTN`

#### Returns

Button 1

### [variable BTN1](#t_l__global_BTN1)

[(top)](javascript:toppos\(\);)

#### Call type:

`variable BTN1`

#### Returns

BTN1

### [function btoa](#t_l__global_btoa) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L315 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function btoa(binaryData)`

#### Parameters

`binaryData` - A string of data to encode

#### Returns

A base64 encoded string

#### Description

Encode the supplied string (or array) into a base64 string

**Note:** This is not available in devices with low flash memory

### [function changeInterval](#t_l__global_changeInterval) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L590 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function changeInterval(id, time)`

#### Parameters

`id` - The id returned by a previous call to setInterval

`time` - The new time period in ms

#### Description

Change the Interval on a callback created with `[setInterval](#l__global_setInterval)`, for example:

`var id = setInterval(function () { print('foo'); }, 1000); // every second`

`changeInterval(id, 1500); // now runs every 1.5 seconds`

This takes effect immediately and resets the timeout, so in the example above, regardless of when you call `[changeInterval](#l__global_changeInterval)`, the next interval will occur 1500ms after it.

### [function clearInterval](#t_l__global_clearInterval) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L515 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function clearInterval(id, ...)`

#### Parameters

`id, ...` - The id returned by a previous call to setInterval. **Only one argument is allowed.**

#### Description

Clear the Interval that was created with `[setInterval](#l__global_setInterval)`, for example:

`var id = setInterval(function () { print('foo'); }, 1000);`

`clearInterval(id);`

If no argument is supplied, all timeouts and intervals are stopped.

To avoid accidentally deleting all Intervals, if a parameter is supplied but is `undefined` then an Exception will be thrown.

### [function clearTimeout](#t_l__global_clearTimeout) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L534 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function clearTimeout(id, ...)`

#### Parameters

`id, ...` - The id returned by a previous call to setTimeout. **Only one argument is allowed.**

#### Description

Clear the Timeout that was created with `[setTimeout](#l__global_setTimeout)`, for example:

`var id = setTimeout(function () { print('foo'); }, 1000);`

`clearTimeout(id);`

If no argument is supplied, all timeouts and intervals are stopped.

To avoid accidentally deleting all Timeouts, if a parameter is supplied but is `undefined` then an Exception will be thrown.

### [function clearWatch](#t_l__global_clearWatch) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L866 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function clearWatch(id, ...)`

#### Parameters

`id, ...` - The id returned by a previous call to setWatch. **Only one argument is allowed.** (or pass nothing to clear all watches)

#### Description

Clear the Watch that was created with setWatch. If no parameter is supplied, all watches will be removed.

To avoid accidentally deleting all Watches, if a parameter is supplied but is `undefined` then an Exception will be thrown.

### [function decodeURIComponent](#t_l__global_decodeURIComponent) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L490 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function decodeURIComponent(str)`

#### Parameters

`str` - A string to decode from a URI

#### Returns

A string containing the decoded data

#### Description

Convert any groups of characters of the form '%ZZ', into characters with hex code '0xZZ'

**Note:** This is not available in devices with low flash memory

### [function digitalPulse](#t_l__global_digitalPulse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L236 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function digitalPulse(pin, value, time)`

#### Parameters

`pin` - The pin to use

`value` - Whether to pulse high (true) or low (false)

`time` - A time in milliseconds, or an array of times (in which case a square wave will be output starting with a pulse of 'value')

#### Description

Pulse the pin with the value for the given time in milliseconds. It uses a hardware timer to produce accurate pulses, and returns immediately (before the pulse has finished). Use `[digitalPulse(A0,1,0)](#l__global_digitalPulse)` to wait until a previous pulse has finished.

e.g. `digitalPulse(A0,1,5);` pulses A0 high for 5ms. `digitalPulse(A0,1,[5,2,4]);` pulses A0 high for 5ms, low for 2ms, and high for 4ms

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset pin's state to `"output"`

digitalPulse is for SHORT pulses that need to be very accurate. If you're doing anything over a few milliseconds, use setTimeout instead.

### [function digitalRead](#t_l__global_digitalRead) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L376 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function digitalRead(pin)`

#### Parameters

`pin` - The pin to use

#### Returns

The digital Value of the Pin

#### Description

Get the digital value of the given pin.

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset pin's state to `"input"`

If the pin argument is an array of pins (e.g. `[A2,A1,A0]`) the value returned will be an number where the last array element is the least significant bit, for example if `A0=A1=1` and `A2=0`, `digitalRead([A2,A1,A0]) == 0b011`

If the pin argument is an object with a `read` method, the `read` method will be called and the integer value it returns passed back.

### [function digitalWrite](#t_l__global_digitalWrite) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L305 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function digitalWrite(pin, value)`

#### Parameters

`pin` - The pin to use

`value` - Whether to write a high (true) or low (false) value

#### Description

Set the digital value of the given pin.

```

digitalWrite(LED1, 1); // light LED1
digitalWrite([LED1,LED2,LED3], 0b101); // lights LED1 and LED3
```

**Note:** if you didn't call `pinMode(pin, ...)` or `[Pin.mode(...)](#l_Pin_mode)` beforehand then this function will also reset pin's state to `"output"`

If pin argument is an array of pins (e.g. `[A2,A1,A0]`) the value argument will be treated as an array of bits where the last array element is the least significant bit.

In this case, pin values are set least significant bit first (from the right-hand side of the array of pins). This means you can use the same pin multiple times, for example `digitalWrite([A1,A1,A0,A0],0b0101)` would pulse A0 followed by A1.

In 2v22 and later firmwares, using a boolean for the value will set _all_ pins in the array to the same value, eg `digitalWrite(pins, value?0xFFFFFFFF:0)`. Previously digitalWrite with a boolean behaved like `digitalWrite(pins, value?1:0)` and would only set the first pin.

If the pin argument is an object with a `write` method, the `write` method will be called with the value passed through.

### [function dump](#t_l__global_dump) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L104 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function dump()`

#### Description

Output current interpreter state in a text form such that it can be copied to a new device

Espruino keeps its current state in RAM (even if the function code is stored in Flash). When you type `[dump()](#l__global_dump)` it dumps the current state of code in RAM plus the hardware state, then if there's code saved in flash it writes "// Code saved with E.setBootCode" and dumps that too.

**Note:** 'Internal' functions are currently not handled correctly. You will need to recreate these in the `onInit` function.

**Note:** This is not available in devices with low flash memory

### [function echo](#t_l__global_echo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L298 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function echo(echoOn)`

#### Parameters

`echoOn` -

#### Description

Should Espruino echo what you type back to you? true = yes (Default), false = no. When echo is off, the result of executing a command is not returned. Instead, you must use 'print' to send output.

### [function edit](#t_l__global_edit) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L230 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function edit(funcName)`

#### Parameters

`funcName` - The name of the function to edit (either a string or just the unquoted name)

#### Description

Fill the console with the contents of the given function, so you can edit it.

NOTE: This is a convenience function - it will not edit 'inner functions'. For that, you must edit the 'outer function' and re-execute it.

**Note:** This is not available in devices with low flash memory

### [function encodeURIComponent](#t_l__global_encodeURIComponent) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L441 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function encodeURIComponent(str)`

#### Parameters

`str` - A string to encode as a URI

#### Returns

A string containing the encoded data

#### Description

Convert a string with any character not alphanumeric or `- _ . ! ~ * ' ( )` converted to the form `%XY` where `XY` is its hexadecimal representation

**Note:** This is not available in devices with low flash memory

### [function eval](#t_l__global_eval) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L152 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function eval(code)`

#### Parameters

`code` -

#### Returns

The result of evaluating the string

#### Description

Evaluate a string containing JavaScript code

### [function getPinMode](#t_l__global_getPinMode) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L508 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function getPinMode(pin)`

#### Parameters

`pin` - The pin to check

#### Returns

The pin mode, as a string

#### Description

Return the current mode of the given pin. See `[pinMode](#l__global_pinMode)` for more information on returned values.

**Note:** This is not available in devices with low flash memory

### [function getSerial](#t_l__global_getSerial) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L361 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function getSerial()`

#### Returns

The board's serial number

#### Description

Get the serial number of this board

**Note:** This is not available in devices with low flash memory

### [function getTime](#t_l__global_getTime) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L317 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function getTime()`

#### Returns

See description above

#### Description

Return the current system time in Seconds (as a floating point number)

### [variable global](#t_l__global_global) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L29 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable global`

#### Returns

The global scope

#### Description

A reference to the global scope, where everything is defined.

`[global](#l__global_global)` is used in Node.js. Later on the ECMAScript spec introduced `[globalThis](#l__global_globalThis)` which is available in-browser too.

### [variable globalThis](#t_l__global_globalThis) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L39 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable globalThis`

#### Returns

The global scope

#### Description

A reference to the global scope, where everything is defined.

This is identical to `[global](#l__global_global)` but was introduced in the ECMAScript spec.

### [variable HIGH](#t_l__global_HIGH) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L144 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable HIGH`

#### Returns

Logic 1 for Arduino compatibility - this is the same as just typing `1`

#### Description

**DEPRECATED** - this will be removed in subsequent versions of Espruino

**Note:** This is not available in devices with low flash memory

### [I2C1](#t_l__global_I2C1) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L550 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`I2C`](#I2C)

#### Description

The first I2C port

**Note:** This is only available in devices with more than 1 ESPR\_I2C peripherals

### [variable Infinity](#t_l__global_Infinity) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L77 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable Infinity`

#### Returns

Positive Infinity (1/0)

#### Description

### [function isFinite](#t_l__global_isFinite) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L245 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function isFinite(x)`

#### Parameters

`x` -

#### Returns

True is the value is a Finite number, false if not.

#### Description

Is the parameter a finite number or not? If needed, the parameter is first converted to a number.

### [function isNaN](#t_l__global_isNaN) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L262 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function isNaN(x)`

#### Parameters

`x` -

#### Returns

True is the value is NaN, false if not.

#### Description

Whether the x is NaN (Not a Number) or not

### [function load](#t_l__global_load) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L121 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function load(filename)`

#### Parameters

`filename` - \[optional\] The name of a text JS file to load from Storage after reset

#### Description

Restart and load the program out of flash - this has an effect similar to completely rebooting Espruino (power off/power on), but without actually performing a full reset of the hardware.

This command only executes when the Interpreter returns to the Idle state - for instance `a=1;load();a=2;` will still leave 'a' as undefined (or what it was set to in the saved program).

Espruino will resume from where it was when you last typed `save()`. If you want code to be executed right after loading (for instance to initialise devices connected to Espruino), add an `init` event handler to `[E](#E)` with

```
E.on('init',
function() { ... your_code ... });
```

. This will then be automatically executed by Espruino every time it starts.

**If you specify a filename in the argument then that file will be loaded from Storage after reset** in much the same way as calling `[reset()](#l__global_reset)` then `eval(require("Storage").read(filename))`

### [LoopbackA](#t_l__global_LoopbackA) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L179 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`Serial`](#Serial)

#### Description

A loopback serial device. Data sent to `[LoopbackA](#l__global_LoopbackA)` comes out of `[LoopbackB](#l__global_LoopbackB)` and vice versa

### [LoopbackB](#t_l__global_LoopbackB) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L187 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`Serial`](#Serial)

#### Description

A loopback serial device. Data sent to `[LoopbackA](#l__global_LoopbackA)` comes out of `[LoopbackB](#l__global_LoopbackB)` and vice versa

### [variable LOW](#t_l__global_LOW) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L154 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable LOW`

#### Returns

Logic 0 for Arduino compatibility - this is the same as just typing `0`

#### Description

**DEPRECATED** - this will be removed in subsequent versions of Espruino

**Note:** This is not available in devices with low flash memory

### [variable NaN](#t_l__global_NaN) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L70 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable NaN`

#### Returns

Not a Number

#### Description

### [function parseFloat](#t_l__global_parseFloat) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L217 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function parseFloat(string)`

#### Parameters

`string` -

#### Returns

The value of the string

#### Description

Convert a string representing a number into an float

### [function parseInt](#t_l__global_parseInt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L171 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function parseInt(string, radix)`

#### Parameters

`string` -

`radix` - \[optional\] The Radix of the string

#### Returns

The integer value of the string (or NaN)

#### Description

Convert a string representing a number into an integer

### [function peek16](#t_l__global_peek16) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L56 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function peek16(addr, count)`

#### Parameters

`addr` - The address in memory to read

`count` - \[optional\] the number of items to read. If >1 a `[Uint16Array](#Uint16Array)` will be returned.

#### Returns

The value of memory at the given location

#### Description

Read 16 bits of memory at the given location - DANGEROUS!

### [function peek32](#t_l__global_peek32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L84 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function peek32(addr, count)`

#### Parameters

`addr` - The address in memory to read

`count` - \[optional\] the number of items to read. If >1 a `[Uint32Array](#Uint32Array)` will be returned.

#### Returns

The value of memory at the given location

#### Description

Read 32 bits of memory at the given location - DANGEROUS!

### [function peek8](#t_l__global_peek8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L28 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function peek8(addr, count)`

#### Parameters

`addr` - The address in memory to read

`count` - \[optional\] the number of items to read. If >1 a `[Uint8Array](#Uint8Array)` will be returned.

#### Returns

The value of memory at the given location

#### Description

Read 8 bits of memory at the given location - DANGEROUS!

### [function pinMode](#t_l__global_pinMode) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L441 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function pinMode(pin, mode, automatic)`

#### Parameters

`pin` - The pin to set pin mode for

`mode` - The mode - a string that is either 'analog', 'input', 'input_pullup', 'input_pulldown', 'output', 'opendrain', 'af_output' or 'af_opendrain'. Do not include this argument or use 'auto' if you want to revert to automatic pin mode setting.

`automatic` - Optional, default is false. If true, subsequent commands will automatically change the state (see notes below)

#### Description

Set the mode of the given pin.

-   `auto`/`undefined` - Don't change state, but allow `[digitalWrite](#l__global_digitalWrite)`/etc to automatically change state as appropriate
-   `analog` - Analog input
-   `input` - Digital input
-   `input_pullup` - Digital input with internal ~40k pull-up resistor
-   `input_pulldown` - Digital input with internal ~40k pull-down resistor
-   `output` - Digital output
-   `opendrain` - Digital output that only ever pulls down to 0v. Sending a logical `1` leaves the pin open circuit
-   `opendrain_pullup` - Digital output that pulls down to 0v. Sending a logical `1` enables internal ~40k pull-up resistor
-   `af_output` - Digital output from built-in peripheral
-   `af_opendrain` - Digital output from built-in peripheral that only ever pulls down to 0v. Sending a logical `1` leaves the pin open circuit
    
    **Note:** `[digitalRead](#l__global_digitalRead)`/`[digitalWrite](#l__global_digitalWrite)`/etc set the pin mode automatically _unless_ `[pinMode](#l__global_pinMode)` has been called first. If you want `[digitalRead](#l__global_digitalRead)`/etc to set the pin mode automatically after you have called `[pinMode](#l__global_pinMode)`, simply call it again with no mode argument (`[pinMode(pin)](#l__global_pinMode)`), `auto` as the argument (
    
    ```
    pinMode(pin,
    "auto")
    ```
    
    ), or with the 3rd 'automatic' argument set to true (
    
    ```
    pinMode(pin,
    "output", true)
    ```
    
    ).
    

### [function poke16](#t_l__global_poke16) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L72 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function poke16(addr, value)`

#### Parameters

`addr` - The address in memory to write

`value` - The value to write, or an array of values

#### Description

Write 16 bits of memory at the given location - VERY DANGEROUS!

### [function poke32](#t_l__global_poke32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L100 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function poke32(addr, value)`

#### Parameters

`addr` - The address in memory to write

`value` - The value to write, or an array of values

#### Description

Write 32 bits of memory at the given location - VERY DANGEROUS!

### [function poke8](#t_l__global_poke8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L44 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function poke8(addr, value)`

#### Parameters

`addr` - The address in memory to write

`value` - The value to write, or an array of values

#### Description

Write 8 bits of memory at the given location - VERY DANGEROUS!

### [function print](#t_l__global_print) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L567 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function print(text, ...)`

#### Parameters

`text, ...` -

#### Description

Print the supplied string(s) to the console

**Note:_\* If you're connected to a computer (not a wall adaptor) via USB but \*_you are not running a terminal app** then when you print data Espruino may pause execution and wait until the computer requests the data it is trying to print.

### [function require](#t_l__global_require) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_modules.c#L38 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function require(moduleName)`

#### Parameters

`moduleName` - A String containing the name of the given module

#### Returns

The result of evaluating the string

#### Description

Load the given module, and return the exported functions and variables.

For example:

```

var s = require("Storage");
s.write("test", "hello world");
print(s.read("test"));
// prints "hello world"
```

Check out [the page on Modules](/Modules) for an explanation of what modules are and how you can use them.

### [function reset](#t_l__global_reset) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L200 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function reset(clearFlash)`

#### Parameters

`clearFlash` - Remove saved code from flash as well

#### Description

Reset the interpreter - clear program memory in RAM, and do not load a saved program from flash. This does NOT reset the underlying hardware (which allows you to reset the device without it disconnecting from USB).

This command only executes when the Interpreter returns to the Idle state - for instance `a=1;reset();a=2;` will still leave 'a' as undefined.

The safest way to do a full reset is to hit the reset button.

If `[reset()](#l__global_reset)` is called with no arguments, it will reset the board's state in RAM but will not reset the state in flash. When next powered on (or when `[load()](#l__global_load)` is called) the board will load the previously saved code.

Calling `[reset(true)](#l__global_reset)` will cause _all saved code in flash memory to be cleared as well_.

### [Serial1](#t_l__global_Serial1) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L130 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`Serial`](#Serial)

#### Description

The first Serial (USART) port

**Note:** This is only available in devices with more than 1 ESPR\_USART peripherals

### [Serial2](#t_l__global_Serial2) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L138 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`Serial`](#Serial)

#### Description

The second Serial (USART) port

**Note:** This is only available in devices with more than 2 ESPR\_USART peripherals

### [function setBusyIndicator](#t_l__global_setBusyIndicator) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L32 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function setBusyIndicator(pin)`

#### Parameters

`pin` -

#### Description

When Espruino is busy, set the pin specified here high. Set this to undefined to disable the feature.

**Note:** This is not available in devices with low flash memory

### [function setInterval](#t_l__global_setInterval) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L391 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function setInterval(function, timeout, args, ...)`

#### Parameters

`function` - A Function or String to be executed

`timeout` - The time between calls to the function (max 3153600000000 = 100 years

`args, ...` - Optional arguments to pass to the function when executed

#### Returns

An ID that can be passed to clearInterval

#### Description

Call the function (or evaluate the string) specified REPEATEDLY after the timeout in milliseconds.

For instance:

```

setInterval(function () {
  console.log("Hello World");
}, 1000);
// or
setInterval('console.log("Hello World");', 1000);
// both print 'Hello World' every second
```

You can also specify extra arguments that will be sent to the function when it is executed. For example:

```

setInterval(function (a,b) {
  console.log(a+" "+b);
}, 1000, "Hello", "World");
// prints 'Hello World' every second
```

If you want to stop your function from being called, pass the number that was returned by `[setInterval](#l__global_setInterval)` into the `[clearInterval](#l__global_clearInterval)` function.

**Note:** If `setDeepSleep(true)` has been called and the interval is greater than 5 seconds, Espruino may execute the interval up to 1 second late. This is because Espruino can only wake from deep sleep every second - and waking early would cause Espruino to waste power while it waited for the correct time.

### [function setSleepIndicator](#t_l__global_setSleepIndicator) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L56 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function setSleepIndicator(pin)`

#### Parameters

`pin` -

#### Description

When Espruino is asleep, set the pin specified here low (when it's awake, set it high). Set this to undefined to disable the feature.

Please see http://www.espruino.com/Power+Consumption for more details on this.

**Note:** This is not available in devices with low flash memory

### [function setTime](#t_l__global_setTime) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L326 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function setTime(time)`

#### Parameters

`time` -

#### Description

Set the current system time in seconds (`time` can be a floating point value).

This is used with `[getTime](#l__global_getTime)`, the time reported from `[setWatch](#l__global_setWatch)`, as well as when using `new Date()`.

`Date.prototype.getTime()` reports the time in milliseconds, so you can set the time to a `[Date](#Date)` object using:

```

setTime((new Date("Tue, 19 Feb 2019 10:57")).getTime()/1000)
```

To set the timezone for all new Dates, use `[E.setTimeZone(hours)](#l_E_setTimeZone)`.

### [function setTimeout](#t_l__global_setTimeout) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_interactive.c#L435 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function setTimeout(function, timeout, args, ...)`

#### Parameters

`function` - A Function or String to be executed

`timeout` - The time until the function will be executed (max 3153600000000 = 100 years

`args, ...` - Optional arguments to pass to the function when executed

#### Returns

An ID that can be passed to clearTimeout

#### Description

Call the function (or evaluate the string) specified ONCE after the timeout in milliseconds.

For instance:

```

setTimeout(function () {
  console.log("Hello World");
}, 1000);
// or
setTimeout('console.log("Hello World");', 1000);
// both print 'Hello World' after a second
```

You can also specify extra arguments that will be sent to the function when it is executed. For example:

```

setTimeout(function (a,b) {
  console.log(a+" "+b);
}, 1000, "Hello", "World");
// prints 'Hello World' after 1 second
```

If you want to stop the function from being called, pass the number that was returned by `[setTimeout](#l__global_setTimeout)` into the `[clearTimeout](#l__global_clearTimeout)` function.

**Note:** If `setDeepSleep(true)` has been called and the interval is greater than 5 seconds, Espruino may execute the interval up to 1 second late. This is because Espruino can only wake from deep sleep every second - and waking early would cause Espruino to waste power while it waited for the correct time.

### [function setWatch](#t_l__global_setWatch) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L684 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function setWatch(function, pin, options)`

#### Parameters

`function` - A Function or String to be executed

`pin` - The pin to watch

`options` - If a boolean or integer, it determines whether to call this once (false = default) or every time a change occurs (true). Can be an object of the form `{ repeat: true/false(default), edge:'rising'/'falling'/'both', debounce:10}` - see below for more information.

#### Returns

An ID that can be passed to clearWatch

#### Description

Call the function specified when the pin changes. Watches set with `[setWatch](#l__global_setWatch)` can be removed using `[clearWatch](#l__global_clearWatch)`.

If the `options` parameter is an object, it can contain the following information (all optional):

```

{
   // Whether to keep producing callbacks, or remove the watch after the first callback
   repeat: true/false(default),
   // Trigger on the rising or falling edge of the signal. Can be a string, or 1='rising', -1='falling', 0='both'
   edge:'rising'(default for built-in buttons)/'falling'/'both'(default for pins),
   // Use software-debouncing to stop multiple calls if a switch bounces
   // This is the time in milliseconds to wait for bounces to subside, or 0 to disable
   debounce:10 (0 is default for pins, 25 is default for built-in buttons),
   // Advanced: If the function supplied is a 'native' function (compiled or assembly)
   // setting irq:true will call that function in the interrupt itself
   irq : false(default)
   // Advanced: If specified, the given pin will be read whenever the watch is called
   // and the state will be included as a 'data' field in the callback (`debounce:0` is required)
   data : pin
   // Advanced: On Nordic devices, a watch may be 'high' or 'low' accuracy. By default low
   // accuracy is used (which is better for power consumption), but this means that
   // high speed pulses (less than 25us) may not be reliably received. Setting hispeed=true
   // allows for detecting high speed pulses at the expense of higher idle power consumption
   hispeed : true
}
```

The `function` callback is called with an argument, which is an object of type `{state:bool, time:float, lastTime:float}`.

-   `state` is whether the pin is currently a `1` or a `0`
-   `time` is the time in seconds at which the pin changed state
-   `lastTime` is the time in seconds at which the **pin last changed state**. When using `edge:'rising'` or `edge:'falling'`, this is not the same as when the function was last called.
-   `data` is included if `data:pin` was specified in the options, and can be used for reading in clocked data. It will only work if `debounce:0` is used

For instance, if you want to measure the length of a positive pulse you could use

```
setWatch(function(e) { console.log(e.time-e.lastTime); }, BTN, {
repeat:true, edge:'falling' });
```

. This will only be called on the falling edge of the pulse, but will be able to measure the width of the pulse because `e.lastTime` is the time of the rising edge.

Internally, an interrupt writes the time of the pin's state change into a queue with the exact time that it happened, and the function supplied to `[setWatch](#l__global_setWatch)` is executed only from the main message loop. However, if the callback is a native function `void (bool state)` then you can add `irq:true` to options, which will cause the function to be called from within the IRQ. When doing this, interrupts will happen on both edges and there will be no debouncing.

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will reset pin's state to `"input"`

**Note:** The STM32 chip (used in the [Espruino Board](/EspruinoBoard) and [Pico](/Pico)) cannot watch two pins with the same number - e.g. `A0` and `B0`.

**Note:** On nRF52 chips (used in Puck.js, Pixl.js, MDBT42Q) `[setWatch](#l__global_setWatch)` disables the GPIO output on that pin. In order to be able to write to the pin again you need to disable the watch with `[clearWatch](#l__global_clearWatch)`.

### [function shiftOut](#t_l__global_shiftOut) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_io.c#L573 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function shiftOut(pins, options, data)`

#### Parameters

`pins` - A pin, or an array of pins to use

`options` - Options, for instance the clock (see below)

`data` - The data to shift out (see `[E.toUint8Array](#l_E_toUint8Array)` for info on the forms this can take)

#### Description

Shift an array of data out using the pins supplied _least significant bit first_, for example:

```

// shift out to single clk+data
shiftOut(A0, { clk : A1 }, [1,0,1,0]);
```

```

// shift out a whole byte (like software SPI)
shiftOut(A0, { clk : A1, repeat: 8 }, [1,2,3,4]);
```

```

// shift out via 4 data pins
shiftOut([A3,A2,A1,A0], { clk : A4 }, [1,2,3,4]);
```

`options` is an object of the form:

```

{
  clk : pin, // a pin to use as the clock (undefined = no pin)
  clkPol : bool, // clock polarity - default is 0 (so 1 normally, pulsing to 0 to clock data in)
  repeat : int, // number of clocks per array item
}
```

Each item in the `data` array will be output to the pins, with the first pin in the array being the MSB and the last the LSB, then the clock will be pulsed in the polarity given.

`repeat` is the amount of times shift data out for each array item. For instance we may want to shift 8 bits out through 2 pins - in which case we need to set repeat to 4.

### [SPI1](#t_l__global_SPI1) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L31 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`SPI`](#SPI)

#### Description

The first SPI port

**Note:** This is only available in devices with more than 1 ESPR\_SPI peripherals

### [SWDCON](#t_l__global_SWDCON) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/swdcon/jswrap_swdcon.c#L73 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`Serial`](#Serial)

#### Description

In memory serial I/O device accessible via SWD debugger. Uses SEGGER RTT so it can be used with openocd and other SEGGER compatible tools.

**Note:** This is only available in USE\_SWDCON

### [Terminal](#t_l__global_Terminal) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_terminal.c#L23 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Instance of [`Serial`](#Serial)

#### Description

A simple VT100 terminal emulator.

When data is sent to the `[Terminal](#l__global_Terminal)` object, `[Graphics.getInstance()](#l_Graphics_getInstance)` is called and if an instance of `[Graphics](#Graphics)` is found then characters are written to it.

**Note:** This is only available in devices with VT100 terminal emulation enabled (Pixl.js only)

### [function trace](#t_l__global_trace) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L539 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function trace(root)`

#### Parameters

`root` - The symbol to output (optional). If nothing is specified, everything will be output

#### Description

Output debugging information

Note: This is not included on boards with low amounts of flash memory, or the Espruino board.

**Note:** This is not available in devices with low flash memory

### [variable VIBRATE](#t_l__global_VIBRATE) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L122 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`variable VIBRATE`

#### Returns

See description above

#### Description

The Bangle.js's vibration motor.

**Note:** This is only available in Bangle.js smartwatches

## [AES Class](#t_AES)

[(top)](javascript:toppos\(\);)

#### Methods and Fields

-   [AES.ccmDecrypt(message, key, iv, tag)](#l_AES_ccmDecrypt)
-   [AES.ccmEncrypt(message, key, iv, tagLen)](#l_AES_ccmEncrypt)

### [AES.ccmDecrypt](#t_l_AES_ccmDecrypt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/crypto/jswrap_crypto.c#L622 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`AES.ccmDecrypt(message, key, iv, tag)`

#### Parameters

`message` - Message to decrypt

`key` - Key to decrypt message - an `[ArrayBuffer](#ArrayBuffer)` of 128 BITS

`iv` - Nonce (initialization vector) - an `[ArrayBuffer](#ArrayBuffer)` of 7 to 13 bytes

`tag` - Tag that came with the message - an `[ArrayBuffer](#ArrayBuffer)`

#### Returns

Decrypted message, or null on error (for example if the tag doesn't match)

#### Description

Decrypt and authenticate an AES CCM encrypted message with an associated tag.

Usage example:

```

let message = "Hello World!";
let key = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff];
let nonce = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66];
let tagLength = 4;
let result = AES.ccmEncrypt(message, key, nonce, tagLength);
let decrypted = AES.ccmDecrypt(result.data, key, nonce, result.tag);
let decryptedMessage = String.fromCharCode.apply(null, decrypted);
```

The `decryptedMessage` variable should now contain "Hello World!".

**Note:** This is only available in USE_AES_CCM

### [AES.ccmEncrypt](#t_l_AES_ccmEncrypt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/crypto/jswrap_crypto.c#L583 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`AES.ccmEncrypt(message, key, iv, tagLen)`

#### Parameters

`message` - Message to encrypt

`key` - Key to encrypt message - an `[ArrayBuffer](#ArrayBuffer)` of 128 BITS

`iv` - nonce (initialization vector) - an `[ArrayBuffer](#ArrayBuffer)` of 7 to 13 bytes

`tagLen` - Length of tag to generate in bytes - must be one of 4, 6, 8, 10, 12, 14 or 16

#### Returns

An object

#### Description

Encrypt a message with a key using AES in CCM authenticated encryption mode.

This returns an object with the encrypted data and a generated tag for message authentication.

Usage example:

```

let message = "Hello World!";
let key = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff];
let nonce = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66];
let tagLength = 4;
let result = AES.ccmEncrypt(message, key, nonce, tagLength);
```

The `result` object should now have a `data` and `tag` attribute; both are needed for decrypting and verifying the message:

```

{
  data: [206, 98, 239, 219, 146, 157, 59, 123, 102, 92, 118, 209],
  tag: [230, 153, 191, 142]
}
```

**Note:** This is only available in USE_AES_CCM

## [Array Class](#t_Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for arrays.

Arrays can be defined with `[]`, `new Array()`, or

```
new
Array(length)
```

#### Methods and Fields

-   [constructor Array(args, ...)](#l_Array_Array)
-   [function Array.concat(args, ...)](#l_Array_concat)
-   [function Array.every(function, thisArg)](#l_Array_every)
-   [function Array.fill(value, start, end)](#l_Array_fill)
-   [function Array.filter(function, thisArg)](#l_Array_filter)
-   [function Array.find(function)](#l_Array_find)
-   [function Array.findIndex(function)](#l_Array_findIndex)
-   [function Array.forEach(function, thisArg)](#l_Array_forEach)
-   [function Array.includes(value, startIndex)](#l_Array_includes)
-   [function Array.indexOf(value, startIndex)](#l_Array_indexOf)
-   [Array.isArray(var)](#l_Array_isArray)
-   [function Array.join(separator)](#l_Array_join)
-   [property Array.length](#l_Array_length)
-   [function Array.map(function, thisArg)](#l_Array_map)
-   [function Array.pop()](#l_Array_pop)
-   [function Array.push(arguments, ...)](#l_Array_push)
-   [function Array.reduce(callback, initialValue)](#l_Array_reduce)
-   [function Array.reverse()](#l_Array_reverse)
-   [function Array.shift()](#l_Array_shift)
-   [function Array.slice(start, end)](#l_Array_slice)
-   [function Array.some(function, thisArg)](#l_Array_some)
-   [function Array.sort(var)](#l_Array_sort)
-   [function Array.splice(index, howMany, elements, ...)](#l_Array_splice)
-   [function Array.toString(radix)](#l_Array_toString)
-   [function Array.unshift(elements, ...)](#l_Array_unshift)

### [constructor Array](#t_l_Array_Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L36 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Array(args, ...)`

#### Parameters

`args, ...` - The length of the array OR any number of items to add to the array

#### Returns

An Array

#### Description

Create an Array. Either give it one integer argument (>=0) which is the length of the array, or any number of arguments

### [function Array.concat](#t_l_Array_concat) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L981 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/concat)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.concat(args, ...)`

#### Parameters

`args, ...` - Any items to add to the array

#### Returns

An Array

#### Description

Create a new array, containing the elements from this one and any arguments, if any argument is an array then those elements will be added.

**Note:** This is not available in devices with low flash memory

### [function Array.every](#t_l_Array_every) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L484 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.every(function, thisArg)`

#### Parameters

`function` - Function to be executed

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Returns

A boolean containing the result

#### Description

Return 'true' if the callback returns 'true' for every element in the array

**Note:** Do not modify the array you're iterating over from inside the callback (`a.every(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

### [function Array.fill](#t_l_Array_fill) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L1019 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.fill(value, start, end)`

#### Parameters

`value` - The value to fill the array with

`start` - Optional. The index to start from (or 0). If start is negative, it is treated as length+start where length is the length of the array

`end` - Optional. The index to end at (or the array length). If end is negative, it is treated as length+end.

#### Returns

This array

#### Description

Fill this array with the given value, for every index `>= start` and `< end`

**Note:** This is not available in devices with low flash memory

### [function Array.filter](#t_l_Array_filter) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L378 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.filter(function, thisArg)`

#### Parameters

`function` - Function to be executed

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Returns

An array containing the results

#### Description

Return an array which contains only those elements for which the callback function returns 'true'

**Note:** Do not modify the array you're iterating over from inside the callback (`a.filter(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

### [function Array.find](#t_l_Array_find) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L403 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.find(function)`

#### Parameters

`function` - Function to be executed

#### Returns

The array element where `function` returns `true`, or `undefined`

#### Description

Return the array element where `function` returns `true`, or `undefined` if it doesn't returns `true` for any element.

```

["Hello","There","World"].find(a=>a[0]=="T")
// returns "There"
```

**Note:** Do not modify the array you're iterating over from inside the callback (`a.find(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

**Note:** This is not available in devices with low flash memory

### [function Array.findIndex](#t_l_Array_findIndex) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L433 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.findIndex(function)`

#### Parameters

`function` - Function to be executed

#### Returns

The array element's index where `function` returns `true`, or `-1`

#### Description

Return the array element's index where `function` returns `true`, or `-1` if it doesn't returns `true` for any element.

```

["Hello","There","World"].findIndex(a=>a[0]=="T")
// returns 1
```

**Note:** Do not modify the array you're iterating over from inside the callback (`a.findIndex(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

**Note:** This is not available in devices with low flash memory

### [function Array.forEach](#t_l_Array_forEach) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L358 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.forEach(function, thisArg)`

#### Parameters

`function` - Function to be executed

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Description

Executes a provided function once per array element.

**Note:** Do not modify the array you're iterating over from inside the callback (`a.forEach(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

### [function Array.includes](#t_l_Array_includes) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L128 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.includes(value, startIndex)`

#### Parameters

`value` - The value to check for

`startIndex` - \[optional\] the index to search from, or 0 if not specified

#### Returns

`true` if the array includes the value, `false` otherwise

#### Description

Return `true` if the array includes the value, `false` otherwise

**Note:** This is not available in devices with low flash memory

### [function Array.indexOf](#t_l_Array_indexOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L107 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.indexOf(value, startIndex)`

#### Parameters

`value` - The value to check for

`startIndex` - \[optional\] the index to search from, or 0 if not specified

#### Returns

the index of the value in the array, or -1

#### Description

Return the index of the value in the array, or -1

### [Array.isArray](#t_l_Array_isArray) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L781 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray)

[(top)](javascript:toppos\(\);)

#### Call type:

`Array.isArray(var)`

#### Parameters

`var` - The variable to be tested

#### Returns

True if var is an array, false if not.

#### Description

Returns true if the provided object is an array

### [function Array.join](#t_l_Array_join) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L171 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.join(separator)`

#### Parameters

`separator` - The separator

#### Returns

A String representing the Joined array

#### Description

Join all elements of this array together into one string, using 'separator' between them. e.g. `[1,2,3].join(' ')=='1 2 3'`

### [property Array.length](#t_l_Array_length) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L96 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)

[(top)](javascript:toppos\(\);)

#### Call type:

`property Array.length`

#### Returns

The length of the array

#### Description

Find the length of the array

### [function Array.map](#t_l_Array_map) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L336 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.map(function, thisArg)`

#### Parameters

`function` - Function used to map one item to another

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Returns

An array containing the results

#### Description

Return an array which is made from the following:

```
A.map(function) =
[function(A[0]), function(A[1]), ...]
```

**Note:** Do not modify the array you're iterating over from inside the callback (`a.map(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

### [function Array.pop](#t_l_Array_pop) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L231 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.pop()`

#### Returns

The value that is popped off

#### Description

Remove and return the value on the end of this array.

This is the opposite of `[1,2,3].shift()`, which removes an element from the beginning of the array.

### [function Array.push](#t_l_Array_push) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L197 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.push(arguments, ...)`

#### Parameters

`arguments, ...` - One or more arguments to add

#### Returns

The new size of the array

#### Description

Push a new value onto the end of this array'

This is the opposite of `[1,2,3].unshift(0)`, which adds one or more elements to the beginning of the array.

### [function Array.reduce](#t_l_Array_reduce) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L505 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.reduce(callback, initialValue)`

#### Parameters

`callback` - Function used to reduce the array

`initialValue` - if specified, the initial value to pass to the function

#### Returns

The value returned by the last function called

#### Description

Execute `previousValue=initialValue` and then

```
previousValue =
callback(previousValue, currentValue, index, array)
```

for each element in the array, and finally return previousValue.

**Note:** Do not modify the array you're iterating over from inside the callback (`a.reduce(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

**Note:** This is not available in devices with low flash memory

### [function Array.reverse](#t_l_Array_reverse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L1105 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.reverse()`

#### Returns

The array, but reversed.

#### Description

Reverse all elements in this array (in place)

**Note:** This is not available in devices with low flash memory

### [function Array.shift](#t_l_Array_shift) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L668 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.shift()`

#### Parameters

#### Returns

The element that was removed

#### Description

Remove and return the first element of the array.

This is the opposite of `[1,2,3].pop()`, which takes an element off the end.

**Note:** This is not available in devices with low flash memory

### [function Array.slice](#t_l_Array_slice) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L720 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.slice(start, end)`

#### Parameters

`start` - Start index

`end` - \[optional\] End index

#### Returns

A new array

#### Description

Return a copy of a portion of this array (in a new array)

### [function Array.some](#t_l_Array_some) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L462 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.some(function, thisArg)`

#### Parameters

`function` - Function to be executed

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Returns

A boolean containing the result

#### Description

Return 'true' if the callback returns 'true' for any of the elements in the array

**Note:** Do not modify the array you're iterating over from inside the callback (`a.some(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

### [function Array.sort](#t_l_Array_sort) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L923 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.sort(var)`

#### Parameters

`var` - A function to use to compare array elements (or undefined)

#### Returns

This array object

#### Description

Do an in-place quicksort of the array

**Note:** Do not modify the array you're iterating over from inside the callback (`a.sort(()=>a.push(0))`). It will cause non-spec-compliant behaviour.

**Note:** This is not available in devices with low flash memory

### [function Array.splice](#t_l_Array_splice) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L574 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.splice(index, howMany, elements, ...)`

#### Parameters

`index` - Index at which to start changing the array. If negative, will begin that many elements from the end

`howMany` - An integer indicating the number of old array elements to remove. If howMany is 0, no elements are removed.

`elements, ...` - One or more items to add to the array

#### Returns

An array containing the removed elements. If only one element is removed, an array of one element is returned.

#### Description

Both remove and add items to an array

### [function Array.toString](#t_l_Array_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L82 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toString)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.toString(radix)`

#### Parameters

`radix` - unused

#### Returns

A String representing the array

#### Description

Convert the Array to a string

### [function Array.unshift](#t_l_Array_unshift) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_array.c#L695 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Array.unshift(elements, ...)`

#### Parameters

`elements, ...` - One or more items to add to the beginning of the array

#### Returns

The new array length

#### Description

Add one or more items to the start of the array, and return its new length.

This is the opposite of `[1,2,3].push(4)`, which puts one or more elements on the end.

**Note:** This is not available in devices with low flash memory

## [ArrayBuffer Class](#t_ArrayBuffer)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for array buffers.

If you want to access arrays of differing types of data you may also find `[DataView](#DataView)` useful.

#### Methods and Fields

-   [constructor ArrayBuffer(byteLength)](#l_ArrayBuffer_ArrayBuffer)
-   [property ArrayBuffer.byteLength](#l_ArrayBuffer_byteLength)

### [constructor ArrayBuffer](#t_l_ArrayBuffer_ArrayBuffer) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L226 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)

[(top)](javascript:toppos\(\);)

#### Call type:

`new ArrayBuffer(byteLength)`

#### Parameters

`byteLength` - The length in Bytes

#### Returns

An ArrayBuffer object

#### Description

Create an Array Buffer object

### [property ArrayBuffer.byteLength](#t_l_ArrayBuffer_byteLength) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L263 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer/byteLength)

[(top)](javascript:toppos\(\);)

#### Call type:

`property ArrayBuffer.byteLength`

#### Returns

The Length in bytes

#### Description

The length, in bytes, of the `[ArrayBuffer](#ArrayBuffer)`

## [ArrayBufferView Class](#t_ArrayBufferView)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class that is the prototype for:

-   [Uint8Array](/Reference#Uint8Array)
-   [UintClamped8Array](/Reference#UintClamped8Array)
-   [Int8Array](/Reference#Int8Array)
-   [Uint16Array](/Reference#Uint16Array)
-   [Int16Array](/Reference#Int16Array)
-   [Uint24Array](/Reference#Uint24Array) (Espruino-specific - not standard JS)
-   [Uint32Array](/Reference#Uint32Array)
-   [Int32Array](/Reference#Int32Array)
-   [Float32Array](/Reference#Float32Array)
-   [Float64Array](/Reference#Float64Array)

If you want to access arrays of differing types of data you may also find `[DataView](#DataView)` useful.

#### Methods and Fields

-   [property ArrayBufferView.buffer](#l_ArrayBufferView_buffer)
-   [property ArrayBufferView.byteLength](#l_ArrayBufferView_byteLength)
-   [property ArrayBufferView.byteOffset](#l_ArrayBufferView_byteOffset)
-   [function ArrayBufferView.every(function, thisArg)](#l_ArrayBufferView_every)
-   [function ArrayBufferView.fill(value, start, end)](#l_ArrayBufferView_fill)
-   [function ArrayBufferView.filter(function, thisArg)](#l_ArrayBufferView_filter)
-   [function ArrayBufferView.find(function)](#l_ArrayBufferView_find)
-   [function ArrayBufferView.findIndex(function)](#l_ArrayBufferView_findIndex)
-   [function ArrayBufferView.forEach(function, thisArg)](#l_ArrayBufferView_forEach)
-   [function ArrayBufferView.includes(value, startIndex)](#l_ArrayBufferView_includes)
-   [function ArrayBufferView.indexOf(value, startIndex)](#l_ArrayBufferView_indexOf)
-   [function ArrayBufferView.join(separator)](#l_ArrayBufferView_join)
-   [function ArrayBufferView.map(function, thisArg)](#l_ArrayBufferView_map)
-   [function ArrayBufferView.reduce(callback, initialValue)](#l_ArrayBufferView_reduce)
-   [function ArrayBufferView.reverse()](#l_ArrayBufferView_reverse)
-   [function ArrayBufferView.set(arr, offset)](#l_ArrayBufferView_set)
-   [function ArrayBufferView.slice(start, end)](#l_ArrayBufferView_slice)
-   [function ArrayBufferView.some(function, thisArg)](#l_ArrayBufferView_some)
-   [function ArrayBufferView.sort(var)](#l_ArrayBufferView_sort)
-   [function ArrayBufferView.subarray(begin, end)](#l_ArrayBufferView_subarray)

### [property ArrayBufferView.buffer](#t_l_ArrayBufferView_buffer) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L575 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property ArrayBufferView.buffer`

#### Returns

An ArrayBuffer object

#### Description

The buffer this view references

### [property ArrayBufferView.byteLength](#t_l_ArrayBufferView_byteLength) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L586 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property ArrayBufferView.byteLength`

#### Returns

The Length

#### Description

The length, in bytes, of the `[ArrayBufferView](#ArrayBufferView)`

### [property ArrayBufferView.byteOffset](#t_l_ArrayBufferView_byteOffset) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L596 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property ArrayBufferView.byteOffset`

#### Returns

The byte Offset

#### Description

The offset, in bytes, to the first byte of the view within the backing `[ArrayBuffer](#ArrayBuffer)`

### [function ArrayBufferView.every](#t_l_ArrayBufferView_every) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L1035 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.every(function, thisArg)`

#### Parameters

`function` - Function to be executed

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Returns

A boolean containing the result

#### Description

Return 'true' if the callback returns 'true' for every element in the array

### [function ArrayBufferView.fill](#t_l_ArrayBufferView_fill) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L927 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.fill(value, start, end)`

#### Parameters

`value` - The value to fill the array with

`start` - Optional. The index to start from (or 0). If start is negative, it is treated as length+start where length is the length of the array

`end` - Optional. The index to end at (or the array length). If end is negative, it is treated as length+end.

#### Returns

This array

#### Description

Fill this array with the given value, for every index `>= start` and `< end`

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.filter](#t_l_ArrayBufferView_filter) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L944 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.filter(function, thisArg)`

#### Parameters

`function` - Function to be executed

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Returns

An array containing the results

#### Description

Return an array which contains only those elements for which the callback function returns 'true'

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.find](#t_l_ArrayBufferView_find) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L960 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.find(function)`

#### Parameters

`function` - Function to be executed

#### Returns

The array element where `function` returns `true`, or `undefined`

#### Description

Return the array element where `function` returns `true`, or `undefined` if it doesn't returns `true` for any element.

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.findIndex](#t_l_ArrayBufferView_findIndex) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L975 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.findIndex(function)`

#### Parameters

`function` - Function to be executed

#### Returns

The array element's index where `function` returns `true`, or `-1`

#### Description

Return the array element's index where `function` returns `true`, or `-1` if it doesn't returns `true` for any element.

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.forEach](#t_l_ArrayBufferView_forEach) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L897 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.forEach(function, thisArg)`

#### Parameters

`function` - Function to be executed

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Description

Executes a provided function once per array element.

### [function ArrayBufferView.includes](#t_l_ArrayBufferView_includes) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L829 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.includes(value, startIndex)`

#### Parameters

`value` - The value to check for

`startIndex` - \[optional\] the index to search from, or 0 if not specified

#### Returns

`true` if the array includes the value, `false` otherwise

#### Description

Return `true` if the array includes the value, `false` otherwise

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.indexOf](#t_l_ArrayBufferView_indexOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L793 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.indexOf(value, startIndex)`

#### Parameters

`value` - The value to check for

`startIndex` - \[optional\] the index to search from, or 0 if not specified

#### Returns

the index of the value in the array, or -1

#### Description

Return the index of the value in the array, or `-1`

### [function ArrayBufferView.join](#t_l_ArrayBufferView_join) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L844 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.join(separator)`

#### Parameters

`separator` - The separator

#### Returns

A String representing the Joined array

#### Description

Join all elements of this array together into one string, using 'separator' between them. e.g. `[1,2,3].join(' ')=='1 2 3'`

### [function ArrayBufferView.map](#t_l_ArrayBufferView_map) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L670 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.map(function, thisArg)`

#### Parameters

`function` - Function used to map one item to another

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Returns

An array containing the results

#### Description

Return an array which is made from the following:

```
A.map(function) =
[function(A[0]), function(A[1]), ...]
```

**Note:** This returns an `[ArrayBuffer](#ArrayBuffer)` of the same type it was called on. To get an `[Array](#Array)`, use `[Array.map](#l_Array_map)`, e.g. `[].map.call(myArray, x=>x+1)`

### [function ArrayBufferView.reduce](#t_l_ArrayBufferView_reduce) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L910 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.reduce(callback, initialValue)`

#### Parameters

`callback` - Function used to reduce the array

`initialValue` - if specified, the initial value to pass to the function

#### Returns

The value returned by the last function called

#### Description

Execute `previousValue=initialValue` and then

```
previousValue =
callback(previousValue, currentValue, index, array)
```

for each element in the array, and finally return previousValue.

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.reverse](#t_l_ArrayBufferView_reverse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L990 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.reverse()`

#### Returns

This array

#### Description

Reverse the contents of this `[ArrayBufferView](#ArrayBufferView)` in-place

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.set](#t_l_ArrayBufferView_set) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L608 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.set(arr, offset)`

#### Parameters

`arr` - Floating point index to access

`offset` - \[optional\] The offset in this array at which to write the values

#### Description

Copy the contents of `array` into this one, mapping `this[x+offset]=array[x];`

### [function ArrayBufferView.slice](#t_l_ArrayBufferView_slice) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L1002 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.slice(start, end)`

#### Parameters

`start` - Start index

`end` - \[optional\] End index

#### Returns

A new array

#### Description

Return a copy of a portion of this array (in a new array).

**Note:** This currently returns a normal `[Array](#Array)`, not an `[ArrayBuffer](#ArrayBuffer)`

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.some](#t_l_ArrayBufferView_some) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L1021 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.some(function, thisArg)`

#### Parameters

`function` - Function to be executed

`thisArg` - \[optional\] If specified, the function is called with 'this' set to thisArg

#### Returns

A boolean containing the result

#### Description

Return 'true' if the callback returns 'true' for any of the elements in thearray

### [function ArrayBufferView.sort](#t_l_ArrayBufferView_sort) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L858 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.sort(var)`

#### Parameters

`var` - A function to use to compare array elements (or undefined)

#### Returns

This array object

#### Description

Do an in-place quicksort of the array

**Note:** This is not available in devices with low flash memory

### [function ArrayBufferView.subarray](#t_l_ArrayBufferView_subarray) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L740 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ArrayBufferView.subarray(begin, end)`

#### Parameters

`begin` - Element to begin at, inclusive. If negative, this is from the end of the array. The entire array is included if this isn't specified

`end` - Element to end at, exclusive. If negative, it is relative to the end of the array. If not specified the whole array is included

#### Returns

An `[ArrayBufferView](#ArrayBufferView)` of the same type as this one, referencing the same data

#### Description

Returns a smaller part of this array which references the same data (it doesn't copy it).

**Note:** This is not available in devices with low flash memory

## [Bangle Class](#t_Bangle)

[(top)](javascript:toppos\(\);)

Class containing utility functions for the [Bangle.js Smart Watch](http://www.espruino.com/Bangle.js)

#### Methods and Fields

-   [event Bangle.accel(xyz)](#l_Bangle_accel)
-   [Bangle.accelRd(reg, cnt)](#l_Bangle_accelRd)
-   [Bangle.accelWr(reg, data)](#l_Bangle_accelWr)
-   [event Bangle.aiGesture(gesture, weights)](#l_Bangle_aiGesture)
-   [Bangle.appRect](#l_Bangle_appRect)
-   [event Bangle.backlight(on)](#l_Bangle_backlight)
-   [Bangle.barometerRd(reg, cnt)](#l_Bangle_barometerRd)
-   [Bangle.barometerWr(reg, data)](#l_Bangle_barometerWr)
-   [Bangle.beep(time, freq)](#l_Bangle_beep)
-   [Bangle.buzz(time, strength)](#l_Bangle_buzz)
-   [event Bangle.charging(charging)](#l_Bangle_charging)
-   [Bangle.compassRd(reg, cnt)](#l_Bangle_compassRd)
-   [Bangle.compassWr(reg, data)](#l_Bangle_compassWr)
-   [Bangle.dbg()](#l_Bangle_dbg)
-   [event Bangle.drag(event)](#l_Bangle_drag)
-   [Bangle.drawWidgets()](#l_Bangle_drawWidgets)
-   [event Bangle.faceUp(up)](#l_Bangle_faceUp)
-   [Bangle.factoryReset(noReboot)](#l_Bangle_factoryReset)
-   [event Bangle.gesture(xyz)](#l_Bangle_gesture)
-   [Bangle.getAccel()](#l_Bangle_getAccel)
-   [Bangle.getCompass()](#l_Bangle_getCompass)
-   [Bangle.getGPSFix()](#l_Bangle_getGPSFix)
-   [Bangle.getHealthStatus(range)](#l_Bangle_getHealthStatus)
-   [Bangle.getLCDMode()](#l_Bangle_getLCDMode)
-   [Bangle.getLogo()](#l_Bangle_getLogo)
-   [Bangle.getOptions()](#l_Bangle_getOptions)
-   [Bangle.getPressure()](#l_Bangle_getPressure)
-   [Bangle.getStepCount()](#l_Bangle_getStepCount)
-   [event Bangle.GPS(fix)](#l_Bangle_GPS)
-   [event Bangle.GPS-raw(nmea, dataLoss)](#l_Bangle_GPS-raw)
-   [event Bangle.health(info)](#l_Bangle_health)
-   [event Bangle.HRM(hrm)](#l_Bangle_HRM)
-   [event Bangle.HRM-env(env)](#l_Bangle_HRM-env)
-   [event Bangle.HRM-raw(hrm)](#l_Bangle_HRM-raw)
-   [Bangle.hrmRd(reg, cnt)](#l_Bangle_hrmRd)
-   [Bangle.hrmWr(reg, data)](#l_Bangle_hrmWr)
-   [Bangle.isBacklightOn()](#l_Bangle_isBacklightOn)
-   [Bangle.isBarometerOn()](#l_Bangle_isBarometerOn)
-   [Bangle.isCharging()](#l_Bangle_isCharging)
-   [Bangle.isCompassOn()](#l_Bangle_isCompassOn)
-   [Bangle.isGPSOn()](#l_Bangle_isGPSOn)
-   [Bangle.isHRMOn()](#l_Bangle_isHRMOn)
-   [Bangle.isLCDOn()](#l_Bangle_isLCDOn)
-   [Bangle.isLocked()](#l_Bangle_isLocked)
-   [event Bangle.lcdPower(on)](#l_Bangle_lcdPower)
-   [Bangle.lcdWr(cmd, data)](#l_Bangle_lcdWr)
-   [Bangle.load(file)](#l_Bangle_load)
-   [Bangle.loadWidgets()](#l_Bangle_loadWidgets)
-   [event Bangle.lock(on, reason)](#l_Bangle_lock)
-   [event Bangle.mag(xyz)](#l_Bangle_mag)
-   [event Bangle.midnight()](#l_Bangle_midnight)
-   [Bangle.off()](#l_Bangle_off)
-   [event Bangle.pressure(e)](#l_Bangle_pressure)
-   [Bangle.project(latlong)](#l_Bangle_project)
-   [Bangle.resetCompass()](#l_Bangle_resetCompass)
-   [Bangle.setBacklight(isOn)](#l_Bangle_setBacklight)
-   [Bangle.setBarometerPower(isOn, appID)](#l_Bangle_setBarometerPower)
-   [Bangle.setCompassPower(isOn, appID)](#l_Bangle_setCompassPower)
-   [Bangle.setGPSPower(isOn, appID)](#l_Bangle_setGPSPower)
-   [Bangle.setHRMPower(isOn, appID)](#l_Bangle_setHRMPower)
-   [Bangle.setLCDBrightness(brightness)](#l_Bangle_setLCDBrightness)
-   [Bangle.setLCDMode(mode)](#l_Bangle_setLCDMode)
-   [Bangle.setLCDOffset(y)](#l_Bangle_setLCDOffset)
-   [Bangle.setLCDOverlay(img, x, y, options)](#l_Bangle_setLCDOverlay)
-   [Bangle.setLCDPower(isOn)](#l_Bangle_setLCDPower)
-   [Bangle.setLCDTimeout(isOn)](#l_Bangle_setLCDTimeout)
-   [Bangle.setLocked(isLocked)](#l_Bangle_setLocked)
-   [Bangle.setOptions(options)](#l_Bangle_setOptions)
-   [Bangle.setPollInterval(interval)](#l_Bangle_setPollInterval)
-   [Bangle.setStepCount(count)](#l_Bangle_setStepCount)
-   [Bangle.setUI(type, callback)](#l_Bangle_setUI)
-   [Bangle.showClock()](#l_Bangle_showClock)
-   [Bangle.showLauncher()](#l_Bangle_showLauncher)
-   [Bangle.showLoadingScreen()](#l_Bangle_showLoadingScreen)
-   [Bangle.showRecoveryMenu()](#l_Bangle_showRecoveryMenu)
-   [Bangle.showTestScreen()](#l_Bangle_showTestScreen)
-   [Bangle.softOff()](#l_Bangle_softOff)
-   [event Bangle.step(up)](#l_Bangle_step)
-   [event Bangle.stroke(event)](#l_Bangle_stroke)
-   [event Bangle.swipe(directionLR, directionUD)](#l_Bangle_swipe)
-   [event Bangle.tap(data)](#l_Bangle_tap)
-   [event Bangle.touch(button, xy)](#l_Bangle_touch)
-   [Bangle.touchRd(reg, cnt)](#l_Bangle_touchRd)
-   [Bangle.touchWr(reg, data)](#l_Bangle_touchWr)
-   [event Bangle.twist()](#l_Bangle_twist)

### [event Bangle.accel](#t_l_Bangle_accel) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L141 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('accel', function(xyz) { ... });`

#### Parameters

`xyz` -

#### Description

Accelerometer data available with `{x,y,z,diff,mag}` object as a parameter.

-   `x` is X axis (left-right) in `g`
-   `y` is Y axis (up-down) in `g`
-   `z` is Z axis (in-out) in `g`
-   `diff` is difference between this and the last reading in `g`
-   `mag` is the magnitude of the acceleration in `g`

You can also retrieve the most recent reading with `[Bangle.getAccel()](#l_Bangle_getAccel)`.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.accelRd](#t_l_Bangle_accelRd) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L4990 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.accelRd(reg, cnt)`

#### Parameters

`reg` -

`cnt` - If specified, returns a `[Uint8Array](#Uint8Array)` of the given length (max 128). If `undefined` (or 0) it returns a number

#### Returns

See description above

#### Description

Reads a register from the accelerometer

**Note:** On Espruino 2v06 and before this function only returns a number (`cnt` is ignored).

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.accelWr](#t_l_Bangle_accelWr) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L4971 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.accelWr(reg, data)`

#### Parameters

`reg` - Register number to write

`data` - An integer value to write to the register

#### Description

Writes a register on the accelerometer

**Note:** This is only available in Bangle.js 2 smartwatches

### [event Bangle.aiGesture](#t_l_Bangle_aiGesture) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L453 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('aiGesture', function(gesture, weights) { ... });`

#### Parameters

`gesture` - The name of the gesture (if '.tfnames' exists, or the index. 'undefined' if not matching

`weights` - An array of floating point values output by the model

#### Description

Emitted when a 'gesture' (fast movement) is detected, and a Tensorflow model is in storage in the `".tfmodel"` file.

If a `".tfnames"` file is specified as a comma-separated list of names, it will be used to decode `gesture` from a number into a string.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.appRect](#t_l_Bangle_appRect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6481 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.appRect`

#### Returns

An object of the form `{x,y,w,h,x2,y2}`

#### Description

Returns the rectangle on the screen that is currently reserved for the app.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.backlight](#t_l_Bangle_backlight) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L395 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('backlight', function(on) { ... });`

#### Parameters

`on` - `true` if backlight is on

#### Description

Has the backlight been turned on or off? Can be used to stop tasks that are no longer useful if want to see in sun screen only. Also see `[Bangle.isBacklightOn()](#l_Bangle_isBacklightOn)`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.barometerRd](#t_l_Bangle_barometerRd) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5041 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.barometerRd(reg, cnt)`

#### Parameters

`reg` -

`cnt` - If specified, returns an array of the given length (max 128). If not (or 0) it returns a number

#### Returns

See description above

#### Description

Reads a register from the barometer IC

**Note:** This is only available in DTNO1\_F5 and Bangle.js 2 smartwatches and DICKENS

### [Bangle.barometerWr](#t_l_Bangle_barometerWr) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5022 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.barometerWr(reg, data)`

#### Parameters

`reg` -

`data` -

#### Description

Writes a register on the barometer IC

**Note:** This is only available in DTNO1\_F5 and Bangle.js 2 smartwatches and DICKENS

### [Bangle.beep](#t_l_Bangle_beep) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5434 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.beep(time, freq)`

#### Parameters

`time` - \[optional\] Time in ms (default 200)

`freq` - \[optional\] Frequency in hz (default 4000)

#### Returns

A promise, completed when beep is finished

#### Description

Use the piezo speaker to Beep for a certain time period and frequency

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.buzz](#t_l_Bangle_buzz) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5496 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.buzz(time, strength)`

#### Parameters

`time` - \[optional\] Time in ms (default 200)

`strength` - \[optional\] Power of vibration from 0 to 1 (Default 1)

#### Returns

A promise, completed when vibration is finished

#### Description

Use the vibration motor to buzz for a certain time period

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.charging](#t_l_Bangle_charging) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L207 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('charging', function(charging) { ... });`

#### Parameters

`charging` - `true` if charging

#### Description

Is the battery charging or not?

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.compassRd](#t_l_Bangle_compassRd) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5087 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.compassRd(reg, cnt)`

#### Parameters

`reg` -

`cnt` - If specified, returns an array of the given length (max 128). If not (or 0) it returns a number

#### Returns

See description above

#### Description

Read a register on the Magnetometer/Compass

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.compassWr](#t_l_Bangle_compassWr) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5068 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.compassWr(reg, data)`

#### Parameters

`reg` -

`data` -

#### Description

Writes a register on the Magnetometer/Compass

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.dbg](#t_l_Bangle_dbg) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L4861 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.dbg()`

#### Returns

See description above

#### Description

Reads debug info. Exposes the current values of `accHistoryIdx`, `accGestureCount`, `accIdleCount`, `pollInterval` and others.

Please see the declaration of this function for more information (click the `==>` link above [this description](http://www.espruino.com/Reference#l_Bangle_dbg))

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.drag](#t_l_Bangle_drag) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L512 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('drag', function(event) { ... });`

#### Parameters

`event` - Object of form `{x,y,dx,dy,b}` containing touch coordinates, difference in touch coordinates, and an integer `b` containing number of touch points (currently 1 or 0)

#### Description

Emitted when the touchscreen is dragged or released

The touchscreen extends past the edge of the screen and while `x` and `y` coordinates are arranged such that they align with the LCD's pixels, if your finger goes towards the edge of the screen, `x` and `y` could end up larger than 175 (the screen's maximum pixel coordinates) or smaller than 0. Coordinates from the `touch` event are clipped.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.drawWidgets](#t_l_Bangle_drawWidgets) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5864 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.drawWidgets()`

#### Description

Draw any onscreen widgets that were loaded with `[Bangle.loadWidgets()](#l_Bangle_loadWidgets)`.

Widgets should redraw themselves when something changes - you'll only need to call drawWidgets if you decide to clear the entire screen with `g.clear()`.

**Note:** This is only available in Bangle.js smartwatches

**Note:** This is only available in Bangle.js smartwatches with Bangle.js 2 smartwatches

### [event Bangle.faceUp](#t_l_Bangle_faceUp) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L187 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('faceUp', function(up) { ... });`

#### Parameters

`up` - `true` if face-up

#### Description

Has the watch been moved so that it is face-up, or not face up?

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.factoryReset](#t_l_Bangle_factoryReset) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6412 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.factoryReset(noReboot)`

#### Parameters

`noReboot` - Do not reboot the watch when done (default false, so will reboot)

#### Description

Erase all storage and reload it with the default contents. As of 2v29 it will also remove any pairing data from flash memory.

This is only available on Bangle.js 2.0. On Bangle.js 1.0 you need to use `Install Default Apps` under the `More...` tab of http://banglejs.com/apps

**Note:** This is only available in Bangle.js 2 smartwatches and EMULATED and DICKENS

### [event Bangle.gesture](#t_l_Bangle_gesture) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L443 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('gesture', function(xyz) { ... });`

#### Parameters

`xyz` - An Int8Array of XYZXYZXYZ data

#### Description

Emitted when a 'gesture' (fast movement) is detected

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.getAccel](#t_l_Bangle_getAccel) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3565 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getAccel()`

#### Returns

An object containing accelerometer readings (as below)

#### Description

Get the most recent accelerometer reading. Data is in the same format as the `Bangle.on('accel',` event.

-   `x` is X axis (left-right) in `g`
-   `y` is Y axis (up-down) in `g`
-   `z` is Z axis (in-out) in `g`
-   `diff` is difference between this and the last reading in `g` (calculated by comparing vectors, not magnitudes)
-   `td` is the elapsed
-   `mag` is the magnitude of the acceleration in `g`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.getCompass](#t_l_Bangle_getCompass) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3511 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getCompass()`

#### Returns

An object containing magnetometer readings (as below)

#### Description

Get the most recent Magnetometer/Compass reading. Data is in the same format as the `Bangle.on('mag',` event.

Returns an `{x,y,z,dx,dy,dz,heading}` object

-   `x/y/z` raw x,y,z magnetometer readings
-   `dx/dy/dz` readings based on calibration since magnetometer turned on
-   `heading` in degrees based on calibrated readings (will be NaN if magnetometer hasn't been rotated around 360 degrees).

**Note:** In 2v15 firmware and earlier the heading is inverted (360-heading). There's a fix in the bootloader which will apply a fix for those headings, but old apps may still expect an inverted value.

To get this event you must turn the compass on with `[Bangle.setCompassPower(1)](#l_Bangle_setCompassPower)`.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.getGPSFix](#t_l_Bangle_getGPSFix) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3220 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getGPSFix()`

#### Returns

A GPS fix object with `{lat,lon,...}`

#### Description

Get the last available GPS fix info (or `undefined` if GPS is off).

The fix info received is the same as you'd get from the `[Bangle.GPS](#l_Bangle_GPS)` event.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.getHealthStatus](#t_l_Bangle_getHealthStatus) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3597 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getHealthStatus(range)`

#### Parameters

`range` - What time period to return data for, see below:

#### Returns

Returns an object containing various health info

#### Description

`range` is one of:

-   `undefined` or `'10min'` - health data so far in this 10 minute block (eg. 9:00.00 - 9:09.59)
-   `'last'` - health data during the last 10 minute block
-   `'day'` - the health data so far for the day

`getHealthStatus` returns an object containing:

-   `movement` is the 32 bit sum of all `acc.diff` readings since power on (and rolls over). It is the difference in accelerometer values as `g*8192`
-   `steps` is the number of steps during this period
-   `bpm` the best BPM reading from HRM sensor during this period
-   `bpmConfidence` best BPM confidence (0-100%) during this period
-   `bpmMin`/`bpmMax` (2v26+) the minimum/maximum BPM reading from HRM sensor during this period (where confidence is over 90)
-   `activity` (2v26+) the currently assumed activity, one of "UNKNOWN","NOT\_WORN","WALKING","EXERCISE"

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.getLCDMode](#t_l_Bangle_getLCDMode) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2419 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getLCDMode()`

#### Returns

The LCD mode as a String

#### Description

The current LCD mode.

See `[Bangle.setLCDMode](#l_Bangle_setLCDMode)` for examples.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.getLogo](#t_l_Bangle_getLogo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5693 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getLogo()`

#### Returns

An image to be used with `g.drawImage` (as a String)

#### Description

-   On platforms with an LCD of >=8bpp this is 222 x 104 x 2 bits
-   Otherwise it's 119 x 56 x 1 bits

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.getOptions](#t_l_Bangle_getOptions) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2885 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getOptions()`

#### Returns

The current state of all options

#### Description

Return the current state of options as set by `[Bangle.setOptions](#l_Bangle_setOptions)`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.getPressure](#t_l_Bangle_getPressure) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5184 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getPressure()`

#### Returns

A promise that will be resolved with `{temperature, pressure, altitude}`

#### Description

Read temperature, pressure and altitude data. A promise is returned which will be resolved with `{temperature (C), pressure (hPa), altitude (meters)}`.

If the Barometer has been turned on with `[Bangle.setBarometerPower](#l_Bangle_setBarometerPower)` then this will return with the _next_ reading as of 2v21 (or the existing reading on 2v20 or earlier). If the Barometer is off, conversions take between 500-750ms.

Altitude assumes a sea-level pressure of 1013.25 hPa, but this cal be adjusted with a call to `Bangle.setOptions({ seaLevelPressure : 1013.25 })` - the Bangle.js Settings app contains a tool to adjust it.

If there's no pressure device (for example, the emulator), this returns `undefined`, rather than a Promise.

```

Bangle.getPressure().then(d=>{
  console.log(d);
  // {temperature, pressure, altitude}
});
```

**Note:** This is only available in DTNO1\_F5 and Bangle.js 2 smartwatches and DICKENS

### [Bangle.getStepCount](#t_l_Bangle_getStepCount) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3481 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.getStepCount()`

#### Returns

The number of steps recorded by the step counter

#### Description

Returns the current amount of steps recorded by the step counter

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.GPS](#t_l_Bangle_GPS) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L279 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('GPS', function(fix) { ... });`

#### Parameters

`fix` - An object with fix info (see below)

#### Description

GPS data, as an object. Contains:

```

{ "lat": number,      // Latitude in degrees
  "lon": number,      // Longitude in degrees
  "alt": number,      // altitude in M
  "speed": number,    // Speed in kph
  "course": number,   // Course in degrees
  "time": Date,       // Current Time (or undefined if not known)
  "satellites": 7,    // Number of satellites
  "fix": 1            // NMEA Fix state - 0 is no fix
  "hdop": number,     // Horizontal Dilution of Precision
}
```

If a value such as `lat` is not known because there is no fix, it'll be `[NaN](#l__global_NaN)`.

`hdop` is a value from the GPS receiver that gives a rough idea of accuracy of lat/lon based on the geometry of the satellites in range. Multiply by 5 to get a value in meters. This is just a ballpark estimation and should not be considered remotely accurate.

To get this event you must turn the GPS on with `[Bangle.setGPSPower(1)](#l_Bangle_setGPSPower)`.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.GPS-raw](#t_l_Bangle_GPS-raw) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L251 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('GPS-raw', function(nmea, dataLoss) { ... });`

#### Parameters

`nmea` - A string containing the raw NMEA data from the GPS

`dataLoss` - This is set to true if some lines of GPS data have previously been lost (eg because system was too busy to queue up a GPS-raw event)

#### Description

Raw NMEA GPS / u-blox data messages received as a string

To get this event you must turn the GPS on with `[Bangle.setGPSPower(1)](#l_Bangle_setGPSPower)`.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.health](#t_l_Bangle_health) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L176 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('health', function(info) { ... });`

#### Parameters

`info` - An object containing the last 10 minutes health data

#### Description

See `[Bangle.getHealthStatus()](#l_Bangle_getHealthStatus)` for more information. This is used for health tracking to allow Bangle.js to record historical exercise data.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.HRM](#t_l_Bangle_HRM) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L311 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('HRM', function(hrm) { ... });`

#### Parameters

`hrm` - An object with heart rate info (see below)

#### Description

Heat rate data, as an object. Contains:

```

{ "bpm": number,             // Beats per minute
  "confidence": number,      // 0-100 percentage confidence in the heart rate
  "raw": Uint8Array,         // raw samples from heart rate monitor
}
```

To get this event you must turn the heart rate monitor on with `[Bangle.setHRMPower(1)](#l_Bangle_setHRMPower)`.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.HRM-env](#t_l_Bangle_HRM-env) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L351 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('HRM-env', function(env) { ... });`

#### Parameters

`env` - An integer containing current environment reading (light level)

#### Description

Called when an environment sample heart rate sensor data is available (this is the amount of light received by the HRM sensor from the environment when its LED is off). On the newest VC31B based watches this is only 4 bit (0..15).

To get it you need to turn the HRM on with `[Bangle.setHRMPower(1)](#l_Bangle_setHRMPower)` and also set `Bangle.setOptions({hrmPushEnv:true})`.

It is also possible to poke registers with `[Bangle.hrmWr](#l_Bangle_hrmWr)` to increase the poll rate if needed. See https://banglejs.com/apps/?id=flashcount for an example of this.

**Note:** This is only available in Bangle.js 2 smartwatches

### [event Bangle.HRM-raw](#t_l_Bangle_HRM-raw) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L331 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('HRM-raw', function(hrm) { ... });`

#### Parameters

`hrm` - A object containing instant readings from the heart rate sensor

#### Description

Called when heart rate sensor data is available - see `[Bangle.setHRMPower(1)](#l_Bangle_setHRMPower)`.

`hrm` is of the form:

```

{ "raw": -1,       // raw value from sensor
  "filt": -1,      // bandpass-filtered raw value from sensor
  "bpm": 88.9,     // last BPM value measured
  "confidence": 0  // confidence in the BPM value
}
```

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.hrmRd](#t_l_Bangle_hrmRd) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5132 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.hrmRd(reg, cnt)`

#### Parameters

`reg` -

`cnt` - If specified, returns an array of the given length (max 128). If not (or 0) it returns a number

#### Returns

See description above

#### Description

Read a register on the Heart rate monitor

**Note:** This is only available in Bangle.js 2 smartwatches

### [Bangle.hrmWr](#t_l_Bangle_hrmWr) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5113 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.hrmWr(reg, data)`

#### Parameters

`reg` -

`data` -

#### Description

Writes a register on the Heart rate monitor

**Note:** This is only available in Bangle.js 2 smartwatches

### [Bangle.isBacklightOn](#t_l_Bangle_isBacklightOn) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2917 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.isBacklightOn()`

#### Returns

Is the backlight on or not?

#### Description

Also see the `[Bangle.backlight](#l_Bangle_backlight)` event

You can use `Bangle.setLCDPowerBacklight` to turn on the LCD backlight.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.isBarometerOn](#t_l_Bangle_isBarometerOn) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3464 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.isBarometerOn()`

#### Returns

Is the Barometer on?

#### Description

Is the Barometer powered?

Set power with `Bangle.setBarometerPower(...);`

**Note:** This is only available in DTNO1\_F5 and Bangle.js 2 smartwatches and DICKENS

### [Bangle.isCharging](#t_l_Bangle_isCharging) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2996 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.isCharging()`

#### Returns

Is the battery charging or not?

#### Description

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.isCompassOn](#t_l_Bangle_isCompassOn) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3323 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.isCompassOn()`

#### Returns

Is the Compass on?

#### Description

Is the compass powered?

Set power with `Bangle.setCompassPower(...);`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.isGPSOn](#t_l_Bangle_isGPSOn) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3203 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.isGPSOn()`

#### Returns

Is the GPS on?

#### Description

Is the GPS powered?

Set power with `Bangle.setGPSPower(...);`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.isHRMOn](#t_l_Bangle_isHRMOn) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3124 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.isHRMOn()`

#### Returns

Is HRM on?

#### Description

Is the Heart rate monitor powered?

Set power with `Bangle.setHRMPower(...);`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.isLCDOn](#t_l_Bangle_isLCDOn) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2900 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.isLCDOn()`

#### Returns

Is the display on or not?

#### Description

Also see the `[Bangle.lcdPower](#l_Bangle_lcdPower)` event

You can use `[Bangle.setLCDPower](#l_Bangle_setLCDPower)` to turn on the LCD (on Bangle.js 2 the LCD is normally on, and draws very little power so can be left on).

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.isLocked](#t_l_Bangle_isLocked) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2981 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.isLocked()`

#### Returns

Is the screen locked or not?

#### Description

Also see the `[Bangle.lock](#l_Bangle_lock)` event

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.lcdPower](#t_l_Bangle_lcdPower) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L385 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('lcdPower', function(on) { ... });`

#### Parameters

`on` - `true` if screen is on

#### Description

Has the screen been turned on or off? Can be used to stop tasks that are no longer useful if nothing is displayed. Also see `[Bangle.isLCDOn()](#l_Bangle_isLCDOn)`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.lcdWr](#t_l_Bangle_lcdWr) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3055 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.lcdWr(cmd, data)`

#### Parameters

`cmd` -

`data` -

#### Description

Writes a command directly to the ST7735 LCD controller

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.load](#t_l_Bangle_load) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5927 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.load(file)`

#### Parameters

`file` - \[optional\] A string containing the file name for the app to be loaded

#### Description

This behaves the same as the global `[load()](#l__global_load)` function, but if fast loading is possible (`[Bangle.setUI](#l_Bangle_setUI)` was called with a `remove` handler) then instead of a complete reload, the `remove` handler will be called and the new app will be loaded straight after with `[eval](#l__global_eval)`.

**This should only be used if the app being loaded also uses widgets** (eg it contains a `[Bangle.loadWidgets()](#l_Bangle_loadWidgets)` call).

`[load()](#l__global_load)` is slower, but safer. As such, care should be taken when using `[Bangle.load()](#l_Bangle_load)` with `Bangle.setUI({..., remove:...})` as if your remove handler doesn't completely clean up after your app, memory leaks or other issues could occur - see `[Bangle.setUI](#l_Bangle_setUI)` for more information.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.loadWidgets](#t_l_Bangle_loadWidgets) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5839 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.loadWidgets()`

#### Description

Load all widgets from flash Storage. Call this once at the beginning of your application if you want any on-screen widgets to be loaded.

They will be loaded into a global `WIDGETS` array, and can be rendered with `[Bangle.drawWidgets](#l_Bangle_drawWidgets)`.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.lock](#t_l_Bangle_lock) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L405 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('lock', function(on, reason) { ... });`

#### Parameters

`on` - `true` if screen is locked, `false` if it is unlocked and touchscreen/buttons will work

`reason` - (2v20 onwards) If known, the reason for locking/unlocking - 'button','js','tap','doubleTap','faceUp','twist','timeout'

#### Description

Has the screen been locked? Also see `[Bangle.isLocked()](#l_Bangle_isLocked)`

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.mag](#t_l_Bangle_mag) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L227 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('mag', function(xyz) { ... });`

#### Parameters

`xyz` -

#### Description

Magnetometer/Compass data available with `{x,y,z,dx,dy,dz,heading}` object as a parameter

-   `x/y/z` raw x,y,z magnetometer readings
-   `dx/dy/dz` readings based on calibration since magnetometer turned on
-   `heading` in degrees based on calibrated readings (will be NaN if magnetometer hasn't been rotated around 360 degrees).

**Note:** In 2v15 firmware and earlier the heading is inverted (360-heading). There's a fix in the bootloader which will apply a fix for those headings, but old apps may still expect an inverted value.

To get this event you must turn the compass on with `[Bangle.setCompassPower(1)](#l_Bangle_setCompassPower)`.

You can also retrieve the most recent reading with `[Bangle.getCompass()](#l_Bangle_getCompass)`.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.midnight](#t_l_Bangle_midnight) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L561 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('midnight', function() { ... });`

#### Description

Emitted at midnight (at the point the `day` health info is reset to 0).

Can be used for housekeeping tasks that don't want to be run during the day.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.off](#t_l_Bangle_off) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5628 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.off()`

#### Description

Turn Bangle.js off. It can only be woken by pressing BTN1.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.pressure](#t_l_Bangle_pressure) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L372 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('pressure', function(e) { ... });`

#### Parameters

`e` - An object containing `{temperature,pressure,altitude}`

#### Description

When `[Bangle.setBarometerPower(true)](#l_Bangle_setBarometerPower)` is called, this event is fired containing barometer readings.

Same format as `[Bangle.getPressure()](#l_Bangle_getPressure)`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.project](#t_l_Bangle_project) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5382 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.project(latlong)`

#### Parameters

`latlong` - `{lat:..., lon:...}`

#### Returns

{x:..., y:...}

#### Description

Perform a Spherical [Web Mercator projection](https://en.wikipedia.org/wiki/Web_Mercator_projection) of latitude and longitude into `x` and `y` coordinates, which are roughly equivalent to meters from `{lat:0,lon:0}`.

This is the formula used for most online mapping and is a good way to compare GPS coordinates to work out the distance between them.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.resetCompass](#t_l_Bangle_resetCompass) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3340 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.resetCompass()`

#### Parameters

#### Description

Resets the compass minimum/maximum values. Can be used if the compass isn't providing a reliable heading any more.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setBacklight](#t_l_Bangle_setBacklight) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2132 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setBacklight(isOn)`

#### Parameters

`isOn` - True if the LCD backlight should be on, false if not

#### Description

This function can be used to turn Bangle.js's LCD backlight off or on.

This function resets the Bangle's 'activity timer' (like pressing a button or the screen would) so after a time period of inactivity set by `Bangle.setOptions({backlightTimeout: X});` the backlight will turn off.

If you want to keep the backlight on permanently (until apps are changed) you can do:

```

Bangle.setOptions({backlightTimeout: 0}) // turn off the timeout
Bangle.setBacklight(1); // keep screen on
```

Of course, the backlight depends on `[Bangle.setLCDPower](#l_Bangle_setLCDPower)` too, so any lcdPowerTimeout/setLCDTimeout will also turn the backlight off. The use case is when you require the backlight timeout to be shorter than the power timeout.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setBarometerPower](#t_l_Bangle_setBarometerPower) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3365 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setBarometerPower(isOn, appID)`

#### Parameters

`isOn` - True if the barometer IC should be on, false if not

`appID` - A string with the app's name in, used to ensure one app can't turn off something another app is using

#### Returns

Is the Barometer on?

#### Description

Set the power to the barometer IC. Once enabled, `[Bangle.pressure](#l_Bangle_pressure)` events are fired each time a new barometer reading is available.

When on, the barometer draws roughly 50uA

**Note:** This is only available in DTNO1\_F5 and Bangle.js 2 smartwatches and DICKENS

### [Bangle.setCompassPower](#t_l_Bangle_setCompassPower) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3242 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setCompassPower(isOn, appID)`

#### Parameters

`isOn` - True if the Compass should be on, false if not

`appID` - A string with the app's name in, used to ensure one app can't turn off something another app is using

#### Returns

Is the Compass on?

#### Description

Set the power to the Compass

When on, data is output via the `mag` event on `[Bangle](#Bangle)`:

```

Bangle.setCompassPower(true, "myapp");
Bangle.on('mag',print);
```

_When on, the compass draws roughly 2mA_

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setGPSPower](#t_l_Bangle_setGPSPower) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3152 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setGPSPower(isOn, appID)`

#### Parameters

`isOn` - True if the GPS should be on, false if not

`appID` - A string with the app's name in, used to ensure one app can't turn off something another app is using

#### Returns

Is the GPS on?

#### Description

Set the power to the GPS.

When on, data is output via the `GPS` event on `[Bangle](#Bangle)`:

```

Bangle.setGPSPower(true, "myapp");
Bangle.on('GPS',print);
```

_When on, the GPS draws roughly 20mA_

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setHRMPower](#t_l_Bangle_setHRMPower) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3079 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setHRMPower(isOn, appID)`

#### Parameters

`isOn` - True if the heart rate monitor should be on, false if not

`appID` - A string with the app's name in, used to ensure one app can't turn off something another app is using

#### Returns

Is HRM on?

#### Description

Set the power to the Heart rate monitor

When on, data is output via the `HRM` event on `[Bangle](#Bangle)`:

```

Bangle.setHRMPower(true, "myapp");
Bangle.on('HRM',print);
```

_When on, the Heart rate monitor draws roughly 5mA_

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setLCDBrightness](#t_l_Bangle_setLCDBrightness) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2273 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setLCDBrightness(brightness)`

#### Parameters

`brightness` - The brightness of Bangle.js's display - from 0(off) to 1(on full)

#### Description

This function can be used to adjust the brightness of Bangle.js's display, and hence prolong its battery life.

Due to hardware design constraints on Bangle.js 1, software PWM has to be used which means that the display may flicker slightly when Bluetooth is active and the display is not at full power.

**Power consumption**

-   0 = 7mA
-   0.1 = 12mA
-   0.2 = 18mA
-   0.5 = 28mA
-   0.9 = 40mA (switching overhead)
-   1 = 40mA

In 2v21 and earlier, this function would erroneously turn the LCD backlight on. 2v22 and later fix this, and if you want the backlight on your should use `Bangle.setLCDPowerBacklight()`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setLCDMode](#t_l_Bangle_setLCDMode) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2318 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setLCDMode(mode)`

#### Parameters

`mode` - The LCD mode (See below)

#### Description

This function can be used to change the way graphics is handled on Bangle.js.

Available options for `[Bangle.setLCDMode](#l_Bangle_setLCDMode)` are:

-   `[Bangle.setLCDMode()](#l_Bangle_setLCDMode)` or `Bangle.setLCDMode("direct")` (the default) - The drawable area is 240x240 16 bit. Unbuffered, so draw calls take effect immediately. Terminal and vertical scrolling work (horizontal scrolling doesn't).
-   `Bangle.setLCDMode("doublebuffered")` - The drawable area is 240x160 16 bit, terminal and scrolling will not work. `g.flip()` must be called for draw operations to take effect.
-   `Bangle.setLCDMode("120x120")` - The drawable area is 120x120 8 bit, `g.getPixel`, terminal, and full scrolling work. Uses an offscreen buffer stored on Bangle.js, `g.flip()` must be called for draw operations to take effect.
-   `Bangle.setLCDMode("80x80")` - The drawable area is 80x80 8 bit, `g.getPixel`, terminal, and full scrolling work. Uses an offscreen buffer stored on Bangle.js, `g.flip()` must be called for draw operations to take effect.

You can also call `[Bangle.setLCDMode()](#l_Bangle_setLCDMode)` to return to normal, unbuffered `"direct"` mode.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setLCDOffset](#t_l_Bangle_setLCDOffset) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2457 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setLCDOffset(y)`

#### Parameters

`y` - The amount of pixels to shift the LCD up or down

#### Description

This can be used to move the displayed memory area up or down temporarily. It's used for displaying notifications while keeping the main display contents intact.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setLCDOverlay](#t_l_Bangle_setLCDOverlay) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2477 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setLCDOverlay(img, x, y, options)`

#### Parameters

`img` - An image, or undefined to clear

`x` - The X offset the graphics instance should be overlaid on the screen with

`y` - The Y offset the graphics instance should be overlaid on the screen with

`options` - \[Optional\] object `{remove:fn, id:"str"}`

#### Description

Overlay an image or graphics instance on top of the contents of the graphics buffer.

This only works on Bangle.js 2 because Bangle.js 1 doesn't have an offscreen buffer accessible from the CPU.

```

// display an alarm clock icon on the screen
var img = require("heatshrink").decompress(atob(`lss4UBvvv///ovBlMyqoADv/VAwlV//1qtfAQX/BINXDoPVq/9DAP
/AYIKDrWq0oREAYPW1QAB1IWCBQXaBQWq04WCAQP6BQeqA4P1AQPq1WggEK1WrBAIkBBQJsCBYO///fBQOoPAcqCwP3BQnwgECCwP9
GwIKCngWC14sB7QKCh4CBCwN/64KDgfACwWn6vWGwYsBCwOputWJgYsCgGqytVBQYsCLYOlqtqwAsFEINVrR4BFgghBBQosDEINWIQ
YsDEIQ3DFgYhCG4msSYeVFgnrFhMvOAgsEkE/FhEggYWCFgIhDkEACwQKBEIYKBCwSGFBQJxCQwYhBBQTKDqohCBQhCCEIJlDXwrKE
BQoWHBQdaCwuqJoI4CCwgKECwJ9CJgIKDq+qBYUq1WtBQf+BYIAC3/VBQX/tQKDz/9BQY5BAAVV/4WCBQJcBKwVf+oHBv4wCAAYhB`));
Bangle.setLCDOverlay(img,66,66, {id: "myOverlay", remove: () => print("Removed")});
```

Or use a `[Graphics](#Graphics)` instance:

```

var ovr = Graphics.createArrayBuffer(100,100,2,{msb:true});
ovr.transparent = 0; // (optional) set a transparent color
ovr.palette = new Uint16Array([0,0,g.toColor("#F00"),g.toColor("#FFF")]); // (optional) set a color palette
ovr.setColor(1).fillRect({x:0,y:0,w:99,h:99,r:8});
ovr.setColor(3).fillRect({x:2,y:2,w:95,h:95,r:7});
ovr.setColor(2).setFont("Vector:30").setFontAlign(0,0).drawString("Hi",50,50);
Bangle.setLCDOverlay(ovr,38,38, {id: "myOverlay", remove: () => print("Removed")});
```

To remove an overlay, simply call:

```

Bangle.setLCDOverlay(undefined, {id: "myOverlay"});
```

Before 2v22 the `options` object isn't parsed, and as a result the remove callback won't be called, and `[Bangle.setLCDOverlay(undefined)](#l_Bangle_setLCDOverlay)` will remove _any_ active overlay.

The `remove` callback is called when the current overlay is removed or replaced with another, but _not_ if setLCDOverlay is called again with an image and the same ID.

**Note:** This is only available in Bangle.js 2 smartwatches and DICKENS

### [Bangle.setLCDPower](#t_l_Bangle_setLCDPower) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2216 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setLCDPower(isOn)`

#### Parameters

`isOn` - True if the LCD should be on, false if not

#### Description

This function can be used to turn Bangle.js's LCD off or on.

This function resets the Bangle's 'activity timer' (like pressing a button or the screen would) so after a time period of inactivity set by `[Bangle.setLCDTimeout](#l_Bangle_setLCDTimeout)` the screen will turn off.

If you want to keep the screen on permanently (until apps are changed) you can do:

```

Bangle.setLCDTimeout(0); // turn off the timeout
Bangle.setLCDPower(1); // keep screen on
```

**When on full, the LCD draws roughly 40mA.** You can adjust When brightness using `[Bangle.setLCDBrightness](#l_Bangle_setLCDBrightness)`.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setLCDTimeout](#t_l_Bangle_setLCDTimeout) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2586 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setLCDTimeout(isOn)`

#### Parameters

`isOn` - The timeout of the display in seconds, or `0`/`undefined` to turn power saving off. Default is 10 seconds.

#### Description

This function can be used to turn Bangle.js's LCD power saving on or off.

With power saving off, the display will remain in the state you set it with `[Bangle.setLCDPower](#l_Bangle_setLCDPower)`.

With power saving on, the display will turn on if a button is pressed, the watch is turned face up, or the screen is updated (see `[Bangle.setOptions](#l_Bangle_setOptions)` for configuration). It'll turn off automatically after the given timeout.

**Note:** This function also sets the Backlight and Lock timeout (the time at which the touchscreen/buttons start being ignored). To set both separately, use `[Bangle.setOptions](#l_Bangle_setOptions)`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setLocked](#t_l_Bangle_setLocked) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2934 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setLocked(isLocked)`

#### Parameters

`isLocked` - `true` if the Bangle is locked (no user input allowed)

#### Description

This function can be used to lock or unlock Bangle.js (e.g. whether buttons and touchscreen work or not)

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setOptions](#t_l_Bangle_setOptions) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2673 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setOptions(options)`

#### Parameters

`options` -

#### Description

Set internal options used for gestures, etc...

-   `wakeOnBTN1` should the LCD turn on when BTN1 is pressed? default = `true`
-   `wakeOnBTN2` (Bangle.js 1) should the LCD turn on when BTN2 is pressed? default = `true`
-   `wakeOnBTN3` (Bangle.js 1) should the LCD turn on when BTN3 is pressed? default = `true`
-   `wakeOnFaceUp` should the LCD turn on when the watch is turned face up? default = `false`
-   `wakeOnTouch` should the LCD turn on when the touchscreen is pressed? On Bangle.js 1 this is a physical press on the touchscreen, on Bangle.js 2 we have to use the accelerometer as the touchscreen cannot be left powered without running the battery down. default = `false`
-   `wakeOnDoubleTap` (2v20 onwards) should the LCD turn on when the watch is double-tapped on the screen? This uses the accelerometer, not the touchscreen itself. default = `false`
-   `wakeOnTwist` should the LCD turn on when the watch is twisted? default = `true`
-   `twistThreshold` How much acceleration to register a twist of the watch strap? Can be negative for opposite direction. default = `800`
-   `twistMaxY` Maximum acceleration in Y to trigger a twist (low Y means watch is facing the right way up). default = `-800`
-   `twistTimeout` How little time (in ms) must a twist take from low->high acceleration? default = `1000`
-   `gestureStartThresh` how big a difference before we consider a gesture started? default = `sqr(800)`
-   `gestureEndThresh` how small a difference before we consider a gesture ended? default = `sqr(2000)`
-   `gestureInactiveCount` how many samples do we keep after a gesture has ended? default = `4`
-   `gestureMinLength` how many samples must a gesture have before we notify about it? default = `10`
-   `powerSave` after a minute of not being moved, Bangle.js will change the accelerometer poll interval down to 800ms (10x accelerometer samples). On movement it'll be raised to the default 80ms. If `[Bangle.setPollInterval](#l_Bangle_setPollInterval)` is used this is disabled, and for it to work the poll interval must be either 80ms or 800ms. default = `true`. Setting `powerSave:false` will disable this automatic power saving, but will **not** change the poll interval from its current value. If you desire a specific interval (e.g. the default 80ms) you must set it manually with `[Bangle.setPollInterval(80)](#l_Bangle_setPollInterval)` after setting `powerSave:false`.
-   `lowResistanceFix` (Bangle.js 2, 2v22+) In the very rare case that your watch button gets damaged such that it has a low resistance and always stays on, putting the watch into a boot loop, setting this flag may improve matters (by forcing the input low before reading and disabling the hardware watch on BTN1).
-   `lockTimeout` how many milliseconds before the screen locks
-   `lcdPowerTimeout` how many milliseconds before the screen turns off
-   `backlightTimeout` how many milliseconds before the screen's backlight turns off
-   `btnLoadTimeout` how many milliseconds does the home button have to be pressed for before the clock is reloaded? 1500ms default, or 0 means never.
-   `manualWatchdog` if set, this disables automatic kicking of the watchdog timer from the interrupt (when the button isn't held). You will then have to manually call `[E.kickWatchdog()](#l_E_kickWatchdog)` from your code or the watch will reset after ~5 seconds.
-   `hrmPollInterval` set the requested poll interval (in milliseconds) for the heart rate monitor. On Bangle.js 2 only 10,20,40,80,160,200 ms are supported, and polling rate may not be exact. The algorithm's filtering is tuned for 20-40ms poll intervals, so higher/lower intervals may effect the reliability of the BPM reading. You must call this _before_ `[Bangle.setHRMPower](#l_Bangle_setHRMPower)` - calling when the HRM is already on will not affect the poll rate.
-   `hrmSportMode` - on the newest Bangle.js 2 builds with with the proprietary heart rate algorithm, this is the sport mode passed to the algorithm. See `libs/misc/vc31_binary/algo.h` for more info. -1 = auto, 0 = normal (default), 1 = running, 2 = ...
-   `hrmGreenAdjust` - (Bangle.js 2, 2v19+) if false (default is true) the green LED intensity won't be adjusted to get the HRM sensor 'exposure' correct. This is reset when the HRM is initialised with `[Bangle.setHRMPower](#l_Bangle_setHRMPower)`.
-   `hrmWearDetect` - (Bangle.js 2, 2v19+) if false (default is true) HRM readings won't be turned off if the watch isn't on your arm (based on HRM proximity sensor). This is reset when the HRM is initialised with `[Bangle.setHRMPower](#l_Bangle_setHRMPower)`.
-   `hrmPushEnv` - (Bangle.js 2, 2v19+) if true (default is false) HRM environment readings will be produced as `Bangle.on(`HRM-env`, ...)` events. This is reset when the HRM is initialised with `[Bangle.setHRMPower](#l_Bangle_setHRMPower)`.
-   `hrmStaticSampleTime` - (Bangle.js 2, 2v28+) if true (default is false) force the HRM to use hrmPollInterval as the sample time rather than the real poll interval
-   `seaLevelPressure` (Bangle.js 2) Default 1013.25 millibars - this is used when calculating altitude from pressure sensor values from `[Bangle.getPressure](#l_Bangle_getPressure)`/`pressure` events.
-   `lcdBufferPtr` (Bangle.js 2 2v21+) Return a pointer to the first pixel of the 3 bit graphics buffer used by Bangle.js for the screen (stride = 178 bytes)
-   `lcdDoubleRefresh` (Bangle.js 2 2v22+) If enabled, pulses EXTCOMIN twice per poll interval (avoids off-axis flicker)
-   `stepCounterDisabled` (Bangle.js 2v29+) If set, this stops steps from being counted

Where accelerations are used they are in internal units, where `8192 = 1g`

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setPollInterval](#t_l_Bangle_setPollInterval) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L2623 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setPollInterval(interval)`

#### Parameters

`interval` - Polling interval in milliseconds (Default is 80ms - 12.5Hz to match accelerometer)

#### Description

Set how often the watch should poll its sensors (accel/hr/mag) for new data and kick the Watchdog timer. It isn't recommended that you make this interval much larger than 1000ms, but values up to 4000ms are allowed.

Calling this will set `Bangle.setOptions({powerSave: false})` - disabling the dynamic adjustment of poll interval to save battery power when Bangle.js is stationary.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setStepCount](#t_l_Bangle_setStepCount) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L3495 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setStepCount(count)`

#### Parameters

`count` - The value with which to reload the step counter

#### Description

Sets the current value of the step counter

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.setUI](#t_l_Bangle_setUI) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6405 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.setUI(type, callback)`

#### Parameters

`type` - The type of UI input: 'updown', 'leftright', 'clock', 'clockupdown' or undefined to cancel. Can also be an object (see below)

`callback` - A function with one argument which is the direction

#### Description

This puts Bangle.js into the specified UI input mode, and calls the callback provided when there is user input.

Currently supported interface types are:

-   'updown' - UI input with upwards motion `cb(-1)`, downwards motion `cb(1)`, and select `cb()`
    -   Bangle.js 1 uses BTN1/3 for up/down and BTN2 for select
    -   Bangle.js 2 uses touchscreen swipe up/down and tap
-   'leftright' - UI input with left motion `cb(-1)`, right motion `cb(1)`, and select `cb()`
    -   Bangle.js 1 uses BTN1/3 for left/right and BTN2 for select
    -   Bangle.js 2 uses touchscreen swipe left/right and tap/BTN1 for select
-   'clock' - called for clocks. Sets `Bangle.CLOCK=1` and allows a button to start the launcher
    -   Bangle.js 1 BTN2 starts the launcher
    -   Bangle.js 2 BTN1 starts the launcher
-   'clockupdown' - called for clocks. Sets `Bangle.CLOCK=1`, allows a button to start the launcher, but also provides up/down functionality
    -   Bangle.js 1 BTN2 starts the launcher, BTN1/BTN3 call `cb(-1)` and `cb(1)`
    -   Bangle.js 2 BTN1 starts the launcher, touchscreen tap in top/bottom right hand side calls `cb(-1)` and `cb(1)`
-   `{mode:"custom", ...}` allows you to specify custom handlers for different interactions. See below.
-   `undefined` removes all user interaction code

While you could use setWatch/etc manually, the benefit here is that you don't end up with multiple `[setWatch](#l__global_setWatch)` instances, and the actual input method (touch, or buttons) is implemented dependent on the watch (Bangle.js 1 or 2)

```

Bangle.setUI("updown", function (dir) {
  // dir is +/- 1 for swipes up/down
  // dir is 0 when button pressed
});
```

The first argument can also be an object, in which case more options can be specified\`:

```

Bangle.setUI({
  mode : "custom", // can also be set to one of the other modes presented above in order to extend them.
  back : function() {}, // optional - add a 'back' icon in top-left widget area and call this function when it is pressed , also call it when the hardware button is clicked (does not override btn if defined)
  remove : function() {}, // optional - add a handler for when the UI should be removed (eg stop any intervals/timers here)
  redraw : function() {}, // optional - add a handler to redraw the UI. Not needed but it can allow widgets/etc to provide other functionality that requires the screen to be redrawn
  touch : function(n,e) {}, // optional - handler for 'touch' events
  swipe : function(dir) {}, // optional - handler for 'swipe' events
  drag : function(e) {}, // optional - (mode:updown/leftright incompatible) handler for 'drag' events (Bangle.js 2 only)
  btn : function(n) {}, // optional - handler for 'button' events (n==1 on Bangle.js 2, n==1/2/3 depending on button for Bangle.js 1)
  btnRelease : function(n) {}, // optional - same as btn but react on release instead of press down.
  clock : 0 // optional - if set the behavior of 'clock' mode is added (does not override btn if defined)
});
```

If `remove` is specified, `[Bangle.showLauncher](#l_Bangle_showLauncher)`, `[Bangle.showClock](#l_Bangle_showClock)`, `[Bangle.load](#l_Bangle_load)` and some apps may choose to just call the `remove` function and then load a new app without resetting Bangle.js. As a result, **if you specify 'remove' you should make sure you test that after calling `[Bangle.setUI()](#l_Bangle_setUI)` without arguments your app is completely unloaded**, otherwise you may end up with memory leaks or other issues when switching apps. Please see the [Bangle.js Fast Load Tutorial](https://www.espruino.com/Bangle.js+Fast+Load) for more details on this.

**Note:** You can override this function in boot code to change the interaction mode with the watch. For instance you could make all clocks start the launcher with a swipe by using:

```

(function() {
  var sui = Bangle.setUI;
  Bangle.setUI = function(mode, cb) {
    var m = ("object"==typeof mode) ? mode.mode : mode;
    if (m!="clock") return sui(mode,cb);
    sui(); // clear
    Bangle.CLOCK=1;
    Bangle.swipeHandler = Bangle.showLauncher;
    Bangle.on("swipe", Bangle.swipeHandler);
  };
})();
```

**Note:** This is only available in Bangle.js smartwatches

**Note:** This is only available in Bangle.js smartwatches with Bangle.js 2 smartwatches

### [Bangle.showClock](#t_l_Bangle_showClock) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5882 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.showClock()`

#### Description

Load the Bangle.js clock - this has the same effect as calling `[Bangle.load()](#l_Bangle_load)`.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.showLauncher](#t_l_Bangle_showLauncher) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5871 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.showLauncher()`

#### Description

Load the Bangle.js app launcher, which will allow the user to select an application to launch.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.showLoadingScreen](#t_l_Bangle_showLoadingScreen) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6440 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.showLoadingScreen()`

#### Description

This displays the loading screen on Bangle.js. It is called automatically when an app is loaded with `[load()](#l__global_load)` or `[Bangle.load()](#l_Bangle_load)`, but can be called manually

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.showRecoveryMenu](#t_l_Bangle_showRecoveryMenu) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5892 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.showRecoveryMenu()`

#### Description

Show a 'recovery' menu that allows you to perform certain tasks on your Bangle.

You can also enter this menu by restarting your Bangle while holding down the button.

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.showTestScreen](#t_l_Bangle_showTestScreen) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5910 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.showTestScreen()`

#### Description

(2v20 and later) Show a test screen that lights green when each sensor on the Bangle works and reports within range.

Swipe on the screen when all items are green and the Bangle will turn bluetooth off and display a `TEST PASS` screen for 60 minutes, after which it will turn off.

You can enter this menu by restarting your Bangle while holding down the button, then choosing `Test` from the recovery menu.

**Note:** This is only available in Bangle.js 2 smartwatches

### [Bangle.softOff](#t_l_Bangle_softOff) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L5651 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.softOff()`

#### Description

Turn Bangle.js (mostly) off, but keep the CPU in sleep mode until BTN1 is pressed to preserve the RTC (current time).

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.step](#t_l_Bangle_step) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L159 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('step', function(up) { ... });`

#### Parameters

`up` - The number of steps since Bangle.js was last reset

#### Description

Called whenever a step is detected by Bangle.js's pedometer.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.stroke](#t_l_Bangle_stroke) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L528 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('stroke', function(event) { ... });`

#### Parameters

`event` - Object of form `{xy:Uint8Array([x1,y1,x2,y2...])}` containing touch coordinates

#### Description

Emitted when the touchscreen is dragged for a large enough distance to count as a gesture.

If Bangle.strokes is defined and populated with data from `[Unistroke.new](#l_Unistroke_new)`, the `event` argument will also contain a `stroke` field containing the most closely matching stroke name.

For example:

```

Bangle.strokes = {
  up : Unistroke.new(new Uint8Array([57, 151, ... 158, 137])),
  alpha : Unistroke.new(new Uint8Array([161, 55, ... 159, 161])),
};
Bangle.on('stroke',o=>{
  print(o.stroke);
  g.clear(1).drawPoly(o.xy);
});
// Might print something like
{
  "xy": new Uint8Array([149, 50, ... 107, 136]),
  "stroke": "alpha"
}
```

**Note:** This is only available in Bangle.js 2 smartwatches

### [event Bangle.swipe](#t_l_Bangle_swipe) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L471 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('swipe', function(directionLR, directionUD) { ... });`

#### Parameters

`directionLR` - `-1` for left, `1` for right, `0` for up/down

`directionUD` - `-1` for up, `1` for down, `0` for left/right (Bangle.js 2 only)

#### Description

Emitted when a swipe on the touchscreen is detected (a movement from left->right, right->left, down->up or up->down)

Bangle.js 1 is only capable of detecting left/right swipes as it only contains a 2 zone touchscreen.

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.tap](#t_l_Bangle_tap) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L420 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('tap', function(data) { ... });`

#### Parameters

`data` - `{dir, double, x, y, z}`

#### Description

If the watch is tapped, this event contains information on the way it was tapped.

`dir` reports the side of the watch that was tapped (not the direction it was tapped in).

```

{
  dir : "left/right/top/bottom/front/back",
  double : true/false // was this a double-tap?
  x : -2 .. 2, // the axis of the tap
  y : -2 .. 2, // the axis of the tap
  z : -2 .. 2 // the axis of the tap
```

**Note:** This is only available in Bangle.js smartwatches

### [event Bangle.touch](#t_l_Bangle_touch) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L490 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('touch', function(button, xy) { ... });`

#### Parameters

`button` - `1` for left, `2` for right

`xy` - Object of form `{x,y,type}` containing touch coordinates (if the device supports full touch). Clipped to 0..175 (LCD pixel coordinates) on firmware 2v13 and later.`type` is only available on Bangle.js 2 and is an integer, either 0 for swift touches or 2 for longer ones.

#### Description

Emitted when the touchscreen is pressed

**Note:** This is only available in Bangle.js smartwatches

### [Bangle.touchRd](#t_l_Bangle_touchRd) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L4937 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.touchRd(reg, cnt)`

#### Parameters

`reg` - Register number to read

`cnt` - If specified, returns an array of the given length (max 128). If not (or 0) it returns a number

#### Returns

See description above

#### Description

Reads a register from the touch controller. See https://github.com/espruino/Espruino/issues/2146#issuecomment-2554296721 for a list of registers. When the touchscreen is off (eg the Bangle is locked) then reading from any register will return `255` (`0xFF`) - so ensure the Bangle is unlocked with `[Bangle.setLocked(false)](#l_Bangle_setLocked)` before trying to read or write.

For example `print(Bangle.touchRd(0xa7).toString(16))` returns the `ChipID` register, which is `0xB4` (CST816S) on older Bangles or `0xB6` (CST816D) on newer ones.

**Note:** On Espruino 2v06 and before this function only returns a number (`cnt` is ignored).

**Note:** This is only available in Bangle.js 2 smartwatches

### [Bangle.touchWr](#t_l_Bangle_touchWr) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L4918 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.touchWr(reg, data)`

#### Parameters

`reg` -

`data` -

#### Description

Writes a register on the touch controller

**Note:** This is only available in Bangle.js 2 smartwatches

### [event Bangle.twist](#t_l_Bangle_twist) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L196 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Bangle.on('twist', function() { ... });`

#### Description

This event happens when the watch has been twisted around it's axis - for instance as if it was rotated so someone could look at the time.

To tweak when this happens, see the `twist*` options in `[Bangle.setOptions()](#l_Bangle_setOptions)`

**Note:** This is only available in Bangle.js smartwatches

## [BluetoothDevice Class](#t_BluetoothDevice)

[(top)](javascript:toppos\(\);)

A Web Bluetooth-style device - you can request one using `[NRF.requestDevice(options)](#l_NRF_requestDevice)`

For example:

```

var gatt;
NRF.requestDevice({ filters: [{ name: 'Puck.js abcd' }] }).then(function(device) {
  console.log("found device");
  return device.gatt.connect();
}).then(function(g) {
  gatt = g;
  console.log("connected");
  return gatt.startBonding();
}).then(function() {
  console.log("bonded", gatt.getSecurityStatus());
  gatt.disconnect();
}).catch(function(e) {
  console.log("ERROR",e);
});
```

#### Methods and Fields

-   [property BluetoothDevice.gatt](#l_BluetoothDevice_gatt)
-   [event BluetoothDevice.gattserverdisconnected(reason)](#l_BluetoothDevice_gattserverdisconnected)
-   [event BluetoothDevice.mtu(arr)](#l_BluetoothDevice_mtu)
-   [event BluetoothDevice.passkey(passkey)](#l_BluetoothDevice_passkey)
-   [event BluetoothDevice.passkeyRequest()](#l_BluetoothDevice_passkeyRequest)
-   [event BluetoothDevice.phy(arr)](#l_BluetoothDevice_phy)
-   [event BluetoothDevice.phy\_req(arr)](#l_BluetoothDevice_phy_req)
-   [property BluetoothDevice.rssi](#l_BluetoothDevice_rssi)
-   [function BluetoothDevice.sendPasskey(passkey)](#l_BluetoothDevice_sendPasskey)

### [property BluetoothDevice.gatt](#t_l_BluetoothDevice_gatt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4043 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property BluetoothDevice.gatt`

#### Returns

A `[BluetoothRemoteGATTServer](#BluetoothRemoteGATTServer)` for this device

#### Description

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [event BluetoothDevice.gattserverdisconnected](#t_l_BluetoothDevice_gattserverdisconnected) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L642 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`BluetoothDevice.on('gattserverdisconnected', function(reason) { ... });`

#### Parameters

`reason` - The reason for the disconnect by the BLE stack - see below

#### Description

This is called when the device gets disconnected.

Common `reason` values for disconnection are:

-   5 - `AUTHENTICATION_FAILURE`
-   8 - `CONNECTION_TIMEOUT`
-   19 - `REMOTE_USER_TERMINATED_CONNECTION`
-   22 - `LOCAL_HOST_TERMINATED_CONNECTION`

For a full list see [`BLE_HCI_STATUS_CODES` in `ble_hci.h`](https://github.com/espruino/Espruino/blob/ebf15226b165744ac40d94996698d53da7e03219/targetlibs/nrf5x_12/components/softdevice/s132/headers/ble_hci.h#L52-L121)

To connect and then print `Disconnected` when the device is disconnected, just do the following:

```

var gatt;
NRF.connect("aa:bb:cc:dd:ee:ff").then(function(gatt) {
  gatt.device.on('gattserverdisconnected', function(reason) {
    console.log("Disconnected ",reason);
  });
});
```

Or:

```

var gatt;
NRF.requestDevice(...).then(function(device) {
  device.on('gattserverdisconnected', function(reason) {
    console.log("Disconnected ",reason);
  });
});
```

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event BluetoothDevice.mtu](#t_l_BluetoothDevice_mtu) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L627 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`BluetoothDevice.on('mtu', function(arr) { ... });`

#### Parameters

`arr` - The negotiated MTU

#### Description

(2v28+) This event is fired when the MTU changes for the active Bluetooth connection. This is the amount of data that can be transferred in one packet.

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event BluetoothDevice.passkey](#t_l_BluetoothDevice_passkey) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4095 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`BluetoothDevice.on('passkey', function(passkey) { ... });`

#### Parameters

`passkey` - A 6 character numeric String to be displayed

#### Description

Called when the device pairs and sends a passkey that Espruino should display.

For this to be used, you'll have to specify that there's a display using `[NRF.setSecurity](#l_NRF_setSecurity)`

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event BluetoothDevice.passkeyRequest](#t_l_BluetoothDevice_passkeyRequest) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4112 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`BluetoothDevice.on('passkeyRequest', function() { ... });`

#### Description

Called when the device pairs, displays a passkey, and wants Espruino to tell it what the passkey was.

Respond with `BluetoothDevice.sendPasskey("123456")` with a 6 character string containing only `0..9`.

For this to be used, you'll have to specify that there's a keyboard using `[NRF.setSecurity](#l_NRF_setSecurity)`

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event BluetoothDevice.phy](#t_l_BluetoothDevice_phy) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L583 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`BluetoothDevice.on('phy', function(arr) { ... });`

#### Parameters

`arr` - An array containing `[tx_phy, rx_phy, status]` (see below)

#### Description

(2v28+, nRF52840 only) This event is fired when the phy (radio) is changed for this Bluetooth connection. The parameter is the data `[tx_phy, rx_phy, status]`

`tx_phy`/`rx_phy` are integers where each bit corresponds to:

-   1 : 1mbps phy
-   2 : 2mbps phy
-   4 : coded phy

`status` is an integer containing the status code. 0 = success

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event BluetoothDevice.phy\_req](#t_l_BluetoothDevice_phy_req) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L605 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`BluetoothDevice.on('phy_req', function(arr) { ... });`

#### Parameters

`arr` - An array containing `[tx_phy, rx_phy]` (see below)

#### Description

(2v28+, nRF52840 only) This event is fired when the phy (radio) is requested to change for this Bluetooth connection. The parameter is the data `[tx_phy, rx_phy]`

`tx_phy`/`rx_phy` are integers where each bit corresponds to:

-   1 : 1mbps phy
-   2 : 2mbps phy
-   4 : coded phy

eg. `7` means all phys (eg any) have been requested

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [property BluetoothDevice.rssi](#t_l_BluetoothDevice_rssi) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4067 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property BluetoothDevice.rssi`

#### Returns

The last received RSSI (signal strength) for this device

#### Description

This is set whenever the RSSI of the connection is changed. `BluetoothGATTServer.on("rssi", ...)` is also emitted.

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [function BluetoothDevice.sendPasskey](#t_l_BluetoothDevice_sendPasskey) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4130 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothDevice.sendPasskey(passkey)`

#### Parameters

`passkey` - A 6 character numeric String to be returned to the device

#### Description

To be used as a response when the event `[BluetoothDevice.sendPasskey](#l_BluetoothDevice_sendPasskey)` has been received.

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

## [BluetoothGATTServer Class](#t_BluetoothGATTServer)

[(top)](javascript:toppos\(\);)

#### Methods and Fields

-   [event BluetoothGATTServer.rssi(rssi)](#l_BluetoothGATTServer_rssi)

### [event BluetoothGATTServer.rssi](#t_l_BluetoothGATTServer_rssi) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4081 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`BluetoothGATTServer.on('rssi', function(rssi) { ... });`

#### Parameters

`rssi` - The current RSSI value for this connection

#### Description

This event is fired whenever the RSSI of the connection is changed. `[BluetoothDevice.rssi](#l_BluetoothDevice_rssi)` is also updated

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

## [BluetoothRemoteGATTCharacteristic Class](#t_BluetoothRemoteGATTCharacteristic)

[(top)](javascript:toppos\(\);)

Web Bluetooth-style GATT characteristic - get this using `[BluetoothRemoteGATTService.getCharacteristic(s)](#l_BluetoothRemoteGATTService_getCharacteristic)`

https://webbluetoothcg.github.io/web-bluetooth/#bluetoothremotegattcharacteristic

#### Methods and Fields

-   [event BluetoothRemoteGATTCharacteristic.characteristicvaluechanged()](#l_BluetoothRemoteGATTCharacteristic_characteristicvaluechanged)
-   [function BluetoothRemoteGATTCharacteristic.readValue()](#l_BluetoothRemoteGATTCharacteristic_readValue)
-   [property BluetoothRemoteGATTCharacteristic.service](#l_BluetoothRemoteGATTCharacteristic_service)
-   [function BluetoothRemoteGATTCharacteristic.startNotifications()](#l_BluetoothRemoteGATTCharacteristic_startNotifications)
-   [function BluetoothRemoteGATTCharacteristic.stopNotifications()](#l_BluetoothRemoteGATTCharacteristic_stopNotifications)
-   [function BluetoothRemoteGATTCharacteristic.writeValue(data)](#l_BluetoothRemoteGATTCharacteristic_writeValue)

### [event BluetoothRemoteGATTCharacteristic.characteristicvaluechanged](#t_l_BluetoothRemoteGATTCharacteristic_characteristicvaluechanged) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L685 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`BluetoothRemoteGATTCharacteristic.on('characteristicvaluechanged', function() { ... });`

#### Description

Called when a characteristic's value changes, _after_ `[BluetoothRemoteGATTCharacteristic.startNotifications](#l_BluetoothRemoteGATTCharacteristic_startNotifications)` has been called.

```

  ...
  return service.getCharacteristic("characteristic_uuid");
}).then(function(c) {
  c.on('characteristicvaluechanged', function(event) {
    console.log("-> "+event.target.value);
  });
  return c.startNotifications();
}).then(...
```

The first argument is of the form

```
{target :
BluetoothRemoteGATTCharacteristic}
```

, and `BluetoothRemoteGATTCharacteristic.value` will then contain the new value (as a DataView).

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [function BluetoothRemoteGATTCharacteristic.readValue](#t_l_BluetoothRemoteGATTCharacteristic_readValue) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4780 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTCharacteristic.readValue()`

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) with a `[DataView](#DataView)` when the characteristic is read

#### Description

Read a characteristic's value, return a promise containing a `[DataView](#DataView)`

```

var device;
NRF.connect(device_address).then(function(d) {
  device = d;
  return d.getPrimaryService("service_uuid");
}).then(function(s) {
  console.log("Service ",s);
  return s.getCharacteristic("characteristic_uuid");
}).then(function(c) {
  return c.readValue();
}).then(function(d) {
  console.log("Got:", JSON.stringify(d.buffer));
  device.disconnect();
}).catch(function() {
  console.log("Something's broken.");
});
```

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [property BluetoothRemoteGATTCharacteristic.service](#t_l_BluetoothRemoteGATTCharacteristic_service) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4723 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property BluetoothRemoteGATTCharacteristic.service`

#### Returns

The `[BluetoothRemoteGATTService](#BluetoothRemoteGATTService)` this Service came from

#### Description

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [function BluetoothRemoteGATTCharacteristic.startNotifications](#t_l_BluetoothRemoteGATTCharacteristic_startNotifications) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4824 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTCharacteristic.startNotifications()`

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) with data when notifications have been added

#### Description

Starts notifications - whenever this characteristic's value changes, a `characteristicvaluechanged` event is fired and `characteristic.value` will then contain the new value as a `[DataView](#DataView)`.

```

var device;
NRF.connect(device_address).then(function(d) {
  device = d;
  return d.getPrimaryService("service_uuid");
}).then(function(s) {
  console.log("Service ",s);
  return s.getCharacteristic("characteristic_uuid");
}).then(function(c) {
  c.on('characteristicvaluechanged', function(event) {
    console.log("-> ",event.target.value); // this is a DataView
  });
  return c.startNotifications();
}).then(function(d) {
  console.log("Waiting for notifications");
}).catch(function() {
  console.log("Something's broken.");
});
```

For example, to listen to the output of another Puck.js's Nordic Serial port service, you can use:

```

var gatt;
NRF.connect("pu:ck:js:ad:dr:es random").then(function(g) {
  gatt = g;
  return gatt.getPrimaryService("6e400001-b5a3-f393-e0a9-e50e24dcca9e");
}).then(function(service) {
  return service.getCharacteristic("6e400003-b5a3-f393-e0a9-e50e24dcca9e");
}).then(function(characteristic) {
  characteristic.on('characteristicvaluechanged', function(event) {
    console.log("RX: "+JSON.stringify(event.target.value.buffer));
  });
  return characteristic.startNotifications();
}).then(function() {
  console.log("Done!");
});
```

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [function BluetoothRemoteGATTCharacteristic.stopNotifications](#t_l_BluetoothRemoteGATTCharacteristic_stopNotifications) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4916 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTCharacteristic.stopNotifications()`

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) with data when notifications have been removed

#### Description

Stop notifications (that were requested with `[BluetoothRemoteGATTCharacteristic.startNotifications](#l_BluetoothRemoteGATTCharacteristic_startNotifications)`)

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [function BluetoothRemoteGATTCharacteristic.writeValue](#t_l_BluetoothRemoteGATTCharacteristic_writeValue) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4732 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTCharacteristic.writeValue(data)`

#### Parameters

`data` - The data to write

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the characteristic is written

#### Description

Write a characteristic's value

```

var device;
NRF.connect(device_address).then(function(d) {
  device = d;
  return d.getPrimaryService("service_uuid");
}).then(function(s) {
  console.log("Service ",s);
  return s.getCharacteristic("characteristic_uuid");
}).then(function(c) {
  return c.writeValue("Hello");
}).then(function(d) {
  device.disconnect();
}).catch(function() {
  console.log("Something's broken.");
});
```

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

## [BluetoothRemoteGATTServer Class](#t_BluetoothRemoteGATTServer)

[(top)](javascript:toppos\(\);)

Web Bluetooth-style GATT server - get this using `[NRF.connect(address)](#l_NRF_connect)` or `[NRF.requestDevice(options)](#l_NRF_requestDevice)` and `response.gatt.connect`

https://webbluetoothcg.github.io/web-bluetooth/#bluetoothremotegattserver

#### Methods and Fields

-   [function BluetoothRemoteGATTServer.connect(options)](#l_BluetoothRemoteGATTServer_connect)
-   [property BluetoothRemoteGATTServer.connected](#l_BluetoothRemoteGATTServer_connected)
-   [function BluetoothRemoteGATTServer.disconnect()](#l_BluetoothRemoteGATTServer_disconnect)
-   [function BluetoothRemoteGATTServer.getPrimaryService(service)](#l_BluetoothRemoteGATTServer_getPrimaryService)
-   [function BluetoothRemoteGATTServer.getPrimaryServices()](#l_BluetoothRemoteGATTServer_getPrimaryServices)
-   [function BluetoothRemoteGATTServer.getSecurityStatus()](#l_BluetoothRemoteGATTServer_getSecurityStatus)
-   [property BluetoothRemoteGATTServer.handle](#l_BluetoothRemoteGATTServer_handle)
-   [function BluetoothRemoteGATTServer.setRSSIHandler(callback)](#l_BluetoothRemoteGATTServer_setRSSIHandler)
-   [function BluetoothRemoteGATTServer.startBonding(forceRePair)](#l_BluetoothRemoteGATTServer_startBonding)
-   [function BluetoothRemoteGATTServer.updateConnection(options)](#l_BluetoothRemoteGATTServer_updateConnection)

### [function BluetoothRemoteGATTServer.connect](#t_l_BluetoothRemoteGATTServer_connect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4251 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTServer.connect(options)`

#### Parameters

`options` - \[optional\] (Espruino-specific) An object of connection options (see below)

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the connection is complete

#### Description

Connect to a BLE device - returns a promise, the argument of which is the `[BluetoothRemoteGATTServer](#BluetoothRemoteGATTServer)` connection.

See [](/Reference#l_NRF_requestDevice)`[NRF.requestDevice](#l_NRF_requestDevice)` for usage examples.

`options` is an optional object containing:

```

{
   minInterval // min connection interval in milliseconds, 7.5 ms to 4 s
   maxInterval // max connection interval in milliseconds, 7.5 ms to 4 s
   slaveLatency : int // (2v28+) number of connection intervals missed before connection is closed, default 4 (or 2 if pre-2v28)
   phy : "1mbps/coded/both/2mbps"
     // (2v26+, NRF52833/NRF52840 only) the type of Bluetooth signals to scan for
     // `1mbps` (default) - standard Bluetooth LE advertising
     // `coded` - long range
     // `both` - standard and long range
     // `2mbps` - high speed 2mbps (not working)
   extended : bool
     // (2v26+, NRF52833/NRF52840 only) support receiving extended-length advertising (default = false, or true if phy isn't `"1mbps"`)
   window : int
     // (2v26+) how long we scan for in milliseconds (default 100ms)
   interval : int
     // (2v26+) how often we scan in milliseconds (default 100ms)
     // When scanning on both `1mbps` and `coded`, `interval` needs to be twice `window`.
}
```

By default the interval is 20-200ms (or 500-1000ms if `[NRF.setLowPowerConnection(true)](#l_NRF_setLowPowerConnection)` was called. During connection Espruino negotiates with the other device to find a common interval that can be used.

For instance calling:

```

NRF.requestDevice({ filters: [{ namePrefix: 'Pixl.js' }] }).then(function(device) {
  return device.gatt.connect({minInterval:7.5, maxInterval:7.5});
}).then(function(g) {
```

will force the connection to use the fastest connection interval possible (as long as the device at the other end supports it).

**Note:** The Web Bluetooth spec states that if a device hasn't advertised its name, when connected to a device the central (in this case Espruino) should automatically retrieve the name from the corresponding characteristic (`0x2a00` on service `0x1800`). Espruino does not automatically do this.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [property BluetoothRemoteGATTServer.connected](#t_l_BluetoothRemoteGATTServer_connected) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4370 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property BluetoothRemoteGATTServer.connected`

#### Returns

Whether the device is connected or not

#### Description

### [function BluetoothRemoteGATTServer.disconnect](#t_l_BluetoothRemoteGATTServer_disconnect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4386 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTServer.disconnect()`

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the disconnection is complete (non-standard)

#### Description

Disconnect from a previously connected BLE device connected with `[BluetoothRemoteGATTServer.connect](#l_BluetoothRemoteGATTServer_connect)` - this does not disconnect from something that has connected to the Espruino.

**Note:** While `.disconnect` is standard Web Bluetooth, in the spec it returns undefined not a `[Promise](#Promise)` for implementation reasons. In Espruino we return a `[Promise](#Promise)` to make it easier to detect when Espruino is free to connect to something else.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [function BluetoothRemoteGATTServer.getPrimaryService](#t_l_BluetoothRemoteGATTServer_getPrimaryService) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4526 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTServer.getPrimaryService(service)`

#### Parameters

`service` - The service UUID

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the primary service is found (the argument contains a `[BluetoothRemoteGATTService](#BluetoothRemoteGATTService)`)

#### Description

See `[NRF.connect](#l_NRF_connect)` for usage examples.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [function BluetoothRemoteGATTServer.getPrimaryServices](#t_l_BluetoothRemoteGATTServer_getPrimaryServices) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4564 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTServer.getPrimaryServices()`

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the primary services are found (the argument contains an array of `[BluetoothRemoteGATTService](#BluetoothRemoteGATTService)`)

#### Description

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [function BluetoothRemoteGATTServer.getSecurityStatus](#t_l_BluetoothRemoteGATTServer_getSecurityStatus) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4489 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTServer.getSecurityStatus()`

#### Returns

An object

#### Description

Return an object with information about the security state of the current connection:

```

{
  connected       // The connection is active (not disconnected).
  encrypted       // Communication on this link is encrypted.
  mitm_protected  // The encrypted communication is also protected against man-in-the-middle attacks.
  bonded          // The peer is bonded with us
}
```

See `[BluetoothRemoteGATTServer.startBonding](#l_BluetoothRemoteGATTServer_startBonding)` for information about negotiating a secure connection.

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Puck.js.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [property BluetoothRemoteGATTServer.handle](#t_l_BluetoothRemoteGATTServer_handle) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4378 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property BluetoothRemoteGATTServer.handle`

#### Returns

The handle to this device (if it is currently connected) - the handle is an internal value used by the Bluetooth Stack

#### Description

### [function BluetoothRemoteGATTServer.setRSSIHandler](#t_l_BluetoothRemoteGATTServer_setRSSIHandler) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4594 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTServer.setRSSIHandler(callback)`

#### Parameters

`callback` - The callback to call with the RSSI value, or undefined to stop

#### Description

Start/stop listening for RSSI values on the active GATT connection

```

// Start listening for RSSI value updates
gattServer.setRSSIHandler(function(rssi) {
  console.log(rssi); // prints -85 (or similar)
});
// Stop listening
gattServer.setRSSIHandler();
```

RSSI is the 'Received Signal Strength Indication' in dBm

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [function BluetoothRemoteGATTServer.startBonding](#t_l_BluetoothRemoteGATTServer_startBonding) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4439 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTServer.startBonding(forceRePair)`

#### Parameters

`forceRePair` - If the device is already bonded, re-pair it

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the bonding is complete

#### Description

Start negotiating bonding (secure communications) with the connected device, and return a Promise that is completed on success or failure.

```

var gatt;
NRF.requestDevice({ filters: [{ name: 'Puck.js abcd' }] }).then(function(device) {
  console.log("found device");
  return device.gatt.connect();
}).then(function(g) {
  gatt = g;
  console.log("connected");
  return gatt.startBonding();
}).then(function() {
  console.log("bonded", gatt.getSecurityStatus());
  gatt.disconnect();
}).catch(function(e) {
  console.log("ERROR",e);
});
```

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [function BluetoothRemoteGATTServer.updateConnection](#t_l_BluetoothRemoteGATTServer_updateConnection) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4191 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTServer.updateConnection(options)`

#### Parameters

`options` - An object containing connection options

#### Description

(2v28+) Update connection parameters on this central connection. Options can be:

```

{
  phy : string // "1mpbs"/"2mpbs"/"coded"/"auto"
}
```

**This is not part of the Web Bluetooth Specification.** It has been added specifically for Espruino.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

## [BluetoothRemoteGATTService Class](#t_BluetoothRemoteGATTService)

[(top)](javascript:toppos\(\);)

Web Bluetooth-style GATT service - get this using `[BluetoothRemoteGATTServer.getPrimaryService(s)](#l_BluetoothRemoteGATTServer_getPrimaryService)`

https://webbluetoothcg.github.io/web-bluetooth/#bluetoothremotegattservice

#### Methods and Fields

-   [property BluetoothRemoteGATTService.device](#l_BluetoothRemoteGATTService_device)
-   [function BluetoothRemoteGATTService.getCharacteristic(characteristic)](#l_BluetoothRemoteGATTService_getCharacteristic)
-   [function BluetoothRemoteGATTService.getCharacteristics()](#l_BluetoothRemoteGATTService_getCharacteristics)

### [property BluetoothRemoteGATTService.device](#t_l_BluetoothRemoteGATTService_device) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4643 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property BluetoothRemoteGATTService.device`

#### Returns

The `[BluetoothDevice](#BluetoothDevice)` this Service came from

#### Description

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [function BluetoothRemoteGATTService.getCharacteristic](#t_l_BluetoothRemoteGATTService_getCharacteristic) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4652 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTService.getCharacteristic(characteristic)`

#### Parameters

`characteristic` - The characteristic UUID

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the characteristic is found (the argument contains a `[BluetoothRemoteGATTCharacteristic](#BluetoothRemoteGATTCharacteristic)`)

#### Description

See `[NRF.connect](#l_NRF_connect)` for usage examples.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [function BluetoothRemoteGATTService.getCharacteristics](#t_l_BluetoothRemoteGATTService_getCharacteristics) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4686 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function BluetoothRemoteGATTService.getCharacteristics()`

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the characteristic is found (the argument contains an array of `[BluetoothRemoteGATTCharacteristic](#BluetoothRemoteGATTCharacteristic)`)

#### Description

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

## [Boolean Class](#t_Boolean)

[(top)](javascript:toppos\(\);)

#### Methods and Fields

-   [constructor Boolean(value)](#l_Boolean_Boolean)

### [constructor Boolean](#t_l_Boolean_Boolean) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L772 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Boolean(value)`

#### Parameters

`value` - A single value to be converted to a number

#### Returns

A Boolean object

#### Description

Creates a boolean

## [console Class](#t_console)

[(top)](javascript:toppos\(\);)

An Object that contains functions for writing to the interactive console

#### Methods and Fields

-   [console.debug(text, ...)](#l_console_debug)
-   [console.error(text, ...)](#l_console_error)
-   [console.info(text, ...)](#l_console_info)
-   [console.log(text, ...)](#l_console_log)
-   [console.trace(text, ...)](#l_console_trace)
-   [console.warn(text, ...)](#l_console_warn)

### [console.debug](#t_l_console_debug) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L620 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`console.debug(text, ...)`

#### Parameters

`text, ...` - One or more arguments to print

#### Description

Implemented in Espruino as an alias of `[console.log](#l_console_log)`

### [console.error](#t_l_console_error) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L653 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`console.error(text, ...)`

#### Parameters

`text, ...` - One or more arguments to print

#### Description

Implemented in Espruino as an alias of `[console.log](#l_console_log)`

### [console.info](#t_l_console_info) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L631 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`console.info(text, ...)`

#### Parameters

`text, ...` - One or more arguments to print

#### Description

Implemented in Espruino as an alias of `[console.log](#l_console_log)`

### [console.log](#t_l_console_log) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L582 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`console.log(text, ...)`

#### Parameters

`text, ...` - One or more arguments to print

#### Description

Print the supplied string(s) to the console

**Note:_\* If you're connected to a computer (not a wall adaptor) via USB but \*_you are not running a terminal app** then when you print data Espruino may pause execution and wait until the computer requests the data it is trying to print.

### [console.trace](#t_l_console_trace) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L665 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`console.trace(text, ...)`

#### Parameters

`text, ...` - One or more arguments to print

#### Description

**Note:** This is not available in devices with low flash memory

### [console.warn](#t_l_console_warn) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L642 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`console.warn(text, ...)`

#### Parameters

`text, ...` - One or more arguments to print

#### Description

Implemented in Espruino as an alias of `[console.log](#l_console_log)`

## [crypto Library](#t_crypto)

[(top)](javascript:toppos\(\);)

Cryptographic functions

**Note:** This library is currently only included in builds for boards where there is space. For other boards there is `crypto.js` which implements SHA1 in JS.

#### Methods and Fields

-   [require("crypto").SHA1(message)](#l_crypto_SHA1)
-   [require("crypto").SHA224(message)](#l_crypto_SHA224)
-   [require("crypto").SHA256(message)](#l_crypto_SHA256)
-   [require("crypto").SHA384(message)](#l_crypto_SHA384)
-   [require("crypto").SHA512(message)](#l_crypto_SHA512)

### [crypto.SHA1](#t_l_crypto_SHA1) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/crypto/jswrap_crypto.c#L188 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("crypto").SHA1(message)`

#### Parameters

`message` - The message to apply the hash to

#### Returns

Returns a 20 byte ArrayBuffer

#### Description

Performs a SHA1 hash and returns the result as a 20 byte ArrayBuffer.

**Note:** On some boards (currently only Espruino Original) there isn't space for a fully unrolled SHA1 implementation so a slower all-JS implementation is used instead.

**Note:** This is only available in devices that support Crypto Functionality (Espruino Pico, Original, Espruino WiFi, Espruino BLE devices, Linux or ESP8266)

### [crypto.SHA224](#t_l_crypto_SHA224) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/crypto/jswrap_crypto.c#L207 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("crypto").SHA224(message)`

#### Parameters

`message` - The message to apply the hash to

#### Returns

Returns a 20 byte ArrayBuffer

#### Description

Performs a SHA224 hash and returns the result as a 28 byte ArrayBuffer

**Note:** This is only available in devices that support SHA256 (Espruino Pico, Espruino WiFi, Espruino BLE devices or Linux)

### [crypto.SHA256](#t_l_crypto_SHA256) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/crypto/jswrap_crypto.c#L222 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("crypto").SHA256(message)`

#### Parameters

`message` - The message to apply the hash to

#### Returns

Returns a 20 byte ArrayBuffer

#### Description

Performs a SHA256 hash and returns the result as a 32 byte ArrayBuffer

**Note:** This is only available in devices that support SHA256 (Espruino Pico, Espruino WiFi, Espruino BLE devices or Linux)

### [crypto.SHA384](#t_l_crypto_SHA384) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/crypto/jswrap_crypto.c#L237 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("crypto").SHA384(message)`

#### Parameters

`message` - The message to apply the hash to

#### Returns

Returns a 20 byte ArrayBuffer

#### Description

Performs a SHA384 hash and returns the result as a 48 byte ArrayBuffer

**Note:** This is only available in devices that support SHA512 (Espruino Pico, Espruino WiFi, Espruino BLE devices or Linux)

### [crypto.SHA512](#t_l_crypto_SHA512) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/crypto/jswrap_crypto.c#L252 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("crypto").SHA512(message)`

#### Parameters

`message` - The message to apply the hash to

#### Returns

Returns a 32 byte ArrayBuffer

#### Description

Performs a SHA512 hash and returns the result as a 64 byte ArrayBuffer

**Note:** This is only available in devices that support SHA512 (Espruino Pico, Espruino WiFi, Espruino BLE devices or Linux)

## [DataView Class](#t_DataView)

[(top)](javascript:toppos\(\);)

This class helps

#### Methods and Fields

-   [constructor DataView(buffer, byteOffset, byteLength)](#l_DataView_DataView)
-   [function DataView.getFloat32(byteOffset, littleEndian)](#l_DataView_getFloat32)
-   [function DataView.getFloat64(byteOffset, littleEndian)](#l_DataView_getFloat64)
-   [function DataView.getInt16(byteOffset, littleEndian)](#l_DataView_getInt16)
-   [function DataView.getInt32(byteOffset, littleEndian)](#l_DataView_getInt32)
-   [function DataView.getInt8(byteOffset, littleEndian)](#l_DataView_getInt8)
-   [function DataView.getUint16(byteOffset, littleEndian)](#l_DataView_getUint16)
-   [function DataView.getUint32(byteOffset, littleEndian)](#l_DataView_getUint32)
-   [function DataView.getUint8(byteOffset, littleEndian)](#l_DataView_getUint8)
-   [function DataView.setFloat32(byteOffset, value, littleEndian)](#l_DataView_setFloat32)
-   [function DataView.setFloat64(byteOffset, value, littleEndian)](#l_DataView_setFloat64)
-   [function DataView.setInt16(byteOffset, value, littleEndian)](#l_DataView_setInt16)
-   [function DataView.setInt32(byteOffset, value, littleEndian)](#l_DataView_setInt32)
-   [function DataView.setInt8(byteOffset, value, littleEndian)](#l_DataView_setInt8)
-   [function DataView.setUint16(byteOffset, value, littleEndian)](#l_DataView_setUint16)
-   [function DataView.setUint32(byteOffset, value, littleEndian)](#l_DataView_setUint32)
-   [function DataView.setUint8(byteOffset, value, littleEndian)](#l_DataView_setUint8)

### [constructor DataView](#t_l_DataView_DataView) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L30 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)

[(top)](javascript:toppos\(\);)

#### Call type:

`new DataView(buffer, byteOffset, byteLength)`

#### Parameters

`buffer` - The `[ArrayBuffer](#ArrayBuffer)` to base this on

`byteOffset` - \[optional\] The offset of this view in bytes

`byteLength` - \[optional\] The length in bytes

#### Returns

A `[DataView](#DataView)` object

#### Description

Create a `[DataView](#DataView)` object that can be used to access the data in an `[ArrayBuffer](#ArrayBuffer)`.

```

var b = new ArrayBuffer(8)
var v = new DataView(b)
v.setUint16(0,"0x1234")
v.setUint8(3,"0x56")
console.log("0x"+v.getUint32(0).toString(16))
// prints 0x12340056
```

**Note:** This is not available in devices with low flash memory

### [function DataView.getFloat32](#t_l_DataView_getFloat32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L115 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getFloat32)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.getFloat32(byteOffset, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to read from

`littleEndian` - \[optional\] Whether to read in little endian - if false or undefined data is read as big endian

#### Returns

The value of the 4 bytes in the array at `byteOffset` when interpreted as a `float`

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.getFloat64](#t_l_DataView_getFloat64) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L129 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getFloat64)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.getFloat64(byteOffset, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to read from

`littleEndian` - \[optional\] Whether to read in little endian - if false or undefined data is read as big endian

#### Returns

The value of the 8 bytes in the array at `byteOffset` when interpreted as a `double`

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.getInt16](#t_l_DataView_getInt16) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L157 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getInt16)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.getInt16(byteOffset, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to read from

`littleEndian` - \[optional\] Whether to read in little endian - if false or undefined data is read as big endian

#### Returns

The value of the 2 bytes in the array at `byteOffset` when interpreted as `int16`

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.getInt32](#t_l_DataView_getInt32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L171 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getInt32)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.getInt32(byteOffset, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to read from

`littleEndian` - \[optional\] Whether to read in little endian - if false or undefined data is read as big endian

#### Returns

The value of the 4 bytes in the array at `byteOffset` when interpreted as `int32`

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.getInt8](#t_l_DataView_getInt8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L143 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getInt8)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.getInt8(byteOffset, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to read from

`littleEndian` - \[optional\] Whether to read in little endian - if false or undefined data is read as big endian

#### Returns

The value of the 1 byte in the array at `byteOffset` when interpreted as `int8`

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.getUint16](#t_l_DataView_getUint16) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L199 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getUint16)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.getUint16(byteOffset, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to read from

`littleEndian` - \[optional\] Whether to read in little endian - if false or undefined data is read as big endian

#### Returns

The value of the 2 bytes in the array at `byteOffset` when interpreted as `uint16`

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.getUint32](#t_l_DataView_getUint32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L213 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getUint32)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.getUint32(byteOffset, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to read from

`littleEndian` - \[optional\] Whether to read in little endian - if false or undefined data is read as big endian

#### Returns

The value of the 4 bytes in the array at `byteOffset` when interpreted as `uint32`

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.getUint8](#t_l_DataView_getUint8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L185 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/getUint8)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.getUint8(byteOffset, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to read from

`littleEndian` - \[optional\] Whether to read in little endian - if false or undefined data is read as big endian

#### Returns

The value of the 1 byte in the array at `byteOffset` when interpreted as `uint8`

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.setFloat32](#t_l_DataView_setFloat32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L230 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setFloat32)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.setFloat32(byteOffset, value, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to write to

`value` - The value to write

`littleEndian` - \[optional\] Whether to write in little endian - if false or undefined data is written as big endian

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.setFloat64](#t_l_DataView_setFloat64) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L244 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setFloat64)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.setFloat64(byteOffset, value, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to write to

`value` - The value to write

`littleEndian` - \[optional\] Whether to write in little endian - if false or undefined data is written as big endian

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.setInt16](#t_l_DataView_setInt16) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L272 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setInt16)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.setInt16(byteOffset, value, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to write to

`value` - The value to write

`littleEndian` - \[optional\] Whether to write in little endian - if false or undefined data is written as big endian

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.setInt32](#t_l_DataView_setInt32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L286 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setInt32)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.setInt32(byteOffset, value, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to write to

`value` - The value to write

`littleEndian` - \[optional\] Whether to write in little endian - if false or undefined data is written as big endian

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.setInt8](#t_l_DataView_setInt8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L258 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setInt8)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.setInt8(byteOffset, value, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to write to

`value` - The value to write

`littleEndian` - \[optional\] Whether to write in little endian - if false or undefined data is written as big endian

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.setUint16](#t_l_DataView_setUint16) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L314 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setUint16)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.setUint16(byteOffset, value, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to write to

`value` - The value to write

`littleEndian` - \[optional\] Whether to write in little endian - if false or undefined data is written as big endian

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.setUint32](#t_l_DataView_setUint32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L328 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setUint32)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.setUint32(byteOffset, value, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to write to

`value` - The value to write

`littleEndian` - \[optional\] Whether to write in little endian - if false or undefined data is written as big endian

#### Description

**Note:** This is not available in devices with low flash memory

### [function DataView.setUint8](#t_l_DataView_setUint8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_dataview.c#L300 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView/setUint8)

[(top)](javascript:toppos\(\);)

#### Call type:

`function DataView.setUint8(byteOffset, value, littleEndian)`

#### Parameters

`byteOffset` - The offset in bytes to write to

`value` - The value to write

`littleEndian` - \[optional\] Whether to write in little endian - if false or undefined data is written as big endian

#### Description

**Note:** This is not available in devices with low flash memory

## [Date Class](#t_Date)

[(top)](javascript:toppos\(\);)

The built-in class for handling Dates.

**Note:** By default the time zone is GMT+0, however you can change the timezone using the `[E.setTimeZone(...)](#l_E_setTimeZone)` function.

For example `[E.setTimeZone(1)](#l_E_setTimeZone)` will be GMT+0100

_However_ if you have daylight savings time set with `[E.setDST(...)](#l_E_setDST)` then the timezone set by `[E.setTimeZone(...)](#l_E_setTimeZone)` will be _ignored_.

#### Methods and Fields

-   [constructor Date(args, ...)](#l_Date_Date)
-   [function Date.getDate()](#l_Date_getDate)
-   [function Date.getDay()](#l_Date_getDay)
-   [function Date.getFullYear()](#l_Date_getFullYear)
-   [function Date.getHours()](#l_Date_getHours)
-   [function Date.getIsDST()](#l_Date_getIsDST)
-   [function Date.getMilliseconds()](#l_Date_getMilliseconds)
-   [function Date.getMinutes()](#l_Date_getMinutes)
-   [function Date.getMonth()](#l_Date_getMonth)
-   [function Date.getSeconds()](#l_Date_getSeconds)
-   [function Date.getTime()](#l_Date_getTime)
-   [function Date.getTimezoneOffset()](#l_Date_getTimezoneOffset)
-   [Date.now()](#l_Date_now)
-   [Date.parse(str)](#l_Date_parse)
-   [function Date.setDate(dayValue)](#l_Date_setDate)
-   [function Date.setFullYear(yearValue, monthValue, dayValue)](#l_Date_setFullYear)
-   [function Date.setHours(hoursValue, minutesValue, secondsValue, millisecondsValue)](#l_Date_setHours)
-   [function Date.setMilliseconds(millisecondsValue)](#l_Date_setMilliseconds)
-   [function Date.setMinutes(minutesValue, secondsValue, millisecondsValue)](#l_Date_setMinutes)
-   [function Date.setMonth(monthValue, dayValue)](#l_Date_setMonth)
-   [function Date.setSeconds(secondsValue, millisecondsValue)](#l_Date_setSeconds)
-   [function Date.setTime(timeValue)](#l_Date_setTime)
-   [function Date.toISOString()](#l_Date_toISOString)
-   [function Date.toJSON()](#l_Date_toJSON)
-   [function Date.toLocalISOString()](#l_Date_toLocalISOString)
-   [function Date.toString()](#l_Date_toString)
-   [function Date.toUTCString()](#l_Date_toUTCString)
-   [function Date.valueOf()](#l_Date_valueOf)

### [constructor Date](#t_l_Date_Date) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L283 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Date(args, ...)`

#### Parameters

`args, ...` - Either nothing (current time), one numeric argument (milliseconds since 1970), a date string (see `[Date.parse](#l_Date_parse)`), or \[year, month, day, hour, minute, second, millisecond\]

#### Returns

A Date object

#### Description

Creates a date object

### [function Date.getDate](#t_l_Date_getDate) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L479 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getDate()`

#### Returns

See description above

#### Description

Day of the month 1..31

### [function Date.getDay](#t_l_Date_getDay) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L466 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getDay()`

#### Returns

See description above

#### Description

Day of the week (0=sunday, 1=monday, etc)

### [function Date.getFullYear](#t_l_Date_getFullYear) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L506 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getFullYear()`

#### Returns

See description above

#### Description

The year, e.g. 2014

### [function Date.getHours](#t_l_Date_getHours) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L414 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getHours)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getHours()`

#### Returns

See description above

#### Description

0..23

### [function Date.getIsDST](#t_l_Date_getIsDST) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L350 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getIsDST()`

#### Returns

true if daylight savings time is in effect

#### Description

This returns a boolean indicating whether daylight savings time is in effect.

**Note:** This is not available in devices with low flash memory

### [function Date.getMilliseconds](#t_l_Date_getMilliseconds) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L453 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMilliseconds)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getMilliseconds()`

#### Returns

See description above

#### Description

0..999

### [function Date.getMinutes](#t_l_Date_getMinutes) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L427 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMinutes)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getMinutes()`

#### Returns

See description above

#### Description

0..59

### [function Date.getMonth](#t_l_Date_getMonth) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L493 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getMonth)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getMonth()`

#### Returns

See description above

#### Description

Month of the year 0..11

### [function Date.getSeconds](#t_l_Date_getSeconds) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L440 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getSeconds)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getSeconds()`

#### Returns

See description above

#### Description

0..59

### [function Date.getTime](#t_l_Date_getTime) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L366 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTime)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getTime()`

#### Returns

See description above

#### Description

Return the number of milliseconds since 1970

### [function Date.getTimezoneOffset](#t_l_Date_getTimezoneOffset) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L334 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.getTimezoneOffset()`

#### Returns

The difference, in minutes, between UTC and local time

#### Description

This returns the time-zone offset from UTC, in minutes.

**Note:** This is not available in devices with low flash memory

### [Date.now](#t_l_Date_now) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L257 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/now)

[(top)](javascript:toppos\(\);)

#### Call type:

`Date.now()`

#### Returns

See description above

#### Description

Get the number of milliseconds elapsed since 1970 (or on embedded platforms, since startup).

**Note:** Desktop JS engines return an integer value for `[Date.now()](#l_Date_now)`, however Espruino returns a floating point value, accurate to fractions of a millisecond.

### [Date.parse](#t_l_Date_parse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L873 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)

[(top)](javascript:toppos\(\);)

#### Call type:

`Date.parse(str)`

#### Parameters

`str` - A String

#### Returns

The number of milliseconds since 1970

#### Description

Parse a date string and return milliseconds since 1970. Data can be either '2011-10-20T14:48:00', '2011-10-20' or 'Mon, 25 Dec 1995 13:30:00 +0430'

### [function Date.setDate](#t_l_Date_setDate) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L622 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setDate)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.setDate(dayValue)`

#### Parameters

`dayValue` - the day of the month, between 0 and 31

#### Returns

The number of milliseconds since 1970

#### Description

Day of the month 1..31

**Note:** This is not available in devices with low flash memory

### [function Date.setFullYear](#t_l_Date_setFullYear) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L671 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setFullYear)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.setFullYear(yearValue, monthValue, dayValue)`

#### Parameters

`yearValue` - The full year - eg. 1989

`monthValue` - \[optional\] the month, between 0 and 11

`dayValue` - \[optional\] the day, between 0 and 31

#### Returns

The number of milliseconds since 1970

#### Description

**Note:** This is not available in devices with low flash memory

### [function Date.setHours](#t_l_Date_setHours) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L522 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setHours)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.setHours(hoursValue, minutesValue, secondsValue, millisecondsValue)`

#### Parameters

`hoursValue` - number of hours, 0..23

`minutesValue` - number of minutes, 0..59

`secondsValue` - \[optional\] number of seconds, 0..59

`millisecondsValue` - \[optional\] number of milliseconds, 0..999

#### Returns

The number of milliseconds since 1970

#### Description

0..23

**Note:** This is not available in devices with low flash memory

### [function Date.setMilliseconds](#t_l_Date_setMilliseconds) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L603 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMilliseconds)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.setMilliseconds(millisecondsValue)`

#### Parameters

`millisecondsValue` - number of milliseconds, 0..999

#### Returns

The number of milliseconds since 1970

#### Description

**Note:** This is not available in devices with low flash memory

### [function Date.setMinutes](#t_l_Date_setMinutes) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L552 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMinutes)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.setMinutes(minutesValue, secondsValue, millisecondsValue)`

#### Parameters

`minutesValue` - number of minutes, 0..59

`secondsValue` - \[optional\] number of seconds, 0..59

`millisecondsValue` - \[optional\] number of milliseconds, 0..999

#### Returns

The number of milliseconds since 1970

#### Description

0..59

**Note:** This is not available in devices with low flash memory

### [function Date.setMonth](#t_l_Date_setMonth) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L645 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setMonth)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.setMonth(monthValue, dayValue)`

#### Parameters

`monthValue` - The month, between 0 and 11

`dayValue` - \[optional\] the day, between 0 and 31

#### Returns

The number of milliseconds since 1970

#### Description

Month of the year 0..11

**Note:** This is not available in devices with low flash memory

### [function Date.setSeconds](#t_l_Date_setSeconds) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L579 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setSeconds)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.setSeconds(secondsValue, millisecondsValue)`

#### Parameters

`secondsValue` - number of seconds, 0..59

`millisecondsValue` - \[optional\] number of milliseconds, 0..999

#### Returns

The number of milliseconds since 1970

#### Description

0..59

**Note:** This is not available in devices with low flash memory

### [function Date.setTime](#t_l_Date_setTime) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L387 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/setTime)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.setTime(timeValue)`

#### Parameters

`timeValue` - the number of milliseconds since 1970

#### Returns

the number of milliseconds since 1970

#### Description

Set the time/date of this Date class

### [function Date.toISOString](#t_l_Date_toISOString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L754 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.toISOString()`

#### Returns

A String

#### Description

Converts to a ISO 8601 String, e.g: `2014-06-20T14:52:20.123Z`

**Note:** This always assumes a timezone of GMT

### [function Date.toJSON](#t_l_Date_toJSON) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L766 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toJSON)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.toJSON()`

#### Returns

A String

#### Description

Calls `[Date.toISOString](#l_Date_toISOString)` to output this date to JSON

### [function Date.toLocalISOString](#t_l_Date_toLocalISOString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L782 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.toLocalISOString()`

#### Returns

A String

#### Description

Converts to a ISO 8601 String (with timezone information), e.g: `2014-06-20T14:52:20.123-0500`

**Note:** This is not available in devices with low flash memory

### [function Date.toString](#t_l_Date_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L703 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toString)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.toString()`

#### Returns

A String

#### Description

Converts to a String, e.g: `Fri Jun 20 2014 14:52:20 GMT+0000`

**Note:** This uses whatever timezone was set with `[E.setTimeZone()](#l_E_setTimeZone)` or `[E.setDST()](#l_E_setDST)`

### [function Date.toUTCString](#t_l_Date_toUTCString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L734 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toUTCString)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.toUTCString()`

#### Returns

A String

#### Description

Converts to a String, e.g: `Fri, 20 Jun 2014 14:52:20 GMT`

**Note:** This always assumes a timezone of GMT

**Note:** This is not available in devices with low flash memory

### [function Date.valueOf](#t_l_Date_valueOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_date.c#L375 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/valueOf)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Date.valueOf()`

#### Returns

See description above

#### Description

Return the number of milliseconds since 1970

## [E Class](#t_E)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for Espruino utility functions.

#### Methods and Fields

-   [event E.AMS(info)](#l_E_AMS)
-   [event E.ANCS(info)](#l_E_ANCS)
-   [E.asm(callspec, assemblycode, ...)](#l_E_asm)
-   [E.asUTF8(str)](#l_E_asUTF8)
-   [E.clip(x, min, max)](#l_E_clip)
-   [event E.comparator(dir)](#l_E_comparator)
-   [E.compiledC(code)](#l_E_compiledC)
-   [E.convolve(arr1, arr2, offset)](#l_E_convolve)
-   [E.CRC32(data)](#l_E_CRC32)
-   [E.decodeUTF8(str, lookup, replaceFn)](#l_E_decodeUTF8)
-   [E.defrag()](#l_E_defrag)
-   [E.dumpFragmentation()](#l_E_dumpFragmentation)
-   [E.dumpFreeList()](#l_E_dumpFreeList)
-   [E.dumpLockedVars()](#l_E_dumpLockedVars)
-   [E.dumpStr()](#l_E_dumpStr)
-   [E.dumpVariables()](#l_E_dumpVariables)
-   [E.enableWatchdog(timeout, isAuto)](#l_E_enableWatchdog)
-   [event E.errorFlag(errorFlags)](#l_E_errorFlag)
-   [E.FFT(arrReal, arrImage, inverse)](#l_E_FFT)
-   [E.fromUTF8(str)](#l_E_fromUTF8)
-   [E.getAddressOf(v, flatAddress)](#l_E_getAddressOf)
-   [E.getAnalogVRef()](#l_E_getAnalogVRef)
-   [E.getBattery()](#l_E_getBattery)
-   [E.getClock()](#l_E_getClock)
-   [E.getConsole()](#l_E_getConsole)
-   [E.getErrorFlags()](#l_E_getErrorFlags)
-   [E.getFlags()](#l_E_getFlags)
-   [E.getPowerUsage()](#l_E_getPowerUsage)
-   [E.getSizeOf(v, depth)](#l_E_getSizeOf)
-   [E.getTemperature(internal)](#l_E_getTemperature)
-   [E.getVDDH()](#l_E_getVDDH)
-   [E.HSBtoRGB(hue, sat, bri, format)](#l_E_HSBtoRGB)
-   [E.hwRand()](#l_E_hwRand)
-   [event E.init()](#l_E_init)
-   [E.internal](#l_E_internal)
-   [E.isUTF8(str)](#l_E_isUTF8)
-   [E.kickWatchdog()](#l_E_kickWatchdog)
-   [event E.kill()](#l_E_kill)
-   [E.lockConsole()](#l_E_lockConsole)
-   [E.lookupNoCase(haystack, needle, returnKey)](#l_E_lookupNoCase)
-   [E.mapInPlace(from, to, map, bits)](#l_E_mapInPlace)
-   [E.memoryArea(addr, len)](#l_E_memoryArea)
-   [E.memoryMap(baseAddress, registers)](#l_E_memoryMap)
-   [E.nativeCall(addr, sig, data)](#l_E_nativeCall)
-   [event E.packet(event)](#l_E_packet)
-   [event E.packetUpload(event)](#l_E_packetUpload)
-   [E.pipe(source, destination, options)](#l_E_pipe)
-   [E.reboot()](#l_E_reboot)
-   [E.reverseByte(x)](#l_E_reverseByte)
-   [E.setBootCode(code, alwaysExec)](#l_E_setBootCode)
-   [E.setClock(options)](#l_E_setClock)
-   [E.setComparator(pin, level)](#l_E_setComparator)
-   [E.setConsole(device, options)](#l_E_setConsole)
-   [E.setDST(params, ...)](#l_E_setDST)
-   [E.setFlags(flags)](#l_E_setFlags)
-   [E.setPassword(password)](#l_E_setPassword)
-   [E.setTimeZone(zone)](#l_E_setTimeZone)
-   [E.showAlert(message, options)](#l_E_showAlert)
-   [E.showMenu(menu)](#l_E_showMenu)
-   [E.showMessage(message, options)](#l_E_showMessage)
-   [E.showPrompt(message, options)](#l_E_showPrompt)
-   [E.showScroller(options)](#l_E_showScroller)
-   [E.srand(v)](#l_E_srand)
-   [E.stopEventPropagation()](#l_E_stopEventPropagation)
-   [E.sum(arr)](#l_E_sum)
-   [E.toArrayBuffer(str)](#l_E_toArrayBuffer)
-   [E.toFlatString(args, ...)](#l_E_toFlatString)
-   [E.toJS(arg)](#l_E_toJS)
-   [E.toString(args, ...)](#l_E_toString)
-   [event E.touch(x, y, b)](#l_E_touch)
-   [E.toUint8Array(args, ...)](#l_E_toUint8Array)
-   [E.variance(arr, mean)](#l_E_variance)

### [event E.AMS](#t_l_E_AMS) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3038 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('AMS', function(info) { ... });`

#### Parameters

`info` - An object (see below)

#### Description

Called when a media event arrives on an Apple iOS device Bangle.js is connected to

```

{
id : "artist"/"album"/"title"/"duration",
value : "Some text",
truncated : bool // the 'value' was too big to be sent completely
}
```

**Note:** This is only available in Bangle.js smartwatches

### [event E.ANCS](#t_l_E_ANCS) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3004 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('ANCS', function(info) { ... });`

#### Parameters

`info` - An object (see below)

#### Description

Called when a notification arrives on an Apple iOS device Bangle.js is connected to

```

{
event:"add",
uid:42,
category:4,
categoryCnt:42,
silent:true,
important:false,
preExisting:true,
positive:false,
negative:true
}
```

You can then get more information with `[NRF.ancsGetNotificationInfo](#l_NRF_ancsGetNotificationInfo)`, for instance:

```

E.on('ANCS', event => {
  NRF.ancsGetNotificationInfo( event.uid ).then(a=>print("Notify",E.toJS(a)));
});
```

**Note:** This is only available in Bangle.js smartwatches

### [E.asm](#t_l_E_asm) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2373 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.asm(callspec, assemblycode, ...)`

#### Parameters

`callspec` - The arguments this assembly takes - e.g. `void(int)`

`assemblycode, ...` - One of more strings of assembler code

#### Description

Provide assembly to Espruino.

**This function is not part of Espruino**. Instead, it is detected by the Espruino IDE (or command-line tools) at upload time and is replaced with machine code and an `[E.nativeCall](#l_E_nativeCall)` call.

See [the documentation on the Assembler](http://www.espruino.com/Assembler) for more information.

**Note:** This is not available in devices with low flash memory

### [E.asUTF8](#t_l_E_asUTF8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1128 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.asUTF8(str)`

#### Parameters

`str` - The string to turn into a UTF8 Unicode String

#### Returns

A String

#### Description

By default, strings in Espruino are standard 8 bit binary strings unless they contain Unicode chars or a `\u####` escape code that doesn't map to the range 0..255.

However calling E.asUTF8 will convert one of those strings to UTF8.

```

var s = String.fromCharCode(0xF0,0x9F,0x8D,0x94);
var u = E.asUTF8(s);
s.length // 4
s[0] // "\xF0"
u.length // 1
u[0] // hamburger emoji
```

**NOTE:** UTF8 is currently only available on Bangle.js devices

**Note:** This is not available in devices with low flash memory

### [E.clip](#t_l_E_clip) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L372 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.clip(x, min, max)`

#### Parameters

`x` - A floating point value to clip

`min` - The smallest the value should be

`max` - The largest the value should be

#### Returns

The value of x, clipped so as not to be below min or above max.

#### Description

Clip a number to be between min and max (inclusive)

**Note:** This is not available in devices with low flash memory

### [event E.comparator](#t_l_E_comparator) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L773 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('comparator', function(dir) { ... });`

#### Parameters

`dir` - The direction of the pin's state change

#### Description

Called when a bit rises or falls above a set level. See `[E.setComparator](#l_E_setComparator)` for setup.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) with not devices with low flash memory

### [E.compiledC](#t_l_E_compiledC) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2400 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.compiledC(code)`

#### Parameters

`code` - A Templated string of C code

#### Description

Provides the ability to write C code inside your JavaScript file.

**This function is not part of Espruino**. Instead, it is detected by the Espruino IDE (or command-line tools) at upload time, is sent to our web service to be compiled, and is replaced with machine code and an `[E.nativeCall](#l_E_nativeCall)` call.

See [the documentation on Inline C](http://www.espruino.com/InlineC) for more information and examples.

**Note:** This is not available in devices with low flash memory

### [E.convolve](#t_l_E_convolve) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L466 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.convolve(arr1, arr2, offset)`

#### Parameters

`arr1` - An array to convolve

`arr2` - An array to convolve

`offset` - The mean value of the array

#### Returns

The variance of the given buffer

#### Description

Convolve arr1 with arr2. This is equivalent to

```
v=0;for (i in arr1) v+=arr1[i] *
arr2[(i+offset) % arr2.length]
```

**Note:** This is not available in devices with low flash memory

### [E.CRC32](#t_l_E_CRC32) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2051 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.CRC32(data)`

#### Parameters

`data` - Iterable data to perform CRC32 on (each element treated as a byte)

#### Returns

The CRC of the supplied data

#### Description

Perform a standard 32 bit CRC (Cyclic redundancy check) on the supplied data (one byte at a time) and return the result as an unsigned integer.

**Note:** This is not available in devices with low flash memory

### [E.decodeUTF8](#t_l_E_decodeUTF8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2784 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.decodeUTF8(str, lookup, replaceFn)`

#### Parameters

`str` - A string of UTF8-encoded data

`lookup` - An array containing a mapping of character code -> replacement string

`replaceFn` - If not in lookup, `replaceFn(charCode)` is called and the result used if it's a function, _or_ if it's a string, the string value is used

#### Returns

A string containing all UTF8 sequences flattened to 8 bits

#### Description

Decode a UTF8 string.

-   Any decoded character less than 256 gets passed straight through
-   Otherwise if `lookup` is an array and an item with that char code exists in `lookup` then that is used
-   Otherwise if `lookup` is an object and an item with that char code (as lowercase hex) exists in `lookup` then that is used
-   Otherwise `replaceFn(charCode)` is called and the result used if `replaceFn` is a function
-   If `replaceFn` is a string, that is used
-   Or finally if nothing else matches, the character is ignored

For instance:

```

let unicodeRemap = {
  0x20ac:"\u0080", // Euro symbol
  0x2026:"\u0085", // Ellipsis
};
E.decodeUTF8("UTF-8 Euro: \u00e2\u0082\u00ac", unicodeRemap, '[?]') == "UTF-8 Euro: \u0080"
```

**Note:** This is not available in devices with low flash memory

### [E.defrag](#t_l_E_defrag) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1721 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.defrag()`

#### Description

This defragment's Espruino's memory.

While Espruino does a lot of work to avoid fragmentation (variables spread over memory) and can usually work around it (such as by allocating data in chunks) sometimes it is useful to be able to allocate a large contiguous chunk of memory, and if memory is low and has been fragmented it may need defragmenting in order to find that chunk.

See `[E.dumpFragmentation()](#l_E_dumpFragmentation)` to show a map of the arrangement of variables within memory.

**Note:** This is not available in devices with low flash memory

### [E.dumpFragmentation](#t_l_E_dumpFragmentation) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1613 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.dumpFragmentation()`

#### Description

Show fragmentation. As of 2v27 this stops at the last allocated variable so as to avoid outputting blank lines if memory isn't full.

-   is free space
-   `#` is a normal variable
-   `L` is a locked variable (address used, cannot be moved)
-   `=` represents data in a Flat String (must be contiguous)

**Note:** This is not available in devices with low flash memory

### [E.dumpFreeList](#t_l_E_dumpFreeList) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1597 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.dumpFreeList()`

#### Description

Dump any locked variables that aren't referenced from `[global](#l__global_global)` - for debugging memory leaks only.

**Note:** This is not available in release builds

### [E.dumpLockedVars](#t_l_E_dumpLockedVars) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1576 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.dumpLockedVars()`

#### Description

Dump any locked variables that aren't referenced from `[global](#l__global_global)` - for debugging memory leaks only.

**Note:** This does a linear scan over memory, finding variables that are currently locked. In some cases it may show variables like `Unknown 66` which happen when _part_ of a string has ended up placed in memory ahead of the String that it's part of. See https://github.com/espruino/Espruino/issues/2345

**Note:** This is not available in release builds

### [E.dumpStr](#t_l_E_dumpStr) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2003 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.dumpStr()`

#### Returns

A String

#### Description

Get the current interpreter state in a text form such that it can be copied to a new device

**Note:** This is not available in devices with low flash memory

### [E.dumpVariables](#t_l_E_dumpVariables) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1660 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.dumpVariables()`

#### Description

Dumps a comma-separated list of all allocated variables along with the variables they link to. Can be used to visualise where memory is used.

**Note:** This is not available in devices with low flash memory

### [E.enableWatchdog](#t_l_E_enableWatchdog) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L702 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.enableWatchdog(timeout, isAuto)`

#### Parameters

`timeout` - The timeout in seconds before a watchdog reset

`isAuto` - If undefined or true, the watchdog is kicked automatically. If not, you must call `[E.kickWatchdog()](#l_E_kickWatchdog)` yourself

#### Description

Enable the watchdog timer. This will reset Espruino if it isn't able to return to the idle loop within the timeout.

If `isAuto` is false, you must call `[E.kickWatchdog()](#l_E_kickWatchdog)` yourself every so often or the chip will reset.

```

E.enableWatchdog(0.5); // automatic mode
while(1); // Espruino will reboot because it has not been idle for 0.5 sec
```

```

E.enableWatchdog(1, false);
setInterval(function() {
  if (everything_ok)
    E.kickWatchdog();
}, 500);
// Espruino will now reset if everything_ok is false,
// or if the interval fails to be called
```

**NOTE:** This is only implemented on STM32, nRF5x and ESP32 devices (all official Espruino boards).

**NOTE:_\* On STM32 (Pico, WiFi, Original) with `setDeepSleep(1)` you need to explicitly wake Espruino up with an interval of less than the watchdog timeout or the watchdog will fire and the board will reboot. You can do this with `setInterval("", time_in_milliseconds)`. \*_NOTE:** On ESP32, the timeout will be rounded to the nearest second.

**Note:** This is not available in devices with low flash memory

### [event E.errorFlag](#t_l_E_errorFlag) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L90 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('errorFlag', function(errorFlags) { ... });`

#### Parameters

`errorFlags` - An array of new error flags, as would be returned by `[E.getErrorFlags()](#l_E_getErrorFlags)`. Error flags that were present before won't be reported.

#### Description

This event is called when an error is created by Espruino itself (rather than JS code) which changes the state of the error flags reported by `[E.getErrorFlags()](#l_E_getErrorFlags)`

This could be low memory, full buffers, UART overflow, etc. `[E.getErrorFlags()](#l_E_getErrorFlags)` has a full description of each type of error.

This event will only be emitted when error flag is set. If the error flag was already set nothing will be emitted. To clear error flags so that you do get a callback each time a flag is set, call `[E.getErrorFlags()](#l_E_getErrorFlags)`.

### [E.FFT](#t_l_E_FFT) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L604 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.FFT(arrReal, arrImage, inverse)`

#### Parameters

`arrReal` - An array of real values

`arrImage` - An array of imaginary values (or if undefined, all values will be taken to be 0)

`inverse` - Set this to true if you want an inverse FFT - otherwise leave as 0

#### Description

Performs a Fast Fourier Transform (FFT) in 32 bit floats on the supplied data and writes it back into the original arrays. Note that if only one array is supplied, the data written back is the modulus of the complex result `sqrt(r*r+i*i)`.

In order to perform the FFT, there has to be enough room on the stack to allocate two arrays of 32 bit floating point numbers - this will limit the maximum size of FFT possible to around 1024 items on most platforms.

**Note:** on the Original Espruino board, FFTs are performed in 64bit arithmetic as there isn't space to include the 32 bit maths routines (2x more RAM is required).

**Note:** This is not available in devices with low flash memory

### [E.fromUTF8](#t_l_E_fromUTF8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1167 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.fromUTF8(str)`

#### Parameters

`str` - The string to check

#### Returns

A String

#### Description

Given a UTF8 String (see `[E.asUTF8](#l_E_asUTF8)`) this returns the underlying representation of that String.

```

E.fromUTF8("\u03C0") == "\xCF\x80"
```

**NOTE:** UTF8 is currently only available on Bangle.js devices

**Note:** This is not available in devices with low flash memory

### [E.getAddressOf](#t_l_E_getAddressOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1822 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getAddressOf(v, flatAddress)`

#### Parameters

`v` - A variable to get the address of

`flatAddress` - (boolean) If `true` and a Flat String or Flat ArrayBuffer is supplied, return the address of the data inside it - otherwise 0. If `false` (the default) return the address of the JsVar itself.

#### Returns

The address of the given variable

#### Description

Return the address in memory of the given variable. This can then be used with `peek` and `poke` functions. However, changing data in JS variables directly (flatAddress=false) will most likely result in a crash.

This functions exists to allow embedded targets to set up peripherals such as DMA so that they write directly to JS variables.

See http://www.espruino.com/Internals for more information

**Note:** This is not available in devices with low flash memory

### [E.getAnalogVRef](#t_l_E_getAnalogVRef) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L227 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getAnalogVRef()`

#### Returns

The voltage (in Volts) that a reading of 1 from `[analogRead](#l__global_analogRead)` actually represents - usually around 3.3v

#### Description

Check the internal voltage reference. To work out an actual voltage of an input pin, you can use `analogRead(pin)*E.getAnalogVRef()`

**Note:** This value is calculated by reading the voltage on an internal voltage reference with the ADC. It will be slightly noisy, so if you need this for accurate measurements we'd recommend that you call this function several times and average the results.

While this is implemented on Espruino boards, it may not be implemented on other devices. If so it'll return NaN.

**Note:** This is not available in devices with low flash memory

### [E.getBattery](#t_l_E_getBattery) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2553 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getBattery()`

#### Returns

A percentage between 0 and 100

#### Description

In devices that come with batteries, this function returns the battery charge percentage as an integer between 0 and 100.

**Note:** this is an estimation only, based on battery voltage. The temperature of the battery (as well as the load being drawn from it at the time `[E.getBattery](#l_E_getBattery)` is called) will affect the readings.

**Note:** This is only available in Puck.js devices and Pixl.js boards and Bangle.js smartwatches

### [E.getClock](#t_l_E_getClock) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1442 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getClock()`

#### Returns

An object containing information about the current clock

#### Description

On boards other than STM32 this currently just returns `undefined`

### STM32

See `[E.setClock](#l_E_setClock)` for more information.

Returns:

```

{
  sysclk, hclk, pclk1, pclk2,  // various clocks in Hz
  M, N, P, Q, PCLK1, PCLK2     // STM32F4: currently set divisors
  RTCCLKSource : "LSI/LSE/HSE_Div#" // STM32F4 source for RTC clock
}
```

**Note:** This is not available in devices with low flash memory

### [E.getConsole](#t_l_E_getConsole) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1535 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getConsole()`

#### Returns

The current console device as a string, or just `null` if the console is null

#### Description

Returns the current console device - see `[E.setConsole](#l_E_setConsole)` for more information.

### [E.getErrorFlags](#t_l_E_getErrorFlags) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L859 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getErrorFlags()`

#### Returns

An array of error flags

#### Description

Get and reset the error flags. Returns an array that can contain:

`'FIFO_FULL'`: The receive FIFO filled up and data was lost. This could be state transitions for setWatch, or received characters.

`'BUFFER_FULL'`: A buffer for a stream filled up and characters were lost. This can happen to any stream - Serial,HTTP,etc.

`'CALLBACK'`: A callback (`[setWatch](#l__global_setWatch)`, `[setInterval](#l__global_setInterval)`, `on('data',...)`) caused an error and so was removed.

`'LOW_MEMORY'`: Memory is running low - Espruino had to run a garbage collection pass or remove some of the command history

`'MEMORY'`: Espruino ran out of memory and was unable to allocate some data that it needed.

`'UART_OVERFLOW'` : A UART received data but it was not read in time and was lost

**Note:** This is not available in devices with low flash memory

### [E.getFlags](#t_l_E_getFlags) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L902 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getFlags()`

#### Returns

An object containing flag names and their values

#### Description

Get Espruino's interpreter flags that control the way it handles your JavaScript code.

-   `deepSleep` - Allow deep sleep modes (also set by setDeepSleep)
-   `pretokenise` - When adding functions, pre-minify them and tokenise reserved words
-   `unsafeFlash` - Some platforms stop writes/erases to interpreter memory to stop you bricking the device accidentally - this removes that protection
-   `unsyncFiles` - When writing files, _don't_ flush all data to the SD card after each command (the default is _to_ flush). This is much faster, but can cause filesystem damage if power is lost without the filesystem unmounted.
-   `jitDebug` - When JIT compiling, outputs debug info to the console
-   `onErrorSave` - (2v27+) when an uncaught error occurs, write it to a file called `ERROR` in Storage (the file is not updated)
-   `onErrorFlash` - (2v27+) when an uncaught error occurs, flash the red LED for 200ms (only on devices with a physical LED)

### [E.getPowerUsage](#t_l_E_getPowerUsage) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2709 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getPowerUsage()`

#### Returns

An object detailing power usage in microamps

#### Description

This function returns an object detailing the current **estimated** power usage of the Espruino device in microamps (uA). It is not intended to be a replacement for measuring actual power consumption, but can be useful for finding obvious power draws.

Where an Espruino device has outputs that are connected to other things, those are not included in the power usage figures.

Results look like:

```

{
  device: {
    CPU : 2000, // microcontroller
    LCD : 100, // LCD
    // ...
  },
  total : 5500 // estimated usage in microamps
}
```

**Note:** Currently only nRF52-based devices have variable CPU power usage figures. These are based on the time passed for each SysTick event, so under heavy usage the figure will update within 0.3s, but under low CPU usage it could take minutes for the CPU usage figure to update.

**Note:** On Jolt.js we take account of internal resistance on H0/H2/H4/H6 where we can measure voltage. H1/H3/H5/H7 cannot be measured.

**Note:** This is not available in devices with low flash memory

### [E.getSizeOf](#t_l_E_getSizeOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1747 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getSizeOf(v, depth)`

#### Parameters

`v` - A variable to get the size of

`depth` - The depth that detail should be provided for. If depth<=0 or undefined, a single integer will be returned

#### Returns

Information about the variable size - see below

#### Description

Return the number of variable blocks used by the supplied variable. This is useful if you're running out of memory and you want to be able to see what is taking up most of the available space.

If `depth>0` and the variable can be recursed into, an array listing all property names (including internal Espruino names) and their sizes is returned. If `depth>1` there is also a `more` field that inspects the objects' children's children.

For instance `E.getSizeOf(function(a,b) { })` returns `5`.

But `E.getSizeOf(function(a,b) { }, 1)` returns:

```

 [
  {
    "name": "a",
    "size": 1 },
  {
    "name": "b",
    "size": 1 },
  {
    "name": "\xFFcod",
    "size": 2 }
 ]
```

In this case setting depth to `2` will make no difference as there are no more children to traverse.

See http://www.espruino.com/Internals for more information

**Note:** This is not available in devices with low flash memory

### [E.getTemperature](#t_l_E_getTemperature) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L196 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getTemperature(internal)`

#### Parameters

`internal` - On Puck.js (where there is an external temperature sensor), set to true to use the internal microcontroller temperature sensor, false to use the external sensor. On other devices this parameter is ignored.

#### Returns

The temperature in degrees C

#### Description

Use the microcontroller's internal thermistor to work out the temperature.

On Puck.js v2.0 this will use the on-board PCT2075TP temperature sensor, but on other devices it may not be desperately well calibrated.

While this is implemented on Espruino boards, it may not be implemented on other devices. If so it'll return NaN.

**Note:_\* This is not entirely accurate and varies by a few degrees from chip to chip. It measures the \*_die temperature**, so when connected to USB it could be reading 10 over degrees C above ambient temperature. When running from battery with `setDeepSleep(true)` it is much more accurate though.

### [E.getVDDH](#t_l_E_getVDDH) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L247 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.getVDDH()`

#### Returns

The voltage on VDDH input

#### Description

Return the voltage on VDDH input

**Note:** This value is calculated by reading the voltage on an internal voltage reference with the ADC. It will be slightly noisy, so if you need this for accurate measurements we'd recommend that you call this function several times and average the results.

**Note:** This is only available in NRF52833 and NRF52840

### [E.HSBtoRGB](#t_l_E_HSBtoRGB) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2080 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.HSBtoRGB(hue, sat, bri, format)`

#### Parameters

`hue` - The hue, as a value between 0 and 1

`sat` - The saturation, as a value between 0 and 1

`bri` - The brightness, as a value between 0 and 1

`format` - If `true` or `1`, return an array of \[R,G,B\] values betwen 0 and 255. If `16`, return a 16 bit number. `undefined`/`24` is the same as normal (returning a 24 bit number)

#### Returns

A 24 bit number containing bytes representing red, green, and blue `0xBBGGRR`. Or if `asArray` is true, an array `[R,G,B]`

#### Description

Convert hue, saturation and brightness to red, green and blue (packed into an integer if `asArray==false` or an array if `asArray==true`).

This replaces `Graphics.setColorHSB` and `Graphics.setBgColorHSB`. On devices with 24 bit colour it can be used as: `Graphics.setColor(E.HSBtoRGB(h, s, b))`, or on devices with 26 bit colour use `Graphics.setColor(E.HSBtoRGB(h, s, b, 16))`

You can quickly set RGB items in an Array or Typed Array using `array.set(E.HSBtoRGB(h, s, b, true), offset)`, which can be useful with arrays used with `require("neopixel").write`.

**Note:** This is not available in devices with low flash memory

### [E.hwRand](#t_l_E_hwRand) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2038 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.hwRand()`

#### Returns

A random number

#### Description

Unlike 'Math.random()' which uses a pseudo-random number generator, this method reads from the internal voltage reference several times, XOR-ing and rotating to try and make a relatively random value from the noise in the signal.

**Note:** This is not available in devices with low flash memory

### [event E.init](#t_l_E_init) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L49 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('init', function() { ... });`

#### Description

This event is called right after the board starts up, and has a similar effect to creating a function called `onInit`.

For example to write `"Hello World"` every time Espruino starts, use:

```

E.on('init', function() {
  console.log("Hello World!");
});
```

**Note:_\* that subsequent calls to `E.on('init',` will \*_add** a new handler, rather than replacing the last one. This allows you to write modular code - something that was not possible with `onInit`.

### [E.internal](#t_l_E_internal) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L182 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.internal`

#### Returns

The 'hidden root'

#### Description

(2v28+) A reference to the "hidden root" that contains internal Espruino JavaScript variables such as lists of timers and watches.

On earlier firmwares this was accessible via `global["\xff"]`

### [E.isUTF8](#t_l_E_isUTF8) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1197 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.isUTF8(str)`

#### Parameters

`str` - The string to check

#### Returns

True if the given String is treated as UTF8 by Espruino

#### Description

By default, strings in Espruino are standard 8 bit binary strings unless they contain Unicode chars or a `\u####` escape code that doesn't map to the range 0..255.

This checks if a String is being treated by Espruino as a UTF8 String

See `[E.asUTF8](#l_E_asUTF8)` to convert to a UTF8 String

**NOTE:** UTF8 is currently only available on Bangle.js devices

**Note:** This is not available in devices with low flash memory

### [E.kickWatchdog](#t_l_E_kickWatchdog) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L753 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.kickWatchdog()`

#### Description

Kicks a Watchdog timer set up with `E.enableWatchdog(..., false)`. See `[E.enableWatchdog](#l_E_enableWatchdog)` for more information.

**NOTE:** This is only implemented on STM32 and nRF5x devices (all official Espruino boards).

**Note:** This is not available in devices with low flash memory

### [event E.kill](#t_l_E_kill) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L69 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('kill', function() { ... });`

#### Description

This event is called just before the device shuts down for commands such as `[reset()](#l__global_reset)`, `[load()](#l__global_load)`, `save()`, `[E.reboot()](#l_E_reboot)` or `[Bangle.off()](#l_Bangle_off)`

For example to write `"Bye!"` just before shutting down use:

```

E.on('kill', function() {
  console.log("Bye!");
});
```

**NOTE:** This event is not called when the device is 'hard reset' - for example by removing power, hitting an actual reset button, or via a Watchdog timer reset.

### [E.lockConsole](#t_l_E_lockConsole) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2198 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.lockConsole()`

#### Description

If a password has been set with `[E.setPassword()](#l_E_setPassword)`, this will lock the console so the password needs to be entered to unlock it.

**Note:** This is not available in devices with low flash memory

### [E.lookupNoCase](#t_l_E_lookupNoCase) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1971 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.lookupNoCase(haystack, needle, returnKey)`

#### Parameters

`haystack` - The Array/Object/Function to search

`needle` - The key to search for

`returnKey` - If true, return the key, else return the value itself

#### Returns

The value in the Object matching 'needle', or if `returnKey==true` the key's name - or undefined

#### Description

Search in an Object, Array, or Function

### [E.mapInPlace](#t_l_E_mapInPlace) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1851 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.mapInPlace(from, to, map, bits)`

#### Parameters

`from` - An ArrayBuffer to read elements from

`to` - An ArrayBuffer to write elements too

`map` - An array or `function(value,index)` to use to map one element to another, or `undefined` to provide no mapping

`bits` - If specified, the number of bits per element (MSB first) - otherwise use a 1:1 mapping. If negative, use LSB first.

#### Description

Take each element of the `from` array, look it up in `map` (or call `map(value,index)` if it is a function), and write it into the corresponding element in the `to` array.

You can use an array to map:

```

var a = new Uint8Array([1,2,3,1,2,3]);
var lut = new Uint8Array([128,129,130,131]);
E.mapInPlace(a, a, lut);
// a = [129, 130, 131, 129, 130, 131]
```

Or `undefined` to pass straight through, or a function to do a normal 'mapping':

```

var a = new Uint8Array([0x12,0x34,0x56,0x78]);
var b = new Uint8Array(8);
E.mapInPlace(a, b, undefined); // straight through
// b = [0x12,0x34,0x56,0x78,0,0,0,0]
E.mapInPlace(a, b, (value,index)=>index); // write the index in the first 4 (because a.length==4)
// b = [0,1,2,3,4,0,0,0]
E.mapInPlace(a, b, undefined, 4); // 4 bits from 8 bit input -> 2x as many outputs, msb-first
// b = [1, 2, 3, 4, 5, 6, 7, 8]
 E.mapInPlace(a, b, undefined, -4); // 4 bits from 8 bit input -> 2x as many outputs, lsb-first
// b = [2, 1, 4, 3, 6, 5, 8, 7]
E.mapInPlace(a, b, a=>a+2, 4);
// b = [3, 4, 5, 6, 7, 8, 9, 10]
var b = new Uint16Array(4);
E.mapInPlace(a, b, undefined, 12); // 12 bits from 8 bit input, msb-first
// b = [0x123, 0x456, 0x780, 0]
E.mapInPlace(a, b, undefined, -12); // 12 bits from 8 bit input, lsb-first
// b = [0x412, 0x563, 0x078, 0]
```

**Note:** This is not available in devices with low flash memory

### [E.memoryArea](#t_l_E_memoryArea) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1332 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.memoryArea(addr, len)`

#### Parameters

`addr` - The address of the memory area

`len` - The length (in bytes) of the memory area

#### Returns

A String

#### Description

This creates and returns a special type of string, which references a specific address in memory. It can be used in order to use sections of Flash memory directly in Espruino (for example `[Storage](#Storage)` uses it to allow files to be read directly from Flash).

**Note:** As of 2v21, Calling `[E.memoryArea](#l_E_memoryArea)` with an address of 0 will return `undefined`

### [E.memoryMap](#t_l_E_memoryMap) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2333 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.memoryMap(baseAddress, registers)`

#### Parameters

`baseAddress` - The base address (added to every address in `registers`)

`registers` - An object containing `{name:address}`

#### Returns

An object where each field is memory-mapped to a register.

#### Description

Create an object where every field accesses a specific 32 bit address in the microcontroller's memory. This is perfect for accessing on-chip peripherals.

```

// for NRF52 based chips
var GPIO = E.memoryMap(0x50000000,{OUT:0x504, OUTSET:0x508, OUTCLR:0x50C, IN:0x510, DIR:0x514, DIRSET:0x518, DIRCLR:0x51C});
GPIO.DIRSET = 1; // set GPIO0 to output
GPIO.OUT ^= 1; // toggle the output state of GPIO0
```

**Note:** This is not available in devices with low flash memory

### [E.nativeCall](#t_l_E_nativeCall) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L284 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.nativeCall(addr, sig, data)`

#### Parameters

`addr` - The address in memory of the function (or offset in `data` if it was supplied

`sig` - The signature of the call, `returnType (arg1,arg2,...)`. Allowed types are `void`,`bool`,`int`,`double`,`float`,`[Pin](#Pin)`,`JsVar`

`data` - (Optional) A string containing the function itself. If not supplied then 'addr' is used as an absolute address.

#### Returns

The native function

#### Description

ADVANCED: It's very easy to crash Espruino using this function if you get the code/arguments you supply wrong!

Create a native function that executes the code at the given address, e.g. `E.nativeCall(0x08012345,'double (double,double)')(1.1, 2.2)`

If you're executing a thumb function, you'll almost certainly need to set the bottom bit of the address to 1.

Note it's not guaranteed that the call signature you provide can be used - there are limits on the number of arguments allowed (5).

When supplying `data`, if it is a 'flat string' then it will be used directly, otherwise it'll be converted to a flat string and used.

The argument types in `sig` are:

-   `void` - returns nothing
-   `bool` - boolean value
-   `int` - 32 bit integer
-   `double` - 64 bit floating point
-   `float` - 32 bit floating point (2v21 and later)
-   `[Pin](#Pin)` - Espruino 'pin' value (8 bit integer)
-   `JsVar` - Pointer to an Espruino JsVar structure

**Note:** This is not available in devices with low flash memory

### [event E.packet](#t_l_E_packet) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L137 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('packet', function(event) { ... });`

#### Parameters

`event` - The decoded JSON object representing the packet

#### Description

\[2v25+\] Called when a packet of type `EVENT` is received via [Espruino's packet upload mechanism](https://github.com/espruino/Espruino/blob/master/README_Protocol.md)

The packet's contents are decoded as RJSON (fields without quotes are allowed like `{a:1}`) and passed into this event.

```

E.on('packet', e => {
  console.log("Packet received:", e);
});
```

### [event E.packetUpload](#t_l_E_packetUpload) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L155 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('packetUpload', function(event) { ... });`

#### Parameters

`event` - An object containing `{ l : int, o : int, s : int, fn : string }`

#### Description

\[2v29+\] Called when a file is uploaded via [Espruino's packet upload mechanism](https://github.com/espruino/Espruino/blob/master/README_Protocol.md)

This is used by `[E.showMessage](#l_E_showMessage)` for Bangle.js to show upload progress.

```

{
  l : int, // bytes uploaded in this one packet
  o : int, // bytes uploaded so far in the file
  s : int, // total size of the file being uploaded
  fn : string // filename being uploaded
}
```

```

E.on('packetUpload', e => {
  console.log("Uploaded ${e.o}/${e.s} bytes to "+e.fn);
});
```

### [E.pipe](#t_l_E_pipe) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L945 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.pipe(source, destination, options)`

#### Parameters

`source` - The source file/stream that will send content. As of 2v19 this can also be a `[String](#String)`

`destination` - The destination file/stream that will receive content from the source.

`options` - \[optional\] An object `{ chunkSize : int=64, end : bool=true, complete : function }`  
chunkSize : The amount of data to pipe from source to destination at a time  
complete : a function to call when the pipe activity is complete  
end : call the 'end' function on the destination when the source is finished

#### Description

Pipe one stream to another.

This can be given any object with a `read` method as a source, and any object with a `.write(data)` method as a destination.

Data will be piped from `source` to `destination` in the idle loop until `source.read(...)` returns `undefined`.

For instance:

```

// Print a really big string to the console, 1 character at a time and write 'Finished!' at the end
E.pipe("This is a really big String",
       {write: print},
       {chunkSize:1, complete:()=>print("Finished!")});
// Pipe the numbers 1 to 100 to a StorageFile in Storage
E.pipe({ n:0, read : function() { if (this.n<100) return (this.n++)+"\n"; }},
       require("Storage").open("testfile","w"));
// Pipe a StorageFile straight to the Bluetooth UART
E.pipe(require("Storage").open("testfile","r"), Bluetooth);
// Pipe a normal file in Storage (not StorageFile) straight to the Bluetooth UART
E.pipe(require("Storage").read("blob.txt"), Bluetooth);
// Pipe a normal file in Storage as a response to an HTTP request
function onPageRequest(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  E.pipe(require("Storage").read("webpage.txt"), res);
}
require("http").createServer(onPageRequest).listen(80);
```

**Note:** This is not available in devices with low flash memory

### [E.reboot](#t_l_E_reboot) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2425 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.reboot()`

#### Description

Forces a hard reboot of the microcontroller - as close as possible to if the reset pin had been toggled.

**Note:** This is different to `[reset()](#l__global_reset)`, which performs a software reset of Espruino (resetting the interpreter and pin states, but not all the hardware)

### [E.reverseByte](#t_l_E_reverseByte) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1552 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.reverseByte(x)`

#### Parameters

`x` - A byte value to reverse the bits of

#### Returns

The byte with reversed bits

#### Description

Reverse the 8 bits in a byte, swapping MSB and LSB.

For example, `E.reverseByte(0b10010000) == 0b00001001`.

Note that you can reverse all the bytes in an array with:

```
arr =
arr.map(E.reverseByte)
```

**Note:** This is not available in devices with low flash memory

### [E.setBootCode](#t_l_E_setBootCode) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1358 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.setBootCode(code, alwaysExec)`

#### Parameters

`code` - The code to execute (as a string)

`alwaysExec` - Whether to always execute the code (even after a reset)

#### Description

This writes JavaScript code into Espruino's flash memory, to be executed on startup. It differs from `save()` in that `save()` saves the whole state of the interpreter, whereas this just saves JS code that is executed at boot.

Code will be executed before `onInit()` and `E.on('init', ...)`.

If `alwaysExec` is `true`, the code will be executed even after a call to `[reset()](#l__global_reset)`. This is useful if you're making something that you want to program, but you want some code that is always built in (for instance setting up a display or keyboard).

To remove boot code that has been saved previously, use `E.setBootCode("")`

**Note:** this removes any code that was previously saved with `save()`

### [E.setClock](#t_l_E_setClock) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1392 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.setClock(options)`

#### Parameters

`options` - Platform-specific options for setting clock speed

#### Returns

The actual frequency the clock has been set to

#### Description

This sets the clock frequency of Espruino's processor. It will return `0` if it is unimplemented or the clock speed cannot be changed.

**Note:** On pretty much all boards, UART, SPI, I2C, PWM, etc will change frequency and will need setting up again in order to work.

### STM32F4

Options is of the form `{ M: int, N: int, P: int, Q: int }` - see the 'Clocks' section of the microcontroller's reference manual for what these mean.

-   System clock = 8Mhz \* N / ( M \* P )
-   USB clock (should be 48Mhz) = 8Mhz \* N / ( M \* Q )

Optional arguments are:

-   `latency` - flash latency from 0..15
-   `PCLK1` - Peripheral clock 1 divisor (default: 2)
-   `PCLK2` - Peripheral clock 2 divisor (default: 4)

The Pico's default is `{M:8, N:336, P:4, Q:7, PCLK1:2, PCLK2:4}`, use

```
{M:8,
N:336, P:8, Q:7, PCLK:1, PCLK2:2}
```

to halve the system clock speed while keeping the peripherals running at the same speed (omitting PCLK1/2 will lead to the peripherals changing speed too).

On STM32F4 boards (e.g. Espruino Pico), the USB clock needs to be kept at 48Mhz or USB will fail to work. You'll also experience USB instability if the processor clock falls much below 48Mhz.

### ESP8266

Just specify an integer value, either 80 or 160 (for 80 or 160Mhz)

**Note:** This is not available in devices with low flash memory

### [E.setComparator](#t_l_E_setComparator) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L801 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.setComparator(pin, level)`

#### Parameters

`pin` - The `[Pin](#Pin)` to enable the comparator on

`level` - The level to trigger on, or `undefined` to disable. (see below for [Jolt.js](https://www.espruino.com/Jolt.js))

#### Description

(Added 2v25) Enable the nRF52 chip's `LPCOMP` hardware. When enabled, it creates an `E.on("comparator", ...)` event whenever the pin supplied rises or falls past the setpoint given (with 50mv hysteresis).

```

E.setComparator(D28, 8/16); // compare with VDD/2
E.on("comparator", e => {
  print(e); // 1 for up, or -1 for down
});
```

**Note:** There is just one LPCOMP, so you can only enable the comparator on one pin.

**On [Jolt.js](https://www.espruino.com/Jolt.js):** when using `[E.setComparator](#l_E_setComparator)` on the analog pins on the Terminal block (`H0`/`H2`/`H4`/`H6`), the `level` you give needs to be in volts. Because the comparator only works in 16 steps, you can only detect multiples of 1.37v (1.37/2.74/4.11/etc)

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) with not devices with low flash memory

### [E.setConsole](#t_l_E_setConsole) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1471 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.setConsole(device, options)`

#### Parameters

`device` -

`options` - \[optional\] object of options, see below

#### Description

Changes the device that the JS console (otherwise known as the REPL) is attached to. If the console is on a device, that device can be used for programming Espruino.

Rather than calling `[Serial.setConsole](#l_Serial_setConsole)` you can call `E.setConsole("DeviceName")`.

This is particularly useful if you just want to remove the console. `[E.setConsole(null)](#l_E_setConsole)` will make the console completely inaccessible.

`device` may be `"Serial1"`,`"USB"`,`"Bluetooth"`,`"Telnet"`,`"Terminal"`, any other _hardware_ `[Serial](#Serial)` device, or `null` to disable the console completely.

`options` is of the form:

```

{
  force : bool // default false, force the console onto this device so it does not move
               //   if false, changes in connection state (e.g. USB/Bluetooth) can move
               //   the console automatically.
}
```

**Note:** This is not available in devices with low flash memory

### [E.setDST](#t_l_E_setDST) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2247 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.setDST(params, ...)`

#### Parameters

`params, ...` - An array containing the settings for DST, or `undefined` to disable

#### Description

Set the daylight savings time parameters to be used with `[Date](#Date)` objects.

The parameters are - dstOffset: The number of minutes daylight savings time adds to the clock (usually 60) - set to 0 to disable DST - timezone: The time zone, in minutes, when DST is not in effect - positive east of Greenwich - startDowNumber: The index of the day-of-week in the month when DST starts - 0 for first, 1 for second, 2 for third, 3 for fourth and 4 for last - startDow: The day-of-week for the DST start calculation - 0 for Sunday, 6 for Saturday - startMonth: The number of the month that DST starts - 0 for January, 11 for December - startDayOffset: The number of days between the selected day-of-week and the actual day that DST starts - usually 0 - startTimeOfDay: The number of minutes elapsed in the day before DST starts - endDowNumber: The index of the day-of-week in the month when DST ends - 0 for first, 1 for second, 2 for third, 3 for fourth and 4 for last - endDow: The day-of-week for the DST end calculation - 0 for Sunday, 6 for Saturday - endMonth: The number of the month that DST ends - 0 for January, 11 for December - endDayOffset: The number of days between the selected day-of-week and the actual day that DST ends - usually 0 - endTimeOfDay: The number of minutes elapsed in the day before DST ends

To determine what the `dowNumber, dow, month, dayOffset, timeOfDay` parameters should be, start with a sentence of the form "DST starts on the last Sunday of March (plus 0 days) at 03:00". Since it's the last Sunday, we have startDowNumber = 4, and since it's Sunday, we have startDow = 0. That it is March gives us startMonth = 2, and that the offset is zero days, we have startDayOffset = 0. The time that DST starts gives us startTimeOfDay = 3\*60.

"DST ends on the Friday before the second Sunday in November at 02:00" would give us endDowNumber=1, endDow=0, endMonth=10, endDayOffset=-2 and endTimeOfDay=120.

Using Ukraine as an example, we have a time which is 2 hours ahead of GMT in winter (EET) and 3 hours in summer (EEST). DST starts at 03:00 EET on the last Sunday in March, and ends at 04:00 EEST on the last Sunday in October. So someone in Ukraine might call `E.setDST(60,120,4,0,2,0,180,4,0,9,0,240);`

Examples:

```

// United Kingdom
E.setDST(60,0,4,0,2,0,60,4,0,9,0,120);
// California, USA
E.setDST(60,-480,1,0,2,0,120,0,0,10,0,120);
// Or adjust -480 (-8 hours) for other US states
// Ukraine
E.setDST(60,120,4,0,2,0,180,4,0,9,0,240);
```

**Note:** This is not compatible with `[E.setTimeZone()](#l_E_setTimeZone)`. Calling `[E.setTimeZone()](#l_E_setTimeZone)` after this will disable DST.

**Note:** This is not available in ESPR_NO_DAYLIGHT\_SAVING

### [E.setFlags](#t_l_E_setFlags) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L927 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.setFlags(flags)`

#### Parameters

`flags` - An object containing flag names and boolean values. You need only specify the flags that you want to change.

#### Description

Set the Espruino interpreter flags that control the way it handles your JavaScript code.

Run `[E.getFlags()](#l_E_getFlags)` and check its description for a list of available flags and their values.

### [E.setPassword](#t_l_E_setPassword) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2165 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.setPassword(password)`

#### Parameters

`password` - The password - max 20 chars

#### Description

Set a password on the console (REPL). When powered on, Espruino will then demand a password before the console can be used. If you want to lock the console immediately after this you can call `[E.lockConsole()](#l_E_lockConsole)`

To remove the password, call this function with no arguments.

**Note:** There is no protection against multiple password attempts, so someone could conceivably try every password in a dictionary.

**Note:** This password is stored in memory in plain text. If someone is able to execute arbitrary JavaScript code on the device (e.g., you use `[eval](#l__global_eval)` on input from unknown sources) or read the device's firmware then they may be able to obtain it.

**Note:** This is not available in devices with low flash memory

### [E.setTimeZone](#t_l_E_setTimeZone) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2217 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.setTimeZone(zone)`

#### Parameters

`zone` - The time zone in hours

#### Description

Set the time zone to be used with `[Date](#Date)` objects.

For example `[E.setTimeZone(1)](#l_E_setTimeZone)` will be GMT+0100

Time can be set with `[setTime](#l__global_setTime)`.

**Note:** If daylight savings time rules have been set with `[E.setDST()](#l_E_setDST)`, calling `[E.setTimeZone()](#l_E_setTimeZone)` will remove them and move back to using a static timezone that doesn't change based on the time of year.

### [E.showAlert](#t_l_E_showAlert) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6220 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.showAlert(message, options)`

#### Parameters

`message` - A message to display. Can include newlines

`options` - \[optional\] a title for the message or an object containing options

#### Returns

A promise that is resolved when 'Ok' is pressed

#### Description

Displays a full screen prompt on the screen, with a single 'Ok' button.

When the button is pressed the promise is resolved.

```

E.showAlert("Hello").then(function() {
  print("Ok pressed");
});
// or
E.showAlert("These are\nLots of\nLines","My Title").then(function() {
  print("Ok pressed");
});
```

To remove the window, call `[E.showAlert()](#l_E_showAlert)` with no arguments.

**Note:** This is only available in Bangle.js smartwatches

### [E.showMenu](#t_l_E_showMenu) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6195 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.showMenu(menu)`

#### Parameters

`menu` - An object containing name->function mappings to to be used in a menu

#### Returns

A menu object with `draw`, `move` and `select` functions

#### Description

Display a menu on the screen, and set up the buttons to navigate through it.

Supply an object containing menu items. When an item is selected, the function it references will be executed. For example:

```

var boolean = false;
var number = 50;
// First menu
var mainmenu = {
  "" : { title : "-- Main Menu --" }, // options
  "LED On" : function() { LED1.set(); },
  "LED Off" : function() { LED1.reset(); },
  "Submenu" : function() { E.showMenu(submenu); },
  "A Boolean" : {
    value : boolean,
    format : v => v?"On":"Off",
    onchange : v => { boolean=v; }
  },
  "A Number" : {
    value : number,
    min:0,max:100,step:10,
    onchange : v => { number=v; }
  },
  "Exit" : function() { E.showMenu(); }, // remove the menu
};
// Submenu
var submenu = {
  "" : { title : "-- SubMenu --",
         back : function() { E.showMenu(mainmenu); } },
  "One" : undefined, // do nothing
  "Two" : undefined // do nothing
};
// Actually display the menu
E.showMenu(mainmenu);
```

The menu will stay onscreen and active until explicitly removed, which you can do by calling `[E.showMenu()](#l_E_showMenu)` without arguments.

See http://www.espruino.com/graphical\_menu for more detailed information.

On Bangle.js there are a few additions over the standard `graphical_menu`:

-   The options object can contain:
    -   `back : function() { }` - add a 'back' button, with the function called when it is pressed
    -   `remove : function() { }` - add a handler function to be called when the menu is removed
    -   (Bangle.js 2) `scroll : int` - an integer specifying how much the initial menu should be scrolled by
-   (Bangle.js 2) The mapped functions can consider the touch event that interacted with the entry: `"Entry" : function(touch) { ... }`
    -   This is also true of `onchange` mapped functions in entry objects: `onchange : (value, touch) => { ... }`
-   The object returned by `[E.showMenu](#l_E_showMenu)` contains:
    -   (Bangle.js 2) `scroller` - the object returned by `[E.showScroller](#l_E_showScroller)` - `scroller.scroll` returns the amount the menu is currently scrolled by
-   In the object specified for editable numbers:
    -   (Bangle.js 2) the `format` function is called with `format(value)` in the main menu, `format(value,1)` when in a scrollable list, or `format(value,2)` when in a popup window.

You can also specify menu items as an array (rather than an Object). This can be useful if you have menu items with the same title, or you want to `push` menu items onto an array:

```

var menu = [
  { title:"Something", onchange:function() { print("selected"); } },
  { title:"On or Off", value:false, onchange: v => print(v) },
  { title:"A Value", value:3, min:0, max:10, onchange: v => print(v) },
];
menu[""] = { title:"Hello" };
E.showMenu(menu);
```

**Note:** This is only available in Bangle.js smartwatches

**Note:** This is only available in Bangle.js smartwatches with Bangle.js 2 smartwatches

### [E.showMessage](#t_l_E_showMessage) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6049 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.showMessage(message, options)`

#### Parameters

`message` - A message to display. Can include newlines

`options` - \[optional\] a title for the message, or an object of options `{title:string, img:image_string}`

#### Description

A utility function for displaying a full screen message on the screen.

Draws to the screen and returns immediately.

```

E.showMessage("These are\nLots of\nLines","My Title")
```

or to display an image as well as text:

```

E.showMessage("Lots of text will wrap automatically",{
  title:"Warning",
  img:atob("FBQBAfgAf+Af/4P//D+fx/n+f5/v+f//n//5//+f//n////3//5/n+P//D//wf/4B/4AH4A=")
})
```

**Note:** This is only available in Bangle.js smartwatches

### [E.showPrompt](#t_l_E_showPrompt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6207 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.showPrompt(message, options)`

#### Parameters

`message` - A message to display. Can include newlines

`options` - \[optional\] an object of options (see below)

#### Returns

A promise that is resolved when 'Ok' is pressed

#### Description

Displays a full screen prompt on the screen, with the buttons requested (or `Yes` and `No` for defaults).

When the button is pressed the promise is resolved with the requested values (for the `Yes` and `No` defaults, `true` and `false` are returned).

```

E.showPrompt("Do you like fish?").then(function(v) {
  if (v) print("'Yes' chosen");
  else print("'No' chosen");
});
// Or
E.showPrompt("How many fish\ndo you like?",{
  title:"Fish",
  buttons : {"One":1,"Two":2,"Three":3}
}).then(function(v) {
  print("You like "+v+" fish");
});
// Or
E.showPrompt("Continue?", {
  title:"Alert",
  img:atob("FBQBAfgAf+Af/4P//D+fx/n+f5/v+f//n//5//+f//n////3//5/n+P//D//wf/4B/4AH4A=")}).then(function(v) {
  if (v) print("'Yes' chosen");
  else print("'No' chosen");
});
```

To remove the prompt, call `[E.showPrompt()](#l_E_showPrompt)` with no arguments.

The second `options` argument can contain:

```

{
  title: "Hello",                       // optional Title
  buttons : {"Ok":true,"Cancel":false}, // optional list of button text & return value
  buttonsLong : {"Ok":2,"Cancel":"Cancel"}, // Bangle.js2: optional subset of buttons that should also have a specific long press action
  img: "image_string"                   // optional image string to draw
  remove: function() { }                // Bangle.js: optional function to be called when the prompt is removed#
  buttonHeight : 30,                    // Bangle.js2: optional height to force the buttons to be
}
```

**Note:** This is only available in Bangle.js smartwatches

**Note:** This is only available in Bangle.js smartwatches with Bangle.js 2 smartwatches

### [E.showScroller](#t_l_E_showScroller) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/banglejs/jswrap_bangle.c#L6213 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.showScroller(options)`

#### Parameters

`options` - An object containing `{ h, c, draw, select, back, remove }` (see below)

#### Returns

A menu object with `draw()` and `drawItem(itemNo)` functions

#### Description

Display a scrollable menu on the screen, and set up the buttons/touchscreen to navigate through it and select items.

Supply an object containing:

```

{
  h : 24, // height of each menu item in pixels
  c : 10, // number of menu items
  // a function to draw a menu item
  draw : function(idx, rect) { ... }
  // a function to call when the item is selected, touch parameter is only relevant
  // for Bangle.js 2 and contains the coordinates touched inside the selected item
  // as well as the type of the touch - see `Bangle.touch`.
  select : function(idx, touch) { ... }
  // optional function to be called when 'back' is tapped
  back : function() { ...}
  // Bangle.js: optional function to be called when the scroller should be removed
  remove : function() {}
}
```

For example to display a list of numbers:

```

E.showScroller({
  h : 40, c : 8,
  draw : (idx, r) => {
    g.setBgColor((idx&1)?"#666":"#CCC").clearRect(r.x,r.y,r.x+r.w-1,r.y+r.h-1);
    g.setFont("6x8:2").drawString("Item Number\n"+idx,r.x+10,r.y+4);
  },
  select : (idx) => console.log("You selected ", idx)
});
```

To remove the scroller, just call `[E.showScroller()](#l_E_showScroller)`

**Note:** This is only available in Bangle.js smartwatches

**Note:** This is only available in Bangle.js smartwatches with Bangle.js 2 smartwatches

### [E.srand](#t_l_E_srand) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2025 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.srand(v)`

#### Parameters

`v` - The 32 bit integer seed to use for the random number generator

#### Description

Set the seed for the random number generator used by `[Math.random()](#l_Math_random)`.

**Note:** This is not available in devices with low flash memory

### [E.stopEventPropagation](#t_l_E_stopEventPropagation) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L2873 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.stopEventPropagation()`

#### Description

When using events with `X.on('foo', function() { ... })` and then `X.emit('foo')` you might want to stop subsequent event handlers from being executed.

Calling this function doing the execution of events will ensure that no subsequent event handlers are executed.

```

var X = {}; // in Espruino all objects are EventEmitters
X.on('foo', function() { print("A"); })
X.on('foo', function() { print("B"); E.stopEventPropagation(); })
X.on('foo', function() { print("C"); })
X.emit('foo');
// prints A,B but not C
```

### [E.sum](#t_l_E_sum) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L394 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.sum(arr)`

#### Parameters

`arr` - The array to sum

#### Returns

The sum of the given buffer

#### Description

Sum the contents of the given Array, String or ArrayBuffer and return the result

**Note:** This is not available in devices with low flash memory

### [E.toArrayBuffer](#t_l_E_toArrayBuffer) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L987 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.toArrayBuffer(str)`

#### Parameters

`str` - The string to convert to an `[ArrayBuffer](#ArrayBuffer)`

#### Returns

An ArrayBuffer that uses the given string

#### Description

Create an ArrayBuffer from the given string. This is done via a reference, not a copy - so it is very fast and memory efficient.

Note that this is an ArrayBuffer, not a Uint8Array. To get one of those, do: `new Uint8Array(E.toArrayBuffer('....'))`.

### [E.toFlatString](#t_l_E_toFlatString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1107 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.toFlatString(args, ...)`

#### Parameters

`args, ...` - The arguments to convert to a Flat String

#### Returns

A Flat String (or undefined)

#### Description

Returns a Flat `[String](#String)` representing the data in the arguments, or `undefined` if one can't be allocated.

This provides the same behaviour that `[E.toString](#l_E_toString)` had in Espruino before 2v18 - see `[E.toString](#l_E_toString)` for more information.

### [E.toJS](#t_l_E_toJS) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1293 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.toJS(arg)`

#### Parameters

`arg` - The JS variable to convert to a string

#### Returns

A String

#### Description

This performs the same basic function as `[JSON.stringify](#l_JSON_stringify)`, however `[JSON.stringify](#l_JSON_stringify)` adds extra characters to conform to the JSON spec which aren't required if outputting JS.

`[E.toJS](#l_E_toJS)` will also stringify JS functions, whereas `[JSON.stringify](#l_JSON_stringify)` ignores them.

For example:

-   `JSON.stringify({a:1,b:2}) == '{"a":1,"b":2}'`
-   `E.toJS({a:1,b:2}) == '{a:1,b:2}'`

**Note:** Strings generated with `[E.toJS](#l_E_toJS)` can't be reliably parsed by `[JSON.parse](#l_JSON_parse)` - however they are valid JS so will work with `[eval](#l__global_eval)` (but this has security implications if you don't trust the source of the string).

On the desktop [JSON5 parsers](https://github.com/json5/json5) will parse the strings produced by `[E.toJS](#l_E_toJS)` without trouble.

### [E.toString](#t_l_E_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1057 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.toString(args, ...)`

#### Parameters

`args, ...` - The arguments to convert to a String

#### Returns

A String

#### Description

Returns a `[String](#String)` representing the data in the arguments.

This creates a string from the given arguments in the same way as `[E.toUint8Array](#l_E_toUint8Array)`. If each argument is:

-   A String or an Array, each element is traversed and added as an 8 bit character
-   `{data : ..., count : N}` causes `data` to be repeated `count` times
-   `{callback : fn}` calls the function and adds the result
-   Anything else is converted to a character directly.

In the case where there's one argument which is an 8 bit typed array backed by a flat string of the same length, the backing string will be returned without doing a copy or other allocation. The same applies if there's a single argument which is itself a flat string.

```

E.toString(0,1,2,"Hi",3)
"\0\1\2Hi\3"
```

```

E.toString(1,2,{data:[3,4], count:4},5,6)
"\1\2\3\4\3\4\3\4\3\4\5\6"
```

```

E.toString(1,2,{callback : () => "Hello World"},5,6)
="\1\2Hello World\5\6"
```

**Note:** Prior to Espruino 2v18 `[E.toString](#l_E_toString)` would always return a flat string, or would return `undefined` if one couldn't be allocated. Now, it will return a normal (fragmented) String if a contiguous chunk of memory cannot be allocated. You can still check if the returned value is a Flat string using `E.getAddressOf(str, true)!=0`, or can use `[E.toFlatString](#l_E_toFlatString)` instead.

### [event E.touch](#t_l_E_touch) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L109 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.on('touch', function(x, y, b) { ... });`

#### Parameters

`x` - X coordinate in display coordinates

`y` - Y coordinate in display coordinates

`b` - Touch count - 0 for released, 1 for pressed

#### Description

This event is called when a full touchscreen device on an Espruino is interacted with.

**Note:** This event is not implemented on Bangle.js because it only has a two area touchscreen.

To use the touchscreen to draw lines, you could do:

```

var last;
E.on('touch',t=>{
  if (last) g.lineTo(t.x, t.y);
  else g.moveTo(t.x, t.y);
  last = t.b;
});
```

### [E.toUint8Array](#t_l_E_toUint8Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L1237 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.toUint8Array(args, ...)`

#### Parameters

`args, ...` - The arguments to convert to a `[Uint8Array](#Uint8Array)`

#### Returns

A Uint8Array

#### Description

This creates a `[Uint8Array](#Uint8Array)` from the given arguments. These are handled as follows:

-   `[Number](#Number)` -> read as an integer, using the lowest 8 bits
-   `[String](#String)` -> use each character's numeric value (e.g. `[String.charCodeAt(...)](#l_String_charCodeAt)`)
-   `[Array](#Array)` -> Call itself on each element
-   `[ArrayBuffer](#ArrayBuffer)` or Typed Array -> use the lowest 8 bits of each element
-   `[Object](#Object)`:
    -   `{data:..., count: int}` -> call itself `object.count` times, on `object.data`
    -   `{callback : function}` -> call the given function, call itself on return value

For example:

```

E.toUint8Array([1,2,3])
=new Uint8Array([1, 2, 3])
E.toUint8Array([1,{data:2,count:3},3])
=new Uint8Array([1, 2, 2, 2, 3])
E.toUint8Array("Hello")
=new Uint8Array([72, 101, 108, 108, 111])
E.toUint8Array(["hi",{callback:function() { return [1,2,3] }}])
=new Uint8Array([104, 105, 1, 2, 3])
```

### [E.variance](#t_l_E_variance) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_espruino.c#L425 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`E.variance(arr, mean)`

#### Parameters

`arr` - The array to work out the variance for

`mean` - The mean value of the array

#### Returns

The variance of the given buffer

#### Description

Work out the variance of the contents of the given Array, String or ArrayBuffer and return the result. This is equivalent to:

\`\`\` v=0; for (i in arr) v+=Math.pow(mean-arr\[i\],2); \`\`\`\`

**Note:** This is not available in devices with low flash memory

## [Error Class](#t_Error)

[(top)](javascript:toppos\(\);)

The base class for runtime errors

#### Methods and Fields

-   [constructor Error(message)](#l_Error_Error)
-   [function Error.toString()](#l_Error_toString)

### [constructor Error](#t_l_Error_Error) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L71 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Error(message)`

#### Parameters

`message` - \[optional\] An message string

#### Returns

An Error object

#### Description

Creates an Error object

### [function Error.toString](#t_l_Error_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L153 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/toString)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Error.toString()`

#### Returns

A String

#### Description

## [Flash Library](#t_Flash)

[(top)](javascript:toppos\(\);)

This module allows you to read and write the nonvolatile flash memory of your device.

Also see the `[Storage](#Storage)` library, which provides a safer file-like interface to nonvolatile storage.

It should be used with extreme caution, as it is easy to overwrite parts of Flash memory belonging to Espruino or even its bootloader. If you damage the bootloader then you may need external hardware such as a USB-TTL converter to restore it. For more information on restoring the bootloader see

```
Advanced
Reflashing
```

in your board's reference pages.

To see which areas of memory you can and can't overwrite, look at the values reported by `[process.memory()](#l_process_memory)`.

**Note:** On Nordic platforms there are checks in place to help you avoid 'bricking' your device be damaging the bootloader. You can disable these with `E.setFlags({unsafeFlash:1})`

#### Methods and Fields

-   [require("Flash").erasePage(addr)](#l_Flash_erasePage)
-   [require("Flash").getFree()](#l_Flash_getFree)
-   [require("Flash").getPage(addr)](#l_Flash_getPage)
-   [require("Flash").read(length, addr)](#l_Flash_read)
-   [require("Flash").write(data, addr)](#l_Flash_write)

### [Flash.erasePage](#t_l_Flash_erasePage) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_flash.c#L94 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Flash").erasePage(addr)`

#### Parameters

`addr` - An address in the page that is to be erased

#### Description

Erase a page of flash memory

**Note:** This is not available in devices with low flash memory

### [Flash.getFree](#t_l_Flash_getFree) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_flash.c#L72 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Flash").getFree()`

#### Returns

Array of objects with `addr` and `length` properties

#### Description

This method returns an array of objects of the form `{addr : #, length : #}`, representing contiguous areas of flash memory in the chip that are not used for anything.

The memory areas returned are on page boundaries. This means that you can safely erase the page containing any address here, and you won't risk deleting part of the Espruino firmware.

**Note:** This is not available in devices with low flash memory

### [Flash.getPage](#t_l_Flash_getPage) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_flash.c#L48 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Flash").getPage(addr)`

#### Parameters

`addr` - An address in memory

#### Returns

An object of the form `{ addr : #, length : #}`, where `addr` is the start address of the page, and `length` is the length of it (in bytes). Returns undefined if no page at address

#### Description

Returns the start and length of the flash page containing the given address.

**Note:** This is not available in devices with low flash memory

### [Flash.read](#t_l_Flash_read) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_flash.c#L144 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Flash").read(length, addr)`

#### Parameters

`length` - The amount of data to read (in bytes)

`addr` - The address to start reading from

#### Returns

A Uint8Array of data

#### Description

Read flash memory from the given address

**Note:** This is not available in devices with low flash memory

### [Flash.write](#t_l_Flash_write) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_flash.c#L114 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Flash").write(data, addr)`

#### Parameters

`data` - The data to write

`addr` - The address to start writing from

#### Description

Write data into memory at the given address

In flash memory you may only turn bits that are 1 into bits that are 0. If you're writing data into an area that you have already written (so `read` doesn't return all `0xFF`) you'll need to call `erasePage` to clear the entire page.

**Note:** This is not available in devices with low flash memory

## [Float32Array Class](#t_Float32Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 32 bit floating point values.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Float32Array(arr, byteOffset, length)](#l_Float32Array_Float32Array)

### [constructor Float32Array](#t_l_Float32Array_Float32Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L470 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float32Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Float32Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

## [Float64Array Class](#t_Float64Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 64 bit floating point values.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Float64Array(arr, byteOffset, length)](#l_Float64Array_Float64Array)

### [constructor Float64Array](#t_l_Float64Array_Float64Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L493 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Float64Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Float64Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`). Maximum 65535.

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

## [fs Class](#t_fs)

[(top)](javascript:toppos\(\);)

#### Methods and Fields

-   [fs.pipe(source, destination, options)](#l_fs_pipe)

### [fs.pipe](#t_l_fs_pipe) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pipe.c#L239 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`fs.pipe(source, destination, options)`

#### Parameters

`source` - The source file/stream that will send content.

`destination` - The destination file/stream that will receive content from the source.

`options` - \[optional\] An object `{ chunkSize : int=64, end : bool=true, complete : function }`  
chunkSize : The amount of data to pipe from source to destination at a time  
complete : a function to call when the pipe activity is complete  
end : call the 'end' function on the destination when the source is finished

#### Description

Pipe this file to a destination stream (object which has a `.write(data)` method).

**Note:** This is not available in devices with low flash memory

## [Function Class](#t_Function)

[(top)](javascript:toppos\(\);)

This is the built-in class for Functions

#### Methods and Fields

-   [function Function.apply(this, args)](#l_Function_apply)
-   [function Function.bind(this, params, ...)](#l_Function_bind)
-   [function Function.call(this, params, ...)](#l_Function_call)
-   [constructor Function(args, ...)](#l_Function_Function)
-   [function Function.replaceWith(newFunc)](#l_Function_replaceWith)

### [function Function.apply](#t_l_Function_apply) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L1211 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Function.apply(this, args)`

#### Parameters

`this` - The value to use as the 'this' argument when executing the function

`args` - Optional Array of Arguments

#### Returns

The return value of executing this function

#### Description

This executes the function with the supplied 'this' argument and parameters

### [function Function.bind](#t_l_Function_bind) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L1266 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Function.bind(this, params, ...)`

#### Parameters

`this` - The value to use as the 'this' argument when executing the function

`params, ...` - Optional Default parameters that are prepended to the call

#### Returns

The 'bound' function

#### Description

This executes the function with the supplied 'this' argument and parameters

### [function Function.call](#t_l_Function_call) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L1195 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Function.call(this, params, ...)`

#### Parameters

`this` - The value to use as the 'this' argument when executing the function

`params, ...` - Optional Parameters

#### Returns

The return value of executing this function

#### Description

This executes the function with the supplied 'this' argument and parameters

### [constructor Function](#t_l_Function_Function) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_functions.c#L102 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Function(args, ...)`

#### Parameters

`args, ...` - Zero or more arguments (as strings), followed by a string representing the code to run

#### Returns

A Number object

#### Description

Creates a function

### [function Function.replaceWith](#t_l_Function_replaceWith) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L1117 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Function.replaceWith(newFunc)`

#### Parameters

`newFunc` - The new function to replace this function with

#### Description

This replaces the function with the one in the argument - while keeping the old function's scope. This allows inner functions to be edited, and is used when edit() is called on an inner function.

## [Graphics Class](#t_Graphics)

[(top)](javascript:toppos\(\);)

This class provides Graphics operations that can be applied to a surface.

Use Graphics.createXXX to create a graphics object that renders in the way you want. See [the Graphics page](https://www.espruino.com/Graphics) for more information.

**Note:** On boards that contain an LCD, there is a built-in `g` object of type `[Graphics](#Graphics)`. For instance to draw a line you'd type: `g.drawLine(0,0,100,100)`

#### Methods and Fields

-   [function Graphics.asBMP()](#l_Graphics_asBMP)
-   [function Graphics.asImage(options)](#l_Graphics_asImage)
-   [function Graphics.asURL()](#l_Graphics_asURL)
-   [function Graphics.blendColor(col\_a, col\_b, amt)](#l_Graphics_blendColor)
-   [function Graphics.blit(options)](#l_Graphics_blit)
-   [property Graphics.buffer](#l_Graphics_buffer)
-   [function Graphics.clear(reset)](#l_Graphics_clear)
-   [function Graphics.clearRect(x1, y1, x2, y2)](#l_Graphics_clearRect)
-   [Graphics.createArrayBuffer(width, height, bpp, options)](#l_Graphics_createArrayBuffer)
-   [Graphics.createCallback(width, height, bpp, callback)](#l_Graphics_createCallback)
-   [Graphics.createImage(str)](#l_Graphics_createImage)
-   [function Graphics.drawCircle(x, y, rad)](#l_Graphics_drawCircle)
-   [function Graphics.drawCircleAA(x, y, r)](#l_Graphics_drawCircleAA)
-   [function Graphics.drawEllipse(x1, y1, x2, y2)](#l_Graphics_drawEllipse)
-   [function Graphics.drawImage(image, x, y, options)](#l_Graphics_drawImage)
-   [function Graphics.drawImages(layers, options)](#l_Graphics_drawImages)
-   [function Graphics.drawLine(x1, y1, x2, y2)](#l_Graphics_drawLine)
-   [function Graphics.drawLineAA(x1, y1, x2, y2)](#l_Graphics_drawLineAA)
-   [function Graphics.drawPoly(poly, closed)](#l_Graphics_drawPoly)
-   [function Graphics.drawPolyAA(poly, closed)](#l_Graphics_drawPolyAA)
-   [function Graphics.drawRect(x1, y1, x2, y2)](#l_Graphics_drawRect)
-   [function Graphics.drawString(str, x, y, solid)](#l_Graphics_drawString)
-   [function Graphics.dump()](#l_Graphics_dump)
-   [function Graphics.fillCircle(x, y, rad)](#l_Graphics_fillCircle)
-   [function Graphics.fillEllipse(x1, y1, x2, y2)](#l_Graphics_fillEllipse)
-   [function Graphics.fillPoly(poly)](#l_Graphics_fillPoly)
-   [function Graphics.fillPolyAA(poly)](#l_Graphics_fillPolyAA)
-   [function Graphics.fillRect(x1, y1, x2, y2)](#l_Graphics_fillRect)
-   [function Graphics.filter(filter, options)](#l_Graphics_filter)
-   [function Graphics.findFont(text, options)](#l_Graphics_findFont)
-   [function Graphics.flip(all)](#l_Graphics_flip)
-   [function Graphics.floodFill(x, y, col)](#l_Graphics_floodFill)
-   [function Graphics.getBgColor()](#l_Graphics_getBgColor)
-   [function Graphics.getBPP()](#l_Graphics_getBPP)
-   [function Graphics.getColor()](#l_Graphics_getColor)
-   [function Graphics.getFont()](#l_Graphics_getFont)
-   [function Graphics.getFontHeight()](#l_Graphics_getFontHeight)
-   [function Graphics.getFonts()](#l_Graphics_getFonts)
-   [function Graphics.getHeight()](#l_Graphics_getHeight)
-   [Graphics.getInstance()](#l_Graphics_getInstance)
-   [function Graphics.getModified(reset)](#l_Graphics_getModified)
-   [function Graphics.getPixel(x, y)](#l_Graphics_getPixel)
-   [function Graphics.getVectorFontPolys(str, options)](#l_Graphics_getVectorFontPolys)
-   [function Graphics.getWidth()](#l_Graphics_getWidth)
-   [function Graphics.imageMetrics(str)](#l_Graphics_imageMetrics)
-   [function Graphics.lineTo(x, y)](#l_Graphics_lineTo)
-   [function Graphics.moveTo(x, y)](#l_Graphics_moveTo)
-   [function Graphics.quadraticBezier(arr, options)](#l_Graphics_quadraticBezier)
-   [function Graphics.reset()](#l_Graphics_reset)
-   [function Graphics.scroll(x, y)](#l_Graphics_scroll)
-   [function Graphics.setBgColor(r, g, b)](#l_Graphics_setBgColor)
-   [function Graphics.setClipRect(x1, y1, x2, y2)](#l_Graphics_setClipRect)
-   [function Graphics.setColor(r, g, b)](#l_Graphics_setColor)
-   [function Graphics.setFont(name, size)](#l_Graphics_setFont)
-   [function Graphics.setFont12x20(scale)](#l_Graphics_setFont12x20)
-   [function Graphics.setFont14(scale)](#l_Graphics_setFont14)
-   [function Graphics.setFont17(scale)](#l_Graphics_setFont17)
-   [function Graphics.setFont22(scale)](#l_Graphics_setFont22)
-   [function Graphics.setFont28(scale)](#l_Graphics_setFont28)
-   [function Graphics.setFont6x15(scale)](#l_Graphics_setFont6x15)
-   [function Graphics.setFontAlign(x, y, rotation)](#l_Graphics_setFontAlign)
-   [function Graphics.setFontBitmap()](#l_Graphics_setFontBitmap)
-   [function Graphics.setFontCustom(bitmap, firstChar, width, height)](#l_Graphics_setFontCustom)
-   [function Graphics.setFontPBF(file, scale)](#l_Graphics_setFontPBF)
-   [function Graphics.setFontVector(size)](#l_Graphics_setFontVector)
-   [function Graphics.setPixel(x, y, col)](#l_Graphics_setPixel)
-   [function Graphics.setRotation(rotation, reflect)](#l_Graphics_setRotation)
-   [function Graphics.setTheme(theme)](#l_Graphics_setTheme)
-   [function Graphics.stringMetrics(str)](#l_Graphics_stringMetrics)
-   [function Graphics.stringWidth(str)](#l_Graphics_stringWidth)
-   [property Graphics.theme](#l_Graphics_theme)
-   [function Graphics.toColor(r, g, b)](#l_Graphics_toColor)
-   [function Graphics.transformVertices(verts, transformation)](#l_Graphics_transformVertices)
-   [function Graphics.wrapString(str, maxWidth)](#l_Graphics_wrapString)

### [function Graphics.asBMP](#t_l_Graphics_asBMP) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4379 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.asBMP()`

#### Returns

A String representing the Graphics as a Windows BMP file (or 'undefined' if not possible)

#### Description

Create a Windows BMP file from this `[Graphics](#Graphics)` instance, and return it as a String.

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.asImage](#t_l_Graphics_asImage) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4036 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.asImage(options)`

#### Parameters

`options` - The type of image to return as a string, or an object `{x,y,w,h,type}` (see below)

#### Returns

An Image that can be used with `[Graphics.drawImage](#l_Graphics_drawImage)`

#### Description

Return this `[Graphics](#Graphics)` object as an Image that can be used with `[Graphics.drawImage](#l_Graphics_drawImage)`. Check out [the Graphics reference page](http://www.espruino.com/Graphics#images-bitmaps) for more information on images.

Will return undefined if data can't be allocated for the image.

`options` can be either:

-   `undefined` or `"object"` - return an image object
-   `string` - return the image as a string
-   (in 2v26 onwards) `{type:undefined/"object"/"string", x,y,w,h}` - Return only a part of the image as an object/string.

The image data itself will be referenced rather than copied if:

-   An image `object` was requested (not `string`)
-   `x`/`y` are 0 and `w`/`h` are the graphics's height
-   The `[Graphics](#Graphics)` instance was created with `[Graphics.createArrayBuffer](#l_Graphics_createArrayBuffer)`
-   Is 8 bpp _OR_ the `{msb:true}` option was given
-   No other format options (zigzag/etc) were given

Otherwise data will be copied, which takes up more space and may be quite slow.

If the `[Graphics](#Graphics)` object contains `transparent` or `palette` fields, [as you might find in an image](http://www.espruino.com/Graphics#images-bitmaps), those will be included in the generated image too.

```

var gfx = Graphics.createArrayBuffer(8,8,1);
gfx.transparent = 0;
gfx.drawString("X",0,0);
var im = gfx.asImage("string");
```

**Note:** This is not available in devices with low flash memory

### [function Graphics.asURL](#t_l_Graphics_asURL) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4560 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.asURL()`

#### Returns

A String representing the Graphics as a URL (or 'undefined' if not possible)

#### Description

Create a URL of the form `data:image/bmp;base64,...` that can be pasted into the browser.

The Espruino Web IDE can detect this data on the console and render the image inline automatically.

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.blendColor](#t_l_Graphics_blendColor) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1575 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.blendColor(col_a, col_b, amt)`

#### Parameters

`col_a` - Color to blend from (either a single integer color value, or a string)

`col_b` - Color to blend to (either a single integer color value, or a string)

`amt` - The amount to blend. 0=col_a, 1=col_b, 0.5=halfway between (and so on)

#### Returns

The color index represented by the blended colors

#### Description

Blend between two colors, and return the result.

```

// dark yellow - halfway between red and green
var col = g.blendColor("#f00","#0f0", 0.5);
// Get a color 25% brighter than the theme's background colour
var col = g.blendColor(g.theme.fg,g.theme.bg, 0.75);
// then...
g.setColor(col).fillRect(10,10,100,100);
```

**Note:** This is only available in devices with Antialiasing support included (Bangle.js or Linux)

### [function Graphics.blit](#t_l_Graphics_blit) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4292 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.blit(options)`

#### Parameters

`options` - options - see below

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Blit one area of the screen (x1,y1 w,h) to another (x2,y2 w,h)

```

g.blit({
  x1:0, y1:0,
  w:32, h:32,
  x2:100, y2:100,
  setModified : true // should we set the modified area?
});
```

Note: This uses repeated pixel reads and writes, so will not work on platforms that don't support pixel reads.

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [property Graphics.buffer](#t_l_Graphics_buffer) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L523 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property Graphics.buffer`

#### Returns

An ArrayBuffer (or not defined on `[Graphics](#Graphics)` instances not created with `[Graphics.createArrayBuffer](#l_Graphics_createArrayBuffer)`)

#### Description

On `[Graphics](#Graphics)` instances with an offscreen buffer, this is an `[ArrayBuffer](#ArrayBuffer)` that provides access to the underlying pixel data.

```

g=Graphics.createArrayBuffer(8,8,8)
g.drawLine(0,0,7,7)
print(new Uint8Array(g.buffer))
new Uint8Array([
255, 0, 0, 0, 0, 0, 0, 0,
0, 255, 0, 0, 0, 0, 0, 0,
0, 0, 255, 0, 0, 0, 0, 0,
0, 0, 0, 255, 0, 0, 0, 0,
0, 0, 0, 0, 255, 0, 0, 0,
0, 0, 0, 0, 0, 255, 0, 0,
0, 0, 0, 0, 0, 0, 255, 0,
0, 0, 0, 0, 0, 0, 0, 255])
```

### [function Graphics.clear](#t_l_Graphics_clear) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1022 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.clear(reset)`

#### Parameters

`[reset](#l__global_reset)` - \[optional\] If `true`, resets the state of Graphics to the default (eg. Color, Font, etc) as if calling `[Graphics.reset](#l_Graphics_reset)`

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Clear the LCD with the Background Color

### [function Graphics.clearRect](#t_l_Graphics_clearRect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1145 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.clearRect(x1, y1, x2, y2)`

#### Parameters

`x1` - The left X coordinate OR an object containing `{x,y,x2,y2}` or `{x,y,w,h}`

`y1` - The top Y coordinate

`x2` - The right X coordinate

`y2` - The bottom Y coordinate

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Fill a rectangular area in the Background Color

On devices with enough memory, you can specify `{x,y,x2,y2,r}` as the first argument, which allows you to draw a rounded rectangle.

**Note:** This is not available in devices with low flash memory

### [Graphics.createArrayBuffer](#t_l_Graphics_createArrayBuffer) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L637 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Graphics.createArrayBuffer(width, height, bpp, options)`

#### Parameters

`width` - Pixels wide

`height` - Pixels high

`bpp` - Number of bits per pixel

`options` - An object of other options. `{ zigzag : true/false(default), vertical_byte : true/false(default), msb : true/false(default), color_order: 'rgb'(default),'bgr',etc }`  
`zigzag` = whether to alternate the direction of scanlines for rows  
`vertical_byte` = whether to align bits in a byte vertically or not  
`msb` = when bits<8, store pixels most significant bit first, when bits>8, store most significant byte first (as of 2v25, msb:true is default)  
`interleavex` = Pixels 0,2,4,etc are from the top half of the image, 1,3,5,etc from the bottom half. Used for P3 LED panels.  
`color_order` = re-orders the colour values that are supplied via setColor  
`buffer` = if specified, createArrayBuffer won't create a new buffer but will use the given one

#### Returns

The new `[Graphics](#Graphics)` object

#### Description

Create a `[Graphics](#Graphics)` object that renders to an `[ArrayBuffer](#ArrayBuffer)`. This will have a field called `'buffer'` that can get used to get at the buffer itself

### [Graphics.createCallback](#t_l_Graphics_createCallback) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L736 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Graphics.createCallback(width, height, bpp, callback)`

#### Parameters

`width` - Pixels wide

`height` - Pixels high

`bpp` - Number of bits per pixel

`callback` - A function of the form `function(x,y,col)` that is called whenever a pixel needs to be drawn, or an object with: `{setPixel:function(x,y,col),fillRect:function(x1,y1,x2,y2,col)}`. All arguments are already bounds checked.

#### Returns

The new `[Graphics](#Graphics)` object

#### Description

Create a `[Graphics](#Graphics)` object that renders by calling a JavaScript callback function to draw pixels

**Note:** This is not available in devices with low flash memory

### [Graphics.createImage](#t_l_Graphics_createImage) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L844 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Graphics.createImage(str)`

#### Parameters

`str` - A String containing a newline-separated image - space/. is 0, anything else is 1

#### Returns

An Image object that can be used with `[Graphics.drawImage](#l_Graphics_drawImage)`

#### Description

Create a simple Black and White image for use with `[Graphics.drawImage](#l_Graphics_drawImage)`.

Use as follows:

```

var img = Graphics.createImage(`
XXXXXXXXX
X       X
X   X   X
X   X   X
X       X
XXXXXXXXX
`);
g.drawImage(img, x,y);
var img = Graphics.createImage(`
.....
.XXX.
.X.X.
.XXX.
.....
`);
g.drawImage(img, x,y);
```

If the characters at the beginning and end of the string are newlines, they will be ignored. Spaces are treated as `0`, and any other character is a `1`

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.drawCircle](#t_l_Graphics_drawCircle) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1266 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawCircle(x, y, rad)`

#### Parameters

`x` - The X axis

`y` - The Y axis

`rad` - The circle radius

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw an unfilled circle 1px wide in the Foreground Color

**Note:** This is not available in devices with low flash memory

### [function Graphics.drawCircleAA](#t_l_Graphics_drawCircleAA) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1286 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawCircleAA(x, y, r)`

#### Parameters

`x` - Centre x-coordinate

`y` - Centre y-coordinate

`r` - Radius

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a circle, centred at (x,y) with radius r in the current foreground color

**Note:** This is only available in devices with Antialiasing support included (Bangle.js or Linux)

### [function Graphics.drawEllipse](#t_l_Graphics_drawEllipse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1336 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawEllipse(x1, y1, x2, y2)`

#### Parameters

`x1` - The left X coordinate

`y1` - The top Y coordinate

`x2` - The right X coordinate

`y2` - The bottom Y coordinate

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw an ellipse in the Foreground Color

**Note:** This is not available in devices with low flash memory

### [function Graphics.drawImage](#t_l_Graphics_drawImage) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3559 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawImage(image, x, y, options)`

#### Parameters

`image` - An image to draw, either a String or an Object (see below)

`x` - The X offset to draw the image

`y` - The Y offset to draw the image

`options` - options for scaling,rotation,etc (see below)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Image can be:

-   An object with the following fields
    
    ```
    { width : int, height : int, bpp :
    optional int, buffer : ArrayBuffer/String, transparent: optional int,
    palette : optional Uint16Array(2/4/16) }
    ```
    
    . bpp = bits per pixel (default is 1), transparent (if defined) is the colour that will be treated as transparent, and palette is a color palette that each pixel will be looked up in first
-   A String where the the first few bytes are: `width,height,bpp,[transparent,]image_bytes...`. If a transparent colour is specified the top bit of `bpp` should be set.
-   An ArrayBuffer `[Graphics](#Graphics)` object (if `bpp<8`, `msb:true` must be set) - this is disabled on devices without much flash memory available. If a `[Graphics](#Graphics)` object is supplied, it can also contain transparent/palette fields as if it were an image.

See https://www.espruino.com/Graphics#images-bitmaps for more information about image formats.

Draw an image at the specified position.

-   If the image is 1 bit, the graphics foreground/background colours will be used.
-   If `img.palette` is a Uint16Array or 2/4/16 elements, color data will be looked from the supplied palette
-   On Bangle.js, 2 bit images blend from background(0) to foreground(1) colours
-   On Bangle.js, 4 bit images use the Apple Mac 16 color palette
-   On Bangle.js, 8 bit images use the Web Safe 216 color palette
-   Otherwise color data will be copied as-is. Bitmaps are rendered MSB-first

If `options` is supplied, `drawImage` will allow images to be rendered at any scale or angle. If `options.rotate` is set it will center images at `x,y`. `options` must be an object of the form:

```

{
  rotate : float, // the amount to rotate the image in radians (default 0)
  scale : float, // the amount to scale the image up (default 1)
  frame : int    // if specified and the image has frames of data
                 //  after the initial frame, draw one of those frames from the image
  filter : bool  // (2v19+) when set, if scale<0.75 perform 2x2 supersampling to smoothly downscale the image
}
```

For example:

```

// In the top left of the screen
g.drawImage(img,0,0);
// In the top left of the screen, twice as big
g.drawImage(img,0,0,{scale:2});
// In the center of the screen, twice as big, 45 degrees
g.drawImage(img, g.getWidth()/2, g.getHeight()/2,
            {scale:2, rotate:Math.PI/4});
```

### [function Graphics.drawImages](#t_l_Graphics_drawImages) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3871 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawImages(layers, options)`

#### Parameters

`layers` - An array of objects {x,y,image,scale,rotate,center} (up to 3)

`options` - options for rendering - see below

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draws multiple images _at once_ - which avoids flicker on unbuffered systems like Bangle.js. Maximum layer count right now is 4.

```

layers = [ {
  {x : float, // x start position
   y : float, // y start position
   image : string/object/Graphics,
   scale : float, // scale factor, default 1
   rotate : float, // angle in radians
   center : bool // center on x,y? default is top left
   repeat : should this image be repeated (tiled?)
   nobounds : bool // if true, the bounds of the image are not used to work out the default area to draw
   palette : new Uint16Array(2/4/8/16/256) // (2v22+) a color palette to use with the image (overrides the image's palette)
   compose : ""/"add"/"or"/"xor" // (2v22+) if set, the operation used when combining with the previous layer
  }
]
options = {
 x,y, : int // the area to render. Defaults to rendering just enough to cover what's requested
 width,height : int
}
```

**Note:** This is only available in Bangle.js smartwatches and Linux-based builds

### [function Graphics.drawLine](#t_l_Graphics_drawLine) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3185 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawLine(x1, y1, x2, y2)`

#### Parameters

`x1` - The left

`y1` - The top

`x2` - The right

`y2` - The bottom

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a line between x1,y1 and x2,y2 in the current foreground color

### [function Graphics.drawLineAA](#t_l_Graphics_drawLineAA) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3208 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawLineAA(x1, y1, x2, y2)`

#### Parameters

`x1` - The left

`y1` - The top

`x2` - The right

`y2` - The bottom

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a line between x1,y1 and x2,y2 in the current foreground color

**Note:** This is only available in devices with Antialiasing support included (Bangle.js or Linux)

### [function Graphics.drawPoly](#t_l_Graphics_drawPoly) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3284 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawPoly(poly, closed)`

#### Parameters

`poly` - An array of vertices, of the form `[x1,y1,x2,y2,x3,y3,etc]`

`closed` - Draw another line between the last element of the array and the first

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a polyline (lines between each of the points in `poly`) in the current foreground color

**Note:** there is a limit of 64 points (128 XY elements) for polygons

**Note:** This is not available in devices with low flash memory

### [function Graphics.drawPolyAA](#t_l_Graphics_drawPolyAA) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3303 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawPolyAA(poly, closed)`

#### Parameters

`poly` - An array of vertices, of the form `[x1,y1,x2,y2,x3,y3,etc]`

`closed` - Draw another line between the last element of the array and the first

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw an **antialiased** polyline (lines between each of the points in `poly`) in the current foreground color

**Note:** there is a limit of 64 points (128 XY elements) for polygons

**Note:** This is only available in devices with Antialiasing support included (Bangle.js or Linux)

### [function Graphics.drawRect](#t_l_Graphics_drawRect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1173 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawRect(x1, y1, x2, y2)`

#### Parameters

`x1` - The left X coordinate OR an object containing `{x,y,x2,y2}` or `{x,y,w,h}`

`y1` - The top Y coordinate

`x2` - The right X coordinate

`y2` - The bottom Y coordinate

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw an unfilled rectangle 1px wide in the Foreground Color

On devices with enough memory, you can specify `{x,y,x2,y2,r}` as the first argument, which allows you to draw a rounded rectangle.

### [function Graphics.drawString](#t_l_Graphics_drawString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L2816 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.drawString(str, x, y, solid)`

#### Parameters

`str` - The string

`x` - The X position of the leftmost pixel

`y` - The Y position of the topmost pixel

`solid` - For bitmap fonts, should empty pixels be filled with the background color?

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a string of text in the current font.

```

g.drawString("Hello World", 10, 10);
```

Images may also be embedded inside strings (e.g. to render Emoji or characters not in the current font). To do this, just add `0` then the image string ([about Images](http://www.espruino.com/Graphics#images-bitmaps)) For example:

```

g.drawString("Hi \0\7\5\1\x82 D\x17\xC0");
// draws:
// # #  #      #     #
// # #            #
// ### ##         #
// # #  #      #     #
// # # ###      #####
```

### [function Graphics.dump](#t_l_Graphics_dump) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4586 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.dump()`

#### Description

Output this image as a bitmap URL of the form `data:image/bmp;base64,...`. The Espruino Web IDE will detect this on the console and will render the image inline automatically.

This is identical to `console.log(g.asURL())` - it is just a convenient function for easy debugging and producing screenshots of what is currently in the `[Graphics](#Graphics)` instance.

**Note:** This may not work on some bit depths of `[Graphics](#Graphics)` instances. It will also not work for the main `[Graphics](#Graphics)` instance of Bangle.js 1 as the graphics on Bangle.js 1 are stored in write-only memory.

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.fillCircle](#t_l_Graphics_fillCircle) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1220 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.fillCircle(x, y, rad)`

#### Parameters

`x` - The X axis

`y` - The Y axis

`rad` - The circle radius

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a filled circle in the Foreground Color

**Note:** This is not available in devices with low flash memory

### [function Graphics.fillEllipse](#t_l_Graphics_fillEllipse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1312 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.fillEllipse(x1, y1, x2, y2)`

#### Parameters

`x1` - The left X coordinate

`y1` - The top Y coordinate

`x2` - The right X coordinate

`y2` - The bottom Y coordinate

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a filled ellipse in the Foreground Color

**Note:** This is not available in devices with low flash memory

### [function Graphics.fillPoly](#t_l_Graphics_fillPoly) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3372 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.fillPoly(poly)`

#### Parameters

`poly` - An array of vertices, of the form `[x1,y1,x2,y2,x3,y3,etc]`

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a filled polygon in the current foreground color.

```

g.fillPoly([
  16, 0,
  31, 31,
  26, 31,
  16, 12,
  6, 28,
  0, 27 ]);
```

This fills from the top left hand side of the polygon (low X, low Y) _down to but not including_ the bottom right. When placed together polygons will align perfectly without overdraw - but this will not fill the same pixels as `drawPoly` (drawing a line around the edge of the polygon).

**Note:** there is a limit of 64 points (128 XY elements) for polygons

**Note:** This is not available in devices with low flash memory

### [function Graphics.fillPolyAA](#t_l_Graphics_fillPolyAA) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3404 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.fillPolyAA(poly)`

#### Parameters

`poly` - An array of vertices, of the form `[x1,y1,x2,y2,x3,y3,etc]`

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a filled polygon in the current foreground color.

```

g.fillPolyAA([
  16, 0,
  31, 31,
  26, 31,
  16, 12,
  6, 28,
  0, 27 ]);
```

This fills from the top left hand side of the polygon (low X, low Y) _down to but not including_ the bottom right. When placed together polygons will align perfectly without overdraw - but this will not fill the same pixels as `drawPoly` (drawing a line around the edge of the polygon).

**Note:** there is a limit of 64 points (128 XY elements) for polygons

**Note:** This is only available in devices with Antialiasing support included (Bangle.js or Linux)

### [function Graphics.fillRect](#t_l_Graphics_fillRect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1116 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.fillRect(x1, y1, x2, y2)`

#### Parameters

`x1` - The left X coordinate OR an object containing `{x,y,x2,y2}` or `{x,y,w,h}`

`y1` - The top Y coordinate

`x2` - The right X coordinate

`y2` - The bottom Y coordinate

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Fill a rectangular area in the Foreground Color

On devices with enough memory, you can specify `{x,y,x2,y2,r}` as the first argument, which allows you to draw a rounded rectangle.

### [function Graphics.filter](#t_l_Graphics_filter) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L5002 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.filter(filter, options)`

#### Parameters

`filter` - An array of filter params between -128 and 127 (2D arrays should be unwrapped)

`options` - An object of options, see below

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Perform a filter on the current `[Graphics](#Graphics)` instance. Requires the Graphics instance to support readback (eg `.getPixel` should work), and only uses 8 bit values for buffer and filter.

```

g.filter([ // a gaussian filter
    1, 4, 7, 4, 1,
    4,16,26,16, 4,
    7,26,41,26, 7,
    4,16,26,16, 4,
    1, 4, 7, 4, 1
], { w:5, h:5, div:273 });
```

```

{
  w,h,    // filter width+height
  div,    // divisor applied after filter
  offset, // DC offset applied to filter before division (default 0)
  max,    // maximum output value (default=max allowed by bpp)
  filter, // undefined (replace), or "max" (use max(original,filtered))
}
```

**Note:** This is only available in Bangle.js 2 smartwatches and Linux-based builds

### [function Graphics.findFont](#t_l_Graphics_findFont) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L2641 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.findFont(text, options)`

#### Parameters

`text` - The text to render

`options` - Options for finding the required font

#### Returns

An object containing info about the font

#### Description

Works out which font to use, and sets the current font to it.

Usage:

```

g.findFont("Hello World", {
  w : 100,    // optional: width available (default = screen width)
  h : 100,    // optional: height available (default = screen height)
  min : 10,   // optional: min font height
  max : 30,   // optional: max font height
  wrap : true, // optional: allow word wrap?
  trim : true // optional: trim to the specified height, add '...'
});
```

Returns:

```

{
  text : "Hello\nWorld"
  font : "..."
}
```

**Note:** This is only available in Bangle.js smartwatches

### [function Graphics.flip](#t_l_Graphics_flip) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L499 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.flip(all)`

#### Parameters

`all` - \[optional\] (only on some devices) If `true` then copy all pixels, not just those that have changed.

#### Description

On instances of graphics that drive a display with an offscreen buffer, calling this function will copy the contents of the offscreen buffer to the screen.

Call this when you have drawn something to Graphics and you want it shown on the screen.

If a display does not have an offscreen buffer, it may not have a `g.flip()` method.

On Bangle.js 1, there are different graphics modes chosen with `[Bangle.setLCDMode()](#l_Bangle_setLCDMode)`. The default mode is unbuffered and in this mode `g.flip()` does not affect the screen contents.

On some devices, this command will attempt to only update the areas of the screen that have changed in order to increase speed. If you have accessed the `[Graphics.buffer](#l_Graphics_buffer)` directly then you may need to use `[Graphics.flip(true)](#l_Graphics_flip)` to force a full update of the screen.

### [function Graphics.floodFill](#t_l_Graphics_floodFill) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4800 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.floodFill(x, y, col)`

#### Parameters

`x` - X coordinate to start from

`y` - Y coordinate to start from

`col` - The color to fill with (if undefined, foreground is used)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Flood fills the given `[Graphics](#Graphics)` instance out from a particular point.

**Note:** This only works on `[Graphics](#Graphics)` instances that support readback with `getPixel`. It is also not capable of filling over dithered patterns (eg non-solid colours on Bangle.js 2)

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.getBgColor](#t_l_Graphics_getBgColor) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1688 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getBgColor()`

#### Returns

The integer value of the colour

#### Description

Get the background color to use for subsequent drawing operations

### [function Graphics.getBPP](#t_l_Graphics_getBPP) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L971 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getBPP()`

#### Returns

The bits per pixel of this `[Graphics](#Graphics)` instance

#### Description

The number of bits per pixel of this `[Graphics](#Graphics)` instance

**Note:** Bangle.js 2 behaves a little differently here. The display is 3 bit, so `getBPP` returns 3 and `asBMP`/`asImage`/etc return 3 bit images. However in order to allow dithering, the colors returned by `[Graphics.getColor](#l_Graphics_getColor)` and `[Graphics.theme](#l_Graphics_theme)` are actually 16 bits.

### [function Graphics.getColor](#t_l_Graphics_getColor) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1679 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getColor()`

#### Returns

The integer value of the colour

#### Description

Get the color to use for subsequent drawing operations

### [function Graphics.getFont](#t_l_Graphics_getFont) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L2086 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getFont()`

#### Returns

Get the name of the current font

#### Description

Get the font by name - can be saved and used with `[Graphics.setFont](#l_Graphics_setFont)`.

Normally this might return something like `"4x6"`, but if a scale factor is specified, a colon and then the size is reported, like "4x6:2"

**Note:** For custom fonts, `Custom` is currently reported instead of the font name.

**Note:** This is not available in devices with low flash memory

### [function Graphics.getFontHeight](#t_l_Graphics_getFontHeight) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L2304 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getFontHeight()`

#### Returns

The height in pixels of the current font

#### Description

Return the height in pixels of the current font

**Note:** This is not available in devices with low flash memory

### [function Graphics.getFonts](#t_l_Graphics_getFonts) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L2139 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getFonts()`

#### Returns

And array of font names

#### Description

Return an array of all fonts currently in the Graphics library.

**Note:** Vector fonts are specified as `Vector#` where `#` is the font height. As there are effectively infinite fonts, just `Vector` is included in the list.

**Note:** This is not available in devices with low flash memory

### [function Graphics.getHeight](#t_l_Graphics_getHeight) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L958 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getHeight()`

#### Returns

The height of this `[Graphics](#Graphics)` instance

#### Description

The height of this `[Graphics](#Graphics)` instance

### [Graphics.getInstance](#t_l_Graphics_getInstance) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L615 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Graphics.getInstance()`

#### Returns

An instance of `[Graphics](#Graphics)` or undefined

#### Description

On devices like Pixl.js or HYSTM boards that contain a built-in display this will return an instance of the graphics class that can be used to access that display.

Internally, this is stored as a member called `gfx` inside the 'hiddenRoot'.

### [function Graphics.getModified](#t_l_Graphics_getModified) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4221 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getModified(reset)`

#### Parameters

`[reset](#l__global_reset)` - Whether to reset the modified area or not

#### Returns

An object {x1,y1,x2,y2} containing the modified area, or undefined if not modified

#### Description

Return the area of the Graphics canvas that has been modified, and optionally clear the modified area to 0.

For instance if `g.setPixel(10,20)` was called, this would return

```
{x1:10,
y1:20, x2:10, y2:20}
```

**Note:** This is not available in devices with low flash memory

### [function Graphics.getPixel](#t_l_Graphics_getPixel) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1360 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getPixel(x, y)`

#### Parameters

`x` - The left

`y` - The top

#### Returns

The color

#### Description

Get a pixel's color

### [function Graphics.getVectorFontPolys](#t_l_Graphics_getVectorFontPolys) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3044 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getVectorFontPolys(str, options)`

#### Parameters

`str` - The string

`options` - \[optional\] `{x,y,w,h}` (see below)

#### Returns

An array of Uint8Arrays for vector font polygons

#### Description

Return the current string as a series of polygons (using the current vector font). `options` is as follows:

-   `x` - X offset of font (default 0)
-   `y` - Y offset of font (default 0)
-   `w` - Width of font (default 256) - the actual width will likely be less than this as most characters are non-square
-   `h` - Height of font (default 256) - the actual height will likely be less than this as most characters don't fully fill the font box

```

g.getVectorFontPolys("Hi", {x:-80,y:-128});
```

**Note:** This is not available in devices with low flash memory or NO_VECTOR_FONT

### [function Graphics.getWidth](#t_l_Graphics_getWidth) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L949 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.getWidth()`

#### Returns

The width of this `[Graphics](#Graphics)` instance

#### Description

The width of this `[Graphics](#Graphics)` instance

### [function Graphics.imageMetrics](#t_l_Graphics_imageMetrics) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3521 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.imageMetrics(str)`

#### Parameters

`str` - The string

#### Returns

An object containing `{width,height,bpp,transparent}` for the image

#### Description

Return the width and height in pixels of an image (either Graphics, Image Object, Image String or ArrayBuffer). Returns `undefined` if image couldn't be decoded.

`frames` is also included is the image contains more information than you'd expect for a single bitmap. In this case the bitmap might be an animation with multiple frames

### [function Graphics.lineTo](#t_l_Graphics_lineTo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3239 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.lineTo(x, y)`

#### Parameters

`x` - X value

`y` - Y value

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Draw a line from the last position of `lineTo` or `moveTo` to this position

### [function Graphics.moveTo](#t_l_Graphics_moveTo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3262 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.moveTo(x, y)`

#### Parameters

`x` - X value

`y` - Y value

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Move the cursor to a position - see lineTo

### [function Graphics.quadraticBezier](#t_l_Graphics_quadraticBezier) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4641 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.quadraticBezier(arr, options)`

#### Parameters

`arr` - An array of three vertices, six enties in form of `[x0,y0,x1,y1,x2,y2]`

`options` - number of points to calulate

#### Returns

Array with calculated points

#### Description

Calculate the square area under a Bezier curve.

x0,y0: start point x1,y1: control point y2,y2: end point

Max 10 points without start point.

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.reset](#t_l_Graphics_reset) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L994 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.reset()`

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Reset the state of Graphics to the defaults (e.g. Color, Font, etc) that would have been used when Graphics was initialised.

**Note:** The current graphics theme is not reset when `g.reset()` is called. To reset that you must store the value from `g.getTheme()` before calling `g.setTheme()`, and manually set it back afterwards.

### [function Graphics.scroll](#t_l_Graphics_scroll) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4265 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.scroll(x, y)`

#### Parameters

`x` - X direction. >0 = to right

`y` - Y direction. >0 = down

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Scroll the contents of this graphics in a certain direction. The remaining area is filled with the background color.

Note: This uses repeated pixel reads and writes, so will not work on platforms that don't support pixel reads.

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.setBgColor](#t_l_Graphics_setBgColor) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1643 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setBgColor(r, g, b)`

#### Parameters

`r` - Red (between 0 and 1) **OR_\* an integer representing the color in the current bit depth and color order \*_OR** a hexidecimal color string of the form `'#012345'`

`g` - Green (between 0 and 1)

`b` - Blue (between 0 and 1)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the background color to use for subsequent drawing operations.

See `[Graphics.setColor](#l_Graphics_setColor)` for more information on the mapping of `r`, `g`, and `b` to pixel values.

**Note:_\* On devices with low flash memory, `r` \*_must** be an integer representing the color in the current bit depth. It cannot be a floating point value, and `g` and `b` are ignored.

### [function Graphics.setClipRect](#t_l_Graphics_setClipRect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1703 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setClipRect(x1, y1, x2, y2)`

#### Parameters

`x1` - Top left X coordinate

`y1` - Top left Y coordinate

`x2` - Bottom right X coordinate

`y2` - Bottom right Y coordinate

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

This sets the 'clip rect' that subsequent drawing operations are clipped to sit between.

These values are inclusive - e.g. `g.setClipRect(1,0,5,0)` will ensure that only pixel rows 1,2,3,4,5 are touched on column 0.

**Note:** For maximum flexibility on Bangle.js 1, the values here are not range checked. For normal use, X and Y should be between 0 and `getWidth()-1`/`getHeight()-1`.

**Note:** The x/y values here are rotated, so that if `[Graphics.setRotation](#l_Graphics_setRotation)` is used they correspond to the coordinates given to the draw functions, _not to the physical device pixels_.

**Note:** This is not available in devices with low flash memory

### [function Graphics.setColor](#t_l_Graphics_setColor) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1608 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setColor(r, g, b)`

#### Parameters

`r` - Red (between 0 and 1) **OR_\* an integer representing the color in the current bit depth and color order \*_OR** a hexidecimal color string of the form `'#012345'`

`g` - \[optional\] Green (between 0 and 1)

`b` - \[optional\] Blue (between 0 and 1)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the color to use for subsequent drawing operations.

If just `r` is specified as an integer, the numeric value will be written directly into a pixel. eg. On a 24 bit `[Graphics](#Graphics)` instance you set bright blue with either `g.setColor(0,0,1)` or `g.setColor(0x0000FF)`.

A good shortcut to ensure you get white on all platforms is to use `g.setColor(-1)`

The mapping is as follows:

-   32 bit: `r,g,b` => `0xFFrrggbb`
-   24 bit: `r,g,b` => `0xrrggbb`
-   16 bit: `r,g,b` => `0brrrrrggggggbbbbb` (RGB565)
-   Other bpp: `r,g,b` => white if `r+g+b > 50%`, otherwise black (use `r` on its own as an integer)

If you specified `color_order` when creating the `[Graphics](#Graphics)` instance, `r`,`g` and `b` will be swapped as you specified.

**Note:_\* On devices with low flash memory, `r` \*_must** be an integer representing the color in the current bit depth. It cannot be a floating point value, and `g` and `b` are ignored.

### [function Graphics.setFont](#t_l_Graphics_setFont) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1982 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFont(name, size)`

#### Parameters

`name` - The name of the font to use (if undefined, the standard 4x6 font will be used)

`size` - The size of the font (or undefined)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the font by name. Various forms are available:

-   `g.setFont("4x6")` - standard 4x6 bitmap font
-   `g.setFont("Vector:12")` - vector font 12px high
-   `g.setFont("4x6:2")` - 4x6 bitmap font, doubled in size
-   `g.setFont("6x8:2x3")` - 6x8 bitmap font, doubled in width, tripled in height

You can also use these forms, but they are not recommended:

-   `g.setFont("Vector12")` - vector font 12px high
-   `g.setFont("4x6",2)` - 4x6 bitmap font, doubled in size

`g.getFont()` will return the current font as a String.

For a list of available font names, you can use `g.getFonts()`.

**Note:** This is not available in devices with low flash memory

### [function Graphics.setFont12x20](#t_l_Graphics_setFont12x20) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_font_12x20.c#L345 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFont12x20(scale)`

#### Parameters

`scale` - \[optional\] If >1 the font will be scaled up by that amount

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the current font

### [function Graphics.setFont14](#t_l_Graphics_setFont14) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_font_14.c#L310 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFont14(scale)`

#### Parameters

`scale` - The scale factor, default=1 (2=2x size)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the current font

### [function Graphics.setFont17](#t_l_Graphics_setFont17) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_font_17.c#L376 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFont17(scale)`

#### Parameters

`scale` - The scale factor, default=1 (2=2x size)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the current font

### [function Graphics.setFont22](#t_l_Graphics_setFont22) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_font_22.c#L473 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFont22(scale)`

#### Parameters

`scale` - The scale factor, default=1 (2=2x size)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the current font

### [function Graphics.setFont28](#t_l_Graphics_setFont28) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_font_28.c#L595 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFont28(scale)`

#### Parameters

`scale` - The scale factor, default=1 (2=2x size)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the current font

### [function Graphics.setFont6x15](#t_l_Graphics_setFont6x15) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_font_6x15.c#L163 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFont6x15(scale)`

#### Parameters

`scale` - (optional) If >1 the font will be scaled up by that amount

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the current font

### [function Graphics.setFontAlign](#t_l_Graphics_setFontAlign) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1916 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFontAlign(x, y, rotation)`

#### Parameters

`x` - X alignment. -1=left (default), 0=center, 1=right

`y` - Y alignment. -1=top (default), 0=center, 1=bottom

`rotation` - Rotation of the text. 0=normal, 1=90 degrees clockwise, 2=180, 3=270

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the alignment for subsequent calls to `drawString`

**Note:** This is not available in devices with low flash memory

### [function Graphics.setFontBitmap](#t_l_Graphics_setFontBitmap) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1763 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFontBitmap()`

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Make subsequent calls to `drawString` use the built-in 4x6 pixel bitmapped Font

It is recommended that you use `Graphics.setFont("4x6")` for more flexibility.

### [function Graphics.setFontCustom](#t_l_Graphics_setFontCustom) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1816 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFontCustom(bitmap, firstChar, width, height)`

#### Parameters

`bitmap` - A column-first, MSB-first, 1bpp bitmap containing the font bitmap

`firstChar` - The first character in the font - usually 32 (space)

`width` - The width of each character in the font. Either an integer, or a string where each character represents the width

`height` - The height as an integer (max 255). Bits 8-15 represent the scale factor (eg. `2<<8` is twice the size). Bits 16-23 represent the BPP (0,1=1 bpp, 2=2 bpp, 4=4 bpp)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Make subsequent calls to `drawString` use a Custom Font of the given height. See the [Fonts page](http://www.espruino.com/Fonts) for more information about custom fonts and how to create them.

For examples of use, see the [font modules](https://www.espruino.com/Fonts#font-modules).

**Note:** while you can specify the character code of the first character with `firstChar`, the newline character 13 will always be treated as a newline and not rendered.

**Note:** This is not available in devices with low flash memory

### [function Graphics.setFontPBF](#t_l_Graphics_setFontPBF) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1882 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFontPBF(file, scale)`

#### Parameters

`file` - The font as a PBF file

`scale` - The scale factor, default=1 (2=2x size)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

**Note:** This is not available in devices with low flash memory

### [function Graphics.setFontVector](#t_l_Graphics_setFontVector) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1775 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setFontVector(size)`

#### Parameters

`size` - The height of the font, as an integer

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Make subsequent calls to `drawString` use a Vector Font of the given height.

It is recommended that you use `Graphics.setFont("Vector", size)` for more flexibility.

**Note:** This is not available in devices with low flash memory or NO_VECTOR_FONT

### [function Graphics.setPixel](#t_l_Graphics_setPixel) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1381 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setPixel(x, y, col)`

#### Parameters

`x` - The left

`y` - The top

`col` - The color (if `undefined`, the foreground color is useD)

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set a pixel's color

### [function Graphics.setRotation](#t_l_Graphics_setRotation) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L3475 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setRotation(rotation, reflect)`

#### Parameters

`rotation` - The clockwise rotation. 0 for no rotation, 1 for 90 degrees, 2 for 180, 3 for 270

`reflect` - Whether to reflect the image

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the current rotation of the graphics device.

### [function Graphics.setTheme](#t_l_Graphics_setTheme) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4937 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.setTheme(theme)`

#### Parameters

`theme` - An object of the form returned by `[Graphics.theme](#l_Graphics_theme)`

#### Returns

The instance of Graphics this was called on, to allow call chaining

#### Description

Set the global colour scheme. On Bangle.js, this is reloaded from `settings.json` for each new app loaded.

See `[Graphics.theme](#l_Graphics_theme)` for the fields that can be provided. For instance you can change the background to red using:

```

g.setTheme({bg:"#f00"});
```

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.stringMetrics](#t_l_Graphics_stringMetrics) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L2433 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.stringMetrics(str)`

#### Parameters

`str` - The string

#### Returns

An object containing `{width,height,etc}` for the string - see below

#### Description

Return the width and height in pixels of a string of text in the current font. The object returned contains:

```

{
  width,              // Width of the string in pixels
  height,             // Height of the string in pixels
  unrenderableChars,  // If true, the string contains characters that the current font isn't able to render.
  imageCount,         // How many inline images are in this string?
  maxImageHeight,     // If there are images, what is the maximum height of all images?
}
```

### [function Graphics.stringWidth](#t_l_Graphics_stringWidth) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L2415 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.stringWidth(str)`

#### Parameters

`str` - The string

#### Returns

The length of the string in pixels

#### Description

Return the size in pixels of a string of text in the current font

### [property Graphics.theme](#t_l_Graphics_theme) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4888 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property Graphics.theme`

#### Returns

An object containing the current 'theme' (see below)

#### Description

Returns an object of the form:

```

{
  fg : 0xFFFF,  // foreground colour
  bg : 0,       // background colour
  fg2 : 0xFFFF,  // accented foreground colour
  bg2 : 0x0007,  // accented background colour
  fgH : 0xFFFF,  // highlighted foreground colour
  bgH : 0x02F7,  // highlighted background colour
  dark : true,  // Is background dark (e.g. foreground should be a light colour)
}
```

These values can then be passed to `g.setColor`/`g.setBgColor` for example `g.setColor(g.theme.fg2)`. When the `[Graphics](#Graphics)` instance is reset, the background color is automatically set to `g.theme.bg` and foreground is set to `g.theme.fg`.

On Bangle.js these values can be changed by writing updated values to `theme` in `settings.js` and reloading the app - or they can be changed temporarily by calling `[Graphics.setTheme](#l_Graphics_setTheme)`

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.toColor](#t_l_Graphics_toColor) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L1409 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.toColor(r, g, b)`

#### Parameters

`r` - Red (between 0 and 1) **OR_\* an integer representing the color in the current bit depth and color order \*_OR** a hexidecimal color string of the form `'#rrggbb'` or `'#rgb'`

`g` - Green (between 0 and 1)

`b` - Blue (between 0 and 1)

#### Returns

The color index represented by the arguments

#### Description

Work out the color value to be used in the current bit depth based on the arguments.

This is used internally by setColor and setBgColor

```

// 1 bit
g.toColor(1,1,1) => 1
// 16 bit
g.toColor(1,0,0) => 0xF800
```

**Note:** This is not available in devices with low flash memory

### [function Graphics.transformVertices](#t_l_Graphics_transformVertices) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L4712 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.transformVertices(verts, transformation)`

#### Parameters

`verts` - An array of vertices, of the form `[x1,y1,x2,y2,x3,y3,etc]`

`transformation` - The transformation to apply, either an Object or an Array (see below)

#### Returns

Array of transformed vertices

#### Description

Transformation can be:

-   An object of the form
    
    ```
    
    {
    x: float, // x offset (default 0)
    y: float, // y offset (default 0)
    scale: float, // scale factor (default 1)
    rotate: float, // angle in radians (default 0)
    }
    ```
    
-   A six-element array of the form `[a,b,c,d,e,f]`, which represents the 2D transformation matrix
    
    ```
    
    a c e
    b d f
    0 0 1
    ```
    
    Apply a transformation to an array of vertices.
    

**Note:** This is not available in devices with low flash memory or 'Original' Espruino boards

### [function Graphics.wrapString](#t_l_Graphics_wrapString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/graphics/jswrap_graphics.c#L2474 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Graphics.wrapString(str, maxWidth)`

#### Parameters

`str` - The string

`maxWidth` - The width in pixels

#### Returns

An array of lines that are all less than `maxWidth`

#### Description

Wrap a string to the given pixel width using the current font, and return the lines as an array.

To render within the screen's width you can do:

```

g.drawString(g.wrapString(text, g.getWidth()).join("\n")),
```

## [heatshrink Library](#t_heatshrink)

[(top)](javascript:toppos\(\);)

Simple library for compression/decompression using [heatshrink](https://github.com/atomicobject/heatshrink), an [LZSS](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Storer%E2%80%93Szymanski) compression tool.

Espruino uses heatshrink internally to compress RAM down to fit in Flash memory when `save()` is used. This just exposes that functionality.

Functions here take and return buffers of data. There is no support for streaming, so both the compressed and decompressed data must be able to fit in memory at the same time.

```

var c = require("heatshrink").compress("Hello World");
// =new Uint8Array([....]).buffer
var d = require("heatshrink").decompress(c);
// =new Uint8Array([72, 101, ...]).buffer
E.toString(d)
// ="Hello World"
```

If you'd like a way to perform compression/decompression on desktop, check out https://github.com/espruino/EspruinoWebTools#heatshrinkjs

#### Methods and Fields

-   [require("heatshrink").compress(data)](#l_heatshrink_compress)
-   [require("heatshrink").decompress(data)](#l_heatshrink_decompress)

### [heatshrink.compress](#t_l_heatshrink_compress) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/compression/jswrap_heatshrink.c#L54 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("heatshrink").compress(data)`

#### Parameters

`data` - The data to compress

#### Returns

Returns the result as an `[ArrayBuffer](#ArrayBuffer)`

#### Description

Compress the data supplied as input, and return heatshrink encoded data as an `[ArrayBuffer](#ArrayBuffer)`.

No type information is stored, and the `data` argument is treated as an array of bytes (whether it is a `[String](#String)`/`[Uint8Array](#Uint8Array)` or even `[Uint16Array](#Uint16Array)`), so the result of decompressing any compressed data will always be an `[ArrayBuffer](#ArrayBuffer)`.

If you'd like a way to perform compression/decompression on desktop, check out https://github.com/espruino/EspruinoWebTools#heatshrinkjs

**Note:** This is not available in devices with low flash memory

### [heatshrink.decompress](#t_l_heatshrink_decompress) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/compression/jswrap_heatshrink.c#L104 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("heatshrink").decompress(data)`

#### Parameters

`data` - The data to decompress

#### Returns

Returns the result as an `[ArrayBuffer](#ArrayBuffer)`

#### Description

Decompress the heatshrink-encoded data supplied as input, and return it as an `[ArrayBuffer](#ArrayBuffer)`.

To get the result as a String, wrap `require("heatshrink").decompress` in `[E.toString](#l_E_toString)`: `E.toString(require("heatshrink").decompress(...))`

If you'd like a way to perform compression/decompression on desktop, check out https://github.com/espruino/EspruinoWebTools#heatshrinkjs

**Note:** This is not available in devices with low flash memory

## [I2C Class](#t_I2C)

[(top)](javascript:toppos\(\);)

This class allows use of the built-in I2C ports. Currently it allows I2C Master mode only.

All addresses are in 7 bit format. If you have an 8 bit address then you need to shift it one bit to the right.

#### Instances

-   [](#l__global_I2C1)`[I2C1](#l__global_I2C1)` The first I2C port

#### Methods and Fields

-   [I2C.find(pin)](#l_I2C_find)
-   [constructor I2C()](#l_I2C_I2C)
-   [function I2C.readFrom(address, quantity)](#l_I2C_readFrom)
-   [function I2C.readReg(address, reg, quantity)](#l_I2C_readReg)
-   [function I2C.setup(options)](#l_I2C_setup)
-   [function I2C.writeTo(address, data, ...)](#l_I2C_writeTo)

### [I2C.find](#t_l_I2C_find) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L533 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`I2C.find(pin)`

#### Parameters

`pin` - A pin to search with

#### Returns

An object of type `[I2C](#I2C)`, or `undefined` if one couldn't be found.

#### Description

**DEPRECATED** - this will be removed in subsequent versions of Espruino

Try and find an I2C hardware device that will work on this pin (e.g. `[I2C1](#l__global_I2C1)`)

May return undefined if no device can be found.

**Note:** This is not available in devices with low flash memory

### [constructor I2C](#t_l_I2C_I2C) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L517 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`new I2C()`

#### Returns

An I2C object

#### Description

Create a software I2C port. This has limited functionality (no baud rate), but it can work on any pins.

Use `[I2C.setup](#l_I2C_setup)` to configure this port.

### [function I2C.readFrom](#t_l_I2C_readFrom) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L678 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function I2C.readFrom(address, quantity)`

#### Parameters

`address` - The 7 bit address of the device to request bytes from, or an object of the form `{address:12, stop:false}` to send this data without a STOP signal.

`quantity` - The number of bytes to request

#### Returns

The data that was returned - as a `[Uint8Array](#Uint8Array)`

#### Description

Request bytes from the given slave device, and return them as a `[Uint8Array](#Uint8Array)` (packed array of bytes). This is like using Arduino Wire's requestFrom, available and read functions. Sends a STOP unless `{address:X, stop:false}` is used.

### [function I2C.readReg](#t_l_I2C_readReg) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L742 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function I2C.readReg(address, reg, quantity)`

#### Parameters

`address` - The 7 bit address of the device to request bytes from

`reg` - The register on the device to read bytes from

`quantity` - The number of bytes to request

#### Returns

The data that was returned - as a `[Uint8Array](#Uint8Array)`

#### Description

Request bytes from a register on the given I2C slave device, and return them as a `[Uint8Array](#Uint8Array)` (packed array of bytes).

This is the same as calling `[I2C.writeTo](#l_I2C_writeTo)` and `[I2C.readFrom](#l_I2C_readFrom)`:

```

I2C.readReg = function(address, reg, quantity) {
  this.writeTo({address:address, stop:false}, reg);
  return this.readFrom(address, quantity);
};
```

### [function I2C.setup](#t_l_I2C_setup) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L577 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function I2C.setup(options)`

#### Parameters

`options` - \[optional\] A structure containing extra information on initialising the I2C port  
`{scl:pin, sda:pin, bitrate:100000}`  
You can find out which pins to use by looking at [your board's reference page](#boards) and searching for pins with the `[I2C](#I2C)` marker. Note that 400kHz is the maximum bitrate for most parts.

#### Description

Set up this I2C port

If not specified in options, the default pins are used (usually the lowest numbered pins on the lowest port that supports this peripheral)

### [function I2C.writeTo](#t_l_I2C_writeTo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L638 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function I2C.writeTo(address, data, ...)`

#### Parameters

`address` - The 7 bit address of the device to transmit to, or an object of the form `{address:12, stop:false}` to send this data without a STOP signal.

`data, ...` - One or more items to write. May be ints, strings, arrays, or special objects (see `[E.toUint8Array](#l_E_toUint8Array)` for more info).

#### Description

Transmit to the slave device with the given address. This is like Arduino's beginTransmission, write, and endTransmission rolled up into one.

## [Int16Array Class](#t_Int16Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 16 bit signed integers.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Int16Array(arr, byteOffset, length)](#l_Int16Array_Int16Array)

### [constructor Int16Array](#t_l_Int16Array_Int16Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L377 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Int16Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

## [Int32Array Class](#t_Int32Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 32 bit signed integers.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Int32Array(arr, byteOffset, length)](#l_Int32Array_Int32Array)

### [constructor Int32Array](#t_l_Int32Array_Int32Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L447 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Int32Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

## [Int8Array Class](#t_Int8Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 8 bit signed integers.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Int8Array(arr, byteOffset, length)](#l_Int8Array_Int8Array)

### [constructor Int8Array](#t_l_Int8Array_Int8Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L331 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Int8Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

## [InternalError Class](#t_InternalError)

[(top)](javascript:toppos\(\);)

The base class for internal errors

#### Methods and Fields

-   [constructor InternalError(message)](#l_InternalError_InternalError)
-   [function InternalError.toString()](#l_InternalError_toString)

### [constructor InternalError](#t_l_InternalError_InternalError) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L119 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/InternalError)

[(top)](javascript:toppos\(\);)

#### Call type:

`new InternalError(message)`

#### Parameters

`message` - \[optional\] An message string

#### Returns

An InternalError object

#### Description

Creates an InternalError object

### [function InternalError.toString](#t_l_InternalError_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L177 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function InternalError.toString()`

#### Returns

A String

#### Description

## [JSON Class](#t_JSON)

[(top)](javascript:toppos\(\);)

An Object that handles conversion to and from the JSON data interchange format

#### Methods and Fields

-   [JSON.parse(string)](#l_JSON_parse)
-   [JSON.stringify(data, replacer, space)](#l_JSON_stringify)

### [JSON.parse](#t_l_JSON_parse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_json.c#L171 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)

[(top)](javascript:toppos\(\);)

#### Call type:

`JSON.parse(string)`

#### Parameters

`string` - A JSON string

#### Returns

The JavaScript object created by parsing the data string

#### Description

Parse the given JSON string into a JavaScript object

### [JSON.stringify](#t_l_JSON_stringify) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_json.c#L37 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)

[(top)](javascript:toppos\(\);)

#### Call type:

`JSON.stringify(data, replacer, space)`

#### Parameters

`data` - The data to be converted to a JSON string

`replacer` - \[optional\] This value is ignored

`space` - \[optional\] The number of spaces to use for padding, a string, or null/undefined for no whitespace

#### Returns

A JSON string

#### Description

Convert the given object into a JSON string which can subsequently be parsed with JSON.parse or eval.

**Note:** This differs from JavaScript's standard `[JSON.stringify](#l_JSON_stringify)` in that:

-   The `replacer` argument is ignored
-   Typed arrays like `new Uint8Array(5)` will be dumped as if they were arrays, not as if they were objects (since it is more compact)

## [Math Class](#t_Math)

[(top)](javascript:toppos\(\);)

This is a standard JavaScript class that contains useful Maths routines

#### Methods and Fields

-   [Math.abs(x)](#l_Math_abs)
-   [Math.acos(x)](#l_Math_acos)
-   [Math.asin(x)](#l_Math_asin)
-   [Math.atan(x)](#l_Math_atan)
-   [Math.atan2(y, x)](#l_Math_atan2)
-   [Math.ceil(x)](#l_Math_ceil)
-   [Math.clip(x, min, max)](#l_Math_clip)
-   [Math.cos(theta)](#l_Math_cos)
-   [Math.E](#l_Math_E)
-   [Math.exp(x)](#l_Math_exp)
-   [Math.floor(x)](#l_Math_floor)
-   [Math.LN10](#l_Math_LN10)
-   [Math.LN2](#l_Math_LN2)
-   [Math.log(x)](#l_Math_log)
-   [Math.LOG10E](#l_Math_LOG10E)
-   [Math.LOG2E](#l_Math_LOG2E)
-   [Math.max(args, ...)](#l_Math_max)
-   [Math.min(args, ...)](#l_Math_min)
-   [Math.PI](#l_Math_PI)
-   [Math.pow(x, y)](#l_Math_pow)
-   [Math.randInt(range)](#l_Math_randInt)
-   [Math.random()](#l_Math_random)
-   [Math.round(x)](#l_Math_round)
-   [Math.sign(x)](#l_Math_sign)
-   [Math.sin(theta)](#l_Math_sin)
-   [Math.sqrt(x)](#l_Math_sqrt)
-   [Math.SQRT1\_2](#l_Math_SQRT1_2)
-   [Math.SQRT2](#l_Math_SQRT2)
-   [Math.tan(theta)](#l_Math_tan)
-   [Math.wrap(x, max)](#l_Math_wrap)

### [Math.abs](#t_l_Math_abs) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L151 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/abs)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.abs(x)`

#### Parameters

`x` - A floating point value

#### Returns

The absolute value of x (eg, `Math.abs(2)==2`, but also `Math.abs(-2)==2`)

#### Description

### [Math.acos](#t_l_Math_acos) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L161 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/acos)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.acos(x)`

#### Parameters

`x` - The value to get the arc cosine of

#### Returns

The arc cosine of x, between 0 and PI

#### Description

**Note:** This is not available in devices with extremely low flash memory (eg. HYSTM32\_28)

### [Math.asin](#t_l_Math_asin) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L172 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/asin)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.asin(x)`

#### Parameters

`x` - The value to get the arc sine of

#### Returns

The arc sine of x, between -PI/2 and PI/2

#### Description

**Note:** This is not available in devices with extremely low flash memory (eg. HYSTM32\_28)

### [Math.atan](#t_l_Math_atan) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L186 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.atan(x)`

#### Parameters

`x` - The value to get the arc tangent of

#### Returns

The arc tangent of x, between -PI/2 and PI/2

#### Description

### [Math.atan2](#t_l_Math_atan2) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L231 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/atan2)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.atan2(y, x)`

#### Parameters

`y` - The Y-part of the angle to get the arc tangent of

`x` - The X-part of the angle to get the arc tangent of

#### Returns

The arctangent of Y/X, between -PI and PI

#### Description

**Note:** This is not available in devices with low flash memory

### [Math.ceil](#t_l_Math_ceil) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L432 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.ceil(x)`

#### Parameters

`x` - The value to round up

#### Returns

x, rounded upwards to the nearest integer

#### Description

### [Math.clip](#t_l_Math_clip) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L476 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.clip(x, min, max)`

#### Parameters

`x` - A floating point value to clip

`min` - The smallest the value should be

`max` - The largest the value should be

#### Returns

The value of x, clipped so as not to be below min or above max.

#### Description

DEPRECATED - Please use `[E.clip()](#l_E_clip)` instead. Clip a number to be between min and max (inclusive)

**Note:** This is not available in devices with low flash memory

### [Math.cos](#t_l_Math_cos) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L260 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cos)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.cos(theta)`

#### Parameters

`theta` - The angle to get the cosine of

#### Returns

The cosine of theta

#### Description

### [Math.E](#t_l_Math_E) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L87 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/E)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.E`

#### Returns

The value of E - 2.718281828459045

#### Description

### [Math.exp](#t_l_Math_exp) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L453 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/exp)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.exp(x)`

#### Parameters

`x` - The value raise E to the power of

#### Returns

E^x

#### Description

**Note:** This is not available in devices with extremely low flash memory (eg. HYSTM32\_28)

### [Math.floor](#t_l_Math_floor) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L442 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.floor(x)`

#### Parameters

`x` - The value to round down

#### Returns

x, rounded downwards to the nearest integer

#### Description

### [Math.LN10](#t_l_Math_LN10) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L109 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/LN10)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.LN10`

#### Returns

The natural logarithm of 10 - 2.302585092994046

#### Description

**Note:** This is not available in devices with low flash memory

### [Math.LN2](#t_l_Math_LN2) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L101 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/LN2)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.LN2`

#### Returns

The natural logarithm of 2 - 0.6931471805599453

#### Description

**Note:** This is not available in devices with low flash memory

### [Math.log](#t_l_Math_log) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L464 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/log)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.log(x)`

#### Parameters

`x` - The value to take the logarithm (base E) root of

#### Returns

The log (base E) of x

#### Description

**Note:** This is not available in devices with extremely low flash memory (eg. HYSTM32\_28)

### [Math.LOG10E](#t_l_Math_LOG10E) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L125 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/LOG10E)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.LOG10E`

#### Returns

The base 10 logarithm of e - 0.4342944819032518

#### Description

**Note:** This is not available in devices with low flash memory

### [Math.LOG2E](#t_l_Math_LOG2E) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L117 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/LOG2E)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.LOG2E`

#### Returns

The base 2 logarithm of e - 1.4426950408889634

#### Description

**Note:** This is not available in devices with low flash memory

### [Math.max](#t_l_Math_max) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L528 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.max(args, ...)`

#### Parameters

`args, ...` - Floating point values to clip

#### Returns

The maximum of the supplied values

#### Description

Find the maximum of a series of numbers

### [Math.min](#t_l_Math_min) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L516 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.min(args, ...)`

#### Parameters

`args, ...` - Floating point values to clip

#### Returns

The minimum of the supplied values

#### Description

Find the minimum of a series of numbers

### [Math.PI](#t_l_Math_PI) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L94 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/PI)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.PI`

#### Returns

The value of PI - 3.141592653589793

#### Description

### [Math.pow](#t_l_Math_pow) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L337 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/pow)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.pow(x, y)`

#### Parameters

`x` - The value to raise to the power

`y` - The power x should be raised to

#### Returns

x raised to the power y (x^y)

#### Description

**Note:** This is not available in devices with extremely low flash memory (eg. HYSTM32\_28)

### [Math.randInt](#t_l_Math_randInt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L356 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.randInt(range)`

#### Parameters

`range` - How big a random number do we want

#### Returns

A random integer

#### Description

(Added in 2v25) Returns a random integer `X`, where `0 <= X < range`, or `-2147483648 <= X <= 2147483647` if `range <= 0` or `undefined`

If `range` is supplied, this value is created using `modulo` of a 31 bit integer, so as `val` gets larger (24+ bits) the values produced will be less randomly distributed, and no values above `0x7FFFFFFF` will ever be returned.

If `val==undefined` or `val<=0` a **32 bit** random number will be returned as an int (`-2147483648` .. `2147483647`).

**Note:** this is not part of the JS spec, but is included in Espruino as it makes a lot of sense on embedded targets

### [Math.random](#t_l_Math_random) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L349 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.random()`

#### Returns

A random number X, where `0 <= X < 1`

#### Description

### [Math.round](#t_l_Math_round) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L375 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.round(x)`

#### Parameters

`x` - The value to round

#### Returns

x, rounded to the nearest integer

#### Description

### [Math.sign](#t_l_Math_sign) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L556 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sign)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.sign(x)`

#### Parameters

`x` - The value to get the sign from

#### Returns

sign on x - -1, 1, or 0

#### Description

**Note:** This is not available in devices with extremely low flash memory (eg. HYSTM32\_28)

### [Math.sin](#t_l_Math_sin) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L394 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sin)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.sin(theta)`

#### Parameters

`theta` - The angle to get the sine of

#### Returns

The sine of theta

#### Description

### [Math.sqrt](#t_l_Math_sqrt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L416 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sqrt)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.sqrt(x)`

#### Parameters

`x` - The value to take the square root of

#### Returns

The square root of x

#### Description

**Note:** This is not available in devices with extremely low flash memory (eg. HYSTM32\_28)

### [Math.SQRT1\_2](#t_l_Math_SQRT1_2) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L141 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/SQRT1_2)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.SQRT1_2`

#### Returns

The square root of 1/2 - 0.7071067811865476

#### Description

**Note:** This is not available in devices with low flash memory

### [Math.SQRT2](#t_l_Math_SQRT2) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L133 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/SQRT2)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.SQRT2`

#### Returns

The square root of 2 - 1.4142135623730951

#### Description

**Note:** This is not available in devices with low flash memory

### [Math.tan](#t_l_Math_tan) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L404 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/tan)

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.tan(theta)`

#### Parameters

`theta` - The angle to get the tangent of

#### Returns

The tangent of theta

#### Description

### [Math.wrap](#t_l_Math_wrap) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_math.c#L498 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Math.wrap(x, max)`

#### Parameters

`x` - A floating point value to wrap

`max` - The largest the value should be

#### Returns

The value of x, wrapped so as not to be below min or above max.

#### Description

DEPRECATED - This is not part of standard JavaScript libraries

Wrap a number around if it is less than 0 or greater than or equal to max. For instance you might do: `Math.wrap(angleInDegrees, 360)`

**Note:** This is not available in devices with low flash memory

## [Modules Class](#t_Modules)

[(top)](javascript:toppos\(\);)

Built-in class that caches the modules used by the `[require](#l__global_require)` command

#### Methods and Fields

-   [Modules.addCached(id, sourcecode)](#l_Modules_addCached)
-   [Modules.getCached()](#l_Modules_getCached)
-   [Modules.removeAllCached()](#l_Modules_removeAllCached)
-   [Modules.removeCached(id)](#l_Modules_removeCached)

### [Modules.addCached](#t_l_Modules_addCached) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_modules.c#L240 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Modules.addCached(id, sourcecode)`

#### Parameters

`id` - The module name to add

`sourcecode` - The module's sourcecode

#### Description

Add the given module to the cache

### [Modules.getCached](#t_l_Modules_getCached) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_modules.c#L166 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Modules.getCached()`

#### Returns

An array of module names

#### Description

Return an array of module names that have been cached

### [Modules.removeAllCached](#t_l_Modules_removeAllCached) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_modules.c#L225 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Modules.removeAllCached()`

#### Description

Remove all cached modules

### [Modules.removeCached](#t_l_Modules_removeCached) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_modules.c#L196 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Modules.removeCached(id)`

#### Parameters

`id` - The module name to remove

#### Description

Remove the given module from the list of cached modules

## [NRF Class](#t_NRF)

[(top)](javascript:toppos\(\);)

The NRF class is for controlling functionality of the Nordic nRF51/nRF52 chips.

Most functionality is related to Bluetooth Low Energy, however there are also some functions related to NFC that apply to NRF52-based devices.

#### Methods and Fields

-   [event NRF.advertising(isAdvertising)](#l_NRF_advertising)
-   [NRF.amsCommand(id)](#l_NRF_amsCommand)
-   [NRF.amsGetPlayerInfo(id)](#l_NRF_amsGetPlayerInfo)
-   [NRF.amsGetTrackInfo(id)](#l_NRF_amsGetTrackInfo)
-   [NRF.amsIsActive()](#l_NRF_amsIsActive)
-   [NRF.ancsAction(uid, positive)](#l_NRF_ancsAction)
-   [NRF.ancsGetAppInfo(id)](#l_NRF_ancsGetAppInfo)
-   [NRF.ancsGetNotificationInfo(uid)](#l_NRF_ancsGetNotificationInfo)
-   [NRF.ancsIsActive()](#l_NRF_ancsIsActive)
-   [event NRF.bond(status)](#l_NRF_bond)
-   [event NRF.characteristicsDiscover()](#l_NRF_characteristicsDiscover)
-   [event NRF.connect(addr)](#l_NRF_connect)
-   [NRF.connect(mac, options)](#l_NRF_connect)
-   [event NRF.CTS(info)](#l_NRF_CTS)
-   [NRF.ctsGetTime()](#l_NRF_ctsGetTime)
-   [NRF.ctsIsActive()](#l_NRF_ctsIsActive)
-   [event NRF.disconnect(reason)](#l_NRF_disconnect)
-   [NRF.disconnect()](#l_NRF_disconnect)
-   [NRF.eraseBonds(callback)](#l_NRF_eraseBonds)
-   [event NRF.error(msg)](#l_NRF_error)
-   [NRF.filterDevices(devices, filters)](#l_NRF_filterDevices)
-   [NRF.findDevices(callback, options)](#l_NRF_findDevices)
-   [NRF.getAddress(current)](#l_NRF_getAddress)
-   [NRF.getAdvertisingData(data, options)](#l_NRF_getAdvertisingData)
-   [NRF.getBattery()](#l_NRF_getBattery)
-   [NRF.getSecurityStatus()](#l_NRF_getSecurityStatus)
-   [event NRF.HID()](#l_NRF_HID)
-   [event NRF.mtu(arr)](#l_NRF_mtu)
-   [event NRF.passkey(passkey)](#l_NRF_passkey)
-   [event NRF.phy(arr)](#l_NRF_phy)
-   [event NRF.phy\_req(arr)](#l_NRF_phy_req)
-   [NRF.requestDevice(options)](#l_NRF_requestDevice)
-   [NRF.resolveAddress(options)](#l_NRF_resolveAddress)
-   [NRF.restart(callback)](#l_NRF_restart)
-   [event NRF.security(status)](#l_NRF_security)
-   [NRF.sendHIDReport(data, callback)](#l_NRF_sendHIDReport)
-   [event NRF.servicesDiscover()](#l_NRF_servicesDiscover)
-   [NRF.setAddress(addr)](#l_NRF_setAddress)
-   [NRF.setAdvertising(data, options)](#l_NRF_setAdvertising)
-   [NRF.setConnectionInterval(interval)](#l_NRF_setConnectionInterval)
-   [NRF.setLowPowerConnection(lowPower)](#l_NRF_setLowPowerConnection)
-   [NRF.setRSSIHandler(callback)](#l_NRF_setRSSIHandler)
-   [NRF.setScan(callback, options)](#l_NRF_setScan)
-   [NRF.setScanResponse(data)](#l_NRF_setScanResponse)
-   [NRF.setSecurity(options)](#l_NRF_setSecurity)
-   [NRF.setServices(data, options)](#l_NRF_setServices)
-   [NRF.setTxPower(power)](#l_NRF_setTxPower)
-   [NRF.setWhitelist(whitelisting)](#l_NRF_setWhitelist)
-   [NRF.sleep()](#l_NRF_sleep)
-   [NRF.startBonding(forceRepair)](#l_NRF_startBonding)
-   [NRF.updateConnection(options)](#l_NRF_updateConnection)
-   [NRF.updateServices(data)](#l_NRF_updateServices)
-   [NRF.wake()](#l_NRF_wake)

### [event NRF.advertising](#t_l_NRF_advertising) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L447 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('advertising', function(isAdvertising) { ... });`

#### Parameters

`isAdvertising` - Whether we are advertising or not

#### Description

Called when Bluetooth advertising starts or stops on Espruino

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.amsCommand](#t_l_NRF_amsCommand) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3314 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.amsCommand(id)`

#### Parameters

`id` - For example, 'play', 'pause', 'volup' or 'voldown'

#### Description

Send an AMS command to an Apple Media Service device to control music playback

Command is one of play, pause, playpause, next, prev, volup, voldown, repeat, shuffle, skipforward, skipback, like, dislike, bookmark

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.amsGetPlayerInfo](#t_l_NRF_amsGetPlayerInfo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3224 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.amsGetPlayerInfo(id)`

#### Parameters

`id` - Either 'name', 'playbackinfo' or 'volume'

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the connection is complete

#### Description

Get Apple Media Service (AMS) info for the current media player. "playbackinfo" returns a concatenation of three comma-separated values:

-   PlaybackState: a string that represents the integer value of the playback state:
    -   PlaybackStatePaused = 0
    -   PlaybackStatePlaying = 1
    -   PlaybackStateRewinding = 2
    -   PlaybackStateFastForwarding = 3
-   PlaybackRate: a string that represents the floating point value of the playback rate.
-   ElapsedTime: a string that represents the floating point value of the elapsed time of the current track, in seconds

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.amsGetTrackInfo](#t_l_NRF_amsGetTrackInfo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3275 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.amsGetTrackInfo(id)`

#### Parameters

`id` - Either 'artist', 'album', 'title' or 'duration'

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the connection is complete

#### Description

Get Apple Media Service (AMS) info for the currently-playing track

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.amsIsActive](#t_l_NRF_amsIsActive) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3205 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.amsIsActive()`

#### Parameters

#### Returns

True if Apple Media Service (AMS) has been initialised and is active

#### Description

Check if Apple Media Service (AMS) is currently active on the BLE connection

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.ancsAction](#t_l_NRF_ancsAction) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3079 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.ancsAction(uid, positive)`

#### Parameters

`uid` - The UID of the notification to respond to

`positive` - `true` for positive action, `false` for negative

#### Description

Send an ANCS action for a specific Notification UID. Corresponds to posaction/negaction in the 'ANCS' event that was received

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.ancsGetAppInfo](#t_l_NRF_ancsGetAppInfo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3156 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.ancsGetAppInfo(id)`

#### Parameters

`id` - The app ID to get information for

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the connection is complete

#### Description

Get ANCS info for an app (app id is available via `[NRF.ancsGetNotificationInfo](#l_NRF_ancsGetNotificationInfo)`)

Promise returns:

```

{
  "uid" : int,
  "appId" : string,
  "title" : string,
  "subtitle" : string,
  "message" : string,
  "messageSize" : string,
  "date" : string,
  "posAction" : string,
  "negAction" : string,
  "name" : string,
}
```

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.ancsGetNotificationInfo](#t_l_NRF_ancsGetNotificationInfo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3103 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.ancsGetNotificationInfo(uid)`

#### Parameters

`uid` - The UID of the notification to get information for

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the connection is complete

#### Description

Get ANCS info for a notification event received via `[E.ANCS](#l_E_ANCS)`, e.g.:

```

E.on('ANCS', event => {
  NRF.ancsGetNotificationInfo( event.uid ).then(a=>print("Notify",E.toJS(a)));
});
```

Returns:

```

{
  "uid" : integer,
  "appId": string,
  "title": string,
  "subtitle": string,
  "message": string,
  "messageSize": string,
  "date": string,
  "posAction": string,
  "negAction": string
}
```

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.ancsIsActive](#t_l_NRF_ancsIsActive) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3059 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.ancsIsActive()`

#### Parameters

#### Returns

True if Apple Notification Center Service (ANCS) has been initialised and is active

#### Description

Check if Apple Notification Center Service (ANCS) is currently active on the BLE connection

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.bond](#t_l_NRF_bond) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L458 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('bond', function(status) { ... });`

#### Parameters

`status` - One of `'request'/'start'/'success'/'fail'`

#### Description

Called during the bonding process to update on status

`status` is one of:

-   `"request"` - Bonding has been requested in code via `[NRF.startBonding](#l_NRF_startBonding)`
-   `"start"` - The bonding procedure has started
-   `"success"` - The bonding procedure has succeeded (`[NRF.startBonding](#l_NRF_startBonding)`'s promise resolves)
-   `"fail"` - The bonding procedure has failed (`[NRF.startBonding](#l_NRF_startBonding)`'s promise rejects)

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.characteristicsDiscover](#t_l_NRF_characteristicsDiscover) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L495 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('characteristicsDiscover', function() { ... });`

#### Description

Called with discovered characteristics when discovery is finished

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [event NRF.connect](#t_l_NRF_connect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L372 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('connect', function(addr) { ... });`

#### Parameters

`addr` - The address of the device that has connected

#### Description

Called when a host device connects to Espruino. The first argument contains the address.

### [NRF.connect](#t_l_NRF_connect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3619 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.connect(mac, options)`

#### Parameters

`mac` - The MAC address to connect to

`options` - (Espruino-specific) An object of connection options (see `[BluetoothRemoteGATTServer.connect](#l_BluetoothRemoteGATTServer_connect)` for full details)

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the connection is complete

#### Description

Connect to a BLE device by MAC address. Returns a promise, the argument of which is the `[BluetoothRemoteGATTServer](#BluetoothRemoteGATTServer)` connection.

```

NRF.connect("aa:bb:cc:dd:ee").then(function(server) {
  // ...
});
```

This has the same effect as calling `BluetoothDevice.gatt.connect` on a `[BluetoothDevice](#BluetoothDevice)` requested using `[NRF.requestDevice](#l_NRF_requestDevice)`. It just allows you to specify the address directly (without having to scan).

You can use it as follows - this would connect to another Puck device and turn its LED on:

```

var gatt;
NRF.connect("aa:bb:cc:dd:ee random").then(function(g) {
  gatt = g;
  return gatt.getPrimaryService("6e400001-b5a3-f393-e0a9-e50e24dcca9e");
}).then(function(service) {
  return service.getCharacteristic("6e400002-b5a3-f393-e0a9-e50e24dcca9e");
}).then(function(characteristic) {
  return characteristic.writeValue("LED1.set()\n");
}).then(function() {
  gatt.disconnect();
  console.log("Done!");
});
```

**Note:** Espruino Bluetooth devices use a type of BLE address known as 'random static', which is different to a 'public' address. To connect to an Espruino device you'll need to use an address string of the form

```
"aa:bb:cc:dd:ee
random"
```

rather than just `"aa:bb:cc:dd:ee"`. If you scan for devices with `[NRF.findDevices](#l_NRF_findDevices)`/`[NRF.setScan](#l_NRF_setScan)` then addresses are already reported in the correct format.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [event NRF.CTS](#t_l_NRF_CTS) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3377 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('CTS', function(info) { ... });`

#### Parameters

`info` - An object (see below)

#### Description

Returns time information from the Current Time Service (if requested with `[NRF.ctsGetTime](#l_NRF_ctsGetTime)` and is activated by calling `NRF.setServices(..., {..., cts:true})`)

```

{
  date : // Date object with the current date
  day :  // if known, 0=sun,1=mon (matches JS `Date`)
  reason : [ // reason for the date change
      "external", // External time change
      "manual",   // Manual update
      "timezone", // Timezone changed
      "DST",      // Daylight savings
    ]
  timezone // if LTI characteristic exists, this is the timezone
  dst      // if LTI characteristic exists, this is the dst adjustment
}
```

For instance this can be used as follows to update Espruino's time:

```

E.on('CTS',e=>{
  setTime(e.date.getTime()/1000);
});
NRF.ctsGetTime(); // also returns a promise with CTS info
```

**Note:** This is only available in Bangle.js smartwatches

### [NRF.ctsGetTime](#t_l_NRF_ctsGetTime) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3412 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.ctsGetTime()`

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when time is received

#### Description

Read the time from CTS - creates an `NRF.on('CTS', ...)` event as well

```

NRF.ctsGetTime(); // also returns a promise
```

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.ctsIsActive](#t_l_NRF_ctsIsActive) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3358 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.ctsIsActive()`

#### Parameters

#### Returns

True if Apple Current Time Service (CTS) has been initialised and is active

#### Description

Check if Apple Current Time Service (CTS) is currently active on the BLE connection

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.disconnect](#t_l_NRF_disconnect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L383 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('disconnect', function(reason) { ... });`

#### Parameters

`reason` - The reason code reported back by the BLE stack - see Nordic's [`ble_hci.h` file](https://github.com/espruino/Espruino/blob/master/targetlibs/nrf5x_12/components/softdevice/s132/headers/ble_hci.h#L71) for more information

#### Description

Called when a host device disconnects from Espruino.

The most common reason is: \* 19 - `REMOTE_USER_TERMINATED_CONNECTION` \* 22 - `LOCAL_HOST_TERMINATED_CONNECTION`

### [NRF.disconnect](#t_l_NRF_disconnect) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L721 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.disconnect()`

#### Description

If a device is connected to Espruino, disconnect from it.

### [NRF.eraseBonds](#t_l_NRF_eraseBonds) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L804 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.eraseBonds(callback)`

#### Parameters

`callback` - \[optional\] A function to be called while the softdevice is uninitialised. Use with caution - accessing console/bluetooth will almost certainly result in a crash.

#### Description

Delete all data stored for all peers (bonding data used for secure connections). This cannot be done while a connection is active, so if there is a connection it will be postponed until everything is disconnected (which can be done by calling `[NRF.disconnect()](#l_NRF_disconnect)` and waiting).

Booting your device while holding all buttons down together should also have the same effect.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.error](#t_l_NRF_error) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L397 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('error', function(msg) { ... });`

#### Parameters

`msg` - The error string

#### Description

Called when the Nordic Bluetooth stack (softdevice) generates an error. In pretty much all cases an Exception will also have been thrown.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.filterDevices](#t_l_NRF_filterDevices) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L2292 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.filterDevices(devices, filters)`

#### Parameters

`devices` - An array of `[BluetoothDevice](#BluetoothDevice)` objects, from `[NRF.findDevices](#l_NRF_findDevices)` or similar

`filters` - A list of filters (as would be passed to `[NRF.requestDevice](#l_NRF_requestDevice)`) to filter devices by

#### Returns

An array of `[BluetoothDevice](#BluetoothDevice)` objects that match the given filters

#### Description

This function can be used to quickly filter through Bluetooth devices.

For instance if you wish to scan for multiple different types of device at the same time then you could use `[NRF.findDevices](#l_NRF_findDevices)` with all the filters you're interested in. When scanning is finished you can then use `[NRF.filterDevices](#l_NRF_filterDevices)` to pick out just the devices of interest.

```

// the two types of device we're interested in
var filter1 = [{serviceData:{"fe95":{}}}];
var filter2 = [{namePrefix:"Pixl.js"}];
// the following filter will return both types of device
var allFilters = filter1.concat(filter2);
// now scan for both types of device, and filter them out afterwards
NRF.findDevices(function(devices) {
  var devices1 = NRF.filterDevices(devices, filter1);
  var devices2 = NRF.filterDevices(devices, filter2);
  // ...
}, {filters : allFilters});
```

### [NRF.findDevices](#t_l_NRF_findDevices) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L2345 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.findDevices(callback, options)`

#### Parameters

`callback` - The callback to call with received advertising packets (as `[BluetoothDevice](#BluetoothDevice)`), or undefined to stop

`options` - \[optional\] A time in milliseconds to scan for (defaults to 2000), Or an optional object `{filters: ..., timeout : ..., active: bool}` (as would be passed to `[NRF.requestDevice](#l_NRF_requestDevice)`) to filter devices by

#### Description

Utility function to return a list of BLE devices detected in range. Behind the scenes, this uses `[NRF.setScan(...)](#l_NRF_setScan)` and collates the results.

```

NRF.findDevices(function(devices) {
  console.log(devices);
}, 1000);
```

prints something like:

```

[
  BluetoothDevice {
    "id" : "e7:e0:57:ad:36:a2 random",
    "rssi": -45,
    "services": [ "4567" ],
    "serviceData" : { "0123" : [ 1 ] },
    "manufacturer" : 1424,
    "manufacturerData" : new Uint8Array([ ... ]).buffer,
    "data": new ArrayBuffer([ ... ]).buffer,
    "name": "Puck.js 36a2"
   },
  BluetoothDevice {
    "id": "c0:52:3f:50:42:c9 random",
    "rssi": -65,
    "data": new ArrayBuffer([ ... ]),
    "name": "Puck.js 8f57"
   }
 ]
```

For more information on the structure returned, see `[NRF.setScan](#l_NRF_setScan)`.

If you want to scan only for specific devices you can replace the timeout with an object of the form `{filters: ..., timeout : ..., active: bool}` using the filters described in `[NRF.requestDevice](#l_NRF_requestDevice)`. For example to search for devices with Espruino's `manufacturerData`:

```

NRF.findDevices(function(devices) {
  ...
}, {timeout : 2000, filters : [{ manufacturerData:{0x0590:{}} }] });
```

You could then use [`BluetoothDevice.gatt.connect(...)`](/Reference#l_BluetoothRemoteGATTServer_connect) on the device returned to make a connection.

You can also use [](/Reference#l_NRF_connect)`[NRF.connect(...)](#l_NRF_connect)` on just the `id` string returned, which may be useful if you always want to connect to a specific device.

**Note:** Using findDevices turns the radio's receive mode on for 2000ms (or however long you specify). This can draw a _lot_ of power (12mA or so), so you should use it sparingly or you can run your battery down quickly.

**Note:** The 'data' field contains the data of _the last packet received_. There may have been more packets. To get data for each packet individually use `[NRF.setScan](#l_NRF_setScan)` instead.

### [NRF.getAddress](#t_l_NRF_getAddress) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L830 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.getAddress(current)`

#### Parameters

`current` - If true, return the current address rather than the default

#### Returns

MAC address - a string of the form 'aa:bb:cc:dd:ee:ff'

#### Description

Get this device's default or current Bluetooth MAC address.

For Puck.js, the last 5 characters of this (e.g. `ee:ff`) are used in the device's advertised Bluetooth name.

### [NRF.getAdvertisingData](#t_l_NRF_getAdvertisingData) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L1441 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.getAdvertisingData(data, options)`

#### Parameters

`data` - The data to advertise as an object

`options` - \[optional\] An object of options

#### Returns

An array containing the advertising data

#### Description

This is just like `[NRF.setAdvertising](#l_NRF_setAdvertising)`, except instead of advertising the data, it returns the packet that would be advertised as an array.

In addition, `options` can contain:

-   (2v26+) `flags : bool` if `flags:false`, the Bluetooth appearance flags are left out (usually `[2,1,6]`). It can be very useful to do this if you're using `[NRF.getAdvertisingData(...)](#l_NRF_getAdvertisingData)` to set a scan response packet:

```

NRF.setScanResponse(NRF.getAdvertisingData({
  0x1809 : [Math.round(E.getTemperature())] // temperature service data in scan response
}, {
  flags : false,
  showName : false
}));
```

### [NRF.getBattery](#t_l_NRF_getBattery) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L957 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.getBattery()`

#### Returns

Battery level in volts

#### Description

Get the battery level in volts (the voltage that the NRF chip is running off of).

This is the battery level of the device itself - it has nothing to with any device that might be connected.

### [NRF.getSecurityStatus](#t_l_NRF_getSecurityStatus) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3960 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.getSecurityStatus()`

#### Returns

An object

#### Description

Return an object with information about the security state of the current peripheral connection:

```

{
  connected       // The connection is active (not disconnected).
  encrypted       // Communication on this link is encrypted.
  mitm_protected  // The encrypted communication is also protected against man-in-the-middle attacks.
  bonded          // The peer is bonded with us
  advertising     // Are we currently advertising?
  connected_addr  // If connected=true, the MAC address of the currently connected device
  privacy         // Current BLE privacy / random address settings.
                  // Only present if Espruino was compiled with private address support (like for example on Bangle.js 2).
}
```

If there is no active connection, `{connected:false}` will be returned.

See `[NRF.setSecurity](#l_NRF_setSecurity)` for information about negotiating a secure connection.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.HID](#t_l_NRF_HID) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L476 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('HID', function() { ... });`

#### Description

Called with a single byte value when Espruino is set up as a HID device and the computer it is connected to sends a HID report back to Espruino. This is usually used for handling indications such as the Caps Lock LED.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.mtu](#t_l_NRF_mtu) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L541 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('mtu', function(arr) { ... });`

#### Parameters

`arr` - The negotiated MTU

#### Description

(2v28+) This event is fired when the MTU changes for the active Bluetooth connection. This is the amount of data that can be transferred in one packet.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.passkey](#t_l_NRF_passkey) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L409 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('passkey', function(passkey) { ... });`

#### Parameters

`passkey` - A 6 character numeric String to be displayed

#### Description

(Added in 2v19) Called when a central device connects to Espruino, pairs, and sends a passkey that Espruino should display.

For this to be used, you'll have to specify that your device has a display using `NRF.setSecurity({mitm:1, display:1});`

For instance:

```

NRF.setSecurity({mitm:1, display:1});
NRF.on("passkey", key => print("Enter PIN: ",passkey));
```

It is also possible to specify a static passkey with `NRF.setSecurity({passkey:"123456", mitm:1, display:1});` in which case no `passkey` event handler is needed (this method works on Espruino 2v02 and later)

**Note:** A similar event, [`BluetoothDevice.on("passkey", ...)`](http://www.espruino.com/Reference#l_BluetoothDevice_passkey) is available for when Espruino is connecting _to_ another device (central mode).

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.phy](#t_l_NRF_phy) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L503 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('phy', function(arr) { ... });`

#### Parameters

`arr` - An array containing `[tx_phy, rx_phy, status]` (see below)

#### Description

(2v28+, nRF52840 only) This event is fired when the phy (radio) is changed for the active Bluetooth connection. The parameter is the data `[tx_phy, rx_phy, status]`

`tx_phy`/`rx_phy` are integers where each bit corresponds to:

-   1 : 1mbps phy
-   2 : 2mbps phy
-   4 : coded phy

`status` is an integer containing the status code. 0 = success

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.phy\_req](#t_l_NRF_phy_req) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L522 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('phy_req', function(arr) { ... });`

#### Parameters

`arr` - An array containing `[tx_phy, rx_phy]` (see below)

#### Description

(2v28+, nRF52840 only) This event is fired when the phy (radio) is requested to change for the active Bluetooth connection. The parameter is the data `[tx_phy, rx_phy]`

`tx_phy`/`rx_phy` are integers where each bit corresponds to:

-   1 : 1mbps phy
-   2 : 2mbps phy
-   4 : coded phy

eg. `7` means all phys (eg any) have been requested

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.requestDevice](#t_l_NRF_requestDevice) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3455 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.requestDevice(options)`

#### Parameters

`options` - Options used to filter the device to use

#### Returns

A `[Promise](#Promise)` that is resolved (or rejected) when the connection is complete

#### Description

Search for available devices matching the given filters. Since we have no UI here, Espruino will pick the FIRST device it finds, or it'll call `catch`.

`options` can have the following fields:

-   `filters` - a list of filters that a device must match before it is returned (see below)
-   `timeout` - the maximum time to scan for in milliseconds (scanning stops when a match is found. e.g. `NRF.requestDevice({ timeout:2000, filters: [ ... ] })`
-   `active` - whether to perform active scanning (requesting 'scan response' packets from any devices that are found). e.g.
    
    ```
    NRF.requestDevice({ active:true,
    filters: [ ... ] })
    ```
    
-   `phy` - (NRF52833/NRF52840 only) the type of Bluetooth signals to scan for (can be `"1mbps/coded/both/2mbps"`)
    -   `1mbps` (default) - standard Bluetooth LE advertising
    -   `coded` - long range
    -   `both` - standard and long range
    -   `2mbps` - high speed 2mbps (not working)
-   `extended` - (NRF52833/NRF52840 only) support receiving extended-length advertising packets (default=false, or true if phy isn't `"1mbps"`)
-   `window` - (2v22+) how long we scan for in milliseconds (default 100ms)
-   `interval` - (2v22+) how often we scan in milliseconds (default 100ms) - `window=interval=100`(default) is all the time. When scanning on both `1mbps` and `coded`, `interval` needs to be twice `window`.

**NOTE:** `timeout` and `active` are not part of the Web Bluetooth standard.

The following filter types are implemented:

-   `services` - list of services as strings (all of which must match). 128 bit services must be in the form '01230123-0123-0123-0123-012301230123'
-   `name` - exact device name
-   `namePrefix` - starting characters of device name
-   `id` - exact device address (`id:"e9:53:86:09:89:99 random"`) (this is Espruino-specific, and is not part of the Web Bluetooth spec)
-   `serviceData` - an object containing **lowercase** service characteristics which must all match (`serviceData:{"1809":{}}`). Matching of actual service data is not supported yet.
-   `manufacturerData` - an object containing manufacturer UUIDs which must all match (`manufacturerData:{0x0590:{}}`). Matching of actual manufacturer data is not supported yet.

```

NRF.requestDevice({ filters: [{ namePrefix: 'Puck.js' }] }).then(function(device) { ... });
// or
NRF.requestDevice({ filters: [{ services: ['1823'] }] }).then(function(device) { ... });
// or
NRF.requestDevice({ filters: [{ manufacturerData:{0x0590:{}} }] }).then(function(device) { ... });
```

As a full example, to send data to another Puck.js to turn an LED on:

```

var gatt;
NRF.requestDevice({ filters: [{ namePrefix: 'Puck.js' }] }).then(function(device) {
  return device.gatt.connect();
}).then(function(g) {
  gatt = g;
  return gatt.getPrimaryService("6e400001-b5a3-f393-e0a9-e50e24dcca9e");
}).then(function(service) {
  return service.getCharacteristic("6e400002-b5a3-f393-e0a9-e50e24dcca9e");
}).then(function(characteristic) {
  return characteristic.writeValue("LED1.set()\n");
}).then(function() {
  gatt.disconnect();
  console.log("Done!");
});
```

Or slightly more concisely, using ES6 arrow functions:

```

var gatt;
NRF.requestDevice({ filters: [{ namePrefix: 'Puck.js' }]}).then(
  device => device.gatt.connect()).then(
  g => (gatt=g).getPrimaryService("6e400001-b5a3-f393-e0a9-e50e24dcca9e")).then(
  service => service.getCharacteristic("6e400002-b5a3-f393-e0a9-e50e24dcca9e")).then(
  characteristic => characteristic.writeValue("LED1.reset()\n")).then(
  () => { gatt.disconnect(); console.log("Done!"); } );
```

Note that you have to keep track of the `gatt` variable so that you can disconnect the Bluetooth connection when you're done.

**Note:** Using a filter in `[NRF.requestDevice](#l_NRF_requestDevice)` filters each advertising packet individually. As soon as a matching advertisement is received, `[NRF.requestDevice](#l_NRF_requestDevice)` resolves the promise and stops scanning. This means that if you filter based on a service UUID and a device advertises with multiple packets (or a scan response when `active:true`) only the packet matching the filter is returned - you may not get the device's name is that was in a separate packet. To aggregate multiple packets you can use `[NRF.findDevices](#l_NRF_findDevices)`.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [NRF.resolveAddress](#t_l_NRF_resolveAddress) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L908 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.resolveAddress(options)`

#### Parameters

`options` - The address that should be resolved.

#### Returns

The resolved address, or `undefined` if it couldn't be resolved.

#### Description

Try to resolve a **bonded** peer's address from a random private resolvable address. If the peer is not bonded, there will be no IRK and `undefined` will be returned.

A bunch of devices, especially smartphones, implement address randomisation and periodically change their bluetooth address to prevent being tracked.

If such a device uses a "random private resolvable address", that address is generated with the help of an identity resolving key (IRK) that is exchanged during bonding.

If we know the IRK of a device, we can check if an address was potentially generated by that device.

The following will check an address against the IRKs of all bonded devices, and return the actual address of a bonded device if the given address was likely generated using that device's IRK:

```

NRF.on('connect',addr=> {
  // addr could be "aa:bb:cc:dd:ee:ff private-resolvable"
  if (addr.endsWith("private-resolvable")) {
    let resolved = NRF.resolveAddress(addr);
    // resolved is "aa:bb:cc:dd:ee:ff public"
    if (resolved) addr = resolved;
  }
  console.log("Device connected: ", addr);
})
```

You can get the current connection's address using `NRF.getSecurityStatus().connected_addr`, so can for instance do `NRF.resolveAddress(NRF.getSecurityStatus().connected_addr)`.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.restart](#t_l_NRF_restart) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L777 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.restart(callback)`

#### Parameters

`callback` - \[optional\] A function to be called while the softdevice is uninitialised. Use with caution - accessing console/bluetooth will almost certainly result in a crash.

#### Description

Restart the Bluetooth softdevice (if there is currently a BLE connection, it will queue a restart to be done when the connection closes).

You shouldn't need to call this function in normal usage. However, Nordic's BLE softdevice has some settings that cannot be reset. For example there are only a certain number of unique UUIDs. Once these are all used the only option is to restart the softdevice to clear them all out.

### [event NRF.security](#t_l_NRF_security) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L435 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('security', function(status) { ... });`

#### Parameters

`status` - An object containing `{auth_status,bonded,lv4,kdist_own,kdist_peer}`

#### Description

Contains updates on the security of the current Bluetooth link.

See Nordic's `ble_gap_evt_auth_status_t` structure for more information.

### [NRF.sendHIDReport](#t_l_NRF_sendHIDReport) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L2976 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.sendHIDReport(data, callback)`

#### Parameters

`data` - Input report data as an array

`callback` - A callback function to be called when the data is sent

#### Description

Send a USB HID report. HID must first be enabled with `NRF.setServices({}, {hid: hid_report})`

See https://www.espruino.com/BLE+Keyboard for some libraries that use `[NRF.sendHIDReport](#l_NRF_sendHIDReport)` internally.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [event NRF.servicesDiscover](#t_l_NRF_servicesDiscover) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L487 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.on('servicesDiscover', function() { ... });`

#### Description

Called with discovered services when discovery is finished

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q) and ESP32 boards

### [NRF.setAddress](#t_l_NRF_setAddress) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L866 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setAddress(addr)`

#### Parameters

`addr` - The address to use (as a string)

#### Description

Set this device's default Bluetooth MAC address:

```

NRF.setAddress("ff:ee:dd:cc:bb:aa random");
```

Addresses take the form:

-   `"ff:ee:dd:cc:bb:aa"` or `"ff:ee:dd:cc:bb:aa public"` for a public address
-   `"ff:ee:dd:cc:bb:aa random"` for a random static address (the default for Espruino)

This may throw a `INVALID_BLE_ADDR` error if the upper two bits of the address don't match the address type.

To change the address, Espruino must restart the softdevice. It will only do so when it is disconnected from other devices.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.setAdvertising](#t_l_NRF_setAdvertising) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L1122 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setAdvertising(data, options)`

#### Parameters

`data` - The service data to advertise as an object - see below for more info

`options` - \[optional\] Object of options

#### Description

Change the data that Espruino advertises. By default Espruino advertises:

-   3 bytes of Bluetooth Connection Flags
-   The device name
-   (2v26+) the Espruino Manufacturer ID of 0x0590, but with no data

Data can be of the form `{ UUID : data_as_byte_array }`. The UUID should be a [Bluetooth Service ID](https://developer.bluetooth.org/gatt/services/Pages/ServicesHome.aspx).

For example to return battery level at 95%, do:

```

NRF.setAdvertising({
  0x180F : [95] // Service data 0x180F = 95
});
```

Or you could report the current temperature:

```

setInterval(function() {
  NRF.setAdvertising({
    0x1809 : [Math.round(E.getTemperature())]
  });
}, 30000);
```

If you specify a value for the object key, Service Data is advertised. However if you specify `undefined`, the Service UUID is advertised:

```

NRF.setAdvertising({
  0x180D : undefined // Advertise service UUID 0x180D (HRM)
});
```

Service UUIDs can also be supplied in the second argument of `[NRF.setServices](#l_NRF_setServices)`, but those go in the scan response packet.

You can also supply the raw advertising data in an array. For example to advertise as an Eddystone beacon:

```

NRF.setAdvertising([0x03,  // Length of Service List
  0x03,  // Param: Service List
  0xAA, 0xFE,  // Eddystone ID
  0x13,  // Length of Service Data
  0x16,  // Service Data
  0xAA, 0xFE, // Eddystone ID
  0x10,  // Frame type: URL
  0xF8, // Power
  0x03, // https://
  'g','o','o','.','g','l','/','B','3','J','0','O','c'],
    {interval:100});
```

(However for Eddystone we'd advise that you use the [Espruino Eddystone library](/Puck.js+Eddystone))

**Note:** When specifying data as an array, certain advertising options such as `discoverable` and `showName` won't have any effect.

**Note:** The size of Bluetooth LE advertising packets is limited to 31 bytes. If you want to advertise more data, consider using an array for `data` (See below), or `[NRF.setScanResponse](#l_NRF_setScanResponse)`.

You can even specify an array of arrays or objects, in which case each advertising packet will be used in turn - for instance to make your device advertise battery level and its name as well as both Eddystone and iBeacon :

```

NRF.setAdvertising([
  {0x180F : [E.getBattery()]}, // normal advertising, with battery %
  require("ble_ibeacon").get(...), // iBeacon
  require("ble_eddystone").get(...), // eddystone
], {interval:300});
```

`options` is an object, which can contain:

```

{
  name: "Hello"              // The name of the device
  showName: true/false       // include full name, or nothing
  discoverable: true/false   // general discoverable, or limited - default is limited
  connectable: true/false    // whether device is connectable - default is true
  scannable : true/false     // whether device can be scanned for scan response packets - default is true
  whenConnected : true/false // keep advertising when connected (nRF52 only)
                             // switches to advertising as non-connectable when it is connected
  interval: 600              // Advertising interval in msec, between 20 and 10000 (default is 375ms)
  manufacturer: 0x0590       // This is the manufacturer ID. Set to `0/false` to disable manufacturer data (2v26+ advertises Espruino's 0x0590 by default)
  manufacturerData: [...]    // If sending manufacturer data, this is an array of data to send
  phy: "1mbps/2mbps/coded/coded,1mbps/1mbps,coded"   // ((2v26+, NRF52833/NRF52840 only) use the long-range coded phy for transmission (1mbps default)
  extended : true // (2v26+, NRF52833/NRF52840 only) force use of extended (>31 byte) advertising packets - usually only done if phy isn't set to "1mbps"
}
```

Setting `connectable` and `scannable` to false gives the lowest power consumption as the BLE radio doesn't have to listen after sending advertising.

**NOTE:** Non-`connectable` advertising can't have an advertising interval less than 100ms according to the BLE spec.

So for instance to set the name of Puck.js without advertising any other data you can just use the command:

```

NRF.setAdvertising({},{name:"Hello"});
```

#### Manufacturer Data

You can also specify 'manufacturer data', which is another form of advertising data. We've registered the Manufacturer ID 0x0590 (as Pur3 Ltd) for use with _Official Espruino devices_ - use it to advertise whatever data you'd like, but we'd recommend using JSON.

For example by not advertising a device name you can send up to 24 bytes of JSON on Espruino's manufacturer ID:

```

var data = {a:1,b:2};
NRF.setAdvertising({},{
  showName:false,
  manufacturer:0x0590,
  manufacturerData:JSON.stringify(data)
});
```

If you're using [EspruinoHub](https://github.com/espruino/EspruinoHub) then it will automatically decode this into the following MQTT topics:

-   `/ble/advertise/ma:c_:_a:dd:re:ss/espruino` -> `{"a":10,"b":15}`
-   `/ble/advertise/ma:c_:_a:dd:re:ss/a` -> `1`
-   `/ble/advertise/ma:c_:_a:dd:re:ss/b` -> `2`

Note that **you only have 24 characters available for JSON**, so try to use the shortest field names possible and avoid floating point values that can be very long when converted to a String.

#### Phy

On NRF52833/NRF52840 based devices you can specify `phy` (the physical connection type used) as:

-   `phy:"1mbps""` - the default Bluetooth phy (compatible with everything)
-   `phy:"2mbps"` - a faster Bluetooth connection
-   `phy:"coded"` - a slower connection with error correction (much longer range)
-   `phy:"coded,1mbps"` - both long range and normal, but advertisements sent on the `coded` phy
-   `phy:"1mbps,coded"` - both long range and normal, but advertisements sent on the `1mbps` phy - this allows for long range connections while also being compatible with everything

If you wish to have the best of both world (long range advertising and compatiblity) then Nordic suggest changing advertising between `coded,1mbps` and `1mbps,coded` every 500ms

### [NRF.setConnectionInterval](#t_l_NRF_setConnectionInterval) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3711 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setConnectionInterval(interval)`

#### Parameters

`interval` - The connection interval to use (see below)

#### Description

When connected, Bluetooth LE devices communicate at a set interval. Lowering the interval (e.g. more packets/second) means a lower delay when sending data, higher bandwidth, but also more power consumption.

By default, when connected as a peripheral Espruino automatically adjusts the connection interval. When connected it's as fast as possible (7.5ms) but when idle for over a minute it drops to 200ms. On continued activity (>1 BLE operation) the interval is raised to 7.5ms again.

The options for `interval` are:

-   `undefined` / `"auto"` : (default) automatically adjust connection interval
-   `100` : set min and max connection interval to the same number (between 7.5ms and 4000ms)
-   `{minInterval:20, maxInterval:100}` : set min and max connection interval as a range

This configuration is not remembered during a `save()` - you will have to re-set it via `onInit`.

**Note:** If connecting to another device (as Central), you can use an extra argument to `[NRF.connect](#l_NRF_connect)` or `[BluetoothRemoteGATTServer.connect](#l_BluetoothRemoteGATTServer_connect)` to specify a connection interval.

**Note:** This overwrites any changes imposed by the deprecated `[NRF.setLowPowerConnection](#l_NRF_setLowPowerConnection)`

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.setLowPowerConnection](#t_l_NRF_setLowPowerConnection) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L2560 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setLowPowerConnection(lowPower)`

#### Parameters

`lowPower` - Whether the connection is low power or not

#### Description

**THIS IS DEPRECATED** - please use `[NRF.setConnectionInterval](#l_NRF_setConnectionInterval)` for peripheral and `NRF.connect(address, options)`/`[BluetoothRemoteGATTServer.connect(options)](#l_BluetoothRemoteGATTServer_connect)` for central connections.

This sets the connection parameters - these affect the transfer speed and power usage when the device is connected.

-   When not low power, the connection interval is between 7.5 and 20ms
-   When low power, the connection interval is between 500 and 1000ms

When low power connection is enabled, transfers of data over Bluetooth will be very slow, however power usage while connected will be drastically decreased.

This will only take effect after the connection is disconnected and re-established.

### [NRF.setRSSIHandler](#t_l_NRF_setRSSIHandler) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L2508 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setRSSIHandler(callback)`

#### Parameters

`callback` - The callback to call with the RSSI value, or undefined to stop

#### Description

Start/stop listening for RSSI values on the currently active peripheral connection (eg when this device is being connected to by a 'central' device)

```

// Start scanning
NRF.setRSSIHandler(function(rssi) {
  console.log(rssi); // prints -85 (or similar)
});
// Stop Scanning
NRF.setRSSIHandler();
```

RSSI is the 'Received Signal Strength Indication' in dBm

### [NRF.setScan](#t_l_NRF_setScan) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L2086 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setScan(callback, options)`

#### Parameters

`callback` - The callback to call with received advertising packets, or undefined to stop

`options` - \[optional\] An object `{filters: ...}` (as would be passed to `[NRF.requestDevice](#l_NRF_requestDevice)`) to filter devices by

#### Description

Start/stop listening for BLE advertising packets within range. Returns a `[BluetoothDevice](#BluetoothDevice)` for each advertising packet. **By default this is not an active scan, so Scan Response advertising data is not included (see below)**

```

// Start scanning
packets=10;
NRF.setScan(function(d) {
  packets--;
  if (packets<=0)
    NRF.setScan(); // stop scanning
  else
    console.log(d); // print packet info
});
```

Each `[BluetoothDevice](#BluetoothDevice)` will look a bit like:

```

BluetoothDevice {
  "id": "aa:bb:cc:dd:ee:ff", // address
  "rssi": -89,               // signal strength
  "services": [ "128bit-uuid", ... ],     // zero or more service UUIDs
  "data": new Uint8Array([ ... ]).buffer, // ArrayBuffer of returned data
  "serviceData" : { "0123" : [ 1 ] }, // if service data is in 'data', it's extracted here
  "manufacturer" : 0x1234, // if manufacturer data is in 'data', the 16 bit manufacturer ID is extracted here
  "manufacturerData" : new Uint8Array([...]).buffer, // if manufacturer data is in 'data', the data is extracted here as an ArrayBuffer
  "name": "DeviceName"       // the advertised device name
 }
```

You can also supply a set of filters (as described in `[NRF.requestDevice](#l_NRF_requestDevice)`) as a second argument, which will allow you to filter the devices you get a callback for. This helps to cut down on the time spent processing JavaScript code in areas with a lot of Bluetooth advertisements. For example to find only devices with the manufacturer data `0x0590` (Espruino's ID) you could do:

```

NRF.setScan(function(d) {
  console.log(d.manufacturerData);
}, { filters: [{ manufacturerData:{0x0590:{}} }] });
```

You can also specify `active:true` in the second argument to perform active scanning (this requests scan response packets) from any devices it finds.

**Note:** Using a filter in `setScan` filters each advertising packet individually. As a result, if you filter based on a service UUID and a device advertises with multiple packets (or a scan response when `active:true`) only the packets matching the filter are returned. To aggregate multiple packets you can use `[NRF.findDevices](#l_NRF_findDevices)`.

**Note:** BLE advertising packets can arrive quickly - faster than you'll be able to print them to the console. It's best only to print a few, or to use a function like `[NRF.findDevices(..)](#l_NRF_findDevices)` which will collate a list of available devices.

**Note:** Using setScan turns the radio's receive mode on constantly. This can draw a _lot_ of power (12mA or so), so you should use it sparingly or you can run your battery down quickly.

### [NRF.setScanResponse](#t_l_NRF_setScanResponse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L1475 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setScanResponse(data)`

#### Parameters

`data` - The data to for the scan response

#### Description

The raw scan response data should be supplied as an array. For example to return "Sample" for the device name:

```

NRF.setScanResponse([0x07,  // Length of Data
  0x09,  // Param: Complete Local Name
  'S', 'a', 'm', 'p', 'l', 'e']);
```

Or you can use `[NRF.getAdvertisingData](#l_NRF_getAdvertisingData)` to correctly format the advertising data for you. For example to advertise the HRM service and temperature in the Scan Response you can do:

```

NRF.setScanResponse(NRF.getAdvertisingData({
  0x180D: undefined, // HRM service
  0x1809: [Math.round(E.getTemperature())] // temperature
},{ flags:false, showName:false }))
```

**Note:** The deprecated `NRF.setServices(..., {advertise:[ ... ]})` writes advertised services into the scan response - so you can't use both `[NRF.setScanResponse](#l_NRF_setScanResponse)` and `NRF.setServices(..., {advertise:[...]})` or one will overwrite the other.

### [NRF.setSecurity](#t_l_NRF_setSecurity) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3768 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setSecurity(options)`

#### Parameters

`options` - An object containing security-related options (see below)

#### Description

Sets the security options used when connecting/pairing. This applies to both central _and_ peripheral mode.

```

NRF.setSecurity({
  display : bool  // default false, can this device display a passkey on a screen/etc?
                  // - sent via the `BluetoothDevice.passkey` event
  keyboard : bool // default false, can this device enter a passkey
                  // - request sent via the `BluetoothDevice.passkeyRequest` event
  pair : bool // default true, allow other devices to pair with this device
  bond : bool // default true, Perform bonding
              // This stores info from pairing in flash and allows reconnecting without having to pair each time
  mitm : bool // default false, Man In The Middle protection
  lesc : bool // default false, LE Secure Connections
  passkey : // default "", or a 6 digit passkey to use (display must be true for this)
  oob : [0..15] // if specified, Out Of Band pairing is enabled and
                // the 16 byte pairing code supplied here is used
  encryptUart : bool // default false (unless oob or passkey specified)
                     // This sets the BLE UART service such that it
                     // is encrypted and can only be used from a paired connection
  privacy : // default false, true to enable with (ideally sensible) defaults,
            // or an object defining BLE privacy / random address options - see below for more info
            // only available if Espruino was compiled with private address support (like for example on Bangle.js 2)
});
```

**NOTE:** Some combinations of arguments will cause an error. For example supplying a passkey without `display:1` is not allowed. If `display:1` is set you do not require a physical display, the user just needs to know the passkey you supplied.

For instance, to require pairing and to specify a passkey, use:

```

NRF.setSecurity({passkey:"123456", mitm:1, display:1});
```

Or to require pairing and to display a PIN that the connecting device provides, use:

```

NRF.setSecurity({mitm:1, display:1});
NRF.on("passkey", key => print("Enter PIN: ", key));
```

However, while most devices will request a passkey for pairing at this point it is still possible for a device to connect without requiring one (e.g. using the 'NRF Connect' app).

To force a passkey you need to protect each characteristic you define with `[NRF.setSecurity](#l_NRF_setSecurity)`. For instance the following code will _require_ that the passkey `123456` is entered before the characteristic `9d020002-bf5f-1d1a-b52a-fe52091d5b12` can be read.

```

NRF.setSecurity({passkey:"123456", mitm:1, display:1});
NRF.setServices({
  "9d020001-bf5f-1d1a-b52a-fe52091d5b12" : {
    "9d020002-bf5f-1d1a-b52a-fe52091d5b12" : {
      // readable always
      value : "Not Secret"
    },
    "9d020003-bf5f-1d1a-b52a-fe52091d5b12" : {
      // readable only once bonded
      value : "Secret",
      readable : true,
      security: {
        read: {
          mitm: true,
          encrypted: true
        }
      }
    },
    "9d020004-bf5f-1d1a-b52a-fe52091d5b12" : {
      // readable always
      // writable only once bonded
      value : "Readable",
      readable : true,
      writable : true,
      onWrite : function(evt) {
        console.log("Wrote ", evt.data);
      },
      security: {
        write: {
          mitm: true,
          encrypted: true
        }
      }
    }
  }
});
```

**Note:** If `passkey` or `oob` is specified, the Nordic UART service (if enabled) will automatically be set to require encryption, but otherwise it is open.

On Bangle.js 2, the `privacy` parameter can be used to set this device's BLE privacy / random address settings.

The privacy feature provides a way to avoid being tracked over a period of time. This works by replacing the real BLE address with a random private address, that automatically changes at a specified interval.

If a `"random_private_resolvable"` address is used, that address is generated with the help of an identity resolving key (IRK), that is exchanged during bonding. This allows a bonded device to still identify another device that is using a random private resolvable address.

Note that, while this can help against being tracked, there are other ways a Bluetooth device can reveal its identity. For example, the name or services it advertises may be unique enough.

```

NRF.setSecurity({
  privacy: {
    mode : "off"/"device_privacy"/"network_privacy" // The privacy mode that should be used.
    addr_type : "random_private_resolvable"/"random_private_non_resolvable" // The type of address to use.
    addr_cycle_s : int // How often the address should change, in seconds.
  }
});
// enabled with (ideally sensible) defaults of:
// mode: device_privacy
// addr_type: random_private_resolvable
// addr_cycle_s: 0 (use default address change interval)
NRF.setSecurity({
  privacy: 1
});
```

`mode` can be one of:

-   `"off"` - Use the real address.
-   `"device_privacy"` - Use a private address.
-   `"network_privacy"` - Use a private address, and reject a peer that uses its real address if we know that peer's IRK.

If `mode` is `"off"`, all other fields are ignored and become optional.

`addr_type` can be one of:

-   `"random_private_resolvable"` - Address that can be resolved by a bonded peer that knows our IRK.
-   `"random_private_non_resolvable"` - Address that cannot be resolved.

`addr_cycle_s` must be an integer. Pass `0` to use the default address change interval. The default is usually to change the address every 15 minutes (or 900 seconds).

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.setServices](#t_l_NRF_setServices) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L1529 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setServices(data, options)`

#### Parameters

`data` - The service (and characteristics) to advertise

`options` - \[optional\] Object containing options

#### Description

Change the services and characteristics Espruino advertises.

If you want to **change** the value of a characteristic, you need to use `[NRF.updateServices()](#l_NRF_updateServices)` instead

To expose some information on Characteristic `ABCD` on service `BCDE` you could do:

```

NRF.setServices({
  0xBCDE : {
    0xABCD : {
      value : "Hello",
      readable : true
    }
  }
});
```

Or to allow the 3 LEDs to be controlled by writing numbers 0 to 7 to a characteristic, you can do the following. `evt.data` is an ArrayBuffer.

```

NRF.setServices({
  0xBCDE : {
    0xABCD : {
      writable : true,
      onWrite : function(evt) {
        digitalWrite([LED3,LED2,LED1], evt.data[0]);
      }
    }
  }
});
```

You can supply many different options:

```

NRF.setServices({
  0xBCDE : {
    0xABCD : {
      value : "Hello", // optional
      maxLen : 5, // optional (otherwise is length of initial value)
      broadcast : false, // optional, default is false
      readable : true,   // optional, default is false
      writable : true,   // optional, default is false
      notify : true,   // optional, default is false
      indicate : true,   // optional, default is false
      description: "My Characteristic",  // optional, default is null,
      security: { // optional - see NRF.setSecurity
        read: { // optional
          encrypted: false, // optional, default is false
          mitm: false, // optional, default is false
          lesc: false, // optional, default is false
          signed: false // optional, default is false
        },
        write: { // optional
          encrypted: true, // optional, default is false
          mitm: false, // optional, default is false
          lesc: false, // optional, default is false
          signed: false // optional, default is false
        }
      },
      onWrite : function(evt) { // optional
        console.log("Got ", evt.data); // an ArrayBuffer
      },
      onWriteDesc : function(evt) { // optional - called when the 'cccd' descriptor is written
        // for example this is called when notifications are requested by the client:
        console.log("Notifications enabled = ", evt.data[0]&1);
      }
    }
    // more characteristics allowed
  }
  // more services allowed
});
```

**Note:** UUIDs can be integers between `0` and `0xFFFF`, strings of the form `"ABCD"`, or strings of the form `"ABCDABCD-ABCD-ABCD-ABCD-ABCDABCDABCD"`

`options` can be of the form:

```

NRF.setServices(undefined, {
  hid : new Uint8Array(...), // optional, default is undefined. Enable BLE HID support
  uart : true, // optional, default is true. Enable BLE UART support
  advertise: [ '180D' ] // optional, list of service UUIDs to advertise in the scan response
                        // (deprecated - use `NRF.setScanResponse(NRF.getAdvertisingData({'180D':undefined},{flags:false, showName:false}))`)
  ancs : true, // optional, Bangle.js-only, enable Apple ANCS support for notifications (see `NRF.ancs*`)
  ams : true // optional, Bangle.js-only, enable Apple AMS support for media control (see `NRF.ams*`)
  cts : true // optional, Bangle.js-only, enable Apple Current Time Service support (see `NRF.ctsGetTime`)
});
```

To enable BLE HID, you must set `hid` to an array which is the BLE report descriptor. The easiest way to do this is to use the `ble_hid_controls` or `ble_hid_keyboard` modules.

**Note:** Just creating a service doesn't mean that the service will be advertised. It will only be available after a device connects. To advertise, specify the UUIDs you wish to advertise in the `advertise` field of the second `options` argument. For example this will create and advertise a heart rate service:

```

NRF.setServices({
  0x180D: { // heart_rate
    0x2A37: { // heart_rate_measurement
      notify: true,
      value : [0x06, heartrate],
    }
  }
}, { advertise: [ '180D' ] });
```

You may specify 128 bit UUIDs to advertise, however you may get a `DATA_SIZE` exception because there is insufficient space in the Bluetooth LE advertising packet for the 128 bit UART UUID as well as the UUID you specified. In this case you can add `uart:false` after the `advertise` element to disable the UART, however you then be unable to connect to Puck.js's console via Bluetooth.

If you absolutely require two or more 128 bit UUIDs then you will have to specify your own raw advertising data packets with `[NRF.setAdvertising](#l_NRF_setAdvertising)`

**Note:_\* The services on Espruino can only be modified when there is no device connected to it as it requires a restart of the Bluetooth stack. \*_iOS devices will 'cache' the list of services** so apps like NRF Connect may incorrectly display the old services even after you have modified them. To fix this, disable and re-enable Bluetooth on your iOS device, or use an Android device to run NRF Connect.

**Note:** Not all combinations of security configuration values are valid, the valid combinations are: encrypted, encrypted + mitm, lesc, signed, signed + mitm. See `[NRF.setSecurity](#l_NRF_setSecurity)` for more information.

### [NRF.setTxPower](#t_l_NRF_setTxPower) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L2544 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setTxPower(power)`

#### Parameters

`power` - Transmit power. Accepted values are -40(nRF52 only), -30(nRF51 only), -20, -16, -12, -8, -4, 0, and 4 dBm. On nRF52840 (eg Bangle.js 2) 5/6/7/8 dBm are available too. Others will give an error code.

#### Description

Set the BLE radio transmit power. The default TX power is 0 dBm (or 4dBm for Bangle.js 2).

### [NRF.setWhitelist](#t_l_NRF_setWhitelist) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3687 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.setWhitelist(whitelisting)`

#### Parameters

`whitelisting` - Are we using a whitelist? (default false)

#### Description

If set to true, whenever a device bonds it will be added to the whitelist.

When set to false, the whitelist is cleared and newly bonded devices will not be added to the whitelist.

**Note:** This is remembered between `[reset()](#l__global_reset)`s but isn't remembered after power-on (you'll have to add it to `onInit()`.

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.sleep](#t_l_NRF_sleep) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L737 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.sleep()`

#### Description

Disable Bluetooth advertising and disconnect from any device that connected to Puck.js as a peripheral (this won't affect any devices that Puck.js initiated connections to).

This makes Puck.js undiscoverable, so it can't be connected to.

Use `[NRF.wake()](#l_NRF_wake)` to wake up and make Puck.js connectable again.

### [NRF.startBonding](#t_l_NRF_startBonding) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L3993 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.startBonding(forceRepair)`

#### Parameters

`forceRepair` - True if we should force repairing even if there is already valid pairing info

#### Returns

A promise

#### Description

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.updateConnection](#t_l_NRF_updateConnection) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L4224 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.updateConnection(options)`

#### Parameters

`options` - An object containing connection options

#### Description

(2v28+) Update connection parameters on the current peripheral connection. Options can be:

```

{
  phy : string // "1mpbs"/"2mpbs"/"coded"/"auto"
}
```

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

**Note:** This is only available in NRF52 devices (like Puck.js, Pixl.js, Jolt.js, Bangle.js and MDBT42Q)

### [NRF.updateServices](#t_l_NRF_updateServices) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L1780 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.updateServices(data)`

#### Parameters

`data` - The service (and characteristics) to update

#### Description

Update values for the services and characteristics Espruino advertises. Only services and characteristics previously declared using `[NRF.setServices](#l_NRF_setServices)` are affected.

To update the '0xABCD' characteristic in the '0xBCDE' service:

```

NRF.updateServices({
  0xBCDE : {
    0xABCD : {
      value : "World"
    }
  }
});
```

You can also use 128 bit UUIDs, for example `"b7920001-3c1b-4b40-869f-3c0db9be80c6"`.

To define a service and characteristic and then notify connected clients of a change to it when a button is pressed:

```

NRF.setServices({
  0xBCDE : {
    0xABCD : {
      value : "Hello",
      maxLen : 20,
      notify: true
    }
  }
});
setWatch(function() {
  NRF.updateServices({
    0xBCDE : {
      0xABCD : {
        value : "World!",
        notify: true
      }
    }
  });
}, BTN, { repeat:true, edge:"rising", debounce: 50 });
```

This only works if the characteristic was created with `notify: true` using `[NRF.setServices](#l_NRF_setServices)`, otherwise the characteristic will be updated but no notification will be sent.

Also note that `maxLen` was specified. If it wasn't then the maximum length of the characteristic would have been 5 - the length of `"Hello"`.

To indicate (i.e. notify with ACK) connected clients of a change to the '0xABCD' characteristic in the '0xBCDE' service:

```

NRF.updateServices({
  0xBCDE : {
    0xABCD : {
      value : "World",
      indicate: true
    }
  }
});
```

This only works if the characteristic was created with `indicate: true` using `[NRF.setServices](#l_NRF_setServices)`, otherwise the characteristic will be updated but no notification will be sent.

**Note:** See `[NRF.setServices](#l_NRF_setServices)` for more information

### [NRF.wake](#t_l_NRF_wake) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/bluetooth/jswrap_bluetooth.c#L761 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`NRF.wake()`

#### Description

Enable Bluetooth advertising (this is enabled by default), which allows other devices to discover and connect to Puck.js.

Use `[NRF.sleep()](#l_NRF_sleep)` to disable advertising.

## [Number Class](#t_Number)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for numbers.

#### Methods and Fields

-   [Number.MAX\_VALUE](#l_Number_MAX_VALUE)
-   [Number.MIN\_VALUE](#l_Number_MIN_VALUE)
-   [Number.NaN](#l_Number_NaN)
-   [Number.NEGATIVE\_INFINITY](#l_Number_NEGATIVE_INFINITY)
-   [constructor Number(value, ...)](#l_Number_Number)
-   [Number.POSITIVE\_INFINITY](#l_Number_POSITIVE_INFINITY)
-   [function Number.toFixed(decimalPlaces)](#l_Number_toFixed)

### [Number.MAX\_VALUE](#t_l_Number_MAX_VALUE) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L92 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_VALUE)

[(top)](javascript:toppos\(\);)

#### Call type:

`Number.MAX_VALUE`

#### Returns

Maximum representable value

#### Description

### [Number.MIN\_VALUE](#t_l_Number_MIN_VALUE) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L100 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_VALUE)

[(top)](javascript:toppos\(\);)

#### Call type:

`Number.MIN_VALUE`

#### Returns

Smallest representable value

#### Description

### [Number.NaN](#t_l_Number_NaN) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L84 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NaN)

[(top)](javascript:toppos\(\);)

#### Call type:

`Number.NaN`

#### Returns

Not a Number

#### Description

### [Number.NEGATIVE\_INFINITY](#t_l_Number_NEGATIVE_INFINITY) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L108 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/NEGATIVE_INFINITY)

[(top)](javascript:toppos\(\);)

#### Call type:

`Number.NEGATIVE_INFINITY`

#### Returns

Negative Infinity (-1/0)

#### Description

### [constructor Number](#t_l_Number_Number) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L26 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Number(value, ...)`

#### Parameters

`value, ...` - A single value to be converted to a number

#### Returns

A Number object

#### Description

Creates a number

### [Number.POSITIVE\_INFINITY](#t_l_Number_POSITIVE_INFINITY) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L116 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/POSITIVE_INFINITY)

[(top)](javascript:toppos\(\);)

#### Call type:

`Number.POSITIVE_INFINITY`

#### Returns

Positive Infinity (1/0)

#### Description

### [function Number.toFixed](#t_l_Number_toFixed) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_number.c#L124 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Number.toFixed(decimalPlaces)`

#### Parameters

`decimalPlaces` - A number between 0 and 20 specifying the number of decimal digits after the decimal point

#### Returns

A string

#### Description

Format the number as a fixed point number

## [Object Class](#t_Object)

[(top)](javascript:toppos\(\);)

This is the built-in class for Objects

#### Methods and Fields

-   [function Object.addListener(event, listener)](#l_Object_addListener)
-   [Object.assign(args, ...)](#l_Object_assign)
-   [function Object.clone()](#l_Object_clone)
-   [Object.create(proto, propertiesObject)](#l_Object_create)
-   [Object.defineProperties(obj, props)](#l_Object_defineProperties)
-   [Object.defineProperty(obj, name, desc)](#l_Object_defineProperty)
-   [function Object.emit(event, args, ...)](#l_Object_emit)
-   [Object.entries(object)](#l_Object_entries)
-   [Object.fromEntries(entries)](#l_Object_fromEntries)
-   [Object.getOwnPropertyDescriptor(obj, name)](#l_Object_getOwnPropertyDescriptor)
-   [Object.getOwnPropertyDescriptors(obj)](#l_Object_getOwnPropertyDescriptors)
-   [Object.getOwnPropertyNames(object)](#l_Object_getOwnPropertyNames)
-   [Object.getPrototypeOf(object)](#l_Object_getPrototypeOf)
-   [function Object.hasOwnProperty(name)](#l_Object_hasOwnProperty)
-   [Object.keys(object)](#l_Object_keys)
-   [property Object.length](#l_Object_length)
-   [constructor Object(value)](#l_Object_Object)
-   [function Object.on(event, listener)](#l_Object_on)
-   [function Object.prependListener(event, listener)](#l_Object_prependListener)
-   [function Object.removeAllListeners(event)](#l_Object_removeAllListeners)
-   [function Object.removeListener(event, listener)](#l_Object_removeListener)
-   [Object.setPrototypeOf(object, prototype)](#l_Object_setPrototypeOf)
-   [function Object.toString(radix)](#l_Object_toString)
-   [function Object.valueOf()](#l_Object_valueOf)
-   [Object.values(object)](#l_Object_values)

### [function Object.addListener](#t_l_Object_addListener) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L857 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.addListener(event, listener)`

#### Parameters

`event` - The name of the event, for instance 'data'

`listener` - The listener to call when this event is received

#### Description

Register an event listener for this object, for instance `Serial1.addListener('data', function(d) {...})`.

An alias for `[Object.on](#l_Object_on)`

**Note:** This is not available in Embeddable Espruino C builds

### [Object.assign](#t_l_Object_assign) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L729 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.assign(args, ...)`

#### Parameters

`args, ...` - The target object, then any items objects to use as sources of keys

#### Returns

The target object

#### Description

Appends all keys and values in any subsequent objects to the first object

**Note:** Unlike the standard ES6 `[Object.assign](#l_Object_assign)`, this will throw an exception if given raw strings, bools or numbers rather than objects.

### [function Object.clone](#t_l_Object_clone) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L137 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.clone()`

#### Returns

A copy of this Object

#### Description

Copy this object to a new object, but as a shallow copy. This has a similar effect to calling `Object.assign({}, obj)`.

```

orig = { a : 1, b : [ 2, 3 ] }
copy = orig.clone();
// copy = { a : 1, b : [ 2, 3 ] }
```

**Note:** This is not a standard JavaScript function, but is unique to Espruino

### [Object.create](#t_l_Object_create) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L406 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.create(proto, propertiesObject)`

#### Parameters

`proto` - A prototype object

`propertiesObject` - An object containing properties. NOT IMPLEMENTED

#### Returns

A new object

#### Description

Creates a new object with the specified prototype object and properties. properties are currently unsupported.

### [Object.defineProperties](#t_l_Object_defineProperties) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L650 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperties)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.defineProperties(obj, props)`

#### Parameters

`obj` - An object

`props` - An object whose fields represent property names, and whose values are property descriptors.

#### Returns

The object, obj.

#### Description

Adds new properties to the Object. See `[Object.defineProperty](#l_Object_defineProperty)` for more information

### [Object.defineProperty](#t_l_Object_defineProperty) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L580 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.defineProperty(obj, name, desc)`

#### Parameters

`obj` - An object

`name` - The name of the property

`desc` - The property descriptor

#### Returns

The object, obj.

#### Description

Add a new property to the Object. 'Desc' is an object with the following fields:

-   `configurable` (bool = false) - can this property be changed/deleted (not implemented)
-   `enumerable` (bool = false) - can this property be enumerated (not implemented)
-   `value` (anything) - the value of this property
-   `writable` (bool = false) - can the value be changed with the assignment operator?
-   `get` (function) - the getter function, or undefined if no getter (only supported on some platforms)
-   `set` (function) - the setter function, or undefined if no setter (only supported on some platforms)

**Note:** `configurable`, `enumerable` and `writable` are not implemented and will be ignored.

### [function Object.emit](#t_l_Object_emit) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L945 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.emit(event, args, ...)`

#### Parameters

`event` - The name of the event, for instance 'data'

`args, ...` - Optional arguments

#### Description

Call any event listeners that were added to this object with `[Object.on](#l_Object_on)`, for instance `obj.emit('data', 'Foo')`.

For more information see `[Object.on](#l_Object_on)`

**Note:** This is not available in Embeddable Espruino C builds

### [Object.entries](#t_l_Object_entries) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L329 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.entries(object)`

#### Parameters

`object` - The object to return values for

#### Returns

An array of `[key,value]` pairs - one for each key on the given object

#### Description

Return all enumerable keys and values of the given object

**Note:** This is not available in devices with low flash memory

### [Object.fromEntries](#t_l_Object_fromEntries) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L372 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.fromEntries(entries)`

#### Parameters

`entries` - An array of `[key,value]` pairs to be used to create an object

#### Returns

An object containing all the specified pairs

#### Description

Transforms an array of key-value pairs into an object

**Note:** This is not available in devices with low flash memory

### [Object.getOwnPropertyDescriptor](#t_l_Object_getOwnPropertyDescriptor) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L436 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.getOwnPropertyDescriptor(obj, name)`

#### Parameters

`obj` - The object

`name` - The name of the property

#### Returns

An object with a description of the property. The values of writable/enumerable/configurable may not be entirely correct due to Espruino's implementation.

#### Description

Get information on the given property in the object, or undefined

### [Object.getOwnPropertyDescriptors](#t_l_Object_getOwnPropertyDescriptors) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L490 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptors)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.getOwnPropertyDescriptors(obj)`

#### Parameters

`obj` - The object

#### Returns

An object containing all the property descriptors of an object

#### Description

Get information on all properties in the object (from `[Object.getOwnPropertyDescriptor](#l_Object_getOwnPropertyDescriptor)`), or just `{}` if no properties

**Note:** This is not available in devices with low flash memory

### [Object.getOwnPropertyNames](#t_l_Object_getOwnPropertyNames) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L172 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.getOwnPropertyNames(object)`

#### Parameters

`object` - The Object to return a list of property names for

#### Returns

An array of the Object's own properties

#### Description

Returns an array of all properties (enumerable or not) found directly on a given object.

### [Object.getPrototypeOf](#t_l_Object_getPrototypeOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L687 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getPrototypeOf)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.getPrototypeOf(object)`

#### Parameters

`object` - An object

#### Returns

The prototype

#### Description

Get the prototype of the given object - this is like writing `object.__proto__` but is the 'proper' ES6 way of doing it

### [function Object.hasOwnProperty](#t_l_Object_hasOwnProperty) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L534 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.hasOwnProperty(name)`

#### Parameters

`name` - The name of the property to search for

#### Returns

True if it exists, false if it doesn't

#### Description

Return true if the object (not its prototype) has the given property.

NOTE: This currently returns false-positives for built-in functions in prototypes

### [Object.keys](#t_l_Object_keys) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L159 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.keys(object)`

#### Parameters

`object` - The object to return keys for

#### Returns

An array of strings - one for each key on the given object

#### Description

Return all enumerable keys of the given object

### [property Object.length](#t_l_Object_length) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L66 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`property Object.length`

#### Returns

The length of the object

#### Description

Find the length of the object

### [constructor Object](#t_l_Object_Object) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L42 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Object(value)`

#### Parameters

`value` - A single value to be converted to an object

#### Returns

An Object

#### Description

Creates an Object from the supplied argument

### [function Object.on](#t_l_Object_on) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L806 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.on(event, listener)`

#### Parameters

`event` - The name of the event, for instance 'data'

`listener` - The listener to call when this event is received

#### Description

Register an event listener for this object, for instance

```
Serial1.on('data',
function(d) {...})
```

.

This is the same as Node.js's [EventEmitter](https://nodejs.org/api/events.html) but on Espruino the functionality is built into every object:

-   `[Object.on](#l_Object_on)`
-   `[Object.emit](#l_Object_emit)`
-   `[Object.removeListener](#l_Object_removeListener)`
-   `[Object.removeAllListeners](#l_Object_removeAllListeners)`

```

var o = {}; // o can be any object...
// call an arrow function when the 'answer' event is received
o.on('answer', x => console.log(x));
// call a named function when the 'answer' event is received
function printAnswer(d) {
  console.log("The answer is", d);
}
o.on('answer', printAnswer);
// emit the 'answer' event - functions added with 'on' will be executed
o.emit('answer', 42);
// prints: 42
// prints: The answer is 42
// If you have a named function, it can be removed by name
o.removeListener('answer', printAnswer);
// Now 'printAnswer' is removed
o.emit('answer', 43);
// prints: 43
// Or you can remove all listeners for 'answer'
o.removeAllListeners('answer')
// Now nothing happens
o.emit('answer', 44);
// nothing printed
```

If you have more than one handler for an event, and you'd like that handler to stop the event being passed to other handlers then you can call `[E.stopEventPropagation()](#l_E_stopEventPropagation)` in that handler.

**Note:** This is not available in Embeddable Espruino C builds

### [function Object.prependListener](#t_l_Object_prependListener) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L923 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.prependListener(event, listener)`

#### Parameters

`event` - The name of the event, for instance 'data'

`listener` - The listener to call when this event is received

#### Description

Register an event listener for this object, for instance `Serial1.addListener('data', function(d) {...})`.

An alias for `[Object.on](#l_Object_on)`

**Note:** This is not available in Embeddable Espruino C builds

### [function Object.removeAllListeners](#t_l_Object_removeAllListeners) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L1051 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.removeAllListeners(event)`

#### Parameters

`event` - \[optional\] The name of the event, for instance `'data'`. If not specified _all_ listeners are removed.

#### Description

Removes all listeners (if `event===undefined`), or those of the specified event.

```

Serial1.on("data", function(data) { ... });
Serial1.removeAllListeners("data");
// or
Serial1.removeAllListeners(); // removes all listeners for all event types
```

For more information see `[Object.on](#l_Object_on)`

### [function Object.removeListener](#t_l_Object_removeListener) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L1001 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.removeListener(event, listener)`

#### Parameters

`event` - The name of the event, for instance 'data'

`listener` - The listener to remove

#### Description

Removes the specified event listener.

```

function foo(d) {
  console.log(d);
}
Serial1.on("data", foo);
Serial1.removeListener("data", foo);
```

For more information see `[Object.on](#l_Object_on)`

### [Object.setPrototypeOf](#t_l_Object_setPrototypeOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L704 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/setPrototypeOf)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.setPrototypeOf(object, prototype)`

#### Parameters

`object` - An object

`prototype` - The prototype to set on the object

#### Returns

The object passed in

#### Description

Set the prototype of the given object - this is like writing

```
object.__proto__ =
prototype
```

but is the 'proper' ES6 way of doing it

### [function Object.toString](#t_l_Object_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L109 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.toString(radix)`

#### Parameters

`radix` - \[optional\] If the object is an integer, the radix (between 2 and 36) to use. NOTE: Setting a radix does not work on floating point numbers.

#### Returns

A String representing the object

#### Description

Convert the Object to a string

### [function Object.valueOf](#t_l_Object_valueOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L92 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/valueOf)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Object.valueOf()`

#### Returns

The primitive value of this object

#### Description

Returns the primitive value of this object.

### [Object.values](#t_l_Object_values) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_object.c#L315 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values)

[(top)](javascript:toppos\(\);)

#### Call type:

`Object.values(object)`

#### Parameters

`object` - The object to return values for

#### Returns

An array of values - one for each key on the given object

#### Description

Return all enumerable values of the given object

**Note:** This is not available in devices with low flash memory

## [OneWire Class](#t_OneWire)

[(top)](javascript:toppos\(\);)

This class provides a software-defined OneWire master. It is designed to be similar to Arduino's OneWire library.

**Note:** OneWire commands are very timing-sensitive, and on nRF52 devices (Bluetooth LE Espruino boards) the bluetooth stack can get in the way. Before version 2v18 of Espruino OneWire could be unreliable, but as of firmware 2v18 Espruino now schedules OneWire accesses with the bluetooth stack to ensure it doesn't interfere. OneWire is now reliable but some functions such as `[OneWire.search](#l_OneWire_search)` can now take a while to execute (around 1 second).

#### Methods and Fields

-   [constructor OneWire(pin)](#l_OneWire_OneWire)
-   [function OneWire.read(count)](#l_OneWire_read)
-   [function OneWire.reset()](#l_OneWire_reset)
-   [function OneWire.search(command)](#l_OneWire_search)
-   [function OneWire.select(rom)](#l_OneWire_select)
-   [function OneWire.skip()](#l_OneWire_skip)
-   [function OneWire.write(data, power)](#l_OneWire_write)

### [constructor OneWire](#t_l_OneWire_OneWire) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_onewire.c#L188 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`new OneWire(pin)`

#### Parameters

`pin` - The pin to implement OneWire on

#### Returns

A OneWire object

#### Description

Create a software OneWire implementation on the given pin

### [function OneWire.read](#t_l_OneWire_read) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_onewire.c#L314 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function OneWire.read(count)`

#### Parameters

`count` - \[optional\] The amount of bytes to read

#### Returns

The byte that was read, or a `[Uint8Array](#Uint8Array)` if count was specified and >=0

#### Description

Read a byte

### [function OneWire.reset](#t_l_OneWire_reset) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_onewire.c#L208 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function OneWire.reset()`

#### Returns

True is a device was present (it held the bus low)

#### Description

Perform a reset cycle

### [function OneWire.search](#t_l_OneWire_search) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_onewire.c#L345 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function OneWire.search(command)`

#### Parameters

`command` - (Optional) command byte. If not specified (or zero), this defaults to 0xF0. This can could be set to 0xEC to perform a DS18B20 'Alarm Search Command'

#### Returns

An array of devices that were found

#### Description

Search for devices

### [function OneWire.select](#t_l_OneWire_select) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_onewire.c#L223 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function OneWire.select(rom)`

#### Parameters

`rom` - The device to select (get this using `[OneWire.search()](#l_OneWire_search)`)

#### Description

Select a ROM - always performs a reset first

### [function OneWire.skip](#t_l_OneWire_skip) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_onewire.c#L265 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function OneWire.skip()`

#### Description

Skip a ROM

### [function OneWire.write](#t_l_OneWire_write) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_onewire.c#L279 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function OneWire.write(data, power)`

#### Parameters

`data` - A byte (or array of bytes) to write

`power` - Whether to leave power on after write (default is false)

#### Description

Write one or more bytes

## [Pin Class](#t_Pin)

[(top)](javascript:toppos\(\);)

This is the built-in class for Pins, such as D0,D1,LED1, or BTN

You can call the methods on Pin, or you can use Wiring-style functions such as digitalWrite

#### Methods and Fields

-   [function Pin.analog()](#l_Pin_analog)
-   [function Pin.getInfo()](#l_Pin_getInfo)
-   [function Pin.getMode()](#l_Pin_getMode)
-   [function Pin.mode(mode)](#l_Pin_mode)
-   [Pin.Pin()](#l_Pin_Pin)
-   [constructor Pin(value)](#l_Pin_Pin)
-   [function Pin.pulse(value, time)](#l_Pin_pulse)
-   [function Pin.pwm(value, options)](#l_Pin_pwm)
-   [function Pin.read()](#l_Pin_read)
-   [function Pin.reset()](#l_Pin_reset)
-   [function Pin.set()](#l_Pin_set)
-   [function Pin.toggle()](#l_Pin_toggle)
-   [function Pin.write(value)](#l_Pin_write)

### [function Pin.analog](#t_l_Pin_analog) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L208 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.analog()`

#### Returns

The analog value of the `[Pin](#Pin)` between 0(GND) and 1(VCC)

#### Description

(Added in 2v20) Get the analogue value of the given pin. See `[analogRead](#l__global_analogRead)` for more information.

### [function Pin.getInfo](#t_l_Pin_getInfo) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L248 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.getInfo()`

#### Returns

An object containing information about this pins

#### Description

Get information about this pin and its capabilities. Of the form:

```

{
  "port"        : "A",    // the Pin's port on the chip
  "num"         : 12,     // the Pin's number
  "negated"     : (2v29+) // true if the pin is negated in firmware, field missing if not
  "mode"        : (2v25+) // string: the pin's mode (same as Pin.getMode())
  "output"      : (2v25+) // 0/1: the state of the pin's output register
  "in_addr"     : 0x..., // (if available) the address of the pin's input address in bit-banded memory (can be used with peek)
  "out_addr"    : 0x..., // (if available) the address of the pin's output address in bit-banded memory (can be used with poke)
  "analog"      : { ADCs : [1], channel : 12 }, // If analog input is available
  "functions"   : {
    "TIM1":{type:"CH1, af:0},
    "I2C3":{type:"SCL", af:1}
  }
}
```

Will return undefined if pin is not valid.

**Note:** This is not available in devices with low flash memory

### [function Pin.getMode](#t_l_Pin_getMode) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L134 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.getMode()`

#### Returns

The pin mode, as a string

#### Description

Return the current mode of the given pin. See `[pinMode](#l__global_pinMode)` for more information.

### [function Pin.mode](#t_l_Pin_mode) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L147 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.mode(mode)`

#### Parameters

`mode` - The mode - a string that is either 'analog', 'input', 'input_pullup', 'input_pulldown', 'output', 'opendrain', 'af_output' or 'af_opendrain'. Do not include this argument if you want to revert to automatic pin mode setting.

#### Description

Set the mode of the given pin. See [](#l__global_pinMode)`[pinMode](#l__global_pinMode)` for more information on pin modes.

### [Pin.Pin](#t_l_Pin_Pin) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L25 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Pin.Pin()`

#### Description

This is the built-in class for Pins, such as D0,D1,LED1, or BTN

You can call the methods on Pin, or you can use Wiring-style functions such as digitalWrite

### [constructor Pin](#t_l_Pin_Pin) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L38 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`new Pin(value)`

#### Parameters

`value` - A value to be converted to a pin. Can be a number, pin, or String.

#### Returns

A Pin object

#### Description

Creates a pin from the given argument (or returns undefined if no argument)

### [function Pin.pulse](#t_l_Pin_pulse) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L185 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.pulse(value, time)`

#### Parameters

`value` - Whether to pulse high (true) or low (false)

`time` - A time in milliseconds, or an array of times (in which case a square wave will be output starting with a pulse of 'value')

#### Description

(Added in 2v20) Pulse the pin with the value for the given time in milliseconds.

```

LED.pulse(1, 100); // pulse LED on for 100ms
LED.pulse(1, [100,1000,100]); // pulse LED on for 100ms, off for 1s, on for 100ms
```

This is identical to `[digitalPulse](#l__global_digitalPulse)`.

### [function Pin.pwm](#t_l_Pin_pwm) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L221 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.pwm(value, options)`

#### Parameters

`value` - A value between 0 and 1

`options` - An object containing options for analog output - see below

#### Description

(Added in 2v20) Set the analog Value of a pin. It will be output using PWM.

See `[analogWrite](#l__global_analogWrite)` for more information.

Objects can contain:

-   `freq` - pulse frequency in Hz, e.g. `analogWrite(A0,0.5,{ freq : 10 });` - specifying a frequency will force PWM output, even if the pin has a DAC
-   `soft` - boolean, If true software PWM is used if hardware is not available.
-   `forceSoft` - boolean, If true software PWM is used even if hardware PWM or a DAC is available

### [function Pin.read](#t_l_Pin_read) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L61 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.read()`

#### Returns

Whether pin is a logical 1 or 0

#### Description

Returns the input state of the pin as a boolean.

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset the pin's state to `"input"`

### [function Pin.reset](#t_l_Pin_reset) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L96 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.reset()`

#### Description

Sets the output state of the pin to a 0

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset the pin's state to `"output"`

### [function Pin.set](#t_l_Pin_set) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L79 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.set()`

#### Description

Sets the output state of the pin to a 1

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset the pin's state to `"output"`

### [function Pin.toggle](#t_l_Pin_toggle) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L163 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.toggle()`

#### Returns

True if the pin is high after calling the function

#### Description

Toggles the state of the pin from off to on, or from on to off.

**Note:** This method doesn't currently work on the ESP8266 port of Espruino.

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset the pin's state to `"output"`

### [function Pin.write](#t_l_Pin_write) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_pin.c#L112 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Pin.write(value)`

#### Parameters

`value` - Whether to set output high (true/1) or low (false/0)

#### Description

Sets the output state of the pin to the parameter given

**Note:** if you didn't call `[pinMode](#l__global_pinMode)` beforehand then this function will also reset the pin's state to `"output"`

## [process Class](#t_process)

[(top)](javascript:toppos\(\);)

This class contains information about Espruino itself

#### Methods and Fields

-   [process.env](#l_process_env)
-   [process.memory(gc)](#l_process_memory)
-   [event process.uncaughtException(exception)](#l_process_uncaughtException)
-   [process.version](#l_process_version)

### [process.env](#t_l_process_env) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_process.c#L98 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`process.env`

#### Returns

An object

#### Description

Returns an Object containing various pre-defined variables.

-   `VERSION` - is the Espruino version
-   `GIT_COMMIT` - is Git commit hash this firmware was built from
-   `BOARD` - the board's ID (e.g. `PUCKJS`)
-   `RAM` - total amount of on-chip RAM in bytes
-   `FLASH` - total amount of on-chip flash memory in bytes
-   `SPIFLASH` - (on Bangle.js) total amount of off-chip flash memory in bytes
-   `HWVERSION` - For Puck.js this is the board revision (1, 2, 2.1), or for Bangle.js it's 1 or 2
-   `STORAGE` - memory in bytes dedicated to the `[Storage](#Storage)` module
-   `SERIAL` - the serial number of this chip
-   `CONSOLE` - the name of the current console device being used (`[Serial1](#l__global_Serial1)`, `USB`, `[Bluetooth](#l__global_Bluetooth)`, etc)
-   `MODULES` - a list of built-in modules separated by commas
-   `EXPTR` - The address of the `exportPtrs` structure in flash (this includes links to built-in functions that compiled JS code needs)
-   `APP_RAM_BASE` - On nRF5x boards, this is the RAM required by the Softdevice _if it doesn't exactly match what was allocated_. You can use this to update `LD_APP_RAM_BASE` in the `BOARD.py` file
-   `SOFTDEVICE` - (on nRF5x) the hex version code of the Bluetooth Softdevice that is installed on the device (see below)

To get a list of built-in modules, you can use `process.env.MODULES.split(',')`

The `process.env.SOFTDEVICE` code is likely one of:

Code

Chip

Softdevice

0x0091 / 145

nRF52832

S132 v3.1.0 (SDK12)

0x00A9 / 169

nRF52840

S140 v6.0.0 (SDK15.3)

0x00B6 / 182

nRF52840

S140 v6.1.1 (SDK15)

**Note:** `[process.env](#l_process_env)` is not writeable - so as not to waste RAM, the contents are generated on demand. If you need to be able to change them, use `process.env=process.env;` first to ensure the values stay allocated.

### [process.memory](#t_l_process_memory) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_process.c#L178 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`process.memory(gc)`

#### Parameters

`gc` - \[optional\] A boolean. If `undefined` or `true` Garbage collection is performed, if `false` it is not

#### Returns

Information about memory usage

#### Description

Run a Garbage Collection pass, and return an object containing information on memory usage.

-   `free` : Memory that is available to be used (in blocks)
-   `usage` : Memory that has been used (in blocks)
-   `total` : Total memory (in blocks)
-   `history` : Memory used for command history - that is freed if memory is low. Note that this is INCLUDED in the figure for 'free'
-   `gc` : Memory freed during the GC pass
-   `gctime` : Time taken for GC pass (in milliseconds)
-   `blocksize` : Size of a block (variable) in bytes
-   `stackEndAddress` : (on ARM) the address (that can be used with peek/poke/etc) of the END of the stack. The stack grows down, so unless you do a lot of recursion the bytes above this can be used.
-   `stackFree` : (on ARM) how many bytes of free execution stack are there at the point of execution.
-   `flash_start` : (on ARM) the address of the start of flash memory (usually `0x8000000`)
-   `flash_binary_end` : (on ARM) the address in flash memory of the end of Espruino's firmware.
-   `flash_code_start` : (on ARM) the address in flash memory of pages that store any code that you save with `save()`.
-   `flash_length` : (on ARM) the amount of flash memory this firmware was built for (in bytes). **Note:** Some STM32 chips actually have more memory than is advertised.

Memory units are specified in 'blocks', which are around 16 bytes each (depending on your device). The actual size is available in `blocksize`. See http://www.espruino.com/Performance for more information.

**Note:** To find free areas of flash memory, see `require('Flash').getFree()`

### [event process.uncaughtException](#t_l_process_uncaughtException) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_process.c#L34 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`process.on('uncaughtException', function(exception) { ... });`

#### Parameters

`exception` - The uncaught exception

#### Description

This event is called when an exception gets thrown and isn't caught (e.g. it gets all the way back to the event loop).

You can use this for logging potential problems that might occur during execution when you might not be able to see what is written to the console, for example:

```

var lastError;
process.on('uncaughtException', function(e) {
  lastError=e;
  print(e,e.stack?"\n"+e.stack:"")
});
function checkError() {
  if (!lastError) return print("No Error");
  print(lastError,lastError.stack?"\n"+lastError.stack:"")
}
```

**Note:** When this is used, exceptions will cease to be reported on the console - which may make debugging difficult!

### [process.version](#t_l_process_version) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_process.c#L63 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`process.version`

#### Returns

The version of Espruino

#### Description

Returns the version of Espruino as a String

## [Promise Class](#t_Promise)

[(top)](javascript:toppos\(\);)

This is the built-in class for ES6 Promises

#### Methods and Fields

-   [Promise.all(promises)](#l_Promise_all)
-   [function Promise.catch(onRejected)](#l_Promise_catch)
-   [constructor Promise(executor)](#l_Promise_Promise)
-   [Promise.reject(promises)](#l_Promise_reject)
-   [Promise.resolve(promises)](#l_Promise_resolve)
-   [function Promise.then(onFulfilled, onRejected)](#l_Promise_then)

### [Promise.all](#t_l_Promise_all) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_promise.c#L361 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)

[(top)](javascript:toppos\(\);)

#### Call type:

`Promise.all(promises)`

#### Parameters

`promises` - An array of promises

#### Returns

A new Promise

#### Description

Return a new promise that is resolved when all promises in the supplied array are resolved.

**Note:** This is not available in devices with low flash memory

### [function Promise.catch](#t_l_Promise_catch) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_promise.c#L558 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Promise.catch(onRejected)`

#### Parameters

`onRejected` - A callback that is called when this promise is rejected

#### Returns

The original Promise

#### Description

**Note:** This is not available in devices with low flash memory

### [constructor Promise](#t_l_Promise_Promise) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_promise.c#L281 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Promise(executor)`

#### Parameters

`executor` - A function of the form `function (resolve, reject)`

#### Returns

A Promise

#### Description

Create a new Promise. The executor function is executed immediately (before the constructor even returns) and

**Note:** This is not available in devices with low flash memory

### [Promise.reject](#t_l_Promise_reject) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_promise.c#L461 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject)

[(top)](javascript:toppos\(\);)

#### Call type:

`Promise.reject(promises)`

#### Parameters

`promises` - Data to pass to the `.catch` handler

#### Returns

A new Promise

#### Description

Return a new promise that is already rejected (at idle it'll call `.catch`)

**Note:** This is not available in devices with low flash memory

### [Promise.resolve](#t_l_Promise_resolve) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_promise.c#L423 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve)

[(top)](javascript:toppos\(\);)

#### Call type:

`Promise.resolve(promises)`

#### Parameters

`promises` - Data to pass to the `.then` handler

#### Returns

A new Promise

#### Description

Return a new promise that is already resolved (at idle it'll call `.then`)

**Note:** This is not available in devices with low flash memory

### [function Promise.then](#t_l_Promise_then) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_promise.c#L515 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)

[(top)](javascript:toppos\(\);)

#### Call type:

`function Promise.then(onFulfilled, onRejected)`

#### Parameters

`onFulfilled` - A callback that is called when this promise is resolved

`onRejected` - \[optional\] A callback that is called when this promise is rejected (or nothing)

#### Returns

The original Promise

#### Description

**Note:** This is not available in devices with low flash memory

## [ReferenceError Class](#t_ReferenceError)

[(top)](javascript:toppos\(\);)

The base class for reference errors - where a variable which doesn't exist has been accessed.

#### Methods and Fields

-   [constructor ReferenceError(message)](#l_ReferenceError_ReferenceError)
-   [function ReferenceError.toString()](#l_ReferenceError_toString)

### [constructor ReferenceError](#t_l_ReferenceError_ReferenceError) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L136 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)

[(top)](javascript:toppos\(\);)

#### Call type:

`new ReferenceError(message)`

#### Parameters

`message` - \[optional\] An message string

#### Returns

A ReferenceError object

#### Description

Creates a ReferenceError object

### [function ReferenceError.toString](#t_l_ReferenceError_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L185 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function ReferenceError.toString()`

#### Returns

A String

#### Description

## [RegExp Class](#t_RegExp)

[(top)](javascript:toppos\(\);)

The built-in class for handling Regular Expressions

**Note:** Espruino's regular expression parser does not contain all the features present in a full ES6 JS engine. however some parts of the spec are not implemented:

-   [Assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Assertions) other than `^` and `$`
-   [Numeric quantifiers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Quantifiers) (eg `x{3}`)

There's a GitHub issue [concerning RegExp features here](https://github.com/espruino/Espruino/issues/1257)

#### Methods and Fields

-   [function RegExp.exec(str)](#l_RegExp_exec)
-   [constructor RegExp(regex, flags)](#l_RegExp_RegExp)
-   [function RegExp.test(str)](#l_RegExp_test)

### [function RegExp.exec](#t_l_RegExp_exec) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_regexp.c#L352 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec)

[(top)](javascript:toppos\(\);)

#### Call type:

`function RegExp.exec(str)`

#### Parameters

`str` - A string to match on

#### Returns

A result array, or null

#### Description

Test this regex on a string - returns a result array on success, or `null` otherwise.

`/Wo/.exec("Hello World")` will return:

```

[
 "Wo",
 "index": 6,
 "input": "Hello World"
]
```

Or with groups `/W(o)rld/.exec("Hello World")` returns:

```

[
 "World",
 "o", "index": 6,
 "input": "Hello World"
]
```

**Note:** This is not available in devices with low flash memory

### [constructor RegExp](#t_l_RegExp_RegExp) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_regexp.c#L287 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)

[(top)](javascript:toppos\(\);)

#### Call type:

`new RegExp(regex, flags)`

#### Parameters

`regex` - A regular expression as a string

`flags` - Flags for the regular expression as a string

#### Returns

A RegExp object

#### Description

Creates a RegExp object, for handling Regular Expressions

**Note:** This is not available in devices with low flash memory

### [function RegExp.test](#t_l_RegExp_test) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_regexp.c#L441 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/test)

[(top)](javascript:toppos\(\);)

#### Call type:

`function RegExp.test(str)`

#### Parameters

`str` - A string to match on

#### Returns

true for a match, or false

#### Description

Test this regex on a string - returns `true` on a successful match, or `false` otherwise

**Note:** This is not available in devices with low flash memory

## [Serial Class](#t_Serial)

[(top)](javascript:toppos\(\);)

This class allows use of the built-in USARTs

Methods may be called on the `USB`, `[Serial1](#l__global_Serial1)`, `[Serial2](#l__global_Serial2)`, `Serial3`, `Serial4`, `Serial5` and `Serial6` objects. While different processors provide different numbers of USARTs, on official Espruino boards you can always rely on at least `[Serial1](#l__global_Serial1)` being available

#### Instances

-   [](#l__global_Bluetooth)`[Bluetooth](#l__global_Bluetooth)` The Bluetooth Serial port - used when data is sent or received over Bluetooth
-   [](#l__global_LoopbackA)`[LoopbackA](#l__global_LoopbackA)` A loopback serial device. Data sent to `[LoopbackA](#l__global_LoopbackA)` comes out of `[LoopbackB](#l__global_LoopbackB)` and
-   [](#l__global_LoopbackB)`[LoopbackB](#l__global_LoopbackB)` A loopback serial device. Data sent to `[LoopbackA](#l__global_LoopbackA)` comes out of `[LoopbackB](#l__global_LoopbackB)` and
-   [](#l__global_Serial1)`[Serial1](#l__global_Serial1)` The first Serial (USART) port
-   [](#l__global_Serial2)`[Serial2](#l__global_Serial2)` The second Serial (USART) port
-   [](#l__global_SWDCON)`[SWDCON](#l__global_SWDCON)` In memory serial I/O device accessible via SWD debugger.
-   [](#l__global_Terminal)`[Terminal](#l__global_Terminal)` A simple VT100 terminal emulator.

#### Methods and Fields

-   [function Serial.available()](#l_Serial_available)
-   [event Serial.data(data)](#l_Serial_data)
-   [Serial.find(pin)](#l_Serial_find)
-   [function Serial.flush()](#l_Serial_flush)
-   [event Serial.framing()](#l_Serial_framing)
-   [function Serial.inject(data, ...)](#l_Serial_inject)
-   [function Serial.isConnected()](#l_Serial_isConnected)
-   [event Serial.parity()](#l_Serial_parity)
-   [function Serial.pipe(destination, options)](#l_Serial_pipe)
-   [function Serial.print(string)](#l_Serial_print)
-   [function Serial.println(string)](#l_Serial_println)
-   [function Serial.read(chars)](#l_Serial_read)
-   [constructor Serial()](#l_Serial_Serial)
-   [function Serial.setConsole(force)](#l_Serial_setConsole)
-   [function Serial.setup(baudrate, options)](#l_Serial_setup)
-   [function Serial.unsetup()](#l_Serial_unsetup)
-   [function Serial.write(data, ...)](#l_Serial_write)

### [function Serial.available](#t_l_Serial_available) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L514 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.available()`

#### Returns

How many bytes are available

#### Description

Return how many bytes are available to read. If there is already a listener for data, this will always return 0.

### [event Serial.data](#t_l_Serial_data) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L53 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Serial.on('data', function(data) { ... });`

#### Parameters

`data` - A string containing one or more characters of received data

#### Description

The `data` event is called when data is received. If a handler is defined with `X.on('data', function(data) { ... })` then it will be called, otherwise data will be stored in an internal buffer, where it can be retrieved with `X.read()`

### [Serial.find](#t_l_Serial_find) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L103 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Serial.find(pin)`

#### Parameters

`pin` - A pin to search with

#### Returns

An object of type `[Serial](#Serial)`, or `undefined` if one couldn't be found.

#### Description

**DEPRECATED** - this will be removed in subsequent versions of Espruino

Try and find a USART (Serial) hardware device that will work on this pin (e.g. `[Serial1](#l__global_Serial1)`)

May return undefined if no device can be found.

**Note:** This is not available in devices with low flash memory

### [function Serial.flush](#t_l_Serial_flush) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L554 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.flush()`

#### Description

Flush this serial stream (pause execution until all data has been sent)

**Note:** This is not available in devices with low flash memory

### [event Serial.framing](#t_l_Serial_framing) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L66 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Serial.on('framing', function() { ... });`

#### Description

The `framing` event is called when there was activity on the input to the UART but the `STOP` bit wasn't in the correct place. This is either because there was noise on the line, or the line has been pulled to 0 for a long period of time.

To enable this, you must initialise Serial with

```
SerialX.setup(..., { ...,
errors:true });
```

**Note:** Even though there was an error, the byte will still be received and passed to the `data` handler.

**Note:** This only works on STM32 and NRF52 based devices (e.g. all official Espruino boards)

### [function Serial.inject](#t_l_Serial_inject) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L482 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.inject(data, ...)`

#### Parameters

`data, ...` - One or more items to write. May be ints, strings, arrays, or special objects (see `[E.toUint8Array](#l_E_toUint8Array)` for more info).

#### Description

Add data to this device as if it came directly from the input - it will be returned via `serial.on('data', ...)`;

```

Serial1.on('data', function(d) { print("Got",d); });
Serial1.inject('Hello World');
// prints "Got Hel","Got lo World" (characters can be split over multiple callbacks)
```

This is most useful if you wish to send characters to Espruino's REPL (console) while it is on another device.

**Note:** This is not available in devices with low flash memory

### [function Serial.isConnected](#t_l_Serial_isConnected) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L569 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.isConnected()`

#### Returns

`true` if connected/initialised, false otherwise

#### Description

(Added 2v25) Is the given Serial device connected?

-   USB/Bluetooth/Telnet/etc: Is this connected?
-   Serial1/etc: Has the device been initialised?
-   LoopbackA/LoopbackB/Terminal: always return true

### [event Serial.parity](#t_l_Serial_parity) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L84 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Serial.on('parity', function() { ... });`

#### Description

The `parity` event is called when the UART was configured with a parity bit, and this doesn't match the bits that have actually been received.

To enable this, you must initialise Serial with

```
SerialX.setup(..., { ...,
errors:true });
```

**Note:** Even though there was an error, the byte will still be received and passed to the `data` handler.

**Note:** This only works on STM32 and NRF52 based devices (e.g. all official Espruino boards)

### [function Serial.pipe](#t_l_Serial_pipe) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L538 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.pipe(destination, options)`

#### Parameters

`destination` - The destination file/stream that will receive content from the source.

`options` - \[optional\] An object `{ chunkSize : int=32, end : bool=true, complete : function }`  
chunkSize : The amount of data to pipe from source to destination at a time  
complete : a function to call when the pipe activity is complete  
end : call the 'end' function on the destination when the source is finished

#### Description

Pipe this USART to a stream (an object with a 'write' method)

**Note:** This is not available in devices with low flash memory

### [function Serial.print](#t_l_Serial_print) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L428 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.print(string)`

#### Parameters

`string` - A String to print

#### Description

Print a string to the serial port - without a line feed

**Note:** This function replaces any occurrences of `\n` in the string with `\r\n`. To avoid this, use `[Serial.write](#l_Serial_write)`.

### [function Serial.println](#t_l_Serial_println) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L442 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.println(string)`

#### Parameters

`string` - A String to print

#### Description

Print a line to the serial port with a newline (`\r\n`) at the end of it.

**Note:** This function converts data to a string first, e.g. `Serial.print([1,2,3])` is equivalent to `Serial.print("1,2,3")`. If you'd like to write raw bytes, use `[Serial.write](#l_Serial_write)`.

### [function Serial.read](#t_l_Serial_read) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L525 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.read(chars)`

#### Parameters

`chars` - The number of characters to read, or undefined/0 for all available

#### Returns

A string containing the required bytes.

#### Description

Return a string containing characters that have been received

### [constructor Serial](#t_l_Serial_Serial) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L38 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`new Serial()`

#### Returns

A Serial object

#### Description

Create a software Serial port. This has limited functionality (only low baud rates), but it can work on any pins.

Use `[Serial.setup](#l_Serial_setup)` to configure this port.

### [function Serial.setConsole](#t_l_Serial_setConsole) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L207 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.setConsole(force)`

#### Parameters

`force` - Whether to force the console to this port

#### Description

Set this Serial port as the port for the JavaScript console (REPL).

Unless `force` is set to true, changes in the connection state of the board (for instance plugging in USB) will cause the console to change.

See `[E.setConsole](#l_E_setConsole)` for a more flexible version of this function.

### [function Serial.setup](#t_l_Serial_setup) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L232 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.setup(baudrate, options)`

#### Parameters

`baudrate` - The baud rate - the default is 9600

`options` - \[optional\] A structure containing extra information on initialising the serial port - see below.

#### Description

Setup this Serial port with the given baud rate and options.

e.g.

```

Serial1.setup(9600,{rx:a_pin, tx:a_pin});
```

The second argument can contain:

```

{
  rx:pin,                           // Receive pin (data in to Espruino)
  tx:pin,                           // Transmit pin (data out of Espruino)
  ck:pin,                           // (default none) Clock Pin
  cts:pin,                          // (default none) Clear to Send Pin
  bytesize:8,                       // (default 8)How many data bits - 7 or 8
  parity:null/'none'/'o'/'odd'/'e'/'even',
                                    // (default none) Parity bit
  stopbits:1,                       // (default 1) Number of stop bits to use
  flow:null/undefined/'none'/'xon', // (default none) software flow control
  path:null/undefined/string        // Linux Only - the path to the Serial device to use
  errors:false                      // (default false) whether to forward framing/parity errors
}
```

You can find out which pins to use by looking at [your board's reference page](#boards) and searching for pins with the `UART`/`USART` markers.

If not specified in options, the default pins are used for rx and tx (usually the lowest numbered pins on the lowest port that supports this peripheral). `ck` and `cts` are not used unless specified.

Note that even after changing the RX and TX pins, if you have called setup before then the previous RX and TX pins will still be connected to the Serial port as well - until you set them to something else using `[digitalWrite](#l__global_digitalWrite)` or `[pinMode](#l__global_pinMode)`.

Flow control can be xOn/xOff (`flow:'xon'`) or hardware flow control (receive only) if `cts` is specified. If `cts` is set to a pin, the pin's value will be 0 when Espruino is ready for data and 1 when it isn't.

By default, framing or parity errors don't create `framing` or `parity` events on the `[Serial](#Serial)` object because storing these errors uses up additional storage in the queue. If you're intending to receive a lot of malformed data then the queue might overflow `[E.getErrorFlags()](#l_E_getErrorFlags)` would return `FIFO_FULL`. However if you need to respond to `framing` or `parity` errors then you'll need to use `errors:true` when initialising serial.

On Linux builds there is no default Serial device, so you must specify a path to a device - for instance: `Serial1.setup(9600,{path:"/dev/ttyACM0"})`

You can also set up 'software serial' using code like:

```

var s = new Serial();
s.setup(9600,{rx:a_pin, tx:a_pin});
```

However software serial doesn't use `ck`, `cts`, `parity`, `flow` or `errors` parts of the initialisation object.

### [function Serial.unsetup](#t_l_Serial_unsetup) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L356 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.unsetup()`

#### Description

If the serial (or software serial) device was set up, uninitialise it.

**Note:** This is not available in devices with low flash memory

### [function Serial.write](#t_l_Serial_write) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_serial.c#L463 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Serial.write(data, ...)`

#### Parameters

`data, ...` - One or more items to write. May be ints, strings, arrays, or special objects (see `[E.toUint8Array](#l_E_toUint8Array)` for more info).

#### Description

Write a character or array of data to the serial port

This method writes unmodified data, e.g. `Serial.write([1,2,3])` is equivalent to `Serial.write("\1\2\3")`. If you'd like data converted to a string first, use `[Serial.print](#l_Serial_print)`.

## [SPI Class](#t_SPI)

[(top)](javascript:toppos\(\);)

This class allows use of the built-in SPI ports. Currently it is SPI master only.

#### Instances

-   [](#l__global_SPI1)`[SPI1](#l__global_SPI1)` The first SPI port

#### Methods and Fields

-   [SPI.find(pin)](#l_SPI_find)
-   [function SPI.send(data, nss\_pin)](#l_SPI_send)
-   [function SPI.send4bit(data, bit0, bit1, nss\_pin)](#l_SPI_send4bit)
-   [function SPI.send8bit(data, bit0, bit1, nss\_pin)](#l_SPI_send8bit)
-   [function SPI.setup(options)](#l_SPI_setup)
-   [constructor SPI()](#l_SPI_SPI)
-   [function SPI.write(data, ...)](#l_SPI_write)

### [SPI.find](#t_l_SPI_find) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L72 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`SPI.find(pin)`

#### Parameters

`pin` - A pin to search with

#### Returns

An object of type `[SPI](#SPI)`, or `undefined` if one couldn't be found.

#### Description

**DEPRECATED** - this will be removed in subsequent versions of Espruino

Try and find an SPI hardware device that will work on this pin (e.g. `[SPI1](#l__global_SPI1)`)

May return undefined if no device can be found.

**Note:** This is not available in devices with low flash memory

### [function SPI.send](#t_l_SPI_send) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L169 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function SPI.send(data, nss_pin)`

#### Parameters

`data` - The data to send - either an Integer, Array, String, or Object of the form `{data: ..., count:#}`

`nss_pin` - An nSS pin - this will be lowered before SPI output and raised afterwards (optional). There will be a small delay between when this is lowered and when sending starts, and also between sending finishing and it being raised.

#### Returns

The data that was returned

#### Description

Send data down SPI, and return the result. Sending an integer will return an integer, a String will return a String, and anything else will return a Uint8Array.

Sending multiple bytes in one call to send is preferable as they can then be transmitted end to end. Using multiple calls to send() will result in significantly slower transmission speeds.

For maximum speeds, please pass either Strings or Typed Arrays as arguments. Note that you can even pass arrays of arrays, like `[1,[2,3,4],5]`

### [function SPI.send4bit](#t_l_SPI_send4bit) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L363 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function SPI.send4bit(data, bit0, bit1, nss_pin)`

#### Parameters

`data` - The data to send - either an integer, array, or string

`bit0` - The 4 bits to send for a 0 (MSB first)

`bit1` - The 4 bits to send for a 1 (MSB first)

`nss_pin` - An nSS pin - this will be lowered before SPI output and raised afterwards (optional). There will be a small delay between when this is lowered and when sending starts, and also between sending finishing and it being raised.

#### Description

Send data down SPI, using 4 bits for each 'real' bit (MSB first). This can be useful for faking one-wire style protocols

Sending multiple bytes in one call to send is preferable as they can then be transmitted end to end. Using multiple calls to send() will result in significantly slower transmission speeds.

### [function SPI.send8bit](#t_l_SPI_send8bit) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L435 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function SPI.send8bit(data, bit0, bit1, nss_pin)`

#### Parameters

`data` - The data to send - either an integer, array, or string

`bit0` - The 8 bits to send for a 0 (MSB first)

`bit1` - The 8 bits to send for a 1 (MSB first)

`nss_pin` - An nSS pin - this will be lowered before SPI output and raised afterwards (optional). There will be a small delay between when this is lowered and when sending starts, and also between sending finishing and it being raised

#### Description

Send data down SPI, using 8 bits for each 'real' bit (MSB first). This can be useful for faking one-wire style protocols

Sending multiple bytes in one call to send is preferable as they can then be transmitted end to end. Using multiple calls to send() will result in significantly slower transmission speeds.

**Note:** This is not available in devices with low flash memory

### [function SPI.setup](#t_l_SPI_setup) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L89 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function SPI.setup(options)`

#### Parameters

`options` - An Object containing extra information on initialising the SPI port

#### Description

Set up this SPI port as an SPI Master.

Options can contain the following (defaults are shown where relevant):

```

{
  sck:pin,
  miso:pin,
  mosi:pin,
  baud:integer=100000, // ignored on software SPI
  mode:integer=0, // between 0 and 3
  order:string='msb' // can be 'msb' or 'lsb'
  bits:8 // only available for software SPI
}
```

If `sck`,`miso` and `mosi` are left out, they will automatically be chosen. However if one or more is specified then the unspecified pins will not be set up.

You can find out which pins to use by looking at [your board's reference page](#boards) and searching for pins with the `[SPI](#SPI)` marker. Some boards such as those based on `nRF52` chips can have SPI on any pins, so don't have specific markings.

The SPI `mode` is between 0 and 3 - see http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus#Clock_polarity_and_phase

On STM32F1-based parts, you cannot mix AF and non-AF pins (SPI pins are usually grouped on the chip - and you can't mix pins from two groups). Espruino will not warn you about this.

### [constructor SPI](#t_l_SPI_SPI) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L56 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`new SPI()`

#### Returns

A SPI object

#### Description

Create a software SPI port. This has limited functionality (no baud rate), but it can work on any pins.

Use `[SPI.setup](#l_SPI_setup)` to configure this port.

### [function SPI.write](#t_l_SPI_write) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_spi_i2c.c#L307 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function SPI.write(data, ...)`

#### Parameters

`data, ...` - One or more items to write. May be ints, strings, arrays, or special objects (see `[E.toUint8Array](#l_E_toUint8Array)` for more info).  
If the last argument is a pin, it is taken to be the NSS pin

#### Description

Write a character or array of characters to SPI - without reading the result back.

For maximum speeds, please pass either Strings or Typed Arrays as arguments.

## [Storage Library](#t_Storage)

[(top)](javascript:toppos\(\);)

This module allows you to read and write part of the nonvolatile flash memory of your device using a filesystem-like API.

Also see the `[Flash](#Flash)` library, which provides a low level, more dangerous way to access all parts of your flash memory.

The `[Storage](#Storage)` library provides two distinct types of file:

-   `require("Storage").write(...)`/`require("Storage").read(...)`/etc create simple contiguous files of fixed length. This is the recommended file type.
-   `require("Storage").open(...)` creates a `[StorageFile](#StorageFile)`, which stores the file in numbered chunks (`"filename\1"`/`"filename\2"`/etc). It allows data to be appended and for the file to be read line by line.

You must read a file using the same method you used to write it - e.g. you can't create a file with `require("Storage").open(...)` and then read it with `require("Storage").read(...)`.

**Note:** In firmware 2v05 and later, the maximum length for filenames is 28 characters. However in 2v04 and earlier the max length is 8.

#### Methods and Fields

-   [require("Storage").compact(showMessage)](#l_Storage_compact)
-   [require("Storage").erase(name)](#l_Storage_erase)
-   [require("Storage").eraseAll()](#l_Storage_eraseAll)
-   [require("Storage").getFree(checkInternalFlash)](#l_Storage_getFree)
-   [require("Storage").getStats(checkInternalFlash)](#l_Storage_getStats)
-   [require("Storage").hash(regex)](#l_Storage_hash)
-   [require("Storage").list(regex, filter)](#l_Storage_list)
-   [require("Storage").open(name, mode)](#l_Storage_open)
-   [require("Storage").optimise()](#l_Storage_optimise)
-   [require("Storage").read(name, offset, length)](#l_Storage_read)
-   [require("Storage").readArrayBuffer(name)](#l_Storage_readArrayBuffer)
-   [require("Storage").readJSON(name, noExceptions)](#l_Storage_readJSON)
-   [require("Storage").write(name, data, offset, size)](#l_Storage_write)
-   [require("Storage").writeJSON(name, data)](#l_Storage_writeJSON)

### [Storage.compact](#t_l_Storage_compact) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L391 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").compact(showMessage)`

#### Parameters

`showMessage` - \[optional\] If true, an overlay message will be displayed on the screen while compaction is happening. Default is false.

#### Description

The Flash Storage system is journaling. To make the most of the limited write cycles of Flash memory, Espruino marks deleted/replaced files as garbage/trash files and moves on to a fresh part of flash memory. Espruino only fully erases those files when it is running low on flash, or when `compact` is called.

`compact` may fail if there isn't enough RAM free on the stack to use as swap space, however in this case it will not lose data.

**Note:** `compact` rearranges the contents of memory. If code is referencing that memory (e.g. functions that have their code stored in flash) then they may become garbled when compaction happens. To avoid this, call `eraseFiles` before uploading data that you intend to reference to ensure that uploaded files are right at the start of flash and cannot be compacted further.

**Note:** This is not available in devices with low flash memory

### [Storage.erase](#t_l_Storage_erase) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L83 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").erase(name)`

#### Parameters

`name` - The filename - max 28 characters (case sensitive)

#### Description

Erase a single file from the flash storage area.

**Note:** This function should be used with normal files, and not `[StorageFile](#StorageFile)`s created with `require("Storage").open(filename, ...)`. To erase those, use `require("Storage").open(..., "r").erase()`.

### [Storage.eraseAll](#t_l_Storage_eraseAll) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L69 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").eraseAll()`

#### Description

Erase the flash storage area. This will remove all files created with `require("Storage").write(...)` as well as any code saved with `save()` or `[E.setBootCode()](#l_E_setBootCode)`.

### [Storage.getFree](#t_l_Storage_getFree) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L433 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").getFree(checkInternalFlash)`

#### Parameters

`checkInternalFlash` - Check the internal flash (rather than external SPI flash). Default false, so will check external storage

#### Returns

The amount of free bytes

#### Description

Return the amount of free bytes available in Storage. Due to fragmentation there may be more bytes available, but this represents the maximum size of file that can be written.

**NOTE:** `checkInternalFlash` is only useful on DICKENS devices - other devices don't use two different flash banks

**Note:** This is not available in devices with low flash memory

### [Storage.getStats](#t_l_Storage_getStats) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L458 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").getStats(checkInternalFlash)`

#### Parameters

`checkInternalFlash` - `true` = Check internal flash, `false` = external SPI flash. Default `undefined`, so will check both

#### Returns

An object containing info about the current Storage system

#### Description

Returns:

```

{
  totalBytes // Amount of bytes in filesystem
  freeBytes // How many bytes are left at the end of storage?
  fileBytes // How many bytes of allocated files do we have?
  fileCount // How many allocated files do we have?
  trashBytes // How many bytes of trash files do we have?
  trashCount // How many trash files do we have? (can be cleared with .compact)
}
```

**NOTE:** `checkInternalFlash` is only useful on DICKENS/BANGLEJS2\_IFLASH devices - other devices don't use two different flash banks

**Note:** This is not available in devices with low flash memory

### [Storage.hash](#t_l_Storage_hash) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L357 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").hash(regex)`

#### Parameters

`regex` - \[optional\] If supplied, filenames are checked against this regular expression (with `[String.match(regexp)](#l_String_match)`) to see if they match before being hashed

#### Returns

A hash of the files matching

#### Description

List all files in the flash storage area matching the specified regex (ignores StorageFiles), and then hash their filenames _and_ file locations.

Identical files may have different hashes (e.g. if Storage is compacted and the file moves) but the chances of different files having the same hash are extremely small.

```

// Hash files
require("Storage").hash()
// Files ending in '.boot.js'
require("Storage").hash(/\.boot\.js$/)
```

**Note:** This function is used by Bangle.js as a way to cache files. For instance the bootloader will add all `.boot.js` files together into a single `.boot0` file, but it needs to know quickly whether anything has changed.

**Note:** This is not available in devices with low flash memory

### [Storage.list](#t_l_Storage_list) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L311 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").list(regex, filter)`

#### Parameters

`regex` - \[optional\] If supplied, filenames are checked against this regular expression (with `[String.match(regexp)](#l_String_match)`) to see if they match before being returned

`filter` - \[optional\] If supplied, File Types are filtered based on this: `{sf:true}` or `{sf:false}` for whether to show StorageFile

#### Returns

An array of filenames

#### Description

List all files in the flash storage area. An array of Strings is returned.

By default this lists files created by `[StorageFile](#StorageFile)` (`require("Storage").open`) which have a file number (`"\1"`/`"\2"`/etc) appended to them.

```

// All files
require("Storage").list()
// Files ending in '.js'
require("Storage").list(/\.js$/)
// All Storage Files
require("Storage").list(undefined, {sf:true})
// All normal files (e.g. created with Storage.write)
require("Storage").list(undefined, {sf:false})
```

**Note:** This will output system files (e.g. saved code) as well as files that you may have written.

### [Storage.open](#t_l_Storage_open) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L532 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").open(name, mode)`

#### Parameters

`name` - The filename - max **27** characters (case sensitive)

`mode` - The open mode - must be either `'r'` for read,`'w'` for write , or `'a'` for append

#### Returns

An object containing {read,write,erase}

#### Description

Open a file in the Storage area. This can be used for appending data (normal read/write operations only write the entire file).

Please see `[StorageFile](#StorageFile)` for more information (and examples).

**Note:** These files write through immediately - they do not need closing.

**Note:** This is not available in devices with low flash memory

### [Storage.optimise](#t_l_Storage_optimise) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L516 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").optimise()`

#### Description

Writes a lookup table for files into Bangle.js's storage. This allows any file stored up to that point to be accessed quickly.

**Note:** This is not available in devices with low flash memory

### [Storage.read](#t_l_Storage_read) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L103 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").read(name, offset, length)`

#### Parameters

`name` - The filename - max 28 characters (case sensitive)

`offset` - \[optional\] The offset in bytes to start from

`length` - \[optional\] The length to read in bytes (if <=0, the entire file is read)

#### Returns

A string of data, or `undefined` if the file is not found

#### Description

Read a file from the flash storage area that has been written with `require("Storage").write(...)`.

This function returns a memory-mapped String that points to the actual memory area in read-only memory, so it won't use up RAM.

As such you can check if a file exists efficiently using `require("Storage").read(filename)!==undefined`.

If you evaluate this string with `[eval](#l__global_eval)`, any functions contained in the String will keep their code stored in flash memory.

**Note:** This function should be used with normal files, and not `[StorageFile](#StorageFile)`s created with `require("Storage").open(filename, ...)`

### [Storage.readArrayBuffer](#t_l_Storage_readArrayBuffer) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L168 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").readArrayBuffer(name)`

#### Parameters

`name` - The filename - max 28 characters (case sensitive)

#### Returns

An ArrayBuffer containing data from the file, or undefined

#### Description

Read a file from the flash storage area that has been written with `require("Storage").write(...)`, and return the raw binary data as an ArrayBuffer.

This can be used:

-   In a `[DataView](#DataView)` with `new DataView(require("Storage").readArrayBuffer("x"))`
-   In a `Uint8Array/Float32Array/etc` with
    
    ```
    new
    Uint8Array(require("Storage").readArrayBuffer("x"))
    ```
    

**Note:** This function should be used with normal files, and not `[StorageFile](#StorageFile)`s created with `require("Storage").open(filename, ...)`

**Note:** This is not available in devices with low flash memory

### [Storage.readJSON](#t_l_Storage_readJSON) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L135 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").readJSON(name, noExceptions)`

#### Parameters

`name` - The filename - max 28 characters (case sensitive)

`noExceptions` - If true and the JSON is not valid, just return `undefined` - otherwise an `Exception` is thrown

#### Returns

An object containing parsed JSON from the file, or undefined

#### Description

Read a file from the flash storage area that has been written with `require("Storage").write(...)`, and parse JSON in it into a JavaScript object.

This is identical to `JSON.parse(require("Storage").read(...))`. It will throw an exception if the data in the file is not valid JSON.

**Note:** This function should be used with normal files, and not `[StorageFile](#StorageFile)`s created with `require("Storage").open(filename, ...)`

**Note:** This is not available in devices with low flash memory

### [Storage.write](#t_l_Storage_write) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L201 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").write(name, data, offset, size)`

#### Parameters

`name` - The filename - max 28 characters (case sensitive)

`data` - The data to write

`offset` - \[optional\] The offset within the file to write (if `0`/`undefined` a new file is created, otherwise Espruino attempts to write within an existing file if one exists)

`size` - \[optional\] The size of the file (if a file is to be created that is bigger than the data)

#### Returns

True on success, false on failure

#### Description

Write/create a file in the flash storage area. This is nonvolatile and will not disappear when the device resets or power is lost.

Simply write `require("Storage").write("MyFile", "Some data")` to write a new file, and `require("Storage").read("MyFile")` to read it.

If you supply:

-   A String, it will be written as-is
-   An array, will be written as a byte array (but read back as a String)
-   An object, it will automatically be converted to a JSON string before being written.

**Note:** If an array is supplied it will not be converted to JSON. To be explicit about the conversion you can use `[Storage.writeJSON](#l_Storage_writeJSON)`

You may also create a file and then populate data later **as long as you don't try and overwrite data that already exists**. For instance:

```

var f = require("Storage");
f.write("a","Hello",0,14); // Creates a new file, 14 chars long
print(JSON.stringify(f.read("a"))); // read the file
// any nonwritten chars will be char code 255:
"Hello\u00FF\u00FF\u00FF\u00FF\u00FF\u00FF\u00FF\u00FF\u00FF"
f.write("a"," ",5); // write within the file
f.write("a","World!!!",6); // write again within the file
print(f.read("a")); // "Hello World!!!"
f.write("a"," ",0); // Writing to location 0 again will cause the file to be re-written
print(f.read("a")); // " "
```

This can be useful if you've got more data to write than you have RAM available - for instance the Web IDE uses this method to write large files into onboard storage.

**Note:** This function should be used with normal files, and not `[StorageFile](#StorageFile)`s created with `require("Storage").open(filename, ...)`

### [Storage.writeJSON](#t_l_Storage_writeJSON) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L268 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("Storage").writeJSON(name, data)`

#### Parameters

`name` - The filename - max 28 characters (case sensitive)

`data` - The JSON data to write

#### Returns

True on success, false on failure

#### Description

Write/create a file in the flash storage area. This is nonvolatile and will not disappear when the device resets or power is lost.

Simply write `require("Storage").writeJSON("MyFile", [1,2,3])` to write a new file, and `require("Storage").readJSON("MyFile")` to read it.

This is (almost) equivalent to `require("Storage").write(name, JSON.stringify(data))` (see the notes below)

**Note:** This function should be used with normal files, and not `[StorageFile](#StorageFile)`s created with `require("Storage").open(filename, ...)`

**Note:** Normally `[JSON.stringify](#l_JSON_stringify)` converts any non-standard character to an escape code with `\uXXXX`, but as of Espruino 2v20, when writing to a file we use the most compact form, like `\xXX` or `\X`, as well as skipping quotes on fields. This saves space and is faster, but also means that if a String wasn't a UTF8 string but contained characters in the UTF8 codepoint range, when saved it won't end up getting reloaded as a UTF8 string. It does mean that you cannot parse the file with just `[JSON.parse](#l_JSON_parse)` as it's no longer standard JSON but is JS, so you must use `[Storage.readJSON](#l_Storage_readJSON)`

**Note:** This is not available in devices with low flash memory

## [StorageFile Class](#t_StorageFile)

[(top)](javascript:toppos\(\);)

These objects are created from `require("Storage").open` and allow Storage items to be read/written.

The `[Storage](#Storage)` library writes into Flash memory (which can only be erased in chunks), and unlike a normal filesystem it allocates files in one long contiguous area to allow them to be accessed easily from Espruino.

This presents a challenge for `[StorageFile](#StorageFile)` which allows you to append to a file, so instead `[StorageFile](#StorageFile)` stores files in chunks. It uses the last character of the filename to denote the chunk number (e.g. `"foobar\1"`, `"foobar\2"`, etc).

This means that while `[StorageFile](#StorageFile)` files exist in the same area as those from `[Storage](#Storage)`, they should be read using `[Storage.open](#l_Storage_open)` (and not `[Storage.read](#l_Storage_read)`).

```

f = require("Storage").open("foobar","w");
f.write("Hell");
f.write("o World\n");
f.write("Hello\n");
f.write("World 2\n");
f.write("Hello World 3\n");
// there's no need to call 'close'
// then
f = require("Storage").open("foobar","r");
f.read(13) // "Hello World\nH"
f.read(13) // "ello\nWorld 2\n"
f.read(13) // "Hello World 3"
f.read(13) // "\n"
f.read(13) // undefined
// or
f = require("Storage").open("foobar","r");
f.readLine() // "Hello World\n"
f.readLine() // "Hello\n"
f.readLine() // "World 2\n"
f.readLine() // "Hello World 3\n"
f.readLine() // undefined
// now get rid of file
f.erase();
```

**Note:** `[StorageFile](#StorageFile)` uses the fact that all bits of erased flash memory are 1 to detect the end of a file. As such you should not write character code 255 (`"\xFF"`) to these files.

#### Methods and Fields

-   [function StorageFile.erase()](#l_StorageFile_erase)
-   [function StorageFile.getLength()](#l_StorageFile_getLength)
-   [function StorageFile.pipe(destination, options)](#l_StorageFile_pipe)
-   [function StorageFile.read(len)](#l_StorageFile_read)
-   [function StorageFile.readLine()](#l_StorageFile_readLine)
-   [function StorageFile.write(data)](#l_StorageFile_write)

### [function StorageFile.erase](#t_l_StorageFile_erase) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L964 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function StorageFile.erase()`

#### Description

Erase this `[StorageFile](#StorageFile)` - after being called this file can no longer be written to.

**Note:** You shouldn't call `require("Storage").erase(...)` on a `[StorageFile](#StorageFile)`, but should instead open the StorageFile and call `.erase` on the returned file: `require("Storage").open(..., "r").erase()`

**Note:** This is not available in devices with low flash memory

### [function StorageFile.getLength](#t_l_StorageFile_getLength) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L801 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function StorageFile.getLength()`

#### Returns

The current length in bytes of the file

#### Description

Return the length of the current file.

This requires Espruino to read the file from scratch, which is not a fast operation.

**Note:** This is not available in devices with low flash memory

### [function StorageFile.pipe](#t_l_StorageFile_pipe) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L995 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function StorageFile.pipe(destination, options)`

#### Parameters

`destination` - The destination file/stream that will receive content from the source.

`options` - \[optional\] An object `{ chunkSize : int=32, end : bool=true, complete : function }`  
chunkSize : The amount of data to pipe from source to destination at a time  
complete : a function to call when the pipe activity is complete  
end : call the 'end' function on the destination when the source is finished

#### Description

Pipe this file to a stream (an object with a 'write' method)

**Note:** This is not available in devices with low flash memory

### [function StorageFile.read](#t_l_StorageFile_read) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L765 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function StorageFile.read(len)`

#### Parameters

`len` - How many bytes to read

#### Returns

A String, or undefined

#### Description

Read 'len' bytes of data from the file, and return a String containing those bytes.

If the end of the file is reached, the String may be smaller than the amount of bytes requested, or if the file is already at the end, `undefined` is returned.

**Note:** This is not available in devices with low flash memory

### [function StorageFile.readLine](#t_l_StorageFile_readLine) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L787 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function StorageFile.readLine()`

#### Returns

A line of data

#### Description

Read a line of data from the file (up to and including `"\n"`)

**Note:** This is not available in devices with low flash memory

### [function StorageFile.write](#t_l_StorageFile_write) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_storage.c#L866 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function StorageFile.write(data)`

#### Parameters

`data` - The data to write. This should not include `'\xFF'` (character code 255)

#### Description

Append the given data to a file. You should not attempt to append `"\xFF"` (character code 255).

**Note:** This is not available in devices with low flash memory

## [String Class](#t_String)

[(top)](javascript:toppos\(\);)

This is the built-in class for Text Strings.

Text Strings in Espruino are not zero-terminated, so you can store zeros in them.

#### Methods and Fields

-   [function String.charAt(pos)](#l_String_charAt)
-   [function String.charCodeAt(pos)](#l_String_charCodeAt)
-   [function String.concat(args, ...)](#l_String_concat)
-   [function String.endsWith(searchString, length)](#l_String_endsWith)
-   [String.fromCharCode(code, ...)](#l_String_fromCharCode)
-   [function String.includes(substring, fromIndex)](#l_String_includes)
-   [function String.indexOf(substring, fromIndex)](#l_String_indexOf)
-   [function String.lastIndexOf(substring, fromIndex)](#l_String_lastIndexOf)
-   [property String.length](#l_String_length)
-   [function String.match(substr)](#l_String_match)
-   [function String.padEnd(targetLength, padString)](#l_String_padEnd)
-   [function String.padStart(targetLength, padString)](#l_String_padStart)
-   [function String.removeAccents()](#l_String_removeAccents)
-   [function String.repeat(count)](#l_String_repeat)
-   [function String.replace(subStr, newSubStr)](#l_String_replace)
-   [function String.replaceAll(subStr, newSubStr)](#l_String_replaceAll)
-   [function String.slice(start, end)](#l_String_slice)
-   [function String.split(separator)](#l_String_split)
-   [function String.startsWith(searchString, position)](#l_String_startsWith)
-   [constructor String(str, ...)](#l_String_String)
-   [function String.substr(start, len)](#l_String_substr)
-   [function String.substring(start, end)](#l_String_substring)
-   [function String.toLowerCase()](#l_String_toLowerCase)
-   [function String.toUpperCase()](#l_String_toUpperCase)
-   [function String.trim()](#l_String_trim)

### [function String.charAt](#t_l_String_charAt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L105 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.charAt(pos)`

#### Parameters

`pos` - The character number in the string. Negative values return characters from end of string (-1 = last char)

#### Returns

The character in the string

#### Description

Return a single character at the given position in the String.

### [function String.charCodeAt](#t_l_String_charCodeAt) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L139 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.charCodeAt(pos)`

#### Parameters

`pos` - The character number in the string. Negative values return characters from end of string (-1 = last char)

#### Returns

The integer value of a character in the string, or `[NaN](#l__global_NaN)` if out of bounds

#### Description

Return the integer value of a single character at the given position in the String.

### [function String.concat](#t_l_String_concat) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L792 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/concat)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.concat(args, ...)`

#### Parameters

`args, ...` - Strings to append

#### Returns

The result of appending all arguments to this string

#### Description

Append all arguments to this `[String](#String)` and return the result. Does not modify the original `[String](#String)`.

**Note:** This is not available in devices with low flash memory

### [function String.endsWith](#t_l_String_endsWith) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L840 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.endsWith(searchString, length)`

#### Parameters

`searchString` - The string to search for

`length` - \[optional\] The 'end' of the string - if left off the actual length of the string is used

#### Returns

`true` if the given characters are found at the end of the string, otherwise, `false`.

#### Description

**Note:** This is not available in devices with low flash memory

### [String.fromCharCode](#t_l_String_fromCharCode) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L66 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/fromCharCode)

[(top)](javascript:toppos\(\);)

#### Call type:

`String.fromCharCode(code, ...)`

#### Parameters

`code, ...` - One or more character codes to create a string from (range 0-255).

#### Returns

The character

#### Description

Return the character(s) represented by the given character code(s).

### [function String.includes](#t_l_String_includes) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L866 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.includes(substring, fromIndex)`

#### Parameters

`substring` - The string to search for

`fromIndex` - \[optional\] The start character index (or 0 if not defined)

#### Returns

`true` if the given characters are in the string, otherwise, `false`.

#### Description

**Note:** This is not available in devices with low flash memory

### [function String.indexOf](#t_l_String_indexOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L159 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/indexOf)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.indexOf(substring, fromIndex)`

#### Parameters

`substring` - The string to search for

`fromIndex` - \[optional\] Index to search from

#### Returns

The index of the string, or -1 if not found

#### Description

Return the index of substring in this string, or -1 if not found

### [function String.lastIndexOf](#t_l_String_lastIndexOf) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L172 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/lastIndexOf)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.lastIndexOf(substring, fromIndex)`

#### Parameters

`substring` - The string to search for

`fromIndex` - \[optional\] Index to search from

#### Returns

The index of the string, or -1 if not found

#### Description

Return the last index of substring in this string, or -1 if not found

### [property String.length](#t_l_String_length) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L56 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)

[(top)](javascript:toppos\(\);)

#### Call type:

`property String.length`

#### Returns

The value of the string

#### Description

Find the length of the string

### [function String.match](#t_l_String_match) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L251 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.match(substr)`

#### Parameters

`substr` - Substring or RegExp to match

#### Returns

A match array or `null` (see below):

#### Description

Matches an occurrence `subStr` in the string.

Returns `null` if no match, or:

```

"abcdef".match("b") == [
  "b",         // array index 0 - the matched string
  index: 1,    // the start index of the match
  input: "b"   // the input string
 ]
"abcdefabcdef".match(/bcd/) == [
  "bcd", index: 1,
  input: "abcdefabcdef"
 ]
```

'Global' RegExp matches just return an array of matches (with no indices):

```

"abcdefabcdef".match(/bcd/g) = [
  "bcd",
  "bcd"
 ]
```

### [function String.padEnd](#t_l_String_padEnd) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L926 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padEnd)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.padEnd(targetLength, padString)`

#### Parameters

`targetLength` - The length to pad this string to

`padString` - \[optional\] The string to pad with, default is `' '`

#### Returns

A string containing this string padded to the correct length

#### Description

Pad this string at the end to the required number of characters

```

"Hello".padEnd(10) == "Hello     "
"123".padEnd(10,".-") == "123.-.-.-."
```

**Note:** This is not available in devices with low flash memory

### [function String.padStart](#t_l_String_padStart) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L906 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/padStart)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.padStart(targetLength, padString)`

#### Parameters

`targetLength` - The length to pad this string to

`padString` - \[optional\] The string to pad with, default is `' '`

#### Returns

A string containing this string padded to the correct length

#### Description

Pad this string at the beginning to the required number of characters

```

"Hello".padStart(10) == "     Hello"
"123".padStart(10,".-") == ".-.-.-.123"
```

**Note:** This is not available in devices with low flash memory

### [function String.removeAccents](#t_l_String_removeAccents) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L668 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.removeAccents()`

#### Returns

This string with the accents/diacritics (such as é, ü) removed from characters in the ISO 8859-1 set

#### Description

This is not a standard JavaScript function, but is provided to allow use of fonts that only support ASCII (char codes 0..127, like the 4x6 font) with character input that might be in the ISO8859-1 range.

**Note:** This is not available in devices with low flash memory

### [function String.repeat](#t_l_String_repeat) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L881 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/repeat)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.repeat(count)`

#### Parameters

`count` - An integer with the amount of times to repeat this String

#### Returns

A string containing repetitions of this string

#### Description

Repeat this string the given number of times.

**Note:** This is not available in devices with low flash memory

### [function String.replace](#t_l_String_replace) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L444 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.replace(subStr, newSubStr)`

#### Parameters

`subStr` - The string (or Regular Expression) to search for

`newSubStr` - The string to replace it with. Replacer functions are supported, but only when subStr is a `[RegExp](#RegExp)`

#### Returns

This string with `subStr` replaced

#### Description

Search and replace ONE occurrence of `subStr` with `newSubStr` and return the result. This doesn't alter the original string.

### [function String.replaceAll](#t_l_String_replaceAll) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L462 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.replaceAll(subStr, newSubStr)`

#### Parameters

`subStr` - The string (or Regular Expression) to search for

`newSubStr` - The string to replace it with. Replacer functions are supported, but only when subStr is a `[RegExp](#RegExp)`

#### Returns

This string with `subStr` replaced

#### Description

Search and replace ALL occurrences of `subStr` with `newSubStr` and return the result. This doesn't alter the original string.

### [function String.slice](#t_l_String_slice) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L522 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.slice(start, end)`

#### Parameters

`start` - The start character index, if negative it is from the end of the string

`end` - \[optional\] The end character index, if negative it is from the end of the string, and if omitted it is the end of the string

#### Returns

Part of this string from start for len characters

#### Description

### [function String.split](#t_l_String_split) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L544 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.split(separator)`

#### Parameters

`separator` - The separator `[String](#String)` or `[RegExp](#RegExp)` to use

#### Returns

Part of this string from start for len characters

#### Description

Return an array made by splitting this string up by the separator. e.g. `'1,2,3'.split(',')==['1', '2', '3']`

Regular Expressions can also be used to split strings, e.g.

```
'1a2b3
4'.split(/[^0-9]/)==['1', '2', '3', '4']
```

.

### [function String.startsWith](#t_l_String_startsWith) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L816 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.startsWith(searchString, position)`

#### Parameters

`searchString` - The string to search for

`position` - \[optional\] The start character index (or 0 if not defined)

#### Returns

`true` if the given characters are found at the beginning of the string, otherwise, `false`.

#### Description

**Note:** This is not available in devices with low flash memory

### [constructor String](#t_l_String_String) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L34 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)

[(top)](javascript:toppos\(\);)

#### Call type:

`new String(str, ...)`

#### Parameters

`str, ...` - A value to turn into a string. If undefined or not supplied, an empty String is created.

#### Returns

A String

#### Description

Create a new String

### [function String.substr](#t_l_String_substr) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L503 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.substr(start, len)`

#### Parameters

`start` - The start character index

`len` - \[optional\] The number of characters

#### Returns

Part of this string from start for len characters

#### Description

### [function String.substring](#t_l_String_substring) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L480 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.substring(start, end)`

#### Parameters

`start` - The start character index (inclusive)

`end` - \[optional\] The end character index (exclusive)

#### Returns

The part of this string between start and end

#### Description

### [function String.toLowerCase](#t_l_String_toLowerCase) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L626 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.toLowerCase()`

#### Parameters

#### Returns

The lowercase version of this string

#### Description

### [function String.toUpperCase](#t_l_String_toUpperCase) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L636 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.toUpperCase()`

#### Parameters

#### Returns

The uppercase version of this string

#### Description

### [function String.trim](#t_l_String_trim) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_string.c#L755 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim)

[(top)](javascript:toppos\(\);)

#### Call type:

`function String.trim()`

#### Returns

A String with Whitespace removed from the beginning and end

#### Description

Return a new string with any whitespace (tabs, space, form feed, newline, carriage return, etc) removed from the beginning and end.

## [SyntaxError Class](#t_SyntaxError)

[(top)](javascript:toppos\(\);)

The base class for syntax errors

#### Methods and Fields

-   [constructor SyntaxError(message)](#l_SyntaxError_SyntaxError)
-   [function SyntaxError.toString()](#l_SyntaxError_toString)

### [constructor SyntaxError](#t_l_SyntaxError_SyntaxError) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L87 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[(top)](javascript:toppos\(\);)

#### Call type:

`new SyntaxError(message)`

#### Parameters

`message` - \[optional\] An message string

#### Returns

A SyntaxError object

#### Description

Creates a SyntaxError object

### [function SyntaxError.toString](#t_l_SyntaxError_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L161 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function SyntaxError.toString()`

#### Returns

A String

#### Description

## [tensorflow Library](#t_tensorflow)

[(top)](javascript:toppos\(\);)

#### Methods and Fields

-   [require("tensorflow").create(arenaSize, model)](#l_tensorflow_create)

### [tensorflow.create](#t_l_tensorflow_create) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/tensorflow/jswrap_tensorflow.c#L43 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("tensorflow").create(arenaSize, model)`

#### Parameters

`arenaSize` - The TensorFlow Arena size

`model` - The model to use - this should be a flat array/string

#### Returns

A tensorflow instance

#### Description

## [TFMicroInterpreter Class](#t_TFMicroInterpreter)

[(top)](javascript:toppos\(\);)

Class containing an instance of TFMicroInterpreter

#### Methods and Fields

-   [function TFMicroInterpreter.getInput()](#l_TFMicroInterpreter_getInput)
-   [function TFMicroInterpreter.getOutput()](#l_TFMicroInterpreter_getOutput)
-   [function TFMicroInterpreter.invoke()](#l_TFMicroInterpreter_invoke)

### [function TFMicroInterpreter.getInput](#t_l_TFMicroInterpreter_getInput) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/tensorflow/jswrap_tensorflow.c#L138 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function TFMicroInterpreter.getInput()`

#### Returns

An arraybuffer referencing the input data

#### Description

### [function TFMicroInterpreter.getOutput](#t_l_TFMicroInterpreter_getOutput) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/tensorflow/jswrap_tensorflow.c#L150 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function TFMicroInterpreter.getOutput()`

#### Returns

An arraybuffer referencing the output data

#### Description

### [function TFMicroInterpreter.invoke](#t_l_TFMicroInterpreter_invoke) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/tensorflow/jswrap_tensorflow.c#L162 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function TFMicroInterpreter.invoke()`

#### Description

## [timer Library](#t_timer)

[(top)](javascript:toppos\(\);)

(2v29+ only) This class allows Espruino to control stepper motors.

```

require("timer").list()
// [ { id: 0, type: 'SET', pins: [ D2, D3, D4, D5 ], value: 0, time: 10 }, ... ]
```

This replaces `E.dumpTimers()` and `Pin.writeAtTime`

#### Methods and Fields

-   [require("timer").add(timer)](#l_timer_add)
-   [require("timer").get(timerID)](#l_timer_get)
-   [require("timer").list()](#l_timer_list)
-   [require("timer").remove(timerID)](#l_timer_remove)

### [timer.add](#t_l_timer_add) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_timer.c#L215 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("timer").add(timer)`

#### Parameters

`[timer](#timer)` - An object describing the timer to add. See below.

#### Returns

Return the ID of the added timer

#### Description

To set one or more pins at a specific point in the future:

```

require("timer").add({
  type : "SET",
  pin : Pin, // required
  pin2 : Pin, // optional
  pin3 : Pin, // optional
  pin4 : Pin, // optional
  value : int, // required
  time : float, // time (in milliseconds) when the timer will first fire
  interval : float // (optional) if the timer repeats, the interval (in milliseconds)
})
// eg. set LED2 in 1 second (note: LED2 should already be an output)
require("timer").add({
  type: "SET",
  pin: LED2, value: 1,
  time: 1000
});
```

To execute some code at a specific point in the future:

```

require("timer").add({
  type : "EXEC",
  ptr : int, userdata : int, // required - pointer to native function(time:uint64, userdate:int) to call, and uint32 userdata to pass to function
  fn : JsVar, // alternative to ptr/userdata - a JS function to call (note: this function must be referenced elsewhere)
  time : float, // time (in milliseconds) when the timer will first fire
  interval : float // (optional) if the timer repeats, the interval (in milliseconds)
})
// eg. execute myFunction in 100ms, then 200ms thereafter
require("timer").add({
  type:"EXEC", fn: () => LED.toggle(),
  time:100,
  interval:200,
});
```

**Note:** `require("timer").add({type:"EXEC",fn:...})` differs from `[setInterval](#l__global_setInterval)`/`[setTimeout](#l__global_setTimeout)` in that it is scheduled using a hardware timer. When the timer fires, JavaScript that's executing will be paused at the next statement and the JS will be executed right away. This can be great for things like scanning out screens where you don't want your execution to be paused even if you're executing JavaScript code.

**Note:** This is not available in devices with low flash memory

### [timer.get](#t_l_timer_get) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_timer.c#L107 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("timer").get(timerID)`

#### Parameters

`timerID` - The ID of the timer to get

#### Returns

An object describing the added timer, with an `id` field added.

#### Description

Returns:

```

{
  id : int, // timer ID (corresponds to array index)
  type : string, // type of timer (eg 'SET/EXEC/STEP/WR8/WR16/RD8/RD16')
  time : float, // time (in milliseconds) when the timer will next fire
  interval : float, // (optional) if the timer repeats, the interval (in milliseconds
  // the following fields are only present on devices with enough flash memory)
  pins : [ Pin, ... ], // (for SET/STEP) the pins used
  value : int, // (for SET) the value being set
  ptr : int, // (for EXEC) pointer to the function being executed
  userdata : int, // (for EXEC) userdata pointer
  buffer : JsVar, // (for WR8/WR16/RD8/RD16) the buffer being used
  buffer2 : JsVar // (for WR8/WR16/RD8/RD16) the second buffer being used (if any)
}
```

**Note:** `time` is set when the timer was last serviced, so if you set a 1 second timer and then look at it after 500ms, it will still show as 1000ms (unless another timer as been serviced before).

**Note:** This is not available in devices with low flash memory

### [timer.list](#t_l_timer_list) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_timer.c#L83 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("timer").list()`

#### Returns

Return a list of objects representing active timers

#### Description

See `require("timer").get` for details of the fields in each timer.

**Note:** This is not available in devices with low flash memory

### [timer.remove](#t_l_timer_remove) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_timer.c#L333 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`require("timer").remove(timerID)`

#### Parameters

`timerID` - The ID of the timer to remove

#### Returns

`true` on success or `false` if there was no timer with that ID

#### Description

**Note:** This is not available in devices with low flash memory

## [TypeError Class](#t_TypeError)

[(top)](javascript:toppos\(\);)

The base class for type errors

#### Methods and Fields

-   [function TypeError.toString()](#l_TypeError_toString)
-   [constructor TypeError(message)](#l_TypeError_TypeError)

### [function TypeError.toString](#t_l_TypeError_toString) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L169 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function TypeError.toString()`

#### Returns

A String

#### Description

### [constructor TypeError](#t_l_TypeError_TypeError) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_error.c#L103 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[(top)](javascript:toppos\(\);)

#### Call type:

`new TypeError(message)`

#### Parameters

`message` - \[optional\] An message string

#### Returns

A TypeError object

#### Description

Creates a TypeError object

## [Uint16Array Class](#t_Uint16Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 16 bit unsigned integers.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Uint16Array(arr, byteOffset, length)](#l_Uint16Array_Uint16Array)

### [constructor Uint16Array](#t_l_Uint16Array_Uint16Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L354 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Uint16Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

## [Uint24Array Class](#t_Uint24Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 24 bit unsigned integers.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Uint24Array(arr, byteOffset, length)](#l_Uint24Array_Uint24Array)

### [constructor Uint24Array](#t_l_Uint24Array_Uint24Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L400 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`new Uint24Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

**Note:** This is not available in devices with low flash memory

## [Uint32Array Class](#t_Uint32Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 32 bit unsigned integers.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Uint32Array(arr, byteOffset, length)](#l_Uint32Array_Uint32Array)

### [constructor Uint32Array](#t_l_Uint32Array_Uint32Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L424 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Uint32Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

## [Uint8Array Class](#t_Uint8Array)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 8 bit unsigned integers.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Uint8Array(arr, byteOffset, length)](#l_Uint8Array_Uint8Array)

### [constructor Uint8Array](#t_l_Uint8Array_Uint8Array) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L282 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Uint8Array(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

## [Uint8ClampedArray Class](#t_Uint8ClampedArray)

[(top)](javascript:toppos\(\);)

This is the built-in JavaScript class for a typed array of 8 bit unsigned integers that are automatically clamped to the range 0 to 255.

Instantiate this in order to efficiently store arrays of data (Espruino's normal arrays store data in a map, which is inefficient for non-sparse arrays).

Arrays of this type include all the methods from [ArrayBufferView](/Reference#ArrayBufferView)

#### Methods and Fields

-   [constructor Uint8ClampedArray(arr, byteOffset, length)](#l_Uint8ClampedArray_Uint8ClampedArray)

### [constructor Uint8ClampedArray](#t_l_Uint8ClampedArray_Uint8ClampedArray) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_arraybuffer.c#L305 "Link to source code on GitHub")

[View MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)

[(top)](javascript:toppos\(\);)

#### Call type:

`new Uint8ClampedArray(arr, byteOffset, length)`

#### Parameters

`arr` - The array or typed array to base this off, or an integer which is the array length

`byteOffset` - The byte offset in the ArrayBuffer (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

`length` - The length (ONLY IF the first argument was an `[ArrayBuffer](#ArrayBuffer)`)

#### Returns

A typed array

#### Description

Create a typed array based on the given input. Either an existing Array Buffer, an Integer as a Length, or a simple array. If an `[ArrayBufferView](#ArrayBufferView)` (e.g. `[Uint8Array](#Uint8Array)` rather than `[ArrayBuffer](#ArrayBuffer)`) is given, it will be completely copied rather than referenced.

Clamped arrays clamp their values to the allowed range, rather than 'wrapping'. e.g. after `a[0]=12345;`, `a[0]==255`.

## [Unistroke Class](#t_Unistroke)

[(top)](javascript:toppos\(\);)

This class provides functionality to recognise gestures drawn on a touchscreen. It is only built into Bangle.js 2.

Usage:

```

var strokes = {
  stroke1 : Unistroke.new(new Uint8Array([x1, y1, x2, y2, x3, y3, ...])),
  stroke2 : Unistroke.new(new Uint8Array([x1, y1, x2, y2, x3, y3, ...])),
  stroke3 : Unistroke.new(new Uint8Array([x1, y1, x2, y2, x3, y3, ...]))
};
var r = Unistroke.recognise(strokes,new Uint8Array([x1, y1, x2, y2, x3, y3, ...]))
print(r); // stroke1/stroke2/stroke3
```

#### Methods and Fields

-   [Unistroke.new(xy)](#l_Unistroke_new)
-   [Unistroke.recognise(strokes, xy)](#l_Unistroke_recognise)

### [Unistroke.new](#t_l_Unistroke_new) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/misc/jswrap_unistroke.c#L39 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Unistroke.new(xy)`

#### Parameters

`xy` - An array of interleaved XY coordinates

#### Returns

A string of data representing this unistroke

#### Description

Create a new Unistroke based on XY coordinates

**Note:** This is only available in Bangle.js 2 smartwatches

### [Unistroke.recognise](#t_l_Unistroke_recognise) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/libs/misc/jswrap_unistroke.c#L56 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Unistroke.recognise(strokes, xy)`

#### Parameters

`strokes` - An object of named strokes : `{arrow:..., circle:...}`

`xy` - An array of interleaved XY coordinates

#### Returns

The key name of the matched stroke

#### Description

Recognise based on an object of named strokes, and a list of XY coordinates

**Note:** This is only available in Bangle.js 2 smartwatches

## [Waveform Class](#t_Waveform)

[(top)](javascript:toppos\(\);)

This class handles waveforms. In Espruino, a Waveform is a set of data that you want to input or output.

#### Methods and Fields

-   [event Waveform.buffer(buffer)](#l_Waveform_buffer)
-   [event Waveform.finish(buffer)](#l_Waveform_finish)
-   [function Waveform.startInput(output, freq, options)](#l_Waveform_startInput)
-   [function Waveform.startOutput(output, freq, options)](#l_Waveform_startOutput)
-   [function Waveform.stop()](#l_Waveform_stop)
-   [constructor Waveform(samples, options)](#l_Waveform_Waveform)

### [event Waveform.buffer](#t_l_Waveform_buffer) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_waveform.c#L44 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Waveform.on('buffer', function(buffer) { ... });`

#### Parameters

`buffer` - the last played buffer (which now needs to be filled ready for playback)

#### Description

When in double-buffered mode, this event is emitted when the `[Waveform](#Waveform)` class swaps to playing a new buffer - so you should then fill this current buffer up with new data.

**Note:** This is only available in Bangle.js smartwatches

### [event Waveform.finish](#t_l_Waveform_finish) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_waveform.c#L35 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`Waveform.on('finish', function(buffer) { ... });`

#### Parameters

`buffer` - the last played buffer

#### Description

Event emitted when playback has finished

**Note:** This is only available in Bangle.js smartwatches

### [function Waveform.startInput](#t_l_Waveform_startInput) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_waveform.c#L286 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Waveform.startInput(output, freq, options)`

#### Parameters

`output` - The pin to output on

`freq` - The frequency to output each sample at

`options` - \[optional\] options struct `{time:float,repeat:bool}` where: `time` is the that the waveform with start output at, e.g. `getTime()+1` (otherwise it is immediate), `repeat` is a boolean specifying whether to repeat the give sample

#### Description

Will start inputting the waveform on the given pin that supports analog. If not repeating, it'll emit a `finish` event when it is done.

**Note:** This is not available in devices with low flash memory

### [function Waveform.startOutput](#t_l_Waveform_startOutput) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_waveform.c#L253 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Waveform.startOutput(output, freq, options)`

#### Parameters

`output` - The pin to output on

`freq` - The frequency to output each sample at

`options` - \[optional\] options struct `{time:float, repeat:bool, npin:Pin}` (see below)

#### Description

Will start outputting the waveform on the given pin - the pin must have previously been initialised with analogWrite. If not repeating, it'll emit a `finish` event when it is done.

```

{
  time : float,        // the that the waveform with start output at, e.g. `getTime()+1` (otherwise it is immediate)
  repeat : bool,       // whether to repeat the given sample
  npin : Pin,          // If specified, the waveform is output across two pins (see below)
}
```

Using `npin` allows you to split the Waveform output between two pins and hence avoid any DC bias (or need to capacitor), for instance you could attach a speaker to `H0` and `H1` on Jolt.js. When the value in the waveform was at 50% both outputs would be 0, below 50% the signal would be on `npin` with `pin` as 0, and above 50% it would be on `pin` with `npin` as 0.

**Note:** This is not available in devices with low flash memory

### [function Waveform.stop](#t_l_Waveform_stop) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_waveform.c#L308 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`function Waveform.stop()`

#### Description

Stop a waveform that is currently outputting

**Note:** This is not available in devices with low flash memory

### [constructor Waveform](#t_l_Waveform_Waveform) [⇒](https://github.com/espruino/Espruino/blob/6106910b8/src/jswrap_waveform.c#L99 "Link to source code on GitHub")

[(top)](javascript:toppos\(\);)

#### Call type:

`new Waveform(samples, options)`

#### Parameters

`samples` - The number of samples to allocate as an integer, _or_ an arraybuffer (2v25+) containing the samples

`options` - \[optional\] options struct `{ doubleBuffer:bool, bits : 8/16 }` (see below)

#### Returns

An Waveform object

#### Description

Create a waveform class. This allows high speed input and output of waveforms. It has an internal variable called `buffer` (as well as `buffer2` when double-buffered - see `options` below) which contains the data to input/output.

Options can contain:

```

{
  doubleBuffer : bool   // whether to allocate two buffers or not (default false)
  bits         : 8/16   // the amount of bits to use (default 8).
}
```

When double-buffered, a 'buffer' event will be emitted each time a buffer is finished with (the argument is that buffer). When the recording stops, a 'finish' event will be emitted (with the first argument as the buffer).

```

// Output a sine wave
var w = new Waveform(1000);
for (var i=0;i<1000;i++) w.buffer[i]=128+120*Math.sin(i/2);
analogWrite(H0, 0.5, {freq:80000}); // set up H0 to output an analog value by PWM
w.on("finish", () => print("Done!"))
w.startOutput(H0,8000); // start playback
```

```

// On 2v25, from Storage
var f = require("Storage").read("sound.pcm");
var w = new Waveform(E.toArrayBuffer(f));
w.on("finish", () => print("Done!"))
w.startOutput(H0,8000); // start playback
```

See https://www.espruino.com/Waveform for more examples.

**Note:** This is not available in devices with low flash memory

---