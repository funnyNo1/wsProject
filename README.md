# wsProject
参考官方文档写的简陋版聊天web页面
https://channels.readthedocs.io/en/latest/tutorial/part_1.html

# 使用步骤
环境搭建 pip install -r requirements.txt
settings.py文件配置CHANNEL_LAYERS，主要redis需要5.0版本以上
后端启动 python manage.py runserver 0:12344
浏览器打开两个页面
http://{ip}:12344/chat/lobby/ #lobby指定同一聊天室

然后文本框输入信息，同一聊天室的人就可以收到消息
![image](https://user-images.githubusercontent.com/58673586/185896992-c76913bc-eaba-4d3e-a035-d0b082f49eca.png)

后端主动发送消息给客户端的调用方式
当客户端建立连接是会生成socket,可以根据channel_name获取到，如下图的可以获取到channel_name
![image](https://user-images.githubusercontent.com/58673586/185897470-0abfbc4e-5a4a-4a51-92b0-46a0ba3f312d.png)

然后发起ws请求
![image](https://user-images.githubusercontent.com/58673586/185898112-7683672e-b515-4211-9685-4d670a3fbc7b.png)

客户端收到的数据
![image](https://user-images.githubusercontent.com/58673586/185898150-472b6869-e6d9-4ca7-a856-aac60ece2796.png)



