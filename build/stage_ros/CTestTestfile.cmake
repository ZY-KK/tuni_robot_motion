# CMake generated Testfile for 
# Source directory: /home/ros/catkin_ws/src/stage_ros
# Build directory: /home/ros/catkin_ws/build/stage_ros
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_stage_ros_rostest_test_hztest.xml "/home/ros/catkin_ws/build/stage_ros/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/ros/catkin_ws/build/stage_ros/test_results/stage_ros/rostest-test_hztest.xml" "--return-code" "/opt/ros/kinetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/ros/catkin_ws/src/stage_ros --package=stage_ros --results-filename test_hztest.xml --results-base-dir \"/home/ros/catkin_ws/build/stage_ros/test_results\" /home/ros/catkin_ws/src/stage_ros/test/hztest.xml ")
add_test(_ctest_stage_ros_rostest_test_intensity_test.xml "/home/ros/catkin_ws/build/stage_ros/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/ros/catkin_ws/build/stage_ros/test_results/stage_ros/rostest-test_intensity_test.xml" "--return-code" "/opt/ros/kinetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/ros/catkin_ws/src/stage_ros --package=stage_ros --results-filename test_intensity_test.xml --results-base-dir \"/home/ros/catkin_ws/build/stage_ros/test_results\" /home/ros/catkin_ws/src/stage_ros/test/intensity_test.xml ")
subdirs(gtest)
