# Mandelbulber2 RoyalRender submitter

## Setup
* Copy contents of **render_apps** folder into RR installation directory.
* Copy `3D20__Mandelbulber.py` from **submitter_sceneparser** into `plugins64\submitter_sceneparser` inside of RR directory
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
	* Open your **.fract** file with **rrSubmitter**, this will automatically set your render output path, renderer, version, frame range, etc.
		* Or alternatively you can drag & drop your **.fract** file on **rrSubmit_Mandelbulber_2_15.bat** launcher
* Manual way *(all those steps are now automated with RR scene parser for Mandelbulber2 files, but I keep it for reference)*
	* Load **.fract** settings file
	* Set *Software* to Mandelbulber
	* Set Mandelbulber version as needed
	* Set *Renderer* to **Flight / Keyframe / Static**
	* Set **Sequence Start, End range** - starting from zero
	* Set **Image Dir**
		* Animation - set it to the same value as in Mandelbulber, Mandelbulber ignores this setting, it is only for RR to check if frames exist
			* For example you can set it to `<SceneFolder>\<Scene>_render`
			* If you follow this convention for setting output path in Mandelbulber, then you don't need to change it
			* e.g. if your **.fract** file is in this location: `\\path\to\scene\my_scene.fract` , then Image Dir will expand to `\\path\to\scene\my_scene_render\`
		* Static frame - Mandelbulber will render into the specified path
			* Set **Image Dir, FileName** to arbitrary path, check **Single output file (.avi, .mov)**, include extension in FileName
			* Set **Sequence Start, End range** to zero
	* Set **FileName** to **frame_#######**
		* This value seems to be hardcoded somewhere in Mandelbulber
	* Set **Ext** (based on your Mandelbulber2 global config file):
		* **jpg** - JPEG format (default)
		* **png** - PNG format
		* **png16** - 16-bit PNG format
		* **png16alpha** - 16-bit PNG with alpha channel format
		* **exr** - EXR format
		* **tiff** - TIFF format

## Notes
* Animation
	* Rendering of the last frame (in batch of 1 frame) doesn't work, it works fine if the last frame is in a larger batch
* Scene parser
	* Seqence start is assumed to be 0
	* If both Keyframe and Flight output directories are set, Keyframe (directory and renderer) is used
* Output format is set globally in Mandelbulber2 configuration file. Keys in the config are `flight_animation_image_type`, `keyframe_animation_image_type` and `queue_image_format`