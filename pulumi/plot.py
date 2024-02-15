DATA = {
    "digitalocean": {
        "version": "v2024-01-01",
        "time": "20240215-113315",
        "os": {
            "arch": "x64",
            "distro": "Ubuntu 22.04.2 LTS",
            "kernel": "5.15.0-67-generic",
            "uptime": 40.76,
            "vm": "KVM",
        },
        "net": {"ipv4": True, "ipv6": False},
        "cpu": {
            "model": "DO-Regular",
            "cores": 2,
            "freq": "2294.608 MHz",
            "aes": True,
            "virt": True,
        },
        "mem": {
            "ram": 4018124,
            "ram_units": "KiB",
            "swap": 0,
            "swap_units": "KiB",
            "disk": 81213726,
            "disk_units": "KB",
        },
        "ip_info": {
            "protocol": "IPv4",
            "isp": "DigitalOcean, LLC",
            "asn": "AS14061 DigitalOcean, LLC",
            "org": "DigitalOcean, LLC",
            "city": "Santa Clara",
            "region": "California",
            "region_code": "CA",
            "country": "United States",
        },
        "partition": "/dev/vda1",
        "fio": [
            {
                "bs": "4k",
                "speed_r": 91044,
                "iops_r": 22761,
                "speed_w": 91284,
                "iops_w": 22821,
                "speed_rw": 182328,
                "iops_rw": 45582,
                "speed_units": "KBps",
            },
            {
                "bs": "64k",
                "speed_r": 704733,
                "iops_r": 11011,
                "speed_w": 708442,
                "iops_w": 11069,
                "speed_rw": 1413175,
                "iops_rw": 22080,
                "speed_units": "KBps",
            },
            {
                "bs": "512k",
                "speed_r": 495844,
                "iops_r": 968,
                "speed_w": 522190,
                "iops_w": 1019,
                "speed_rw": 1018034,
                "iops_rw": 1987,
                "speed_units": "KBps",
            },
            {
                "bs": "1m",
                "speed_r": 740177,
                "iops_r": 722,
                "speed_w": 789473,
                "iops_w": 770,
                "speed_rw": 1529650,
                "iops_rw": 1492,
                "speed_units": "KBps",
            },
        ],
        "iperf": [
            {
                "mode": "IPv4",
                "provider": "Clouvider",
                "loc": "London, UK (10G)",
                "send": "866 Mbits/sec",
                "recv": "1.28 Gbits/sec",
                "latency": "138 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Scaleway",
                "loc": "Paris, FR (10G)",
                "send": "busy ",
                "recv": "busy ",
                "latency": "150 ms",
            },
            {
                "mode": "IPv4",
                "provider": "NovoServe",
                "loc": "North Holland, NL (40G)",
                "send": "1.15 Gbits/sec",
                "recv": "1.21 Gbits/sec",
                "latency": "144 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Uztelecom",
                "loc": "Tashkent, UZ (10G)",
                "send": "622 Mbits/sec",
                "recv": "712 Mbits/sec",
                "latency": "237 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Clouvider",
                "loc": "NYC, NY, US (10G)",
                "send": "1.85 Gbits/sec",
                "recv": "2.65 Gbits/sec",
                "latency": "70.5 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Clouvider",
                "loc": "Dallas, TX, US (10G)",
                "send": "1.66 Gbits/sec",
                "recv": "4.70 Gbits/sec",
                "latency": "39.7 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Clouvider",
                "loc": "Los Angeles, CA, US (10G)",
                "send": "2.00 Gbits/sec",
                "recv": "6.13 Gbits/sec",
                "latency": "8.82 ms",
            },
        ],
        "runtime": {"start": 1707996795, "end": 1707997093, "elapsed": 298},
    },
    "linode": {
        "version": "v2024-01-01",
        "time": "20240215-113324",
        "os": {
            "arch": "x64",
            "distro": "Ubuntu 22.04.3 LTS",
            "kernel": "5.15.0-91-generic",
            "uptime": 34.13,
            "vm": "KVM",
        },
        "net": {"ipv4": True, "ipv6": True},
        "cpu": {
            "model": "AMD EPYC 7713 64-Core Processor",
            "cores": 2,
            "freq": "1999.999 MHz",
            "aes": True,
            "virt": False,
        },
        "mem": {
            "ram": 4005896,
            "ram_units": "KiB",
            "swap": 524284,
            "swap_units": "KiB",
            "disk": 81970760,
            "disk_units": "KB",
        },
        "ip_info": {
            "protocol": "IPv6",
            "isp": "Akamai Technologies, Inc.",
            "asn": "AS63949 Akamai Connected Cloud",
            "org": "ACC Mia3",
            "city": "Miami",
            "region": "Florida",
            "region_code": "FL",
            "country": "United States",
        },
        "partition": "/dev/sda",
        "fio": [
            {
                "bs": "4k",
                "speed_r": 270732,
                "iops_r": 67683,
                "speed_w": 271447,
                "iops_w": 67861,
                "speed_rw": 542179,
                "iops_rw": 135544,
                "speed_units": "KBps",
            },
            {
                "bs": "64k",
                "speed_r": 3569365,
                "iops_r": 55771,
                "speed_w": 3588150,
                "iops_w": 56064,
                "speed_rw": 7157515,
                "iops_rw": 111835,
                "speed_units": "KBps",
            },
            {
                "bs": "512k",
                "speed_r": 8960000,
                "iops_r": 17500,
                "speed_w": 9436070,
                "iops_w": 18429,
                "speed_rw": 18396070,
                "iops_rw": 35929,
                "speed_units": "KBps",
            },
            {
                "bs": "1m",
                "speed_r": 9060571,
                "iops_r": 8848,
                "speed_w": 9664000,
                "iops_w": 9437,
                "speed_rw": 18724571,
                "iops_rw": 18285,
                "speed_units": "KBps",
            },
        ],
        "iperf": [
            {
                "mode": "IPv4",
                "provider": "Clouvider",
                "loc": "London, UK (10G)",
                "send": "1.39 Gbits/sec",
                "recv": "busy ",
                "latency": "102 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Scaleway",
                "loc": "Paris, FR (10G)",
                "send": "2.25 Gbits/sec",
                "recv": "1.80 Gbits/sec",
                "latency": "103 ms",
            },
            {
                "mode": "IPv4",
                "provider": "NovoServe",
                "loc": "North Holland, NL (40G)",
                "send": "1.43 Gbits/sec",
                "recv": "1.59 Gbits/sec",
                "latency": "114 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Uztelecom",
                "loc": "Tashkent, UZ (10G)",
                "send": "594 Mbits/sec",
                "recv": "606 Mbits/sec",
                "latency": "203 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Clouvider",
                "loc": "NYC, NY, US (10G)",
                "send": "4.29 Gbits/sec",
                "recv": "6.06 Gbits/sec",
                "latency": "30.4 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Clouvider",
                "loc": "Dallas, TX, US (10G)",
                "send": "577 Mbits/sec",
                "recv": "6.14 Gbits/sec",
                "latency": "29.3 ms",
            },
            {
                "mode": "IPv4",
                "provider": "Clouvider",
                "loc": "Los Angeles, CA, US (10G)",
                "send": "2.24 Gbits/sec",
                "recv": "3.09 Gbits/sec",
                "latency": "62.3 ms",
            },
            {
                "mode": "IPv6",
                "provider": "Clouvider",
                "loc": "London, UK (10G)",
                "send": "1.58 Gbits/sec",
                "recv": "1.78 Gbits/sec",
                "latency": "105 ms",
            },
            {
                "mode": "IPv6",
                "provider": "Scaleway",
                "loc": "Paris, FR (10G)",
                "send": "2.23 Gbits/sec",
                "recv": "busy ",
                "latency": "102 ms",
            },
            {
                "mode": "IPv6",
                "provider": "NovoServe",
                "loc": "North Holland, NL (40G)",
                "send": "1.46 Gbits/sec",
                "recv": "1.58 Gbits/sec",
                "latency": "114 ms",
            },
            {
                "mode": "IPv6",
                "provider": "Uztelecom",
                "loc": "Tashkent, UZ (10G)",
                "send": "584 Mbits/sec",
                "recv": "768 Mbits/sec",
                "latency": "202 ms",
            },
            {
                "mode": "IPv6",
                "provider": "Clouvider",
                "loc": "NYC, NY, US (10G)",
                "send": "3.88 Gbits/sec",
                "recv": "5.95 Gbits/sec",
                "latency": "30.3 ms",
            },
            {
                "mode": "IPv6",
                "provider": "Clouvider",
                "loc": "Dallas, TX, US (10G)",
                "send": "351 Mbits/sec",
                "recv": "6.35 Gbits/sec",
                "latency": "29.2 ms",
            },
            {
                "mode": "IPv6",
                "provider": "Clouvider",
                "loc": "Los Angeles, CA, US (10G)",
                "send": "2.25 Gbits/sec",
                "recv": "2.97 Gbits/sec",
                "latency": "62.2 ms",
            },
        ],
        "runtime": {"start": 1707996804, "end": 1707997207, "elapsed": 403},
    },
}


