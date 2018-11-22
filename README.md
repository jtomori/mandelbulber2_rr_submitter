# Mandelbulber2 RoyalRender submitter

## Setup
* Copy contents of **render_apps** folder into RR installation directory.
* Put Mandelbulber2 standalone version on a network share
	* Set **ExeCopyFromDir** in *render_apps/_config/3D20__Mandelbulber__inhouse.inc* to that location
* Put your Mandelbulber2 configuration file on a network share
	* Set **\<rrLocalBin\>rrCopy -oa** source path to that location (first path is source, the second one is destination)
	* RR copies this settings file before each render to local render user directory, where it is picked up by Mandelbulber2

## Usage
* Automatic way
	* Drag & drop your **.fract** file on **rrSubmit_Mandelbulber_2_15.bat** launcher, this will set all of the previous settings
	* Change your Renderer to **Keyframe / Flight / Static** if needed
	* Set **Sequence Start, End range**
* Manual way
	* Load **.fract** settings file
	* Set *Software* to Mandelbulber
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
* In order for version selection to work properly in RR, remove any additional numbers from paths, because they confuse RR
	* for example path like this:
	```
	\\smaug\Shader\Mandelbulber2\mandelbulber_2.15\mandelbulber2.exe
	```
	needs to be converted into this:
	```
	\\smaug\Shader\Mandelbulber\mandelbulber_2.15\mandelbulber.exe
	```
* Animation
	* Rendering of the last frame (when batch of 1) doesn't work, it works fine if the last frame is in larger batch