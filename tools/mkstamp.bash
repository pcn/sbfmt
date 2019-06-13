#!/bin/bash
echo BUILD_DATE $(TZ=Etc/UTC date -Iseconds)
# XXX: change the below to using describe, if possible, to get most recent tag and offset instead
# of having to construct that kind of info from pieces
echo BUILD_SCM_HASH $(git rev-parse HEAD)
echo BUILD_SCM_VERSION $(git describe)-$USER
echo BUILD_BAZEL_ROOT $PWD
if [[ "$(uname -s)" == "Darwin" ]]; then
  echo BUILD_IP_ADDR "$(ipconfig getifaddr "$(networksetup -listallhardwareports \
        | awk '/Hardware Port: Wi-Fi/{getline; print $2}')")"
else
  echo BUILD_IP_ADDR $(hostname -I | cut -d' ' -f1)
fi
