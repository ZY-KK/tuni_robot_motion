# CMake generated Testfile for 
# Source directory: /home/ros/catkin_ws/src/moro_ros/moro_navigation
# Build directory: /home/ros/catkin_ws/build/moro_navigation
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_moro_navigation_nosetests_test "/home/ros/catkin_ws/build/moro_navigation/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/ros/catkin_ws/build/moro_navigation/test_results/moro_navigation/nosetests-test.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/ros/catkin_ws/build/moro_navigation/test_results/moro_navigation" "/usr/bin/nosetests-2.7 -P --process-timeout=60 --where=/home/ros/catkin_ws/src/moro_ros/moro_navigation/test --with-xunit --xunit-file=/home/ros/catkin_ws/build/moro_navigation/test_results/moro_navigation/nosetests-test.xml")
subdirs(gtest)
