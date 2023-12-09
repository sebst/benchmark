import json
import os
from pathlib import Path
from statistics import mean as avg
from math import floor
from io import StringIO
from collections import OrderedDict
from textwrap import dedent

from pint import UnitRegistry
from markdown_table_generator import Alignment, generate_markdown, table_from_string_list
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
SCRIPT_PATH = Path(SCRIPT_DIR)

ureg = UnitRegistry()
ℝ = ureg
ureg.define("MBps = 1 * megabyte / second")
ureg.define("KBps = 1 * kilobyte / second")
ureg.define("workmonth = 160 * hour")
ureg.define("workweek = 40 * hour")
ureg.define("workfortnight = 2 * workweek")
ureg.define("workyear = 12 * workmonth")
ureg.define("EUR = [currency]")
ureg.define("USD = [currency]")


mallory_ultra = FontProperties()
mallory_ultra.set_family('serif')
mallory_ultra.set_name('Mallory')
mallory_ultra.set_style('normal')


def try_ureg(value, unit=None):
    # print(value, unit)
    # return 12
    if unit is not None:
        to_parse = f"{value} {unit}"
    else:
        to_parse = value
    try:

        r = ℝ(to_parse)
    except:
        r = ℝ("1 ms")
    print(value, unit, r)
    return r


def fig_to_svg(fig):
    svg = StringIO()
    fig.savefig(svg, format="svg")
    svg.seek(0)
    return ""
    return svg.read()


def graph_ci(report_config, fig, ax, legend):
    # Change the font color
    ax.tick_params(colors=report_config["globals"]["colors"][0])
    for label in ax.get_xticklabels():
        label.set_color(report_config["globals"]["colors"][0])
    for label in ax.get_yticklabels():
        label.set_color(report_config["globals"]["colors"][0])
    for text in legend.get_texts():
        text.set_color(report_config["globals"]["colors"][0])
    ax.spines['bottom'].set_color(report_config["globals"]["colors"][0])
    ax.spines['top'].set_color(report_config["globals"]["colors"][0]) 
    ax.spines['right'].set_color(report_config["globals"]["colors"][0])
    ax.spines['left'].set_color(report_config["globals"]["colors"][0])

    # Watermark
    # ax.text(0.5, 0.5, report_config["globals"]["watermark"], fontsize=40, color='gray', ha='center', va='center', alpha=0.1)
    fig.text(0.2, 0.1, report_config["globals"]["watermark"], fontsize=20, color='gray', ha='center', va='center', alpha=0.2, fontproperties=mallory_ultra)
    return fig, ax


def graph_geekbench(report_config, GEEKBENCH_RESULTS):
    single_core_scores = [GEEKBENCH_RESULTS[k][0] for k in GEEKBENCH_RESULTS.keys()]
    multi_core_scores = [GEEKBENCH_RESULTS[k][1] for k in GEEKBENCH_RESULTS.keys()]
    with plt.xkcd():
        fig, ax = plt.subplots()
        ax.set_title(f"Geekbench 6 Scores", color=report_config["globals"]["colors"][0])
        ax.set_xlabel("Score", color=report_config["globals"]["colors"][0])
        y_values = np.arange(len(GEEKBENCH_RESULTS))
        ax.set_yticks(y_values + 0.2)  # Adjust y-ticks to be in the middle of the bars
        ax.set_yticklabels(GEEKBENCH_RESULTS.keys())
        ax.barh(y_values - 0.2, single_core_scores, height=0.4, label="single core", color=report_config["globals"]["colors"][0])  # Adjust y-values and set height
        ax.barh(y_values + 0.2, multi_core_scores, height=0.4, label="multi core", color=report_config["globals"]["colors"][1])  # Adjust y-values and set height
        ax.grid(False, axis="x")
        # ax.grid(True, axis="y", color=report_config["globals"]["colors"][0])
        legend = ax.legend()
        plt.tight_layout() 

        fig, ax = graph_ci(report_config, fig, ax, legend)


        return fig, ax


