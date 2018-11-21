# Mandelbulber2 RoyalRender submitter

## Setup
* Copy contents of **render_apps** folder into RR installation directory.
* Put Mandelbulber2 standalone version on a network share
    * Set **ExeCopyFromDir** in *render_apps/_config/3D20__Mandelbulber__inhouse.inc* to that location
* Put your Mandelbulber2 configuration file on a network share
    * Set **\<rrLocalBin\>rrCopy -oa** source path to that location (first path is source, the second one is destination)
    * RR copies this settings file before each render to local render user directory, where it is picked up by Mandelbulber2

## Usage
* Drag & drop your **.fract** scene onto **rrSubmit_Mandelbulber_2_15.bat** which is located in *render_apps/_submitplugins* folder
* Three rendering modes are supported:
    * Flight
    * Keyframe
    * Static

## Notes
* In order for version selection to work properly in RR, remove any additional numbers from paths, because they confuse RR
    * for example path like this:
    ```
    \\smaug\Shader\Mandelbulber2\mandelbulber_2.15\mandelbulber2.exe
    ```
    needs to be converted into this:
    ```
    \\smaug\Shader\Mandelbulber\mandelbulber_2.15\mandelbulber.exe
    ```