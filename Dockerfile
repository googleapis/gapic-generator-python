FROM python:3.7-slim-stretch

# Install system packages.
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    pandoc \
  && rm -rf /var/lib/apt/lists/*

# Add protoc and our common protos.
COPY --from gcr.io/gapic-images/api-common-protos:latest /usr/local/bin/protoc /usr/local/bin/protoc
COPY --from gcr.io/gapic-images/api-common-protos:latest /protos/ /protos/

#