def graph_fio(report_config, FIO_RESULTS):
    with plt.xkcd():
        fig, ax = plt.subplots()
        ax.set_title(f"FIO report", color=report_config["globals"]["colors"][0])
        ax.set_xlabel("RW Speed [MBps]", color=report_config["globals"]["colors"][0])
        y_values = np.arange(len(FIO_RESULTS))
        ax.set_yticks(y_values + 0.2)
        ax.set_yticklabels(FIO_RESULTS.keys())
        # 1 = 1   - 0*0.2
        # 2 = 0.5 - 1*0.1
        # 3 = 1/3 - 2*0.1

        n = len(FIO_RESULTS)

        ax.barh(y_values - 0.2*2, [fio[0].magnitude for fio in FIO_RESULTS.values()], height=0.2, label="0", color=report_config["globals"]["colors"][0])
        ax.barh(y_values - 0.2*1, [fio[1].magnitude for fio in FIO_RESULTS.values()], height=0.2, label="1", color=report_config["globals"]["colors"][1])
        ax.barh(y_values + 0.2*0, [fio[2].magnitude for fio in FIO_RESULTS.values()], height=0.2, label="2", color="green")
        ax.barh(y_values + 0.2*1, [fio[3].magnitude for fio in FIO_RESULTS.values()], height=0.2, label="3", color="yellow")
        
        ax.grid(False, axis="x")
        # ax.grid(True, axis="y", color=report_config["globals"]["colors"][0])
        legend = ax.legend()
        plt.tight_layout()

        fig, ax = graph_ci(report_config, fig, ax, legend)


        # plt.show()

        return fig, ax


def graph_pricing(report_config, PRICING_RESULTS):
    with plt.xkcd():
        price_display_unit = "USD / workfortnight"
        fig, ax = plt.subplots()
        ax.set_title(f"Pricing report", color=report_config["globals"]["colors"][0])
        ax.set_xlabel(f"Price [{price_display_unit}]", color=report_config["globals"]["colors"][0])
        y_values = np.arange(len(PRICING_RESULTS))
        ax.set_yticks(y_values)
        ax.set_yticklabels(PRICING_RESULTS.keys())
        bars = ax.barh(y_values, [price.to(price_display_unit).magnitude for price in PRICING_RESULTS.values()], height=0.4, color=report_config["globals"]["colors"][0])
        for i, bar in enumerate(bars):
            width = bar.get_width()
            t1 = [f'$ {price.to("USD / hour").magnitude:.4f} / hr' for price in PRICING_RESULTS.values()][i]
            t2 = [f'$ {price.to("USD / workmonth").magnitude:.2f} / workmonth' for price in PRICING_RESULTS.values()][i]
            ax.text(width + 0.1, 
                    bar.get_y() + bar.get_height() / 2, 
                    f'{t1}\n{t2}', 
                    ha = 'left', 
                    va = 'center',
                    color = report_config["globals"]["colors"][0],
                    fontsize=6)
        ax.grid(False, axis="x")
        legend = ax.legend()
        plt.tight_layout()

        fig, ax = graph_ci(report_config, fig, ax, legend)

        # plt.show()

        return fig, ax


