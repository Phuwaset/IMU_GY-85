# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_gy85_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED gy85_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(gy85_FOUND FALSE)
  elseif(NOT gy85_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(gy85_FOUND FALSE)
  endif()
  return()
endif()
set(_gy85_CONFIG_INCLUDED TRUE)

# output package information
if(NOT gy85_FIND_QUIETLY)
  message(STATUS "Found gy85: 0.0.0 (${gy85_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'gy85' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${gy85_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(gy85_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${gy85_DIR}/${_extra}")
endforeach()
