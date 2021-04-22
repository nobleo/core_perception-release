%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-points-preprocessor
Version:        1.14.14
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS points_preprocessor package

License:        Apache 2
Source0:        %{name}-%{version}.tar.gz

Requires:       gtest-devel
Requires:       qt5-qtbase-devel
Requires:       ros-noetic-autoware-config-msgs
Requires:       ros-noetic-cv-bridge
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-pcl-conversions
Requires:       ros-noetic-pcl-ros
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roslint
Requires:       ros-noetic-rostest
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2
Requires:       ros-noetic-tf2-eigen
Requires:       ros-noetic-tf2-ros
Requires:       ros-noetic-velodyne-pcl
Requires:       yaml-cpp-devel
BuildRequires:  gtest-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-noetic-autoware-config-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cv-bridge
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-pcl-conversions
BuildRequires:  ros-noetic-pcl-ros
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf2
BuildRequires:  ros-noetic-tf2-eigen
BuildRequires:  ros-noetic-tf2-ros
BuildRequires:  ros-noetic-velodyne-pcl
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The points_preprocessor package

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Apr 22 2021 amc-nu <abrahammonrroy@yahoo.com> - 1.14.14-1
- Autogenerated by Bloom

* Tue Mar 30 2021 amc-nu <abrahammonrroy@yahoo.com> - 1.14.11-3
- Autogenerated by Bloom

* Mon Mar 01 2021 amc-nu <abrahammonrroy@yahoo.com> - 1.14.11-2
- Autogenerated by Bloom

* Mon Mar 01 2021 amc-nu <abrahammonrroy@yahoo.com> - 1.14.11-1
- Autogenerated by Bloom

* Mon Jan 11 2021 amc-nu <abrahammonrroy@yahoo.com> - 1.14.10-1
- Autogenerated by Bloom

* Mon Jan 11 2021 amc-nu <abrahammonrroy@yahoo.com> - 1.14.9-4
- Autogenerated by Bloom

* Thu Jan 07 2021 amc-nu <abrahammonrroy@yahoo.com> - 1.14.9-3
- Autogenerated by Bloom

* Tue Nov 10 2020 amc-nu <abrahammonrroy@yahoo.com> - 1.14.9-2
- Autogenerated by Bloom

* Tue Nov 10 2020 amc-nu <abrahammonrroy@yahoo.com> - 1.14.9-1
- Autogenerated by Bloom