from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
from pint import UnitRegistry

ureg = UnitRegistry()
ureg.define("MBps = 1 * megabyte / second")
ureg.define("KBps = 1 * kilobyte / second")


def graph_fio(FIO_RESULTS):
    with plt.xkcd():
        fig, ax = plt.subplots()
        ax.set_title(f"FIO report")
        ax.set_xlabel("RW Speed [MBps]")
        y_values = np.arange(len(FIO_RESULTS))
        ax.set_yticks(y_values + 0.2)
        ax.set_yticklabels(FIO_RESULTS.keys())

        n = len(FIO_RESULTS)

        ax.barh(
            y_values - 0.2 * 2,
            [fio[0].magnitude for fio in FIO_RESULTS.values()],
            height=0.2,
            label="0",
        )
        ax.barh(
            y_values - 0.2 * 1,
            [fio[1].magnitude for fio in FIO_RESULTS.values()],
            height=0.2,
            label="1",
        )
        ax.barh(
            y_values + 0.2 * 0,
            [fio[2].magnitude for fio in FIO_RESULTS.values()],
            height=0.2,
            label="2",
        )
        ax.barh(
            y_values + 0.2 * 1,
            [fio[3].magnitude for fio in FIO_RESULTS.values()],
            height=0.2,
            label="3",
        )

        ax.grid(False, axis="x")
        legend = ax.legend()
        plt.tight_layout()

        plt.show()

        return fig, ax


def show_plots(DATA):
    FIO_RESULTS = OrderedDict()
    for contestant, data in DATA.items():
        fios = data["fio"]
        fios_rw = [
            ureg(f'{fio["speed_rw"]} {fio["speed_units"]}').to("MBps") for fio in fios
        ]
        FIO_RESULTS[contestant] = fios_rw
    fig, ax = graph_fio(FIO_RESULTS)
    return fig, ax