def graph_network_latency(report_config, NETWORK_LATENCY_RESULTS):
    single_core_scores = [NETWORK_LATENCY_RESULTS[k][0] for k in NETWORK_LATENCY_RESULTS.keys()]
    multi_core_scores = [NETWORK_LATENCY_RESULTS[k][1] for k in NETWORK_LATENCY_RESULTS.keys()]
    with plt.xkcd():
        fig, ax = plt.subplots()
        ax.set_title(f"Network Latency", color=report_config["globals"]["colors"][0])
        ax.set_xlabel("Score", color=report_config["globals"]["colors"][0])
        y_values = np.arange(len(NETWORK_LATENCY_RESULTS))
        ax.set_yticks(y_values + 0.2)  # Adjust y-ticks to be in the middle of the bars
        ax.set_yticklabels(NETWORK_LATENCY_RESULTS.keys())
        ax.barh(y_values - 0.2, single_core_scores, height=0.4, label="single core", color=report_config["globals"]["colors"][0])  # Adjust y-values and set height
        ax.barh(y_values + 0.2, multi_core_scores, height=0.4, label="multi core", color=report_config["globals"]["colors"][1])  # Adjust y-values and set height
        ax.grid(False, axis="x")
        # ax.grid(True, axis="y", color=report_config["globals"]["colors"][0])
        legend = ax.legend()
        plt.tight_layout() 

        fig, ax = graph_ci(report_config, fig, ax, legend)

        plt.show()
        return fig, ax


