#!/usr/bin/env sh

CUR_DIR=$(cd "$(dirname "$0")"; pwd)
echo $CUR_DIR
mkdir -p $CUR_DIR/benchmark-results

curl -sL yabs.sh | bash -s -- -w "${CUR_DIR}/benchmark-results/${1}"