import argparse

def parameter_parser():
    parser = argparse.ArgumentParser(description = "A basic images to gif format converter script. "\
                                                   "Supported file formats are JPEG and PNG.")

    parser.add_argument("--input-path",
                        nargs = "?",
                        default = "./photos/",
	                help = "Input folder with files. Given files should be ordered by their names for correct "\
                           "ordering while creating the output file. default = ./photos/")

    parser.add_argument("--output-path",
                        nargs = "?",
                        default = "./best_gif_ever",
	                help = "Output for gif file without gif extension. default = ./best_gif_ever")

    parser.add_argument("--duration",
                        type=float,
                        nargs = "?",
                        default = 0.5,
	                help = "Duration for each frame in seconds. default = 0.5")

    parser.add_argument("--height",
                        type=int,
                        nargs = "?",
                        default = 800,
	                help = "Height for the output gif. default = 800")

    return parser.parse_args()
