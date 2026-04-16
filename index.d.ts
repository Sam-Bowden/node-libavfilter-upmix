export interface UpmixOptions {
	sampleRate: number
	bitDepth: 16 | 32
	inputLayout: string
	outputLayout: 'stereo' | '5.1' | '7.1'
	winSize: number
}

export declare class Upmix {
	constructor(options: UpmixOptions)
	process(input: Buffer): Buffer

	close(): void
	reset(): void
}
