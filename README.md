# tuni_robot_motion

## motion model
### *motion without noise*
![](https://latex.codecogs.com/svg.latex?%5C%5Cx_%7Bi&plus;1%7D%20%3D%20x_i&plus;%7B%5Cfrac%7BV_i%7D%7Bw_i%7D%7Dsin%28%5Ctheta_i&plus;w_i%5CDelta%20t%29%5C%5C%20y_%7Bi&plus;1%7D%20%3D%20y_i-%7B%5Cfrac%7BV_i%7D%7Bw_i%7D%7Dcos%28%5Ctheta_i&plus;w_i%5CDelta%20t%29%5C%5C%20%5Ctheta_%7Bi&plus;1%7D%20%3D%20%5Ctheta_i&plus;w_i%5CDelta%20t)

### *motion with noise*
![](https://latex.codecogs.com/svg.latex?%5C%5Cx_%7Bi&plus;1%7D%20%3D%20x_i&plus;%7B%5Cfrac%7BV_i&plus;%5CDelta%20V%7D%7BV_i&plus;%5CDelta%20V%7D%7Dsin%28%5Ctheta_i&plus;%28w_i&plus;%20%5CDelta%20w%29%5CDelta%20t%29%5C%5C%20y_%7Bi&plus;1%7D%20%3D%20y_i-%7B%5Cfrac%7BV_i&plus;%5CDelta%20V%7D%7BV_i&plus;%5CDelta%20V%7D%7Dcos%28%5Ctheta_i&plus;%28w_i&plus;%20%5CDelta%20w%29%5CDelta%20t%29%5C%5C%20%5Ctheta_%7Bi&plus;1%7D%20%3D%20%5Ctheta_i&plus;%28w_i&plus;%5CDelta%20w%29%5CDelta%20t)


