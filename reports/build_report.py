import json
import os
from pathlib import Path
from statistics import mean as avg
from math import floor
from io import StringIO

from pint import UnitRegistry
from markdown_table_generator import Alignment, generate_markdown, table_from_string_list
import matplotlib.pyplot as plt
import numpy as np


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
SCRIPT_PATH = Path(SCRIPT_DIR)

ureg = UnitRegistry()


def main(report, report_name):

    REPORT_MARKDOWN = f"# {report_name} \n\n\n"

    report_config = json.load(open(SCRIPT_PATH / f"{report}.conf.json"))

    contestants = report_config["contestants"]

    GEEKBENCH_RESULTS = {}

    for contestant in contestants:
        # print(contestant["name"])

        REPORT_MARKDOWN += f"## {contestant['name']} \n\n"

        # print(contestant["file"])
        contestant_yabs = json.load(open(SCRIPT_PATH / '..' / 'benchmark-results' / contestant["file"]))
        # print(contestant_yabs["version"])
        vcpus = contestant_yabs["cpu"]["cores"]
        ram = (contestant_yabs["mem"]["ram"] * ureg(contestant_yabs["mem"]["ram_units"])).to("GB")
        ram = floor(ram.magnitude) * ureg("GB")
        print(f"vCPUs: {vcpus} RAM: {ram.to('GB')}")

        data = [
            ["", "vCPUs", "RAM", "shared", "IPv4", "IPv6"],
            [contestant["name"], str(vcpus), str(ram), ("✅" if contestant["vCPUshared"] else "❌"), ("✅" if contestant_yabs["net"]["ipv4"] else "❌"), ("✅" if contestant_yabs["net"]["ipv6"] else "❌")],
        ]
        # print(data)
        table = table_from_string_list(data, Alignment.CENTER)
        markdown = generate_markdown(table)
        REPORT_MARKDOWN += markdown + "\n\n"
        
        gb6 = contestant_yabs["geekbench"].pop()
        assert gb6["version"] == 6
        GEEKBENCH_RESULTS[contestant["name"]] = [gb6["single"], gb6["multi"]]
        


    local_hardware = report_config["localHardware"].pop()
    local_hardware_yabs = json.load(open(SCRIPT_PATH / '..' / 'benchmark-results' / local_hardware["file"]))
    gb6 = local_hardware_yabs["geekbench"].pop()
    assert gb6["version"] == 6
    GEEKBENCH_RESULTS[local_hardware["name"]] = [gb6["single"], gb6["multi"]]

    # make a bar plot with the results in GEEKBENCH_RESULTS, so that the key is on the left and the bars are horizontal
    # with plt.xkcd():
    #     fig, ax = plt.subplots()
    #     ax.set_title(f"Geekbench 6 results")
    #     ax.set_xlabel("Score")
    #     # ax.set_ylabel("Contestant")
    #     ax.set_yticks(np.arange(len(GEEKBENCH_RESULTS)))
    #     ax.set_yticklabels(GEEKBENCH_RESULTS.keys())
    #     # ax.set_xlim([0, 10000])
    #     # ax.set_xticks(np.arange(0, 10000, 1000))
    #     # ax.set_xticklabels(np.arange(0, 10000, 1000))
    #     # ax.barh(list(GEEKBENCH_RESULTS.keys()), [GEEKBENCH_RESULTS[k][0] for k in GEEKBENCH_RESULTS.keys()], label="Single-Core")
    #     # ax.barh(list(GEEKBENCH_RESULTS.keys()), [GEEKBENCH_RESULTS[k][1] for k in GEEKBENCH_RESULTS.keys()], label="Multi-Core")
    #     single_core_scores = [GEEKBENCH_RESULTS[k][0] for k in GEEKBENCH_RESULTS.keys()]
    #     multi_core_scores = [GEEKBENCH_RESULTS[k][1] for k in GEEKBENCH_RESULTS.keys()]
    #     ax.barh(list(GEEKBENCH_RESULTS.keys()), single_core_scores, label="Single-Core")
    #     ax.barh(list(GEEKBENCH_RESULTS.keys()), multi_core_scores, left=single_core_scores, label="Multi-Core")
    #     ax.grid(True, axis="x")
    #     plt.tight_layout() 
    #     plt.show()
    single_core_scores = [GEEKBENCH_RESULTS[k][0] for k in GEEKBENCH_RESULTS.keys()]
    multi_core_scores = [GEEKBENCH_RESULTS[k][1] for k in GEEKBENCH_RESULTS.keys()]
    with plt.xkcd():
        fig, ax = plt.subplots()
        ax.set_title(f"Geekbench 6 results")
        ax.set_xlabel("Score")
        y_values = np.arange(len(GEEKBENCH_RESULTS))
        ax.set_yticks(y_values + 0.2)  # Adjust y-ticks to be in the middle of the bars
        ax.set_yticklabels(GEEKBENCH_RESULTS.keys())
        ax.barh(y_values - 0.2, single_core_scores, height=0.4, label="Single-Core")  # Adjust y-values and set height
        ax.barh(y_values + 0.2, multi_core_scores, height=0.4, label="Multi-Core")  # Adjust y-values and set height
        ax.grid(False, axis="x")
        ax.legend()
        plt.tight_layout() 
        plt.show()

        # save plt to svg string:
        svg = StringIO()
        fig.savefig(svg, format="svg")
        svg.seek(0)
        REPORT_MARKDOWN += f"## Geekbench 6 results for {report_name} \n\n"
        REPORT_MARKDOWN += svg.read() + "\n\n"
        print(svg)
        del svg


    # print( REPORT_MARKDOWN)
    with open(f"{report}.report.md", "w") as f:
        f.write(REPORT_MARKDOWN)


if __name__ == "__main__":
    REPORT = "2023-12-07"
    REPORT_NAME = "December 2023"
    main(REPORT, REPORT_NAME)




# speeds = [ureg("1.0 GiB/s").to("MB/s"), ureg("2 GiB/s").to("MB/s")]
# print(speeds)
# print(avg(speeds))
