# Simulación y diseño de robot móvil tipo Ackerman.

Requisitos para la ejecución del proyecto.

- Python.
- ROS2.
- RViz.
- Gazebo.

## Creación de modelo URDF.

El archivo URDF que modela el robot móvil de tipo Ackerman se puede encontrar clickeando en el siguiente enlace [ackerman.urdf](https://github.com/Willica/Ackerman-ROS-Project/tree/master/urdf).

## Modularización con Xacro.

El archivo URDF generado se modularizó a modo de poder comprender el código que modela el robot de mejor forma. 

A continuación se mencionan los archivos modularizados con Xacro y su finalidad.

- [ackerman_plus.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/ackerman_plus.xacro): Es el archivo principal que permite integrar elementos al robot.
- [ackerman.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/ackerman.xacro): Archivo que integra todas las partes para la correcta creación del robot tipo Ackerman.
- [base.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/base.xacro): Modularización de la base del robot.
- [steering.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/steering.xacro): Modularización de las direcciones del robot.
- [wheel.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/wheel.xacro): Modularización de las ruedas del robot.
- [params.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/params.xacro): Permite modificar aspectos relevantes del robot.
- [camera.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/camera.xacro): Modularización de la cámara.
- [lidar.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/lidar.xacro): Modularización del sensor tipo LIDAR.

## Visualización en RViz.

La visualización en RViz se llevó a cabo mediante el siguiente archivo launch file [visualization_rviz.launch.py](https://github.com/Willica/Ackerman-ROS-Project/blob/master/ackerman/launch/visualization_rviz.launch.py) escrito en Python.

Para arrancar el archivo de visualización se hizo uso de los siguientes comandos:

- cd /directorio_repositorio
- source install/setup.bash 
- ros2 launch ackerman visualization_rviz.launch.py

>Nota: Del visualization_rviz.launch.py se debe cambiar la ruta escrita en la linea 9 y 28. La primera asociada al archivo XACRO y la segunda a la configutación del RViz.

A continuación se muestra cómo se visualiza:

<div align="center">
  <table>
    <tr>
      <td style="text-align: center;">
        <img src="images/rviz1.png" width="450"/>
      </td>
      <td style="text-align: center;">
        <img src="images/rviz2.png" width="450"/>
      </td>
    </tr>
    <tr>
      <td style="text-align: center;">
        <img src="images/rviz3.png" width="450"/>
      </td>
      <td style="text-align: center;">
        <img src="images/rviz4.png" width="450"/>
      </td>
    </tr>
  </table>
</div>

>NOTA: Se debe comentar la cámara y el LIDAR en el archivo [ackerman_plus.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/ackerman_plus.xacro) para visualizarlo como se ve en la imagen.

La imagen mostrada a continuación muestra la comunicación entre los distintos nodos y tópicos.

![alt text](<images/nodelist1.png>)

## Simulación en Gazebo e integración de cámara y LIDAR.

La visualización en Gazebo del robot móvil tipo Ackerman se llevó a cabo mediante el siguiente launch file [visualization_gazebo.launch.py](https://github.com/Willica/Ackerman-ROS-Project/blob/master/ackerman/launch/visualization_gazebo.launch.py) escrito en Python. Por otro lado, a su vez se integraron elementos al robot como la [camera.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/camera.xacro) y el sensor [lidar.xacro](https://github.com/Willica/Ackerman-ROS-Project/blob/master/xacro/lidar.xacro).

Para arrancar el archivo de visualización se hizo uso de los siguientes comandos:

- cd /directorio_repositorio
- source install/setup.bash 
- ros2 launch ackerman visualization_gazebo.launch.py

>Nota: Del visualization_gazebo.launch.py se debe cambiar la ruta escrita en la linea 12, 26 y 44. La primera asociada al archivo XACRO, la segunda al mundo de Gazebo y la tercera al archivo de configuración del RViz.

Para operar el robot se debe hacer uso del siguiente comando en otra terminal:
- ros2 run teleop_twist_keyboard teleop_twist_keyboard

Al ejecutar el archivo de lanzamiento se ejecutará tanto Gazebo como RViz. El siguiente video [Ackerman Gazebo / RViz](https://www.youtube.com/watch?v=nsB6UI4z3HA) muestra el comportamiento del launch file.

![alt text](<images/RVIZ&GAZEBO.png>)

La imagen mostrada a continuación muestra la comunicación entre los distintos nodos y tópicos.

![alt text](<images/nodelist2.png>)
