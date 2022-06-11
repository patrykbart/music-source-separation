from spleeter.separator import Separator


def main(input_path, output_path, num_tracks=2):

    Separator(f"spleeter:{num_tracks}stems").separate_to_file(input_path, output_path)


if __name__ == "__main__":
    main(input_path="input/audio_example.mp3", output_path="output/")
