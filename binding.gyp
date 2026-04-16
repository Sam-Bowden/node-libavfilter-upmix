{
	"targets": [
		{
			"target_name": "upmix",
			"sources": ["src/upmix.cpp"],
			"dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")",
				"<!@(pkg-config --cflags-only-I libavfilter libavutil | sed 's/-I//g')"
			],
			"libraries": ["<!@(pkg-config --libs libavfilter libavutil)"],
			"cflags_cc!": ["-fno-exceptions"]
		}
	]
}
