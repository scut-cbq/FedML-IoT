**更新：**
1. 已移除上个版本使用的符号链接，改为使用sys和os协助寻址
2. 修改client加载了完整MNIST数据集的代码错误——client只应使用远程下载的预处理后的小数据集进行训练

**实验简述：**
1. 在本地进行联邦学习实验，使用数据集为MNIST，需要在本地启动server和2个client
  
**注意事项：**
1. 整个FedML-IoT中只有一个FedML(FedML-IoT/FedML)目录，其余FedML均为符号链接（如FedML/fedml_server/FedML-Server/executor/FedML），注意需要先删除我上传的符号链接，再新建一个
2. MNIST数据集超过了github上传文件大小的限制，因此附在邮件中，需要将mnist.zip复制到FedML/data/MNIST下，然后sh download_and_unzip.sh，并且运行executor下的server_start.sh，将生成的MNIST_mobile和MNIST_mobile_zip移动到executor/preprocessed_dataset中
3. 树莓派上的实验也已经配置好，在两台树莓派上启动raspberry_pi/fedavg/fedavg_rpi_client.py，自己的电脑上启动server即可，但注意要修改树莓派上grpc_ipconfig.csv文件0号设备的ip地址为server的ip地址；1号和2号设备即两台树莓派，使用了静态ip，不需要修改；还要修改server上的grpc_ipconfig.csv文件的1、2号设备的ip地址为两台树莓派的ip地址，0号设备保持127.0.0.1


**运行步骤：**

**1. 启动server端**
```
cd FedML/fedml_server/FedML-Server/executor
python3 app.py
```
  
**2. 启动2个client端**

另启动两个终端
  
终端1：
```
cd FedML-IoT/FedML/fedml_server/FedML-Server/client_simulator
python3 mobile_client_simulator.py --client_uuid '0'
```
终端2：
```
cd FedML-IoT/FedML/fedml_server/FedML-Server/client_simulator
python3 mobile_client_simulator.py --client_uuid '1'
```
