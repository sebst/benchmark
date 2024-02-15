import io
import json
import time
import pulumi
import paramiko
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend


from providers.digitalocean import digitalocean_program
# from providers.hetzner import hetzner_program
# from providers.linode import linode_program


def ttt(provider, pulumi_program):
    workspace = pulumi.automation.LocalWorkspace()
    stack = pulumi.automation.create_or_select_stack(
        stack_name=f"benchmark-{provider}",
        project_name="pulumi-benchmark",
        program=pulumi_program,
        # workspace=workspace
    )
    stack.up()
    outputs = stack.outputs()
    # print(outputs)
    ip = outputs.get("ip").value
    ssh_key_private = outputs.get("ssh_key_private").value

    print(">>>>>>>", "stack up done. ")
    time.sleep(30)

    # Run /root/benchmark.sh via ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.RSAKey.from_private_key(io.StringIO(ssh_key_private))
    ssh.connect(ip, username="root", pkey=pkey)
    stdin, stdout, stderr = ssh.exec_command("bash /root/benchmark.sh")
    data = None
    for line in stdout:
        try:
            data = json.loads(line)
        except:
            print(line)
    stdin.close()
    ssh.close()

    print(f"{data=}")

    # print(ssh_key_private)

    print(">>>>>>>", "benchmark done. ")
    # time.sleep(1)

    stack.destroy()

    print(">>>>>>>", "stack destroy done. ")

    return data


def main():
    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )
    ttt("digitalocean", digitalocean_program(key))
    from threading import Thread

    threads = [
        Thread(target=ttt, args=("digitalocean", digitalocean_program(key))),
        # Thread(target=ttt, args=("hetzner", hetzner_program(key))),
        # Thread(target=ttt, args=("linode", linode_program(key))),
    ]

    for thread in threads:
        thread.start()
        thread.join()



if __name__ == "__main__":
    main()