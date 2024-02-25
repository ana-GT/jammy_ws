cmake_minimum_required(VERSION 3.5)
project(humble_robots)


find_package(ament_cmake REQUIRED)


install(DIRECTORY config launch worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()