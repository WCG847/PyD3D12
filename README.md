# PyD3D12 Module for Python
________________________________________________________
## Overview
This module provides a 1-1 binding of Direct3D12 to Python, with a similar experience as C++ bindings. It is designed to be used with the Python programming language and provides a raw interface for working with Direct3D12.

## Installation
To install the PyD3D12 module, you can use pip:

```bash
pip install PyD3D12
```

## Required Architecture
The PyD3D12 module requires a 64-bit architecture to function properly. It is not compatible with 32-bit systems.
OS = Windows 10 or later
Python = 3.8 or later

## Recommended Components
- GPU: NVIDIA GeForce RTX 20 series or later, AMD Radeon RX 5000 series or later, or Intel Iris Xe Graphics or later.
- DirectX: DirectX 12 or later.
- CPU: Intel Core i5 or AMD Ryzen 5 or better.
- RAM: 8 GB or more.
- Storage: SSD with at least 1 GB of free space.
- Graphics Driver: Latest graphics driver from the GPU manufacturer (NVIDIA, AMD, or Intel).

## No Abstractions!
This module provides a raw interface to Direct3D12, meaning that it does not provide any abstractions or higher-level functionality. It is designed to be used by developers who are familiar with Direct3D12 and want to work with it directly in Python.
## Usage
To use the PyD3D12 module, you can import it in your Python code:

```python
import PyD3D12
# Example usage
device = PyD3D12.D3D12CreateDevice()
# Create a command queue
command_queue = device.CreateCommandQueue(PyD3D12.D3D12_COMMAND_LIST_TYPE_DIRECT)
# Create a command allocator
command_allocator = device.CreateCommandAllocator(PyD3D12.D3D12_COMMAND_LIST_TYPE_DIRECT)
# Create a command list
command_list = device.CreateCommandList(0, PyD3D12.D3D12_COMMAND_LIST_TYPE_DIRECT, command_allocator, None)
# Close the command list
command_list.Close()
```
It is best to alias the module as `dx` for convenience:

```python
import PyD3D12 as dx
```
If there are conflicting Direct3D bindings, use `dx12` but it's best to deprecate older versions for consistency.

https://pypi.org/project/PyD3D12/

⭐ If you find this project useful, consider giving it a star to support development
