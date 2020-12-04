#!/bin/bash
#
# RPM build wrapper for ocaml-flac, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/ocaml.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap:/ocaml/CentOS_8/home:radiorabe:liquidsoap:ocaml.repo"
curl -o /etc/yum.repos.d/liquidsoap.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/CentOS_8/home:radiorabe:liquidsoap.repo"

yum install -y flac-devel --enablerepo=PowerTools

chown root:root ocaml-flac.spec

build-rpm-package.sh ocaml-flac.spec
