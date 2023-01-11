import os

import pandas as pd


input_path = 'C:/Users/mcca512/OneDrive - PNNL/McCann Documents/MMD Adult Study/mmd_sum_2022/data/parquet_raw_data'




df = pd.read_parquet(os.path.join(input_path, '1_MITAS_20220626_20220627.parquet'), engine = 'pyarrow')


def whitespace_to_csv(input_file: str,
                      output_dir: str) -> str:
    """Generate new output files with whitespace converted to CSV."""

    # extract basename from input file
    basename = os.path.splitext(os.path.basename(input_file))[0]

    # construct output file name
    output_file = os.path.join(output_dir, f"{basename}.csv")

    # open file to write
    with open(output_file, "w") as out:
        # read input file as string
        with open(input_file) as get:
            content = get.read()

        # write content replacing any whitespace with commas but keeping new lines or carriage returns
        out.write(re.sub("[^\S^\r\n]+", ",", content))

    return output_file