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


def fig_to_svg(fig):
    svg = StringIO()
    fig.savefig(svg, format="svg")
    svg.seek(0)
    return svg.read()


def main(report, report_name):

    REPORT_MARKDOWN = f"# {report_name} \n\n\n"

    report_config = json.load(open(SCRIPT_PATH / f"{report}.conf.json"))

    contestants = report_config["contestants"]

    GEEKBENCH_RESULTS = {}

    for contestant in contestants:
        REPORT_MARKDOWN += f"## {contestant['name']} \n\n"

        contestant_yabs = json.load(open(SCRIPT_PATH / '..' / 'benchmark-results' / contestant["file"]))
        vcpus = contestant_yabs["cpu"]["cores"]
        ram = (contestant_yabs["mem"]["ram"] * ureg(contestant_yabs["mem"]["ram_units"])).to("GB")
        ram = floor(ram.magnitude) * ureg("GB")

        data = [
            ["", "vCPUs", "RAM (GB)", "shared", "IPv4", "IPv6"],
            [contestant["name"], str(vcpus), str(ram.magnitude), ("✅" if contestant["vCPUshared"] else "❌"), ("✅" if contestant_yabs["net"]["ipv4"] else "❌"), ("✅" if contestant_yabs["net"]["ipv6"] else "❌")],
        ]
        table = table_from_string_list(data, Alignment.CENTER)
        markdown = generate_markdown(table) #.replace("✅ ", "✅").replace("❌ ", "❌")
        REPORT_MARKDOWN += markdown + "\n\n"

        data = [
            ["CPU Model", contestant_yabs["cpu"]["model"]],
            ["CPU Frequency", f"{contestant_yabs['cpu']['freq']}"],
            ["ASN", contestant_yabs["ip_info"]["asn"]],
            ["OS", contestant_yabs["os"]["distro"]],
            ["Kernel", contestant_yabs["os"]["kernel"]],
            ["HyperVisor", contestant_yabs["os"]["vm"]],
            ["Time", contestant_yabs["time"]],
        ]
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
        # plt.show()

        REPORT_MARKDOWN += f"## Geekbench 6 results for {report_name} \n\n"
        REPORT_MARKDOWN += fig_to_svg(fig) + "\n\n"

    with open(f"{report}.report.md", "w") as f:
        f.write(REPORT_MARKDOWN)


if __name__ == "__main__":
    REPORT = "2023-12-07"
    REPORT_NAME = "December 2023"
    main(REPORT, REPORT_NAME)
