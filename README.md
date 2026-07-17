# Modena Common
Common Python utilities shared across Modena ROS 2 packages.

## Features
Currently includes:

- Shared enumerations for robot teleoperation:
  - `JogType`
  - `JogIndex`
  - `JogDirection`

## Installation
This package assumes an existing ROS 2 workspace.

Clone the repository into your workspace:

```bash
cd ~/ros2_ws/src
git clone https://github.com/modena-robotics/modena_common.git
```

Build the package:

```bash
cd ~/ros2_ws
colcon build --packages-select modena_common
source install/setup.bash
```

## Usage
```python
from modena_common.enums import JogType, JogIndex, JogDirection

jog_type = JogType.JOG_JOINT
jog_index = JogIndex.JOG_INDEX_1
jog_dir = JogDirection.JOG_POS
```

## Used by
- `mr3_mini_driver`
- `modena_teleop`

## License
This project is licensed under the BSD 3-Clause License.