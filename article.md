

In this article, we will use Pulumi to set up virtual computers in the cloud and compare their performance.

By the end of the article, you will know
* how to create multiple cloud instances with the Pulumi Automation API with Python
* how to use cloud-init to provision those instances
* how to use yabs.sh to create reproducible benchmarks and extract performance data
* how to plot the data using matplotlib and Python

Ever wondered whcih cloud provider gives you the best bang for the buck when it comes to virtual machines? You've probably seen my December 2023 benchmark with some unexpected results, especially in the lower bracket of machine prices. 
In this benchmark, Linode, and Hetzner stood out with a great performance for low prices.

You may want to conduct your own benchmark on the cloud providers of your choice. Here's how to do that with Pulumi

### What is Pulumi

Pulumi is a infrastructure as code (IaC) tool that enables developers to manage cloud resources using familiar programming languages such as Python, JavaScript, TypeScript, and Go. Unlike traditional IaC tools, such like Terraform, Pulumi uses programming languages instead of static configuration files to manage infrastructure across multiple cloud providers. 

For a quick start, you can use Pulumi locally – without their cloud offering.

### Getting started

#### Provisioning using cloud-init
#### A Pulumi Program for each provider

### Collecting The Results

### Plotting The Results

### Putting it all together