def main(report):
    report_config = json.load(open(SCRIPT_PATH / f"{report}.conf.json"))
    # ureg.define("€ = [currency]")
    # ureg.define("$ = [currency]")
    # ureg.define("USD = 1 * $")
    # ureg.define("EUR = 1 * €")
    for currency, exchange_rate in report_config["globals"]["currencies"].items():
        ureg.define(f"{currency} = {exchange_rate}")
    report_name = report_config["globals"]["name"]

    REPORT_MARKDOWN = f"# {report_name} \n\n\n"

    contestants = report_config["contestants"]

    GEEKBENCH_RESULTS = OrderedDict()
    FIO_RESULTS = OrderedDict()
    IPERF_RESULTS = OrderedDict()
    PRICING_RESULTS = OrderedDict()
    ALL_DATA = list()

    for contestant in contestants:
        REPORT_MARKDOWN += f"## {contestant['name']} \n\n"

        contestant_yabs = json.load(open(SCRIPT_PATH / '..' / 'benchmark-results' / contestant["file"]))
        vcpus = contestant_yabs["cpu"]["cores"]
        ram = (contestant_yabs["mem"]["ram"] * ℝ(contestant_yabs["mem"]["ram_units"])).to("GB")
        ram = floor(ram.magnitude) * ℝ("GB")

        data = [
            ["", "vCPUs", "RAM (GB)", "shared", "IPv4", "IPv6"],
            [contestant["name"], str(vcpus), str(ram.magnitude), ("✅" if contestant["vCPUshared"] else "❌"), ("✅" if contestant_yabs["net"]["ipv4"] else "❌"), ("✅" if contestant_yabs["net"]["ipv6"] else "❌")],
        ]
        if len(ALL_DATA) == 0:
            ALL_DATA.append(data[0])
        ALL_DATA.append(data[1])
        table = table_from_string_list(data, Alignment.CENTER)
        markdown = generate_markdown(table) #.replace("✅ ", "✅").replace("❌ ", "❌")
        REPORT_MARKDOWN += markdown + "\n\n"

        data = [
            ["", "Value"],
            ["CPU Model", contestant_yabs["cpu"]["model"]],
            ["CPU Frequency", f"{contestant_yabs['cpu']['freq']}"],
            ["ASN", contestant_yabs["ip_info"]["asn"]],
            ["OS", contestant_yabs["os"]["distro"]],
            ["Kernel", contestant_yabs["os"]["kernel"]],
            ["HyperVisor", contestant_yabs["os"]["vm"]],
            ["Time", contestant_yabs["time"]],
            ["Geekbench Score", f'[Single: {contestant_yabs["geekbench"][0]["single"]}<br />Multi: {contestant_yabs["geekbench"][0]["multi"]}]({contestant_yabs["geekbench"][0]["url"]})'],
            ["Price per hour", f'{ℝ(contestant["price"]).to("USD / hour").magnitude}'],
            ["Price per work-month", f'{ℝ(contestant["price"]).to("USD / workmonth").magnitude}'],
            ["Price per month", f'{ℝ(contestant["price"]).to("USD / month").magnitude}'],
        ]
        table = table_from_string_list(data, Alignment.LEFT)
        markdown = generate_markdown(table)
        REPORT_MARKDOWN += markdown + "\n\n"

        
        gb6 = contestant_yabs["geekbench"].pop()
        assert gb6["version"] == 6
        GEEKBENCH_RESULTS[contestant["name"]] = [gb6["single"], gb6["multi"]]
        
        fios = contestant_yabs["fio"]
        block_sizes = [fio["bs"] for fio in fios]
        fios_rw = [ℝ(f'{fio["speed_rw"]} {fio["speed_units"]}').to("MBps") for fio in fios]
        FIO_RESULTS[contestant["name"]] = fios_rw

        PRICING_RESULTS[contestant["name"]] = ℝ(contestant["price"]).to("USD / month")

        network = contestant_yabs["iperf"]
        def iperf_latency(measurement):
            # return 1
            # return ureg("1 ms")
            try:
                return ℝ(f'{measurement["latency"]}').to("ms")
            except:
                return ℝ("nan ms")

        fios_latency = [iperf_latency(measurement) for measurement in network]
        fios_latency = [q.magnitude for q in fios_latency if q.units == ureg("ms")]
        IPERF_RESULTS[contestant["name"]] = fios_latency
        print(f"{IPERF_RESULTS=}")

        # break



    local_hardware = report_config["localHardware"].pop()
    local_hardware_yabs = json.load(open(SCRIPT_PATH / '..' / 'benchmark-results' / local_hardware["file"]))
    gb6 = local_hardware_yabs["geekbench"].pop()
    assert gb6["version"] == 6
    GEEKBENCH_RESULTS[local_hardware["name"]] = [gb6["single"], gb6["multi"]]
    # FIO_RESULTS[local_hardware["name"]] = [ℝ(f'{fio["speed_rw"]} {fio["speed_units"]}').to("MBps") for fio in local_hardware_yabs["fio"]]
    PRICING_RESULTS[local_hardware["name"]] = ℝ(local_hardware["price"]).to("USD / month")
    # PRICING_RESULTS.move_to_end(local_hardware["name"], last=False)


    fig, ax = graph_geekbench(report_config, GEEKBENCH_RESULTS)
    REPORT_MARKDOWN += f"## Geekbench 6 results for {report_name} \n\n"
    REPORT_MARKDOWN += fig_to_svg(fig) + "\n\n"


    fig, ax = graph_fio(report_config, FIO_RESULTS)
    REPORT_MARKDOWN += f"## Disk speed results for {report_name} \n\n"
    REPORT_MARKDOWN += fig_to_svg(fig) + "\n\n"


    fig, ax = graph_pricing(report_config, PRICING_RESULTS)
    REPORT_MARKDOWN += f"## Pricing results for {report_name} \n\n"
    REPORT_MARKDOWN += fig_to_svg(fig) + "\n\n"


    fig, ax = graph_network_latency(report_config, IPERF_RESULTS)


    table = table_from_string_list(ALL_DATA, Alignment.CENTER)
    markdown = generate_markdown(table) #.replace("✅ ", "✅").replace("❌ ", "❌")
    REPORT_MARKDOWN += markdown + "\n\n"

    asof = report_config["globals"]["asof"]
    exchange_rate = f"1 EUR = {ℝ('1 EUR').to('USD'):.4f}"
    notes_on_prices = f"""
    Pricing is approximate based on the hourly rates published by the providers. The displayed prices are without VAT, do not include promotions, saving plans or other non-standard deductions, as of {asof} and denominated in US-Dollar based on an exchange rate of {exchange_rate} at the time of writing.
    """
    REPORT_MARKDOWN += dedent(notes_on_prices) + "\n\n"

    with open(f"{report}.report.md", "w") as f:
        f.write(REPORT_MARKDOWN)


if __name__ == "__main__":
    REPORT = "2023-12-07"
    main(REPORT)
