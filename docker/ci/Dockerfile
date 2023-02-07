# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM python:3.10.9-buster

ENV SHOWCASE_VERSION=0.25.0
ENV PROTOC_RELEASE=21.12
ENV PROTOC_VERSION=4.21.12

ENV PYTHON_3_11_VERSION=3.11.1

RUN apt-get update && apt-get install -y pandoc unzip lsb-release


###################### Install python 3.11

# Download python 3.11
RUN wget https://www.python.org/ftp/python/${PYTHON_3_11_VERSION}/Python-${PYTHON_3_11_VERSION}.tgz

# Extract files
RUN tar -xvf Python-${PYTHON_3_11_VERSION}.tgz

# Install python 3.11
RUN ./Python-${PYTHON_3_11_VERSION}/configure --enable-optimizations
RUN make altinstall
######################


COPY requirements.txt ./

# Install requirements
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --require-hashes -r requirements.txt

# Download protoc
RUN mkdir -p /usr/src/protoc
RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_RELEASE}/protoc-${PROTOC_RELEASE}-linux-x86_64.zip -P /usr/src/protoc

# Install protoc
WORKDIR /usr/src/protoc
RUN unzip protoc-${PROTOC_RELEASE}-linux-x86_64.zip
RUN ln -s /usr/src/protoc/bin/protoc /usr/local/bin/protoc

# Download showcase
RUN mkdir -p /usr/src/showcase
RUN wget https://github.com/googleapis/gapic-showcase/releases/download/v${SHOWCASE_VERSION}/gapic-showcase-${SHOWCASE_VERSION}-linux-amd64.tar.gz -P /usr/src/showcase

# Install showcase
WORKDIR /usr/src/showcase
RUN ls gapic-showcase-*
RUN tar -xf gapic-showcase-${SHOWCASE_VERSION}-linux-amd64.tar.gz 

RUN protoc --version
ENTRYPOINT [ "/bin/bash" ]
