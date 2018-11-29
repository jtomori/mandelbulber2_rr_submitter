# Mandelbulber2 RoyalRender submitter

## Setup
* Copy contents of **render_apps** folder into RR installation directory.
* Put Mandelbulber2 standalone version on a network share (e.g. `\\share\renderers\Mandelbulber\mandelbulber_*` where `*` is version, like 2.14 or 2.15..)
	* Set **ExeCopyFromDir** in *render_apps/_config/3D20__Mandelbulber__inhouse.inc* to that location
		* e.g.
			```
			ExeCopyFromDir = \\share\renderers\Mandelbulber
			```
* Put your Mandelbulber2 configuration file on a network share (e.g. `\\share\renderers\Mandelbulber\config\mandelbulber_*.ini`, you can find it after first local run of Mandelbulber2 in `C:\Users\<user>\mandelbulber\mandelbulber_*.ini`)
	* Make sure that `<rrLocalBin>rrCopy -oa "\\share\renderers\Mandelbulber\config\mandelbulber_<rrJobVersionMajor><rrJobVersionMinor>.ini"` line in submitters config files (*3D20_Mandelbulber_\*.cfg*) is pointing to the location of your config file

## Usage
* Automatic way
	* Drag & drop your **.fract** file on **rrSubmit_Mandelbulber_2_15.bat** launcher, this will set all of the previous settings
	* Change Mandelbulber version if needed
	* Change your Renderer to **Keyframe / Flight / Static** if needed
	* Set **Sequence Start, End range**
* Manual way
	* Load **.fract** settings file
	* Set *Software* to Mandelbulber
	* Set Mandelbulber version as needed
	* Set *Renderer* to **Flight / Keyframe / Static**
	* Set **Sequence Start, End range** - starting from zero (and subtract one from End range)
	* Set **Image Dir**
		* Animation - set it to the same value as in Mandelbulber, Mandelbulber ignores this setting, it is only for RR to check if frames exist
			* Default value is set to **<SceneFolder>\<Scene>_render\**
			* If you follow this convention for setting output path in Mandelbulber, then you don't need to change it
			* .g. if your **.fract** file is in this location: `\\path\to\scene\my_scene.fract` , then Image Dir will expand to `\\path\to\scene\my_scene_render\`
		* Static frame - Mandelbulber will render into the specified path
			* Set **Image Dir, FileName** to arbitrary path, check **Single output file (.avi, .mov)**, include extension in FileName
			* Set **Sequence Start, End range** to zero
	* Set **FileName** to **frame_#######**
		* This value seems to be hardcoded somewhere in Mandelbulber
	* Set **Ext**:
		* **jpg** - JPEG format (default)
		* **png** - PNG format
		* **png16** - 16-bit PNG format
		* **png16alpha** - 16-bit PNG with alpha channel format
		* **exr** - EXR format
		* **tiff** - TIFF format
	* Enable **Sequence Divide**, and set it from 10 to 30 for example
	* Set **Company Project**

## Notes
* Animation
	* Rendering of the last frame (in batch of 1 frame) doesn't work, it works fine if the last frame is in a larger batch
* *test* folder with xml files is not needed currently, but might be useful for testing later on

## Todo
* Do a Python scene parser for Mandelbulber2 `*.fract` files which will fill in correct settings in **rrSubmitter**