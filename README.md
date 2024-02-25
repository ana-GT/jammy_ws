# jammy_ws
Jammy devcontainer


Start demo:

``` 
$ ros2 launch humble_robots husky_sim.launch.py 
```

Send twist

```
$ ros2 topic pub -r 10 /w200_0000/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.3, y: 0.0, z: 0.0}}"
```