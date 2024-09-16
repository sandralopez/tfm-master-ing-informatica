FROM python:3.9-slim

RUN apt-get update -yqq && \
    apt-get install -yqq libblas-dev \
    liblapack-dev \
    libjpeg-dev \
    libbz2-dev \
    zlib1g-dev \
    libpng-dev \
    libtiff-dev \
    libffi-dev \
    libssl-dev \
    libsnappy-dev \
    libzstd-dev \
    liblzma-dev \
    libfreetype6-dev \
    libgif-dev \
    libhdf5-dev \
    libicu-dev \
    libkrb5-dev \
    liblcms2-dev \
    libdeflate-dev \
    libedit-dev \
    libev-dev \
    libopenblas-dev \
    libreadline-dev \
    libsqlite3-dev \
    tk-dev \
    uuid-dev \
    libwebp-dev \
    libxcb1-dev \
    xz-utils \
    libncurses-dev \
    libopenjp2-7-dev \
    liblz4-tool \
    libnghttp2-dev \
    libre2-dev \
    libgstreamer-plugins-base1.0-0 \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY explainer_lib/ /explainer_lib

RUN pip install /explainer_lib
