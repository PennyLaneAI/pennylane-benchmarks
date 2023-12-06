from mdutils.mdutils import MdUtils

import argparse
########################################################################
# Parsing arguments
########################################################################
def parse_args():
    """Parse external arguments provided to the script."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--last_updated",
        type=str,
        help="Last time updates",
    )

    parser.add_argument(
        "--pl_commit",
        type=str,
        help="Head commit for the PennyLane benchmarked branch.",
    )

    parser.add_argument(
        "--pl_ref_commit",
        type=str,
        help="Head commit for the PennyLane reference branch.",
    )

    return parser.parse_args()

if __name__ == "__main__":
    parsed_args = parse_args()

    mdFile = MdUtils(file_name='README',
                    title='pennylane-benchmarks')

    mdFile.new_line("Performs periodic benchmark runs on PennyLane.")
    mdFile.new_line("Last updated: "+parsed_args.last_updated)
    mdFile.write('  \n')

    mdFile.new_header(level=1, title="PennyLane Benchmarks")

    base_link = "https://github.com/PennyLaneAI/pennylane/commit/"
    mdFile.new_line("Benchmark reference head commit: "+ mdFile.new_inline_link(base_link+parsed_args.pl_ref_commit, parsed_args.pl_ref_commit[0:7]))
    mdFile.new_line("Benchmark head commit: "+ mdFile.new_inline_link(base_link+parsed_args.pl_commit, parsed_args.pl_commit[0:7]))
    mdFile.write('  \n')

    # Adding plots to the markdown file.
    bm_name_list = ["device-tests-default.mixed-None-3.9",
                    "device-tests-default.qubit.autograd-None-3.9",
                    "device-tests-default.qubit.legacy-10000-3.9",
                    "device-tests-default.qubit.legacy-None-3.9",
                    "jax-tests-1-3.9"]

    for bm_name in bm_name_list:
        mdFile.new_line(mdFile.new_inline_image(text=bm_name+"-benchmarks", path="pennylane_benchmarks/"+bm_name+"-benchmarks/"+bm_name+".png"))
        mdFile.write('  \n')

    mdFile.create_md_file()