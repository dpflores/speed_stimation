git clone --recurse-submodules https://github.com/dpflores/speed_stimation


# para un nuevo dockerfile
sudo docker run --name ros_container --privileged --network host -it ros:noetic-ros-core 

apt update
apt install net-tools
apt install nano
apt install git
apt install python3-pip

sudo apt install g++
apt-get install make

sudo apt-get install ros-noetic-catkin

sudo apt-get install cmake




Messages
Bool.msg            Float32MultiArray.msg  Int64.msg                UInt16.msg
Byte.msg            Float64.msg            Int64MultiArray.msg      UInt16MultiArray.msg
ByteMultiArray.msg  Float64MultiArray.msg  Int8.msg                 UInt32.msg
Char.msg            Header.msg             Int8MultiArray.msg       UInt32MultiArray.msg
ColorRGBA.msg       Int16.msg              MultiArrayDimension.msg  UInt64.msg
Duration.msg        Int16MultiArray.msg    MultiArrayLayout.msg     UInt64MultiArray.msg
Empty.msg           Int32.msg              String.msg               UInt8.msg
Float32.msg         Int32MultiArray.msg    Time.msg                 UInt8MultiArray.msg