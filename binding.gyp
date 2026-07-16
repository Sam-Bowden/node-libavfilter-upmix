{
	"targets": [
		{
			"target_name": "upmix",
			"sources": ["src/upmix.cpp"],
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")",
				"<!@(node -e \"process.stdout.write(process.env.FFMPEG_INCLUDE_DIR || '')\")"
			],
			"library_dirs": [
				"<!@(node -e \"process.stdout.write(process.env.FFMPEG_LIB_DIR || '')\")"
			],
			"libraries": ["-lavfilter", "-lavutil", "-lswresample"],
			"ldflags": [
				"<!@(node -e \"const d=process.env.FFMPEG_LIB_DIR; process.stdout.write(d ? '-Wl,-rpath,'+d : '')\")"
			],
			"cflags_cc!": ["-fno-exceptions"]
		}
	]
}
